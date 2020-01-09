import socket
import select

class ConvertToPrism:

    def __init__(self, inputs):
        self.inputs = inputs.alphabet

    def make_PRISM_TS(self, TS, prefix):

        # every state gets converted to 4 states
        # EXCEPT for the initial state
        class microinteraction:
            def __init__(self, i, inp_cats, out_labels, in_labels, out_cond_labels, in_cond_labels, init=None):
                self.inps = {}
                self.outs = {}
                self.init = None
                for inp in inp_cats:
                    self.inps[inp] = i
                    in_cond_labels[inp].append(i)
                    in_labels.append(i)
                    if init is not None and inp == init:
                        self.init=i
                    self.outs[inp] = i+len(inp_cats)
                    out_cond_labels[inp].append(i+len(inp_cats))
                    out_labels.append(i+len(inp_cats))
                    i+=1
                self.num_states = len(self.inps) + len(self.outs)

        state2num = {}
        out_labs = []
        in_labs = []
        out_conds = {}
        in_conds = {}
        for inp in self.inputs:
            out_conds[inp] = []
            in_conds[inp] = []

        states = list(TS.states.values())
        init_num = -1
        i = 0
        for st in states:
            if int(st.id)==0:
                state2num[st] = microinteraction(i, self.inputs, out_labs, in_labs, out_conds, in_conds, init="Ready")
                init_num = state2num[st].init
            else:
                state2num[st] = microinteraction(i, self.inputs, out_labs, in_labs, out_conds, in_conds, init=False)
            i+=(2*len(self.inputs))

        with open("{}.pm".format(prefix), "w") as pfile:

            pfile.write("mdp")

            # write the single module
            pfile.write("\n\nmodule model\n\n")
            pfile.write("\ts: [{}..{}] init {};\n".format(0,i,init_num))

            # outer transitions
            transitions = TS.transitions
            #print(TS)
            for _,temp in transitions.items():
                for _,trans_list in temp.items():
                    for trans in trans_list:
                        #print("~~~~~~~~\nsource: {}".format(trans.source.name))
                        #print("target: {}".format(trans.target.name))
                        pfile.write("\t[] s={} -> (s'={});\n".format(state2num[trans.source].outs[trans.condition],
                                                                     state2num[trans.target].inps[trans.condition]))

            # inner transitions
            for state,nums in state2num.items():
                for inp in nums.inps:
                    for out in nums.outs:
                        pfile.write("\t[] s={} -> (s'={});  //{} \n".format(nums.inps[inp],nums.outs[out],state.name))

            # end
            pfile.write("endmodule\n\n")

            # groups
            for _,state in TS.states.items():
                pfile.write("label \"group_{}\"=(".format(state.name))
                inps = list(state2num[state].inps.values())
                for i in range(len(inps)):
                    pfile.write(" s={} | ".format(inps[i]))
                outs = list(state2num[state].outs.values())
                for i in range(len(outs)-1):
                    pfile.write(" s={} | ".format(outs[i]))
                pfile.write(" s={} );\n".format(outs[len(outs)-1]))

            # outs/ins
            pfile.write("\nlabel \"out_state\"=(")
            for i in range(len(out_labs)-1):
                pfile.write(" s={} | ".format(out_labs[i]))
            pfile.write(" s={} );\n".format(out_labs[len(out_labs)-1]))

            pfile.write("\nlabel \"in_state\"=(")
            for i in range(len(in_labs)-1):
                pfile.write(" s={} | ".format(in_labs[i]))
            pfile.write(" s={} );\n".format(in_labs[len(in_labs)-1]))

            for cond in self.inputs:
                pfile.write("\nlabel \"out_{}\"=(".format(cond))
                for i in range(len(out_conds[cond])-1):
                    pfile.write(" s={} | ".format(out_conds[cond][i]))
                pfile.write(" s={} );\n".format(out_conds[cond][len(out_conds[cond])-1]))

                pfile.write("\nlabel \"in_{}\"=(".format(cond))
                for i in range(len(in_conds[cond])-1):
                    pfile.write(" s={} | ".format(in_conds[cond][i]))
                pfile.write(" s={} );\n".format(in_conds[cond][len(in_conds[cond])-1]))

