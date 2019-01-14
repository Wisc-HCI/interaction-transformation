import copy
import random

class Kosajaru:

    def __init__(self, TS):
        self.TS = TS

    def visit(self,u,visited,L):
        if not visited[u]:
            visited[u] = True
            for trans in u.out_trans:
                self.visit(trans.target, visited, L)
            L.insert(0,u)

    def assign(self,u,scc,sccs):
        exists = False
        for scc in sccs:
            if scc.is_member(u):
                exists = True
        if not exists and not scc.is_member(u):
            scc.add(u)
            for trans in u.in_trans:
                self.assign(trans.source,scc,sccs)

    def compute(self,inputs):
        sccs = []

        visited = {}
        L = []

        #1 for each vertex, mark it as unvisited
        for state_id,state in self.TS.states.items():
            visited[state] = False

        #2
        self.visit(self.TS.init,visited,L)

        #3
        for u in L:
            exists = False
            for scc in sccs:
                if scc.is_member(u):
                    exists = True
            if not exists:
                sccs.append(SCC(u))
                self.assign(u,sccs[-1],sccs)

        #4: find the strongest of the sccs
        strong_sccs = []
        for scc in sccs:
            if scc.is_max_strong(inputs):
                strong_sccs.append(scc)

        return strong_sccs

    def bfs(self,curr,dest,input_dict,trans_to_try,visited_trans,curr_path,path_to_dest):
        if len(path_to_dest) > 0:
            return

        elif curr==dest:
            for item in curr_path:
                path_to_dest.append(item)
            return

        # append to the list
        for trans in curr.out_trans:
            if trans not in visited_trans:
                #trans_to_try.append((curr_path.copy(),trans))
                trans_to_try.append((self.copy_path(curr_path),trans))

        while len(trans_to_try)>0:
            next_trans = trans_to_try.pop(0)
            if next_trans in visited_trans:
                continue
            else:
                visited_trans.append(next_trans)
            next = next_trans[1].target
            curr_path_copy = next_trans[0]
            curr_path_copy.append((input_dict[next_trans[1].condition],int(next.id)))
            return self.bfs(next,dest,input_dict,trans_to_try,visited_trans,curr_path_copy,path_to_dest)
        '''

        print("BEGINNING CALL: {},{}".format(curr,dest))
        for v in visited:
            print("   visited {}".format(v.name))

        if len(path_to_dest) > 0:
            print("path to dest is greater than 0, returning")
            return

        elif curr==dest:
            for item in curr_path:
                print("found dest, adding to the path to dest")
                path_to_dest.append(item)
            return

        elif curr in visited:
            print("already visited curr {}".format(curr))
            return

        # put curr in visited
        visited.append(curr)

        # append to the list
        for trans in curr.out_trans:
            #trans_to_try.append((curr_path.copy(),trans))
            trans_to_try.append((self.copy_path(curr_path),trans))

        while len(trans_to_try)>0:
            next_trans = trans_to_try.pop(0)
            next = next_trans[1].target
            print("visiting {} next".format(next))
            curr_path_copy = next_trans[0]
            curr_path_copy.append((input_dict[next_trans[1].condition],int(next.id)))
            return self.bfs(next,dest,input_dict,trans_to_try,visited,curr_path_copy,path_to_dest)

        '''

    def bfs_scc(self, curr_state, dest, input_dict, trans_to_try, visited_trans, curr_path, path_to_dest):

        print("start {}, dest ({},{}) ----- path: {}".format(curr_state.id,dest[0],dest[1].id,curr_path))
        if len(path_to_dest) > 0:
            return

        dest_is_reachable = False
        for trans in curr_state.out_trans:
            if input_dict[trans.condition] == dest[0] and trans.target == dest[1]:
                dest_is_reachable = True
        if dest_is_reachable:
            for item in curr_path:
                path_to_dest.append(item)
            return

        # append to the list
        for trans in curr_state.out_trans:
            if trans not in visited_trans:
                #trans_to_try.append((curr_path.copy(),trans))
                trans_to_try.append((self.copy_path(curr_path),trans))

        while len(trans_to_try)>0:
            next_trans = trans_to_try.pop(0)
            if next_trans in visited_trans:
                continue
            else:
                visited_trans.append(next_trans)
            next = next_trans[1].target
            curr_path_copy = next_trans[0]
            curr_path_copy.append((input_dict[next_trans[1].condition],int(next.id)))
            return self.bfs_scc(next,dest,input_dict,trans_to_try,visited_trans,curr_path_copy,path_to_dest)

    def get_scc_counterexample(self, scc, input_dict):
        root = scc.root
        init = self.TS.init

        curr_path = [(0,0)]
        path_to_dest = []

        self.bfs(init,root,input_dict,[],[],curr_path,path_to_dest)
        if len(path_to_dest) == 0:
            print("no path to destination")
            return None

        # now that we have the path to dest, get a path through the scc
        path = path_to_dest
        to_remove = []
        path_post_root = []
        curr = root
        for state in scc.vertices:
            for trans in state.in_trans:
                to_remove.append((input_dict[trans.condition],state))
        tup = (input_dict[root.out_trans[0].condition],root.out_trans[0].target)
        path_post_root.append((tup[0],int(tup[1].id)))
        to_remove.remove(tup)
        print("next: {}".format(path_post_root))
        curr = tup[1]

        while len(to_remove) > 0:
            # randomly select a transition to take
            trans_tup = random.choice(to_remove)
            print("   destination -- {}-{}".format(trans_tup[0],trans_tup[1].id))

            curr_path = []
            path_from_curr_to_next = []
            self.bfs_scc(curr,trans_tup,input_dict,[],[],curr_path,path_from_curr_to_next)
            path_from_curr_to_next.append((trans_tup[0],int(trans_tup[1].id)))
            curr = trans_tup[1]

            for tup in path_from_curr_to_next:
                if str(tup[1]) in self.TS.id2state:
                    tup_to_remove = (tup[0],self.TS.id2state[str(tup[1])])
                else:
                    for state_name,state in self.TS.states.items():
                        if state.id == str(tup[1]):
                            tup_to_remove = (tup[0],state)
                if tup_to_remove in to_remove:
                    to_remove.remove(tup_to_remove)

            print("further: {}".format(path_from_curr_to_next))
            path_post_root += path_from_curr_to_next

        return path + path_post_root

    def copy_path(self,path):
        new_path = []

        for item in path:
            new_path.append(item)

        return new_path

class SCC:

    def __init__(self,root):
        self.vertices = []
        self.root = root

    def add(self,v):
        if not self.is_member(v):
            self.vertices.append(v)

    def is_member(self,v):
        if v in self.vertices:
            return True
        else:
            return False

    def is_max_strong(self,inputs):
        yes = True
        for v in self.vertices:

            # if a transition leads elsewhere
            for trans in v.out_trans:
                if trans.target not in self.vertices:
                    yes = False
                    break

            # if v is missing a transition
            for inp in inputs:
                exists = False
                for trans in v.out_trans:
                    if trans.condition == inp:
                        exists = True
                if not exists:
                    yes = False

            if not yes:
                break
        return yes

    def __str__(self):
        string = ""

        string += "SCC: root={}\n".format(self.root.id)
        string += "  -- verts: "
        for v in self.vertices:
            string += " {}".format(v.id)

        return string
