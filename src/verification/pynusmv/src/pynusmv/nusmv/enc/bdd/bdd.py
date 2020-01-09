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
        mname = '.'.join((pkg, '_bdd')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_bdd')
    _bdd = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_bdd', [dirname(__file__)])
        except ImportError:
            import _bdd
            return _bdd
        try:
            _mod = imp.load_module('_bdd', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _bdd = swig_import_helper()
    del swig_import_helper
else:
    import _bdd
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


def bddenc2baseenc(bdd_enc: 'BddEnc_ptr') -> "BaseEnc_ptr":
    """bddenc2baseenc(BddEnc_ptr bdd_enc) -> BaseEnc_ptr"""
    return _bdd.bddenc2baseenc(bdd_enc)

def pick_one_state(arg1: 'BddEnc_ptr const', states: 'bdd_ptr') -> "bdd_ptr":
    """pick_one_state(BddEnc_ptr const arg1, bdd_ptr states) -> bdd_ptr"""
    return _bdd.pick_one_state(arg1, states)

def pick_one_state_rand(arg1: 'BddEnc_ptr const', states: 'bdd_ptr') -> "bdd_ptr":
    """pick_one_state_rand(BddEnc_ptr const arg1, bdd_ptr states) -> bdd_ptr"""
    return _bdd.pick_one_state_rand(arg1, states)

def pick_one_input(arg1: 'BddEnc_ptr const', inputs: 'bdd_ptr') -> "bdd_ptr":
    """pick_one_input(BddEnc_ptr const arg1, bdd_ptr inputs) -> bdd_ptr"""
    return _bdd.pick_one_input(arg1, inputs)

def pick_one_input_rand(arg1: 'BddEnc_ptr const', inputs: 'bdd_ptr') -> "bdd_ptr":
    """pick_one_input_rand(BddEnc_ptr const arg1, bdd_ptr inputs) -> bdd_ptr"""
    return _bdd.pick_one_input_rand(arg1, inputs)

def bdd_dup(dd_node: 'bdd_ptr') -> "bdd_ptr":
    """bdd_dup(bdd_ptr dd_node) -> bdd_ptr"""
    return _bdd.bdd_dup(dd_node)

def new_bddArray(nelements: 'size_t') -> "bdd_ptr *":
    """new_bddArray(size_t nelements) -> bdd_ptr *"""
    return _bdd.new_bddArray(nelements)

def delete_bddArray(ary: 'bdd_ptr *') -> "void":
    """delete_bddArray(bdd_ptr * ary)"""
    return _bdd.delete_bddArray(ary)

def bddArray_getitem(ary: 'bdd_ptr *', index: 'size_t') -> "bdd_ptr":
    """bddArray_getitem(bdd_ptr * ary, size_t index) -> bdd_ptr"""
    return _bdd.bddArray_getitem(ary, index)

def bddArray_setitem(ary: 'bdd_ptr *', index: 'size_t', value: 'bdd_ptr') -> "void":
    """bddArray_setitem(bdd_ptr * ary, size_t index, bdd_ptr value)"""
    return _bdd.bddArray_setitem(ary, index, value)


def pick_all_terms_states(bddenc, bdd):
# count states
    count = int(BddEnc_count_states_of_bdd(bddenc, bdd))

    if count <= 0:
        return (0, tuple())

# init array
    array = new_bddArray(count)
    for i in range(count):
        bddArray_setitem(array, i, None)

# call function
    err = _pick_all_terms_states(bddenc, bdd, array, count)

    if err:
        delete_bddArray(array)
        return (err, tuple())

    else:
# create tuple from array
        l = list()
        for i in range(count):
            if bddArray_getitem(array, i) is not None:
                l.append(bddArray_getitem(array, i))
        t = tuple(l)

# delete array
        delete_bddArray(array)

        return (err, t)


def pick_all_terms_inputs(bddenc, bdd):
# count states
    count = int(BddEnc_count_inputs_of_bdd(bddenc, bdd))

    if count <= 0:
        return (0, tuple())

# init array
    array = new_bddArray(count)
    for i in range(count):
        bddArray_setitem(array, i, None)

# call function
    err = _pick_all_terms_inputs(bddenc, bdd, array, count)

    if err:
        delete_bddArray(array)
        return (err, tuple())

    else:
# create tuple from array
        l = list()
        for i in range(count):
            if bddArray_getitem(array, i) is not None:
                l.append(bddArray_getitem(array, i))
        t = tuple(l)

# delete array
        delete_bddArray(array)

        return (err, t)

def pick_all_terms_states_inputs(bddenc, bdd):
# count states
    count = int(BddEnc_count_states_inputs_of_bdd(bddenc, bdd))

    if count <= 0:
        return (0, tuple())

# init array
    array = new_bddArray(count)
    for i in range(count):
        bddArray_setitem(array, i, None)

# call function
    err = _pick_all_terms_states_inputs(bddenc, bdd, array, count)

    if err:
        delete_bddArray(array)
        return (err, tuple())

    else:
# create tuple from array
        l = list()
        for i in range(count):
            if bddArray_getitem(array, i) is not None:
                l.append(bddArray_getitem(array, i))
        t = tuple(l)

# delete array
        delete_bddArray(array)

        return (err, t)


def _pick_all_terms_states(arg1: 'BddEnc_ptr const', bdd: 'bdd_ptr', result_array: 'bdd_ptr *', array_len: 'int const') -> "boolean":
    """_pick_all_terms_states(BddEnc_ptr const arg1, bdd_ptr bdd, bdd_ptr * result_array, int const array_len) -> boolean"""
    return _bdd._pick_all_terms_states(arg1, bdd, result_array, array_len)

def _pick_all_terms_inputs(arg1: 'BddEnc_ptr const', bdd: 'bdd_ptr', result_array: 'bdd_ptr *', array_len: 'int const') -> "boolean":
    """_pick_all_terms_inputs(BddEnc_ptr const arg1, bdd_ptr bdd, bdd_ptr * result_array, int const array_len) -> boolean"""
    return _bdd._pick_all_terms_inputs(arg1, bdd, result_array, array_len)

def _pick_all_terms_states_inputs(arg1: 'BddEnc_ptr const', bdd: 'bdd_ptr', result_array: 'bdd_ptr *', array_len: 'int const') -> "boolean":
    """_pick_all_terms_states_inputs(BddEnc_ptr const arg1, bdd_ptr bdd, bdd_ptr * result_array, int const array_len) -> boolean"""
    return _bdd._pick_all_terms_states_inputs(arg1, bdd, result_array, array_len)

def pick_one_state_input(arg1: 'BddEnc_ptr const', si: 'bdd_ptr') -> "bdd_ptr":
    """pick_one_state_input(BddEnc_ptr const arg1, bdd_ptr si) -> bdd_ptr"""
    return _bdd.pick_one_state_input(arg1, si)

def pick_one_state_input_rand(arg1: 'BddEnc_ptr const', si: 'bdd_ptr') -> "bdd_ptr":
    """pick_one_state_input_rand(BddEnc_ptr const arg1, bdd_ptr si) -> bdd_ptr"""
    return _bdd.pick_one_state_input_rand(arg1, si)

def BddEnc_force_order_from_filename(arg1: 'BddEnc_ptr const', filename: 'char const *') -> "int":
    """BddEnc_force_order_from_filename(BddEnc_ptr const arg1, char const * filename) -> int"""
    return _bdd.BddEnc_force_order_from_filename(arg1, filename)
PRIuPTR = _bdd.PRIuPTR
PRIdPTR = _bdd.PRIdPTR
LLU = _bdd.LLU
LLO = _bdd.LLO
LLX = _bdd.LLX
false = _bdd.false
true = _bdd.true
OUTCOME_GENERIC_ERROR = _bdd.OUTCOME_GENERIC_ERROR
OUTCOME_PARSER_ERROR = _bdd.OUTCOME_PARSER_ERROR
OUTCOME_SYNTAX_ERROR = _bdd.OUTCOME_SYNTAX_ERROR
OUTCOME_FILE_ERROR = _bdd.OUTCOME_FILE_ERROR
OUTCOME_SUCCESS_REQUIRED_HELP = _bdd.OUTCOME_SUCCESS_REQUIRED_HELP
OUTCOME_SUCCESS = _bdd.OUTCOME_SUCCESS

def Object_destroy(arg1: 'Object_ptr', arg: 'void *') -> "void":
    """Object_destroy(Object_ptr arg1, void * arg)"""
    return _bdd.Object_destroy(arg1, arg)

def Object_copy(arg1: 'Object_ptr const') -> "Object_ptr":
    """Object_copy(Object_ptr const arg1) -> Object_ptr"""
    return _bdd.Object_copy(arg1)
DUMP_DEFAULT = _bdd.DUMP_DEFAULT
DUMP_BITS = _bdd.DUMP_BITS
DUMP_SCALARS_ONLY = _bdd.DUMP_SCALARS_ONLY

def BddEnc_create(symb_table: 'SymbTable_ptr', bool_enc: 'BoolEnc_ptr', dd_vars_hndr: 'VarsHandler_ptr', ord_groups: 'OrdGroups_ptr') -> "BddEnc_ptr":
    """BddEnc_create(SymbTable_ptr symb_table, BoolEnc_ptr bool_enc, VarsHandler_ptr dd_vars_hndr, OrdGroups_ptr ord_groups) -> BddEnc_ptr"""
    return _bdd.BddEnc_create(symb_table, bool_enc, dd_vars_hndr, ord_groups)

def BddEnc_destroy(arg1: 'BddEnc_ptr') -> "void":
    """BddEnc_destroy(BddEnc_ptr arg1)"""
    return _bdd.BddEnc_destroy(arg1)

def BddEnc_get_dd_vars_handler(arg1: 'BddEnc_ptr const') -> "VarsHandler_ptr":
    """BddEnc_get_dd_vars_handler(BddEnc_ptr const arg1) -> VarsHandler_ptr"""
    return _bdd.BddEnc_get_dd_vars_handler(arg1)

def BddEnc_get_dd_manager(arg1: 'BddEnc_ptr const') -> "DdManager *":
    """BddEnc_get_dd_manager(BddEnc_ptr const arg1) -> DdManager *"""
    return _bdd.BddEnc_get_dd_manager(arg1)

def BddEnc_get_ord_groups(arg1: 'BddEnc_ptr const') -> "OrdGroups_ptr":
    """BddEnc_get_ord_groups(BddEnc_ptr const arg1) -> OrdGroups_ptr"""
    return _bdd.BddEnc_get_ord_groups(arg1)

def BddEnc_expr_to_add(arg1: 'BddEnc_ptr', expr: 'Expr_ptr const', context: 'node_ptr const') -> "add_ptr":
    """BddEnc_expr_to_add(BddEnc_ptr arg1, Expr_ptr const expr, node_ptr const context) -> add_ptr"""
    return _bdd.BddEnc_expr_to_add(arg1, expr, context)

def BddEnc_expr_to_addarray(arg1: 'BddEnc_ptr', expr: 'Expr_ptr const', context: 'node_ptr const') -> "AddArray_ptr":
    """BddEnc_expr_to_addarray(BddEnc_ptr arg1, Expr_ptr const expr, node_ptr const context) -> AddArray_ptr"""
    return _bdd.BddEnc_expr_to_addarray(arg1, expr, context)

def BddEnc_expr_to_bdd(arg1: 'BddEnc_ptr', expr: 'Expr_ptr const', context: 'node_ptr const') -> "bdd_ptr":
    """BddEnc_expr_to_bdd(BddEnc_ptr arg1, Expr_ptr const expr, node_ptr const context) -> bdd_ptr"""
    return _bdd.BddEnc_expr_to_bdd(arg1, expr, context)

def BddEnc_add_to_expr(arg1: 'BddEnc_ptr', add: 'add_ptr const', det_layer: 'SymbLayer_ptr') -> "node_ptr":
    """BddEnc_add_to_expr(BddEnc_ptr arg1, add_ptr const add, SymbLayer_ptr det_layer) -> node_ptr"""
    return _bdd.BddEnc_add_to_expr(arg1, add, det_layer)

def BddEnc_add_to_scalar_expr(arg1: 'BddEnc_ptr', add: 'add_ptr const', det_layer: 'SymbLayer_ptr') -> "node_ptr":
    """BddEnc_add_to_scalar_expr(BddEnc_ptr arg1, add_ptr const add, SymbLayer_ptr det_layer) -> node_ptr"""
    return _bdd.BddEnc_add_to_scalar_expr(arg1, add, det_layer)

def BddEnc_bdd_to_expr(arg1: 'BddEnc_ptr', bdd: 'bdd_ptr const') -> "node_ptr":
    """BddEnc_bdd_to_expr(BddEnc_ptr arg1, bdd_ptr const bdd) -> node_ptr"""
    return _bdd.BddEnc_bdd_to_expr(arg1, bdd)

def BddEnc_get_state_vars_cube(arg1: 'BddEnc_ptr const') -> "BddVarSet_ptr":
    """BddEnc_get_state_vars_cube(BddEnc_ptr const arg1) -> BddVarSet_ptr"""
    return _bdd.BddEnc_get_state_vars_cube(arg1)

def BddEnc_get_next_state_vars_cube(arg1: 'BddEnc_ptr const') -> "BddVarSet_ptr":
    """BddEnc_get_next_state_vars_cube(BddEnc_ptr const arg1) -> BddVarSet_ptr"""
    return _bdd.BddEnc_get_next_state_vars_cube(arg1)

def BddEnc_get_frozen_vars_cube(arg1: 'BddEnc_ptr const') -> "BddVarSet_ptr":
    """BddEnc_get_frozen_vars_cube(BddEnc_ptr const arg1) -> BddVarSet_ptr"""
    return _bdd.BddEnc_get_frozen_vars_cube(arg1)

def BddEnc_get_state_frozen_vars_cube(arg1: 'BddEnc_ptr const') -> "BddVarSet_ptr":
    """BddEnc_get_state_frozen_vars_cube(BddEnc_ptr const arg1) -> BddVarSet_ptr"""
    return _bdd.BddEnc_get_state_frozen_vars_cube(arg1)

def BddEnc_get_input_vars_cube(arg1: 'BddEnc_ptr const') -> "BddVarSet_ptr":
    """BddEnc_get_input_vars_cube(BddEnc_ptr const arg1) -> BddVarSet_ptr"""
    return _bdd.BddEnc_get_input_vars_cube(arg1)

def BddEnc_get_layer_vars_cube(arg1: 'BddEnc_ptr const', layer: 'SymbLayer_ptr', vt: 'SymbFilterType') -> "BddVarSet_ptr":
    """BddEnc_get_layer_vars_cube(BddEnc_ptr const arg1, SymbLayer_ptr layer, SymbFilterType vt) -> BddVarSet_ptr"""
    return _bdd.BddEnc_get_layer_vars_cube(arg1, layer, vt)

def BddEnc_is_var_in_cube(arg1: 'BddEnc_ptr const', name: 'node_ptr', cube: 'add_ptr') -> "boolean":
    """BddEnc_is_var_in_cube(BddEnc_ptr const arg1, node_ptr name, add_ptr cube) -> boolean"""
    return _bdd.BddEnc_is_var_in_cube(arg1, name, cube)

def BddEnc_state_var_to_next_state_var_add(arg1: 'BddEnc_ptr const', add: 'add_ptr') -> "add_ptr":
    """BddEnc_state_var_to_next_state_var_add(BddEnc_ptr const arg1, add_ptr add) -> add_ptr"""
    return _bdd.BddEnc_state_var_to_next_state_var_add(arg1, add)

def BddEnc_next_state_var_to_state_var_add(arg1: 'BddEnc_ptr const', add: 'add_ptr') -> "add_ptr":
    """BddEnc_next_state_var_to_state_var_add(BddEnc_ptr const arg1, add_ptr add) -> add_ptr"""
    return _bdd.BddEnc_next_state_var_to_state_var_add(arg1, add)

def BddEnc_state_var_to_next_state_var(arg1: 'BddEnc_ptr const', bdd: 'bdd_ptr') -> "bdd_ptr":
    """BddEnc_state_var_to_next_state_var(BddEnc_ptr const arg1, bdd_ptr bdd) -> bdd_ptr"""
    return _bdd.BddEnc_state_var_to_next_state_var(arg1, bdd)

def BddEnc_next_state_var_to_state_var(arg1: 'BddEnc_ptr const', bdd: 'bdd_ptr') -> "bdd_ptr":
    """BddEnc_next_state_var_to_state_var(BddEnc_ptr const arg1, bdd_ptr bdd) -> bdd_ptr"""
    return _bdd.BddEnc_next_state_var_to_state_var(arg1, bdd)

def BddEnc_print_bdd_begin(arg1: 'BddEnc_ptr', symbols: 'NodeList_ptr', changes_only: 'boolean') -> "void":
    """BddEnc_print_bdd_begin(BddEnc_ptr arg1, NodeList_ptr symbols, boolean changes_only)"""
    return _bdd.BddEnc_print_bdd_begin(arg1, symbols, changes_only)

def BddEnc_print_bdd_end(arg1: 'BddEnc_ptr') -> "void":
    """BddEnc_print_bdd_end(BddEnc_ptr arg1)"""
    return _bdd.BddEnc_print_bdd_end(arg1)

def BddEnc_print_bdd(arg1: 'BddEnc_ptr', bdd: 'bdd_ptr', p_fun: 'VPFNNF', file: 'FILE *') -> "int":
    """BddEnc_print_bdd(BddEnc_ptr arg1, bdd_ptr bdd, VPFNNF p_fun, FILE * file) -> int"""
    return _bdd.BddEnc_print_bdd(arg1, bdd, p_fun, file)

def BddEnc_print_set_of_states(arg1: 'BddEnc_ptr', states: 'bdd_ptr', changes_only: 'boolean', print_defines: 'boolean', p_fun: 'VPFNNF', file: 'FILE *') -> "void":
    """BddEnc_print_set_of_states(BddEnc_ptr arg1, bdd_ptr states, boolean changes_only, boolean print_defines, VPFNNF p_fun, FILE * file)"""
    return _bdd.BddEnc_print_set_of_states(arg1, states, changes_only, print_defines, p_fun, file)

def BddEnc_print_set_of_inputs(arg1: 'BddEnc_ptr', inputs: 'bdd_ptr', changes_only: 'boolean', p_fun: 'VPFNNF', file: 'FILE *') -> "void":
    """BddEnc_print_set_of_inputs(BddEnc_ptr arg1, bdd_ptr inputs, boolean changes_only, VPFNNF p_fun, FILE * file)"""
    return _bdd.BddEnc_print_set_of_inputs(arg1, inputs, changes_only, p_fun, file)

def BddEnc_print_set_of_state_input_pairs(arg1: 'BddEnc_ptr', state_input_pairs: 'bdd_ptr', changes_only: 'boolean', p_fun: 'VPFNNF', file: 'FILE *') -> "void":
    """BddEnc_print_set_of_state_input_pairs(BddEnc_ptr arg1, bdd_ptr state_input_pairs, boolean changes_only, VPFNNF p_fun, FILE * file)"""
    return _bdd.BddEnc_print_set_of_state_input_pairs(arg1, state_input_pairs, changes_only, p_fun, file)

def BddEnc_print_set_of_trans_models(arg1: 'BddEnc_ptr', state_input_pairs: 'bdd_ptr', file: 'FILE *') -> "void":
    """BddEnc_print_set_of_trans_models(BddEnc_ptr arg1, bdd_ptr state_input_pairs, FILE * file)"""
    return _bdd.BddEnc_print_set_of_trans_models(arg1, state_input_pairs, file)

def BddEnc_assign_symbols(arg1: 'BddEnc_ptr', bdd: 'bdd_ptr', symbols: 'NodeList_ptr', onlyRequiredSymbs: 'boolean', resultBdd: 'bdd_ptr *') -> "node_ptr":
    """BddEnc_assign_symbols(BddEnc_ptr arg1, bdd_ptr bdd, NodeList_ptr symbols, boolean onlyRequiredSymbs, bdd_ptr * resultBdd) -> node_ptr"""
    return _bdd.BddEnc_assign_symbols(arg1, bdd, symbols, onlyRequiredSymbs, resultBdd)

def BddEnc_print_vars_in_cube(arg1: 'BddEnc_ptr', cube: 'bdd_ptr', list_of_sym: 'node_ptr', file: 'FILE *') -> "void":
    """BddEnc_print_vars_in_cube(BddEnc_ptr arg1, bdd_ptr cube, node_ptr list_of_sym, FILE * file)"""
    return _bdd.BddEnc_print_vars_in_cube(arg1, cube, list_of_sym, file)

def BddEnc_get_var_ordering(arg1: 'BddEnc_ptr const', ord_type: 'VarOrderingType const') -> "NodeList_ptr":
    """BddEnc_get_var_ordering(BddEnc_ptr const arg1, VarOrderingType const ord_type) -> NodeList_ptr"""
    return _bdd.BddEnc_get_var_ordering(arg1, ord_type)

def BddEnc_write_var_ordering(arg1: 'BddEnc_ptr const', output_order_file_name: 'char const *', dump_type: 'VarOrderingType const') -> "void":
    """BddEnc_write_var_ordering(BddEnc_ptr const arg1, char const * output_order_file_name, VarOrderingType const dump_type)"""
    return _bdd.BddEnc_write_var_ordering(arg1, output_order_file_name, dump_type)

def BddEnc_get_reordering_count(arg1: 'BddEnc_ptr const') -> "int":
    """BddEnc_get_reordering_count(BddEnc_ptr const arg1) -> int"""
    return _bdd.BddEnc_get_reordering_count(arg1)

def BddEnc_reset_reordering_count(arg1: 'BddEnc_ptr') -> "void":
    """BddEnc_reset_reordering_count(BddEnc_ptr arg1)"""
    return _bdd.BddEnc_reset_reordering_count(arg1)

def BddEnc_count_states_of_add(arg1: 'BddEnc_ptr const', add: 'add_ptr') -> "double":
    """BddEnc_count_states_of_add(BddEnc_ptr const arg1, add_ptr add) -> double"""
    return _bdd.BddEnc_count_states_of_add(arg1, add)

def BddEnc_count_states_of_bdd(arg1: 'BddEnc_ptr const', bdd: 'bdd_ptr') -> "double":
    """BddEnc_count_states_of_bdd(BddEnc_ptr const arg1, bdd_ptr bdd) -> double"""
    return _bdd.BddEnc_count_states_of_bdd(arg1, bdd)

def BddEnc_count_inputs_of_bdd(arg1: 'BddEnc_ptr const', bdd: 'bdd_ptr') -> "double":
    """BddEnc_count_inputs_of_bdd(BddEnc_ptr const arg1, bdd_ptr bdd) -> double"""
    return _bdd.BddEnc_count_inputs_of_bdd(arg1, bdd)

def BddEnc_count_states_inputs_of_bdd(arg1: 'BddEnc_ptr const', bdd: 'bdd_ptr') -> "double":
    """BddEnc_count_states_inputs_of_bdd(BddEnc_ptr const arg1, bdd_ptr bdd) -> double"""
    return _bdd.BddEnc_count_states_inputs_of_bdd(arg1, bdd)

def BddEnc_get_minterms_of_add(arg1: 'BddEnc_ptr const', add: 'add_ptr') -> "double":
    """BddEnc_get_minterms_of_add(BddEnc_ptr const arg1, add_ptr add) -> double"""
    return _bdd.BddEnc_get_minterms_of_add(arg1, add)

def BddEnc_get_minterms_of_bdd(arg1: 'BddEnc_ptr const', bdd: 'bdd_ptr') -> "double":
    """BddEnc_get_minterms_of_bdd(BddEnc_ptr const arg1, bdd_ptr bdd) -> double"""
    return _bdd.BddEnc_get_minterms_of_bdd(arg1, bdd)

def BddEnc_pick_one_state(arg1: 'BddEnc_ptr const', states: 'bdd_ptr') -> "bdd_ptr":
    """BddEnc_pick_one_state(BddEnc_ptr const arg1, bdd_ptr states) -> bdd_ptr"""
    return _bdd.BddEnc_pick_one_state(arg1, states)

def BddEnc_pick_one_input(arg1: 'BddEnc_ptr const', inputs: 'bdd_ptr') -> "bdd_ptr":
    """BddEnc_pick_one_input(BddEnc_ptr const arg1, bdd_ptr inputs) -> bdd_ptr"""
    return _bdd.BddEnc_pick_one_input(arg1, inputs)

def BddEnc_pick_all_terms_states_inputs(arg1: 'BddEnc_ptr const', bdd: 'bdd_ptr', result_array: 'bdd_ptr *', array_len: 'int const') -> "boolean":
    """BddEnc_pick_all_terms_states_inputs(BddEnc_ptr const arg1, bdd_ptr bdd, bdd_ptr * result_array, int const array_len) -> boolean"""
    return _bdd.BddEnc_pick_all_terms_states_inputs(arg1, bdd, result_array, array_len)

def BddEnc_pick_all_terms_states(arg1: 'BddEnc_ptr const', bdd: 'bdd_ptr', result_array: 'bdd_ptr *', array_len: 'int const') -> "boolean":
    """BddEnc_pick_all_terms_states(BddEnc_ptr const arg1, bdd_ptr bdd, bdd_ptr * result_array, int const array_len) -> boolean"""
    return _bdd.BddEnc_pick_all_terms_states(arg1, bdd, result_array, array_len)

def BddEnc_pick_all_terms_inputs(arg1: 'BddEnc_ptr const', bdd: 'bdd_ptr', result_array: 'bdd_ptr *', array_len: 'int const') -> "boolean":
    """BddEnc_pick_all_terms_inputs(BddEnc_ptr const arg1, bdd_ptr bdd, bdd_ptr * result_array, int const array_len) -> boolean"""
    return _bdd.BddEnc_pick_all_terms_inputs(arg1, bdd, result_array, array_len)

def BddEnc_pick_one_state_rand(arg1: 'BddEnc_ptr const', states: 'bdd_ptr') -> "bdd_ptr":
    """BddEnc_pick_one_state_rand(BddEnc_ptr const arg1, bdd_ptr states) -> bdd_ptr"""
    return _bdd.BddEnc_pick_one_state_rand(arg1, states)

def BddEnc_pick_one_input_rand(arg1: 'BddEnc_ptr const', inputs: 'bdd_ptr') -> "bdd_ptr":
    """BddEnc_pick_one_input_rand(BddEnc_ptr const arg1, bdd_ptr inputs) -> bdd_ptr"""
    return _bdd.BddEnc_pick_one_input_rand(arg1, inputs)

def BddEnc_get_var_name_from_index(arg1: 'BddEnc_ptr const', index: 'int') -> "node_ptr":
    """BddEnc_get_var_name_from_index(BddEnc_ptr const arg1, int index) -> node_ptr"""
    return _bdd.BddEnc_get_var_name_from_index(arg1, index)

def BddEnc_has_var_at_index(arg1: 'BddEnc_ptr const', index: 'int') -> "boolean":
    """BddEnc_has_var_at_index(BddEnc_ptr const arg1, int index) -> boolean"""
    return _bdd.BddEnc_has_var_at_index(arg1, index)

def BddEnc_get_var_index_from_name(arg1: 'BddEnc_ptr const', name: 'node_ptr') -> "int":
    """BddEnc_get_var_index_from_name(BddEnc_ptr const arg1, node_ptr name) -> int"""
    return _bdd.BddEnc_get_var_index_from_name(arg1, name)

def BddEnc_constant_to_add(arg1: 'BddEnc_ptr const', constant: 'node_ptr') -> "add_ptr":
    """BddEnc_constant_to_add(BddEnc_ptr const arg1, node_ptr constant) -> add_ptr"""
    return _bdd.BddEnc_constant_to_add(arg1, constant)

def BddEnc_eval_sign_add(arg1: 'BddEnc_ptr', a: 'add_ptr', flag: 'int') -> "add_ptr":
    """BddEnc_eval_sign_add(BddEnc_ptr arg1, add_ptr a, int flag) -> add_ptr"""
    return _bdd.BddEnc_eval_sign_add(arg1, a, flag)

def BddEnc_eval_sign_bdd(arg1: 'BddEnc_ptr', a: 'bdd_ptr', flag: 'int') -> "bdd_ptr":
    """BddEnc_eval_sign_bdd(BddEnc_ptr arg1, bdd_ptr a, int flag) -> bdd_ptr"""
    return _bdd.BddEnc_eval_sign_bdd(arg1, a, flag)

def BddEnc_eval_num(arg1: 'BddEnc_ptr', e: 'node_ptr', context: 'node_ptr') -> "int":
    """BddEnc_eval_num(BddEnc_ptr arg1, node_ptr e, node_ptr context) -> int"""
    return _bdd.BddEnc_eval_num(arg1, e, context)

def BddEnc_eval_constant(arg1: 'BddEnc_ptr', expr: 'Expr_ptr', context: 'node_ptr') -> "add_ptr":
    """BddEnc_eval_constant(BddEnc_ptr arg1, Expr_ptr expr, node_ptr context) -> add_ptr"""
    return _bdd.BddEnc_eval_constant(arg1, expr, context)

def BddEnc_get_symbol_add(arg1: 'BddEnc_ptr', name: 'node_ptr') -> "AddArray_ptr":
    """BddEnc_get_symbol_add(BddEnc_ptr arg1, node_ptr name) -> AddArray_ptr"""
    return _bdd.BddEnc_get_symbol_add(arg1, name)

def BddEnc_get_state_frozen_vars_mask_add(arg1: 'BddEnc_ptr') -> "add_ptr":
    """BddEnc_get_state_frozen_vars_mask_add(BddEnc_ptr arg1) -> add_ptr"""
    return _bdd.BddEnc_get_state_frozen_vars_mask_add(arg1)

def BddEnc_get_input_vars_mask_add(arg1: 'BddEnc_ptr') -> "add_ptr":
    """BddEnc_get_input_vars_mask_add(BddEnc_ptr arg1) -> add_ptr"""
    return _bdd.BddEnc_get_input_vars_mask_add(arg1)

def BddEnc_get_state_frozen_input_vars_mask_add(arg1: 'BddEnc_ptr') -> "add_ptr":
    """BddEnc_get_state_frozen_input_vars_mask_add(BddEnc_ptr arg1) -> add_ptr"""
    return _bdd.BddEnc_get_state_frozen_input_vars_mask_add(arg1)

def BddEnc_get_state_frozen_vars_mask_bdd(arg1: 'BddEnc_ptr') -> "bdd_ptr":
    """BddEnc_get_state_frozen_vars_mask_bdd(BddEnc_ptr arg1) -> bdd_ptr"""
    return _bdd.BddEnc_get_state_frozen_vars_mask_bdd(arg1)

def BddEnc_get_input_vars_mask_bdd(arg1: 'BddEnc_ptr') -> "bdd_ptr":
    """BddEnc_get_input_vars_mask_bdd(BddEnc_ptr arg1) -> bdd_ptr"""
    return _bdd.BddEnc_get_input_vars_mask_bdd(arg1)

def BddEnc_get_state_frozen_input_vars_mask_bdd(arg1: 'BddEnc_ptr') -> "bdd_ptr":
    """BddEnc_get_state_frozen_input_vars_mask_bdd(BddEnc_ptr arg1) -> bdd_ptr"""
    return _bdd.BddEnc_get_state_frozen_input_vars_mask_bdd(arg1)

def BddEnc_apply_state_frozen_vars_mask_add(arg1: 'BddEnc_ptr', states: 'add_ptr') -> "add_ptr":
    """BddEnc_apply_state_frozen_vars_mask_add(BddEnc_ptr arg1, add_ptr states) -> add_ptr"""
    return _bdd.BddEnc_apply_state_frozen_vars_mask_add(arg1, states)

def BddEnc_apply_input_vars_mask_add(arg1: 'BddEnc_ptr', inputs: 'add_ptr') -> "add_ptr":
    """BddEnc_apply_input_vars_mask_add(BddEnc_ptr arg1, add_ptr inputs) -> add_ptr"""
    return _bdd.BddEnc_apply_input_vars_mask_add(arg1, inputs)

def BddEnc_apply_state_frozen_input_vars_mask_add(arg1: 'BddEnc_ptr', states_inputs: 'add_ptr') -> "add_ptr":
    """BddEnc_apply_state_frozen_input_vars_mask_add(BddEnc_ptr arg1, add_ptr states_inputs) -> add_ptr"""
    return _bdd.BddEnc_apply_state_frozen_input_vars_mask_add(arg1, states_inputs)

def BddEnc_apply_state_frozen_vars_mask_bdd(arg1: 'BddEnc_ptr', states: 'BddStates') -> "BddStates":
    """BddEnc_apply_state_frozen_vars_mask_bdd(BddEnc_ptr arg1, BddStates states) -> BddStates"""
    return _bdd.BddEnc_apply_state_frozen_vars_mask_bdd(arg1, states)

def BddEnc_apply_input_vars_mask_bdd(arg1: 'BddEnc_ptr', inputs: 'BddInputs') -> "BddInputs":
    """BddEnc_apply_input_vars_mask_bdd(BddEnc_ptr arg1, BddInputs inputs) -> BddInputs"""
    return _bdd.BddEnc_apply_input_vars_mask_bdd(arg1, inputs)

def BddEnc_apply_state_frozen_input_vars_mask_bdd(arg1: 'BddEnc_ptr', states_inputs: 'BddStatesInputs') -> "BddStatesInputs":
    """BddEnc_apply_state_frozen_input_vars_mask_bdd(BddEnc_ptr arg1, BddStatesInputs states_inputs) -> BddStatesInputs"""
    return _bdd.BddEnc_apply_state_frozen_input_vars_mask_bdd(arg1, states_inputs)

def BddEnc_get_var_mask(arg1: 'BddEnc_ptr', var_name: 'node_ptr') -> "add_ptr":
    """BddEnc_get_var_mask(BddEnc_ptr arg1, node_ptr var_name) -> add_ptr"""
    return _bdd.BddEnc_get_var_mask(arg1, var_name)

def BddEnc_ComputePrimeImplicants(arg1: 'BddEnc_ptr', layer_names: 'array_t const *', formula: 'bdd_ptr') -> "array_t *":
    """BddEnc_ComputePrimeImplicants(BddEnc_ptr arg1, array_t const * layer_names, bdd_ptr formula) -> array_t *"""
    return _bdd.BddEnc_ComputePrimeImplicants(arg1, layer_names, formula)

def BddEnc_force_order(arg1: 'BddEnc_ptr', new_po_grps: 'OrdGroups_ptr') -> "void":
    """BddEnc_force_order(BddEnc_ptr arg1, OrdGroups_ptr new_po_grps)"""
    return _bdd.BddEnc_force_order(arg1, new_po_grps)

def BddEnc_force_order_from_file(arg1: 'BddEnc_ptr', orderfile: 'FILE *') -> "void":
    """BddEnc_force_order_from_file(BddEnc_ptr arg1, FILE * orderfile)"""
    return _bdd.BddEnc_force_order_from_file(arg1, orderfile)

def BddEnc_print_bdd_wff(arg1: 'BddEnc_ptr', bdd: 'bdd_ptr', vars: 'NodeList_ptr', do_sharing: 'boolean', do_indent: 'boolean', start_at_column: 'int', out: 'FILE *') -> "void":
    """BddEnc_print_bdd_wff(BddEnc_ptr arg1, bdd_ptr bdd, NodeList_ptr vars, boolean do_sharing, boolean do_indent, int start_at_column, FILE * out)"""
    return _bdd.BddEnc_print_bdd_wff(arg1, bdd, vars, do_sharing, do_indent, start_at_column, out)

def BddEnc_print_formula_info(arg1: 'BddEnc_ptr', formula: 'Expr_ptr', print_models: 'boolean', print_formula: 'boolean', out: 'FILE *') -> "void":
    """BddEnc_print_formula_info(BddEnc_ptr arg1, Expr_ptr formula, boolean print_models, boolean print_formula, FILE * out)"""
    return _bdd.BddEnc_print_formula_info(arg1, formula, print_models, print_formula, out)

def BddEnc_bdd_to_wff(arg1: 'BddEnc_ptr', bdd: 'bdd_ptr', vars: 'NodeList_ptr') -> "node_ptr":
    """BddEnc_bdd_to_wff(BddEnc_ptr arg1, bdd_ptr bdd, NodeList_ptr vars) -> node_ptr"""
    return _bdd.BddEnc_bdd_to_wff(arg1, bdd, vars)

def BddEnc_clean_evaluation_cache(arg1: 'BddEnc_ptr') -> "void":
    """BddEnc_clean_evaluation_cache(BddEnc_ptr arg1)"""
    return _bdd.BddEnc_clean_evaluation_cache(arg1)

def BddEnc_get_vars_cube(arg1: 'BddEnc_ptr const', vars: 'Set_t', vt: 'SymbFilterType') -> "BddVarSet_ptr":
    """BddEnc_get_vars_cube(BddEnc_ptr const arg1, Set_t vars, SymbFilterType vt) -> BddVarSet_ptr"""
    return _bdd.BddEnc_get_vars_cube(arg1, vars, vt)

def BddEnc_get_unfiltered_vars_cube(arg1: 'BddEnc_ptr const', vars: 'Set_t') -> "BddVarSet_ptr":
    """BddEnc_get_unfiltered_vars_cube(BddEnc_ptr const arg1, Set_t vars) -> BddVarSet_ptr"""
    return _bdd.BddEnc_get_unfiltered_vars_cube(arg1, vars)

def BddEnc_dump_addarray_dot(arg1: 'BddEnc_ptr', addarray: 'AddArray_ptr', labels: 'char const **', outfile: 'FILE *') -> "int":
    """BddEnc_dump_addarray_dot(BddEnc_ptr arg1, AddArray_ptr addarray, char const ** labels, FILE * outfile) -> int"""
    return _bdd.BddEnc_dump_addarray_dot(arg1, addarray, labels, outfile)

def BddEnc_dump_addarray_davinci(arg1: 'BddEnc_ptr', addarray: 'AddArray_ptr', labels: 'char const **', outfile: 'FILE *') -> "int":
    """BddEnc_dump_addarray_davinci(BddEnc_ptr arg1, AddArray_ptr addarray, char const ** labels, FILE * outfile) -> int"""
    return _bdd.BddEnc_dump_addarray_davinci(arg1, addarray, labels, outfile)

def BddEncCache_create(symb_table: 'SymbTable_ptr', dd: 'DdManager *') -> "BddEncCache_ptr":
    """BddEncCache_create(SymbTable_ptr symb_table, DdManager * dd) -> BddEncCache_ptr"""
    return _bdd.BddEncCache_create(symb_table, dd)

def BddEncCache_destroy(arg1: 'BddEncCache_ptr') -> "void":
    """BddEncCache_destroy(BddEncCache_ptr arg1)"""
    return _bdd.BddEncCache_destroy(arg1)

def BddEncCache_new_constant(arg1: 'BddEncCache_ptr', constant: 'node_ptr', constant_add: 'add_ptr') -> "void":
    """BddEncCache_new_constant(BddEncCache_ptr arg1, node_ptr constant, add_ptr constant_add)"""
    return _bdd.BddEncCache_new_constant(arg1, constant, constant_add)

def BddEncCache_remove_constant(arg1: 'BddEncCache_ptr', constant: 'node_ptr') -> "void":
    """BddEncCache_remove_constant(BddEncCache_ptr arg1, node_ptr constant)"""
    return _bdd.BddEncCache_remove_constant(arg1, constant)

def BddEncCache_is_constant_encoded(arg1: 'BddEncCache_ptr const', constant: 'node_ptr') -> "boolean":
    """BddEncCache_is_constant_encoded(BddEncCache_ptr const arg1, node_ptr constant) -> boolean"""
    return _bdd.BddEncCache_is_constant_encoded(arg1, constant)

def BddEncCache_lookup_constant(arg1: 'BddEncCache_ptr const', constant: 'node_ptr') -> "add_ptr":
    """BddEncCache_lookup_constant(BddEncCache_ptr const arg1, node_ptr constant) -> add_ptr"""
    return _bdd.BddEncCache_lookup_constant(arg1, constant)

def BddEncCache_new_boolean_var(arg1: 'BddEncCache_ptr', var_name: 'node_ptr', var_add: 'add_ptr') -> "void":
    """BddEncCache_new_boolean_var(BddEncCache_ptr arg1, node_ptr var_name, add_ptr var_add)"""
    return _bdd.BddEncCache_new_boolean_var(arg1, var_name, var_add)

def BddEncCache_remove_boolean_var(arg1: 'BddEncCache_ptr', var_name: 'node_ptr') -> "void":
    """BddEncCache_remove_boolean_var(BddEncCache_ptr arg1, node_ptr var_name)"""
    return _bdd.BddEncCache_remove_boolean_var(arg1, var_name)

def BddEncCache_is_boolean_var_encoded(arg1: 'BddEncCache_ptr const', var_name: 'node_ptr') -> "boolean":
    """BddEncCache_is_boolean_var_encoded(BddEncCache_ptr const arg1, node_ptr var_name) -> boolean"""
    return _bdd.BddEncCache_is_boolean_var_encoded(arg1, var_name)

def BddEncCache_lookup_boolean_var(arg1: 'BddEncCache_ptr const', var_name: 'node_ptr') -> "add_ptr":
    """BddEncCache_lookup_boolean_var(BddEncCache_ptr const arg1, node_ptr var_name) -> add_ptr"""
    return _bdd.BddEncCache_lookup_boolean_var(arg1, var_name)

def BddEncCache_set_evaluation(arg1: 'BddEncCache_ptr', expr: 'node_ptr', add_array: 'AddArray_ptr') -> "void":
    """BddEncCache_set_evaluation(BddEncCache_ptr arg1, node_ptr expr, AddArray_ptr add_array)"""
    return _bdd.BddEncCache_set_evaluation(arg1, expr, add_array)

def BddEncCache_remove_evaluation(arg1: 'BddEncCache_ptr', expr: 'node_ptr') -> "void":
    """BddEncCache_remove_evaluation(BddEncCache_ptr arg1, node_ptr expr)"""
    return _bdd.BddEncCache_remove_evaluation(arg1, expr)

def BddEncCache_get_evaluation(arg1: 'BddEncCache_ptr', expr: 'node_ptr') -> "AddArray_ptr":
    """BddEncCache_get_evaluation(BddEncCache_ptr arg1, node_ptr expr) -> AddArray_ptr"""
    return _bdd.BddEncCache_get_evaluation(arg1, expr)

def BddEncCache_clean_evaluation_about(arg1: 'BddEncCache_ptr', symbs: 'NodeList_ptr') -> "void":
    """BddEncCache_clean_evaluation_about(BddEncCache_ptr arg1, NodeList_ptr symbs)"""
    return _bdd.BddEncCache_clean_evaluation_about(arg1, symbs)

def BddEncCache_clean_evaluation(arg1: 'BddEncCache_ptr') -> "void":
    """BddEncCache_clean_evaluation(BddEncCache_ptr arg1)"""
    return _bdd.BddEncCache_clean_evaluation(arg1)
# This file is compatible with both classic and new-style classes.

cvar = _bdd.cvar

