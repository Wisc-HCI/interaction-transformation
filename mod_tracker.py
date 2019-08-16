import pickle

class ModificationTracker:

    def __init__(self):
        self.mod_tracker = {}

    def reset_tracker(self, TS, inputs):
        self.mod_tracker.clear()
        for state in TS.states.values():
            for inp in inputs.alphabet:
                dest_properties = None
                dest = None
                for trans in state.out_trans:
                    if trans.condition == inp:
                        dest = trans.target
                        dest_properties = dest.micros[0]["name"]
                #self.mod_tracker[(state,inp)] = [0,dest]
                self.mod_tracker[(state,inp)] = [0,dest_properties]

    def update_mod_tracker(self, transition, deleted=False):
        if (transition.source, transition.condition) not in self.mod_tracker:
            #print("   MC: returning prematurely")
            return

        if deleted and self.mod_tracker[(transition.source,transition.condition)][1] is None:
            self.mod_tracker[(transition.source,transition.condition)][0] = 0
            #print("   MC: deleting, but it was meant to be deleted anyway........")
        elif deleted:
            self.mod_tracker[(transition.source,transition.condition)][0] = 1
            #print("   MC: deleting, it was NOT meant to be")
        #elif self.mod_tracker[(transition.source,transition.condition)][1] == transition.target:
        elif self.mod_tracker[(transition.source,transition.condition)][1] == transition.target.micros[0]["name"]:
            self.mod_tracker[(transition.source,transition.condition)][0] = 0
            #print("   MC: not deleting, and it was meant to be")
        else:
            self.mod_tracker[(transition.source,transition.condition)][0] = 1
            #print("   MC: it was NOT meant to be")

    def check_mod_tracker_sum(self):
        sum = 0
        for item in self.mod_tracker:
            sum += self.mod_tracker[item][0]
        return sum

    def check_mod_tracker_empties(self, removed_transitions):
        '''
        count how many removed transitions are modded transitions
        (those that aren't supposed to be removed)
        '''
        sum = 0
        for item in self.mod_tracker:
            if self.mod_tracker[item][0] == 1:
                for trans in removed_transitions:
                    if trans.source == item[0] and trans.condition == item[1]:
                        sum += 1
        return sum

    def check_mod_tracker_nonempties(self, removed_transitions):
        '''
        count how many NOT removed transitions are modded transitions
        (those that aren't supposed to be removed)
        '''
        sum = 0
        for item in self.mod_tracker:
            if self.mod_tracker[item][0] == 1:
                for trans in item[0].out_trans:
                    if trans.condition == item[1]:
                        not_exists = True
                        for rtrans in removed_transitions:
                            if trans.source == rtrans.source and trans.condition == rtrans.condition:
                                not_exists = False
                        if not_exists:
                            sum += 1
        return sum

    def get_mod_tracker_nonempty_trans(self, removed_transitions):
        '''
        point here is to get the modified transitions that are NOT removed
        '''
        trans_mods = []
        for item in self.mod_tracker:
            if self.mod_tracker[item][0] == 1:   # if we're looking at a modification
                for trans in item[0].out_trans:
                    if trans.condition == item[1]:
                        exists_in_removed = False
                        for rtrans in removed_transitions:
                            if trans.source == rtrans.source and trans.condition == rtrans.condition:
                                exists_in_removed = True
                        if not exists_in_removed:
                            trans_mods.append(trans)
        return trans_mods

    def get_mod_tracker_empty_trans(self, removed_transitions):
        '''
        point here is to get the modified transitions that ARE removed
        '''
        trans_mods = []
        for item in self.mod_tracker:
            if self.mod_tracker[item][0] == 1:
                for trans in removed_transitions:
                    if trans.source == item[0] and trans.condition == item[1]:
                        trans_mods.append(trans)
        return trans_mods

    def get_mods(self):
        mods = []
        for item in self.mod_tracker:
            if self.mod_tracker[item][0] == 1:
                mods.append(item)
        return mods

    def copy(self):
        new_mc = ModificationTracker()
        for item in self.mod_tracker:
            new_mc.mod_tracker[item] = self.mod_tracker[item]
        return new_mc

    def write_to_file(self,path):
        # create a condensed version
        condensed_mod_tracker = {}
        for item in self.mod_tracker:
            state_id = item[0].id
            condensed_mod_tracker[(state_id,item[1])] = self.mod_tracker[item]

        with open("{}/best_mod_tracker.pkl".format(path), "wb") as outfile:
            pickle.dump(condensed_mod_tracker,outfile)

    def __str__(self):
        string = ""
        for item in self.mod_tracker:
            string += "{}-{} == {}-{}\n".format(str(item[0]), str(item[1]), str(self.mod_tracker[item][0]), str(self.mod_tracker[item][1]))
        return string
