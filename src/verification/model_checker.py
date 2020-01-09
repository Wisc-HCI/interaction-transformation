import sys
sys.path.append("/Users/david/Documents/UW_Research/Repair/repair_algorithms/verification/pynusmv/src/")
import tools.tlace.tlace

class ModelChecker:

    def __init__(self, prop_strings):
        #pynusmv.init.init_nusmv()
        self.raw_props = prop_strings

    def create_and_load_model(self, TS, removed_transitions, inputs, outputs):
        '''
        First create the properties
        '''
        properties = []
        for prop in self.raw_props:
            # determine if prop does not need to be modified
            if '~' not in prop:
                properties.append(prop)
                continue
            else:
                refined_prop = prop
                while '~' in refined_prop:
                    #print("raw prop: {}".format(refined_prop))
                    str_to_replace = refined_prop[refined_prop.index('~')+1:]
                    after_to_not_replace = str_to_replace[str_to_replace.index('~')+1:]
                    str_to_replace = str_to_replace[:str_to_replace.index('~')]

                    before_to_not_replace = refined_prop[:refined_prop.index('~')]
                    #print("before to not replace: {}".format(before_to_not_replace))
                    #print("after to not replace: {}".format(after_to_not_replace))
                    #print("str to replace: {}".format(str_to_replace))

                    micro_to_replace = str_to_replace[str_to_replace.index('\\')+1:]
                    after_micro_to_not_replace = micro_to_replace[micro_to_replace.index('\\')+1:]
                    micro_to_replace = micro_to_replace[:micro_to_replace.index('\\')]

                    before_micro_to_not_replace = str_to_replace[:str_to_replace.index('\\')]
                    #print("before micro to not replace: {}".format(before_micro_to_not_replace))
                    #print("after micro to not replace: {}".format(after_micro_to_not_replace))
                    #print("micro to replace: {}".format(micro_to_replace))

                    satisfying_micros = []

                    for st_name,st in TS.states.items():
                        if st.micros[0]["name"] == micro_to_replace:
                            satisfying_micros.append(st_name)
                            #print("found satisfying micro: {}".format(st_name))

                    if len(satisfying_micros) == 0:
                        #print("no satisfying micros")
                        satisfying_micros.append(micro_to_replace)

                    new_component = ""
                    if len(satisfying_micros) == 1:
                        new_component = before_micro_to_not_replace + satisfying_micros[0] + after_micro_to_not_replace
                    else:
                        new_component += "("
                        for mic in satisfying_micros[:-1]:
                            new_component += before_micro_to_not_replace + mic + after_micro_to_not_replace + " | "
                        new_component += before_micro_to_not_replace + satisfying_micros[-1] + after_micro_to_not_replace
                        new_component += ")"
                    refined_prop = before_to_not_replace + new_component + after_to_not_replace


                properties.append(refined_prop)
                #print("refined property: {}".format(refined_prop))

        '''
        Now create the .smv file
        '''
        unused_outputs = []
        for out in outputs.alphabet:
            unused_outputs.append(out)
        for st in TS.states:
            micro_name = TS.states[st].micros[0]["name"]
            if micro_name in unused_outputs:
                unused_outputs.remove(micro_name)
        # create a model file called model.smv
        file_string = "MODULE main\n\tVAR\n\t\tst : {"
        outs = list(TS.states)
        for out in outs:
            file_string += "{}, ".format(out)
        for out in unused_outputs:
            file_string += "{}, ".format(out)

        file_string += "END, ERROR};\n\t\thst : {"
        ins = list(inputs.alphabet)
        for inp in ins[:-1]:
            file_string += "{}, ".format(inp)
        file_string += "{}".format(ins[-1])

        file_string += "}};\n\tASSIGN\n\t\tinit(st) := {};\n\t\tnext(st) := case\n".format(TS.init.name)

        for st_name,st in TS.states.items():
            for trans in st.out_trans:
                file_string += "\t\t\t\tst={} & hst={} : {};\n".format(st_name,trans.condition,trans.target.name)

        for trans in removed_transitions:
            file_string += "\t\t\t\tst={} & hst={} : {};\n".format(trans.source.name,trans.condition,"END")

        file_string += "\t\t\t\tst=END : END;\n"
        file_string += "\t\t\t\tst=ERROR : END;\n"
        file_string += "\t\t\t\tTRUE : ERROR;\n"
        file_string += "\t\t\t    esac;\n"

        file_string += "\t\tinit(hst) := {UnsatRequest, RequestInfo, AskClarify, Affirm, Deny, Goodbye, General, Ignore};\n"
        file_string += "\t\tnext(hst) := {UnsatRequest, RequestInfo, AskClarify, Affirm, Deny, Goodbye, General, Ignore};\n"

        for prop in properties:
            file_string += "{}".format(prop)

        with open("verification/model.smv", "w") as outfile:
            outfile.write(file_string)

    def check(self):
        results, counterexamples = tools.tlace.tlace.check_and_explain("verification/model.smv")
        return results, counterexamples
