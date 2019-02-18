class ModificationTracker:

    def __init__(self, TS, inputs):
        self.mod_tracker = {}
        for state in TS.states.values():
            for inp in inputs.alphabet:
                dest = None
                for trans in state.out_trans:
                    if trans.condition == inp:
                        dest = trans.target
                self.mod_tracker[(state,inp)] = [0,dest]

    def update_mod_tracker(self, transition, deleted=False):
        if (transition.source, transition.condition) not in self.mod_tracker:
            return

        if deleted and self.mod_tracker[(transition.source,transition.condition)][1] is None:
            self.mod_tracker[(transition.source,transition.condition)][0] = 0
            #print("deleting, but it was meant to be deleted anyway........")
        elif deleted:
            self.mod_tracker[(transition.source,transition.condition)][0] = 1
            #print("deleting, it was NOT meant to be")
        elif self.mod_tracker[(transition.source,transition.condition)][1] == transition.target:
            self.mod_tracker[(transition.source,transition.condition)][0] = 0
            #print("not deleting, and it was meant to be")
        else:
            self.mod_tracker[(transition.source,transition.condition)][0] = 1
            #print("it was NOT meant to be")

    def check_mod_tracker_sum(self):
        sum = 0
        for item in self.mod_tracker:
            sum += self.mod_tracker[item][0]
        return sum

    def check_mod_tracker_empties(self, removed_transitions):
        sum = 0
        for item in self.mod_tracker:
            if self.mod_tracker[item][0] == 1:
                for trans in removed_transitions:
                    if trans.source == item[0] and trans.condition == item[1]:
                        sum += 1
        return sum

    def get_mod_tracker_nonempty_trans(self, removed_transitions):
        trans_mods = []
        for item in self.mod_tracker:
            if self.mod_tracker[item][0] == 1:
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

    def __str__(self):
        string = ""
        for item in self.mod_tracker:
            string += "{}-{} == {}-{}\n".format(str(item[0]), str(item[1]), str(self.mod_tracker[item][0]), str(self.mod_tracker[item][1]))
        return string
