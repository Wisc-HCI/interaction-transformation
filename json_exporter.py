import json

from dot_graph import *

class JSONExporter:

    def __init__(self):
        pass

    def export_from_object(self, TS, st_reachables, freqs):
        json_array = {}
        json_array["links"] = []
        print(st_reachables)
        for _,val in TS.transitions.items():
            for _,transitions in val.items():
                for transition in transitions:
                    if st_reachables[transition.source.name]:
                        json_array["links"].append({"source": int(transition.source_id),
                                                    "source_name": transition.source.name,
                                                    "target": int(transition.target_id),
                                                    "input": transition.condition})

        # consolidate links
        to_remove = []
        for link1 in json_array["links"]:
            if link1 not in to_remove:
                for link2 in json_array["links"]:
                    if link2 != link1:
                        if link1["source"] == link2["source"] and link1["target"] == link2["target"]:
                            to_remove.append(link2)
                            link1["input"] = "{}\n{}".format(link1["input"],link2["input"])

        for removable in to_remove:
            json_array["links"].remove(removable)

        json_array["states"] = {}
        for _,state in TS.states.items():
            if st_reachables[state.name]:
                json_array["states"][str(state.id)] = {"id": state.id, "gesture": None, "reachble": True, "final": False, "prob": freqs.probs[state.micros[0]["name"]]["Ready"], "micro": state.micros[0]["name"]}

        with open('d3js/links.json', 'w') as outfile:
            json.dump(json_array, outfile)

    def export_from_z3(self, solution):
        # offline graphing with dot
        grapher = Grapher()
        grapher.make_graph(solution)

        raw_edges = solution.results

        # first consolidate transitions with the same io
        edges_dict = {}
        for edge in raw_edges:
            edge_io = (edge[0], edge[2])
            if edge_io in edges_dict:
                input_to_append = edge[1]
                edges_dict[edge_io] = (edges_dict[edge_io][0],
                                       edges_dict[edge_io][1] + "\n{}".format(input_to_append),
                                       edges_dict[edge_io][2],
                                       edges_dict[edge_io][3])
            else:
                edges_dict[edge_io] = edge

        edges = []
        for key, value in edges_dict.items():
            edges.append(value)

        # loop through the results and map states to names
        state2name = {}
        for edge in edges:
            if edge[0] != -1:
                state2name[edge[0]] = edge[3]

        json_array = {}
        json_array["links"] = []
        for edge in edges:
            if str(edge[2]) != '-1':
                temp_dict = {"source": int(str(edge[0])),
                             "source_name": state2name[int(str(edge[0]))],
                             "target": int(str(edge[2])),
                             "input": edge[1]}
                json_array["links"].append(temp_dict)

        states = solution.get_reachability()
        json_array["states"] = {}

        '''
        TODO: NUANCE
        '''
        for st in range(len(states)):
            json_array["states"][st] = {"id": st,
                                        "gesture": "None",
                                        "reachable": True,
                                        "final": states[st]["final"]}

        with open('d3js/links.json', 'w') as outfile:
            json.dump(json_array, outfile)
