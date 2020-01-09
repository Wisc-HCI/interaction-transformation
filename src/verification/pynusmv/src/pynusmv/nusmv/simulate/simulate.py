# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_simulate')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_simulate')
    _simulate = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_simulate', [dirname(__file__)])
        except ImportError:
            import _simulate
            return _simulate
        try:
            _mod = imp.load_module('_simulate', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _simulate = swig_import_helper()
    del swig_import_helper
else:
    import _simulate
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

PRIuPTR = _simulate.PRIuPTR
PRIdPTR = _simulate.PRIdPTR
LLU = _simulate.LLU
LLO = _simulate.LLO
LLX = _simulate.LLX
false = _simulate.false
true = _simulate.true
OUTCOME_GENERIC_ERROR = _simulate.OUTCOME_GENERIC_ERROR
OUTCOME_PARSER_ERROR = _simulate.OUTCOME_PARSER_ERROR
OUTCOME_SYNTAX_ERROR = _simulate.OUTCOME_SYNTAX_ERROR
OUTCOME_FILE_ERROR = _simulate.OUTCOME_FILE_ERROR
OUTCOME_SUCCESS_REQUIRED_HELP = _simulate.OUTCOME_SUCCESS_REQUIRED_HELP
OUTCOME_SUCCESS = _simulate.OUTCOME_SUCCESS
Deterministic = _simulate.Deterministic
Random = _simulate.Random
Interactive = _simulate.Interactive

def Simulate_Init() -> "void":
    """Simulate_Init()"""
    return _simulate.Simulate_Init()

def Simulate_End() -> "void":
    """Simulate_End()"""
    return _simulate.Simulate_End()

def Simulate_ChooseOneState(arg1: 'BddFsm_ptr', arg2: 'bdd_ptr', arg3: 'Simulation_Mode', arg4: 'int') -> "bdd_ptr":
    """Simulate_ChooseOneState(BddFsm_ptr arg1, bdd_ptr arg2, Simulation_Mode arg3, int arg4) -> bdd_ptr"""
    return _simulate.Simulate_ChooseOneState(arg1, arg2, arg3, arg4)

def Simulate_ChooseOneStateInput(arg1: 'BddFsm_ptr', arg2: 'bdd_ptr', arg3: 'bdd_ptr', arg4: 'Simulation_Mode', arg5: 'int', arg6: 'bdd_ptr *', arg7: 'bdd_ptr *') -> "void":
    """Simulate_ChooseOneStateInput(BddFsm_ptr arg1, bdd_ptr arg2, bdd_ptr arg3, Simulation_Mode arg4, int arg5, bdd_ptr * arg6, bdd_ptr * arg7)"""
    return _simulate.Simulate_ChooseOneStateInput(arg1, arg2, arg3, arg4, arg5, arg6, arg7)

def Simulate_MultipleSteps(arg1: 'BddFsm_ptr', arg2: 'bdd_ptr', arg3: 'boolean', arg4: 'Simulation_Mode', arg5: 'int', arg6: 'int') -> "node_ptr":
    """Simulate_MultipleSteps(BddFsm_ptr arg1, bdd_ptr arg2, boolean arg3, Simulation_Mode arg4, int arg5, int arg6) -> node_ptr"""
    return _simulate.Simulate_MultipleSteps(arg1, arg2, arg3, arg4, arg5, arg6)

def SimulateTransSet_create(fsm: 'BddFsm_ptr', enc: 'BddEnc_ptr', from_state: 'bdd_ptr', next_states_set: 'bdd_ptr', next_states_count: 'double') -> "SimulateTransSet_ptr":
    """SimulateTransSet_create(BddFsm_ptr fsm, BddEnc_ptr enc, bdd_ptr from_state, bdd_ptr next_states_set, double next_states_count) -> SimulateTransSet_ptr"""
    return _simulate.SimulateTransSet_create(fsm, enc, from_state, next_states_set, next_states_count)

def SimulateTransSet_destroy(arg1: 'SimulateTransSet_ptr') -> "void":
    """SimulateTransSet_destroy(SimulateTransSet_ptr arg1)"""
    return _simulate.SimulateTransSet_destroy(arg1)

def SimulateTransSet_get_from_state(arg1: 'SimulateTransSet_ptr const') -> "bdd_ptr":
    """SimulateTransSet_get_from_state(SimulateTransSet_ptr const arg1) -> bdd_ptr"""
    return _simulate.SimulateTransSet_get_from_state(arg1)

def SimulateTransSet_get_next_state_num(arg1: 'SimulateTransSet_ptr const') -> "int":
    """SimulateTransSet_get_next_state_num(SimulateTransSet_ptr const arg1) -> int"""
    return _simulate.SimulateTransSet_get_next_state_num(arg1)

def SimulateTransSet_get_next_state(arg1: 'SimulateTransSet_ptr const', state_index: 'int') -> "bdd_ptr":
    """SimulateTransSet_get_next_state(SimulateTransSet_ptr const arg1, int state_index) -> bdd_ptr"""
    return _simulate.SimulateTransSet_get_next_state(arg1, state_index)

def SimulateTransSet_get_inputs_num_at_state(arg1: 'SimulateTransSet_ptr const', state_index: 'int') -> "int":
    """SimulateTransSet_get_inputs_num_at_state(SimulateTransSet_ptr const arg1, int state_index) -> int"""
    return _simulate.SimulateTransSet_get_inputs_num_at_state(arg1, state_index)

def SimulateTransSet_get_input_at_state(arg1: 'SimulateTransSet_ptr const', state_index: 'int', input_index: 'int') -> "bdd_ptr":
    """SimulateTransSet_get_input_at_state(SimulateTransSet_ptr const arg1, int state_index, int input_index) -> bdd_ptr"""
    return _simulate.SimulateTransSet_get_input_at_state(arg1, state_index, input_index)

def SimulateTransSet_print(arg1: 'SimulateTransSet_ptr const', show_changes_only: 'boolean', output: 'FILE *') -> "int":
    """SimulateTransSet_print(SimulateTransSet_ptr const arg1, boolean show_changes_only, FILE * output) -> int"""
    return _simulate.SimulateTransSet_print(arg1, show_changes_only, output)

def SimulateTransSet_get_state_input_at(arg1: 'SimulateTransSet_ptr const', index: 'int', state: 'bdd_ptr *', input: 'bdd_ptr *') -> "void":
    """SimulateTransSet_get_state_input_at(SimulateTransSet_ptr const arg1, int index, bdd_ptr * state, bdd_ptr * input)"""
    return _simulate.SimulateTransSet_get_state_input_at(arg1, index, state, input)

def SimulateTransSet_get_state_input_rand(arg1: 'SimulateTransSet_ptr const', state: 'bdd_ptr *', input: 'bdd_ptr *') -> "void":
    """SimulateTransSet_get_state_input_rand(SimulateTransSet_ptr const arg1, bdd_ptr * state, bdd_ptr * input)"""
    return _simulate.SimulateTransSet_get_state_input_rand(arg1, state, input)

def SimulateTransSet_get_state_input_det(arg1: 'SimulateTransSet_ptr const', state: 'bdd_ptr *', input: 'bdd_ptr *') -> "void":
    """SimulateTransSet_get_state_input_det(SimulateTransSet_ptr const arg1, bdd_ptr * state, bdd_ptr * input)"""
    return _simulate.SimulateTransSet_get_state_input_det(arg1, state, input)
# This file is compatible with both classic and new-style classes.


