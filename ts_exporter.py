import xml.etree.ElementTree as ET

class TSExporter:

    def __init__(self, TS, io_data):
        self.TS = TS
        self.io_data = io_data

    def export(self, path, mod_tracker=None, ts_name="updated_interaction.xml"):

        # make the states
        st2id = {}
        root = ET.Element('nta')
        tree = ET.ElementTree(root)
        for st in self.TS.states:

            state = self.TS.states[st]

            group = ET.SubElement(root,'group')
            if self.TS.init == state:
                group.set('init','true')
            else:
                group.set('init','false')
            group.set('id',str(state.id))
            st2id[state] = state.id
            group.set('x',str(0))
            group.set('y',str(0))

            name = ET.SubElement(group,'name')
            name.text = state.name

            micro = ET.SubElement(group,'micro')

            micro_name = ET.SubElement(micro,'name')
            micro_name.text = self.io_data["outputs"][state.micros[0]["name"]]["micro"]

            micro_inst = ET.SubElement(micro,'instantiation')
            micro_inst.text = state.micros[0]["name"]

        # link up the transitions
        transition_dict = self.TS.transitions
        for source_st in self.TS.states:
            source_state = self.TS.states[source_st]
            for target_st in transition_dict[source_state.id]:
                target_state = None #self.TS.id2state[target_st]
                for state_name,state_obj in self.TS.states.items():
                    if state_obj.id == target_st:
                        target_state = state_obj
                if len(transition_dict[source_state.id][target_state.id]) > 0:

                    transition = ET.SubElement(root,'transition')
                    source_id = st2id[source_state]
                    target_id = st2id[target_state]

                    source_el = ET.SubElement(transition,'source')
                    source_el.set('ref',str(source_id))

                    target_el = ET.SubElement(transition,'target')
                    target_el.set('ref',str(target_id))

                    for trans in transition_dict[source_state.id][target_state.id]:
                        condition = trans.condition
                        condition = "human_" + condition[0].lower() + condition[1:]

                        cond_el = ET.SubElement(transition,'guard')
                        cond_el.set('condition',condition)
        # export the file
        tree.write(open("{}/{}".format(path,ts_name),"w"),encoding="unicode")

        if mod_tracker is not None:
            mod_tracker.write_to_file(path)