class Checker():

    def __init__(self, port):

        print("Initializing the Prism Model Checker...")
        HOST = "localhost"
        self.PORT = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket created')

        try:
            self.s.bind((HOST, self.PORT))
        except socket.error as err:
            print('Bind failed. Error Code : ' .format(err))

    def connect(self):
        self.s.listen(10)
        print("Socket Listening")
        self.conn, addr = self.s.accept()
        data = self.conn.recv(1024)
        print(data)

    def close_connection(self):
        self.s.close()

    def split_property_file(self, prop_file, num_threads):
        props = open("{}".format(prop_file), "r")
        counts = [0 for i in range(num_threads)]
        file_contents = [[] for i in range(num_threads)]

        fairness = False
        fairness_idx = -1
        for prop in props:

            # choose an index
            idx = counts.index(min(counts))

            # handle comments and white space
            if prop[0] == "#" or prop == "\n":
                continue

            prop = prop.strip('\n')

            if prop == "EOP":
                break

            # see if a fairness block
            if prop == "FAIRNESS TRUE":
                fairness = True
                fairness_idx = idx
                file_contents[fairness_idx].append(prop)
                continue
            elif prop == "FAIRNESS FALSE":
                fairness = False
                file_contents[fairness_idx].append(prop)
                continue

            if fairness:
                file_contents[fairness_idx].append(prop)
                counts[fairness_idx] += 1
            else:
                file_contents[idx].append(prop)
                counts[idx] += 1

        for i in range(len(file_contents)):
            contents = file_contents[i]
            output_file = open("{}{}".format(i,prop_file), "w")
            for prop in contents:
                output_file.write("{}\n".format(prop))
            output_file.write("EOP")

    def check(self, model_file, prop_file, halt_if_false=False):
        rewardsToReturn = {}
        satisfies_properties = True

        msg = "../{}\r\n".format(model_file)
        ready_to_read, ready_to_write, in_error = select.select([], [self.conn], [])
        ready_to_write[0].send(msg.encode('UTF-8'))

        ready_to_read, ready_to_write, in_error = select.select([self.conn], [], [])
        data = ready_to_read[0].recv(1024)

        props = open("{}".format(prop_file), "r")
        num_props = 0
        num_satisfied = 0
        for prop in props:

            # handle comments and white space
            if prop[0] == "#" or prop == "\n":
                continue

            prop = prop.strip('\n')
            print("sending property {}".format(prop))
			#self.conn.send(str(bytes(prop + "\r\n"), 'UTF-8'))
            msg = "{}\r\n".format(prop)
            ready_to_read, ready_to_write, in_error = select.select([], [self.conn], [])
            ready_to_write[0].send(msg.encode('UTF-8'))
            print("property sent ({})".format(self.PORT))

            if prop == "EOP":
                break;

            #confirmation of received property
            print("getting confirmation... ({})".format(self.PORT))
            ready_to_read, ready_to_write, in_error = select.select([self.conn], [], [])
            data = ready_to_read[0].recv(1024)
            print("confirmation received ({})".format(self.PORT))

            # obtain result
            print("obtaining result... ({})".format(self.PORT))
            ready_to_read, ready_to_write, in_error = select.select([self.conn], [], [])
            data = ready_to_read[0].recv(1024)
            print("result obtained ({})".format(self.PORT))

            if "R{\"pos\"}=" in prop:
                rewardsToReturn["R{\"pos\"}"] = float('inf') if data == "infinity" else float(data)
            elif "R{\"neg\"}=" in prop:
                rewardsToReturn["R{\"neg\"}"] = float('inf') if data == "infinity" else float(data)
            elif "R{\"pos\"}max" in prop:
                rewardsToReturn["R{\"pos\"}max"] = float('inf') if data == "infinity" else float(data)
            elif "R{\"neg\"}max" in prop:
                rewardsToReturn["R{\"neg\"}max"] = float('inf') if data == "infinity" else float(data)
            elif "R{\"pos\"}min" in prop:
                rewardsToReturn["R{\"pos\"}min"] = float('inf') if data == "infinity" else float(data)
            elif "R{\"neg\"}min" in prop:
                rewardsToReturn["R{\"neg\"}min"] = float('inf') if data == "infinity" else float(data)
            else:
                if "true" in str(data) or "false" in str(data):
                    num_props += 1
                    if "false" in str(data):
                        satisfies_properties = False
                    else:
                        num_satisfied += 1

		#self.conn.send(unicode(bytes("EOP\r\n"), 'UTF-8'))
            if halt_if_false and satisfies_properties == False:
                print("ERROR: property is false: {}".format(prop))
                exit()

        # calculate the satisfaction ratio
        sat_ratio = num_satisfied*1.0/num_props if num_props > 0 else 0

        self.satisfies_properties = satisfies_properties
        self.rewardsToReturn = rewardsToReturn
        self.sat_ratio = sat_ratio
        self.num_props = num_props
        self.num_satisfied = num_satisfied

        return satisfies_properties, rewardsToReturn, sat_ratio, num_props, num_satisfied
