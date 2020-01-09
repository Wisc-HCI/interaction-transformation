import pynusmv
pynusmv.init.init_nusmv()
pynusmv.glob.load_from_file("../../model.smv")
pynusmv.glob.compute_model()
fsm = pynusmv.glob.prop_database().master.bddFsm
for prop in pynusmv.glob.prop_database():
    spec = prop.expr
    print(spec)
    result = pynusmv.mc.check_ctl_spec(fsm,spec)
    print(result)

    '''
    if result:
        inits = fsm.init
        print(inits)
        tup = pynusmv.mc.explain(fsm,inits,spec)
        for item in tup:
            print(item.get_str_values())
    '''
exit()

# get an initial state
inits = fsm.init
print(inits)
tup = pynusmv.mc.explain(fsm,inits,spec)
for item in tup:
    print(item.get_str_values())
#init = inits.pick_one_state()

#if not result:
