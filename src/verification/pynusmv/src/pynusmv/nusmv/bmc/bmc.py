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
        mname = '.'.join((pkg, '_bmc')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_bmc')
    _bmc = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_bmc', [dirname(__file__)])
        except ImportError:
            import _bmc
            return _bmc
        try:
            _mod = imp.load_module('_bmc', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _bmc = swig_import_helper()
    del swig_import_helper
else:
    import _bmc
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

PRIuPTR = _bmc.PRIuPTR
PRIdPTR = _bmc.PRIdPTR
LLU = _bmc.LLU
LLO = _bmc.LLO
LLX = _bmc.LLX
false = _bmc.false
true = _bmc.true
OUTCOME_GENERIC_ERROR = _bmc.OUTCOME_GENERIC_ERROR
OUTCOME_PARSER_ERROR = _bmc.OUTCOME_PARSER_ERROR
OUTCOME_SYNTAX_ERROR = _bmc.OUTCOME_SYNTAX_ERROR
OUTCOME_FILE_ERROR = _bmc.OUTCOME_FILE_ERROR
OUTCOME_SUCCESS_REQUIRED_HELP = _bmc.OUTCOME_SUCCESS_REQUIRED_HELP
OUTCOME_SUCCESS = _bmc.OUTCOME_SUCCESS
BMC_OPT_INITIALIZED = _bmc.BMC_OPT_INITIALIZED
BMC_MODE = _bmc.BMC_MODE
BMC_DIMACS_FILENAME = _bmc.BMC_DIMACS_FILENAME
BMC_INVAR_DIMACS_FILENAME = _bmc.BMC_INVAR_DIMACS_FILENAME
BMC_PB_LENGTH = _bmc.BMC_PB_LENGTH
BMC_PB_LOOP = _bmc.BMC_PB_LOOP
BMC_INVAR_ALG = _bmc.BMC_INVAR_ALG
BMC_OPTIMIZED_TABLEAU = _bmc.BMC_OPTIMIZED_TABLEAU
BMC_FORCE_PLTL_TABLEAU = _bmc.BMC_FORCE_PLTL_TABLEAU
BMC_SBMC_IL_OPT = _bmc.BMC_SBMC_IL_OPT
BMC_SBMC_GF_FG_OPT = _bmc.BMC_SBMC_GF_FG_OPT
BMC_SBMC_CACHE_OPT = _bmc.BMC_SBMC_CACHE_OPT
BMC_INVAR_ALG_CLASSIC = _bmc.BMC_INVAR_ALG_CLASSIC
BMC_INVAR_ALG_EEN_SORENSSON = _bmc.BMC_INVAR_ALG_EEN_SORENSSON
BMC_INVAR_ALG_FALSIFICATION = _bmc.BMC_INVAR_ALG_FALSIFICATION
BMC_INC_INVAR_ALG_DUAL = _bmc.BMC_INC_INVAR_ALG_DUAL
BMC_INC_INVAR_ALG_ZIGZAG = _bmc.BMC_INC_INVAR_ALG_ZIGZAG
BMC_INC_INVAR_ALG_FALSIFICATION = _bmc.BMC_INC_INVAR_ALG_FALSIFICATION
BMC_INC_INVAR_ALG_INTERP_SEQ = _bmc.BMC_INC_INVAR_ALG_INTERP_SEQ
BMC_INC_INVAR_ALG_INTERPOLANTS = _bmc.BMC_INC_INVAR_ALG_INTERPOLANTS
BMC_INVAR_BACKWARD = _bmc.BMC_INVAR_BACKWARD
BMC_INVAR_FORWARD = _bmc.BMC_INVAR_FORWARD

def set_bmc_mode(arg1: 'OptsHandler_ptr') -> "void":
    """set_bmc_mode(OptsHandler_ptr arg1)"""
    return _bmc.set_bmc_mode(arg1)

def unset_bmc_mode(arg1: 'OptsHandler_ptr') -> "void":
    """unset_bmc_mode(OptsHandler_ptr arg1)"""
    return _bmc.unset_bmc_mode(arg1)

def opt_bmc_mode(arg1: 'OptsHandler_ptr') -> "boolean":
    """opt_bmc_mode(OptsHandler_ptr arg1) -> boolean"""
    return _bmc.opt_bmc_mode(arg1)

def get_bmc_dimacs_filename(arg1: 'OptsHandler_ptr') -> "char *":
    """get_bmc_dimacs_filename(OptsHandler_ptr arg1) -> char *"""
    return _bmc.get_bmc_dimacs_filename(arg1)

def set_bmc_dimacs_filename(arg1: 'OptsHandler_ptr', arg2: 'char *') -> "void":
    """set_bmc_dimacs_filename(OptsHandler_ptr arg1, char * arg2)"""
    return _bmc.set_bmc_dimacs_filename(arg1, arg2)

def get_bmc_invar_dimacs_filename(arg1: 'OptsHandler_ptr') -> "char *":
    """get_bmc_invar_dimacs_filename(OptsHandler_ptr arg1) -> char *"""
    return _bmc.get_bmc_invar_dimacs_filename(arg1)

def set_bmc_invar_dimacs_filename(arg1: 'OptsHandler_ptr', arg2: 'char *') -> "void":
    """set_bmc_invar_dimacs_filename(OptsHandler_ptr arg1, char * arg2)"""
    return _bmc.set_bmc_invar_dimacs_filename(arg1, arg2)

def set_bmc_pb_length(opt: 'OptsHandler_ptr', k: 'int const') -> "void":
    """set_bmc_pb_length(OptsHandler_ptr opt, int const k)"""
    return _bmc.set_bmc_pb_length(opt, k)

def get_bmc_pb_length(arg1: 'OptsHandler_ptr') -> "int":
    """get_bmc_pb_length(OptsHandler_ptr arg1) -> int"""
    return _bmc.get_bmc_pb_length(arg1)

def set_bmc_pb_loop(opt: 'OptsHandler_ptr', loop: 'char const *') -> "void":
    """set_bmc_pb_loop(OptsHandler_ptr opt, char const * loop)"""
    return _bmc.set_bmc_pb_loop(opt, loop)

def get_bmc_pb_loop(arg1: 'OptsHandler_ptr') -> "char const *":
    """get_bmc_pb_loop(OptsHandler_ptr arg1) -> char const *"""
    return _bmc.get_bmc_pb_loop(arg1)

def set_bmc_invar_alg(opt: 'OptsHandler_ptr', loop: 'char const *') -> "void":
    """set_bmc_invar_alg(OptsHandler_ptr opt, char const * loop)"""
    return _bmc.set_bmc_invar_alg(opt, loop)

def get_bmc_invar_alg(arg1: 'OptsHandler_ptr') -> "char const *":
    """get_bmc_invar_alg(OptsHandler_ptr arg1) -> char const *"""
    return _bmc.get_bmc_invar_alg(arg1)

def set_bmc_optimized_tableau(arg1: 'OptsHandler_ptr') -> "void":
    """set_bmc_optimized_tableau(OptsHandler_ptr arg1)"""
    return _bmc.set_bmc_optimized_tableau(arg1)

def unset_bmc_optimized_tableau(arg1: 'OptsHandler_ptr') -> "void":
    """unset_bmc_optimized_tableau(OptsHandler_ptr arg1)"""
    return _bmc.unset_bmc_optimized_tableau(arg1)

def opt_bmc_optimized_tableau(arg1: 'OptsHandler_ptr') -> "boolean":
    """opt_bmc_optimized_tableau(OptsHandler_ptr arg1) -> boolean"""
    return _bmc.opt_bmc_optimized_tableau(arg1)

def set_bmc_force_pltl_tableau(arg1: 'OptsHandler_ptr') -> "void":
    """set_bmc_force_pltl_tableau(OptsHandler_ptr arg1)"""
    return _bmc.set_bmc_force_pltl_tableau(arg1)

def unset_bmc_force_pltl_tableau(arg1: 'OptsHandler_ptr') -> "void":
    """unset_bmc_force_pltl_tableau(OptsHandler_ptr arg1)"""
    return _bmc.unset_bmc_force_pltl_tableau(arg1)

def opt_bmc_force_pltl_tableau(arg1: 'OptsHandler_ptr') -> "boolean":
    """opt_bmc_force_pltl_tableau(OptsHandler_ptr arg1) -> boolean"""
    return _bmc.opt_bmc_force_pltl_tableau(arg1)

def set_bmc_sbmc_gf_fg_opt(opt: 'OptsHandler_ptr') -> "void":
    """set_bmc_sbmc_gf_fg_opt(OptsHandler_ptr opt)"""
    return _bmc.set_bmc_sbmc_gf_fg_opt(opt)

def unset_bmc_sbmc_gf_fg_opt(opt: 'OptsHandler_ptr') -> "void":
    """unset_bmc_sbmc_gf_fg_opt(OptsHandler_ptr opt)"""
    return _bmc.unset_bmc_sbmc_gf_fg_opt(opt)

def opt_bmc_sbmc_gf_fg_opt(opt: 'OptsHandler_ptr') -> "boolean":
    """opt_bmc_sbmc_gf_fg_opt(OptsHandler_ptr opt) -> boolean"""
    return _bmc.opt_bmc_sbmc_gf_fg_opt(opt)

def set_bmc_sbmc_il_opt(opt: 'OptsHandler_ptr') -> "void":
    """set_bmc_sbmc_il_opt(OptsHandler_ptr opt)"""
    return _bmc.set_bmc_sbmc_il_opt(opt)

def unset_bmc_sbmc_il_opt(opt: 'OptsHandler_ptr') -> "void":
    """unset_bmc_sbmc_il_opt(OptsHandler_ptr opt)"""
    return _bmc.unset_bmc_sbmc_il_opt(opt)

def opt_bmc_sbmc_il_opt(opt: 'OptsHandler_ptr') -> "boolean":
    """opt_bmc_sbmc_il_opt(OptsHandler_ptr opt) -> boolean"""
    return _bmc.opt_bmc_sbmc_il_opt(opt)

def set_bmc_sbmc_cache(opt: 'OptsHandler_ptr') -> "void":
    """set_bmc_sbmc_cache(OptsHandler_ptr opt)"""
    return _bmc.set_bmc_sbmc_cache(opt)

def unset_bmc_sbmc_cache(opt: 'OptsHandler_ptr') -> "void":
    """unset_bmc_sbmc_cache(OptsHandler_ptr opt)"""
    return _bmc.unset_bmc_sbmc_cache(opt)

def opt_bmc_sbmc_cache(opt: 'OptsHandler_ptr') -> "boolean":
    """opt_bmc_sbmc_cache(OptsHandler_ptr opt) -> boolean"""
    return _bmc.opt_bmc_sbmc_cache(opt)
BMC_TRUE = _bmc.BMC_TRUE
BMC_FALSE = _bmc.BMC_FALSE
BMC_UNKNOWN = _bmc.BMC_UNKNOWN
BMC_ERROR = _bmc.BMC_ERROR
BMC_INVAR_BACKWARD_CLOSURE = _bmc.BMC_INVAR_BACKWARD_CLOSURE
BMC_INVAR_FORWARD_CLOSURE = _bmc.BMC_INVAR_FORWARD_CLOSURE

def Bmc_GenSolveLtl(ltlprop: 'Prop_ptr', k: 'int const', relative_loop: 'int const', must_inc_length: 'boolean const', must_solve: 'boolean const', dump_type: 'Bmc_DumpType const', dump_fname_template: 'char const *') -> "int":
    """Bmc_GenSolveLtl(Prop_ptr ltlprop, int const k, int const relative_loop, boolean const must_inc_length, boolean const must_solve, Bmc_DumpType const dump_type, char const * dump_fname_template) -> int"""
    return _bmc.Bmc_GenSolveLtl(ltlprop, k, relative_loop, must_inc_length, must_solve, dump_type, dump_fname_template)

def Bmc_GenSolveInvar(invarprop: 'Prop_ptr', must_solve: 'boolean const', dump_type: 'Bmc_DumpType const', dump_fname_template: 'char const *') -> "int":
    """Bmc_GenSolveInvar(Prop_ptr invarprop, boolean const must_solve, Bmc_DumpType const dump_type, char const * dump_fname_template) -> int"""
    return _bmc.Bmc_GenSolveInvar(invarprop, must_solve, dump_type, dump_fname_template)

def Bmc_induction_algorithm(be_fsm: 'BeFsm_ptr', binvarspec: 'node_ptr', trace_index: 'Trace_ptr *', symbols: 'NodeList_ptr') -> "Bmc_result":
    """Bmc_induction_algorithm(BeFsm_ptr be_fsm, node_ptr binvarspec, Trace_ptr * trace_index, NodeList_ptr symbols) -> Bmc_result"""
    return _bmc.Bmc_induction_algorithm(be_fsm, binvarspec, trace_index, symbols)

def Bmc_een_sorensson_algorithm(be_fsm: 'BeFsm_ptr', bool_fsm: 'BoolSexpFsm_ptr', binvarspec: 'node_ptr', max_k: 'int', dump_type: 'Bmc_DumpType const', dump_fname_template: 'char const *', pp: 'Prop_ptr', print_steps: 'boolean', use_extra_step: 'boolean', trace: 'Trace_ptr *') -> "Bmc_result":
    """Bmc_een_sorensson_algorithm(BeFsm_ptr be_fsm, BoolSexpFsm_ptr bool_fsm, node_ptr binvarspec, int max_k, Bmc_DumpType const dump_type, char const * dump_fname_template, Prop_ptr pp, boolean print_steps, boolean use_extra_step, Trace_ptr * trace) -> Bmc_result"""
    return _bmc.Bmc_een_sorensson_algorithm(be_fsm, bool_fsm, binvarspec, max_k, dump_type, dump_fname_template, pp, print_steps, use_extra_step, trace)

def Bmc_een_sorensson_algorithm_without_dump(be_fsm: 'BeFsm_ptr', bool_fsm: 'BoolSexpFsm_ptr', binvarspec: 'node_ptr', max_k: 'int', use_extra_step: 'boolean', trace: 'Trace_ptr *') -> "Bmc_result":
    """Bmc_een_sorensson_algorithm_without_dump(BeFsm_ptr be_fsm, BoolSexpFsm_ptr bool_fsm, node_ptr binvarspec, int max_k, boolean use_extra_step, Trace_ptr * trace) -> Bmc_result"""
    return _bmc.Bmc_een_sorensson_algorithm_without_dump(be_fsm, bool_fsm, binvarspec, max_k, use_extra_step, trace)

def Bmc_GenSolveInvar_EenSorensson(invarprop: 'Prop_ptr', max_k: 'int const', dump_type: 'Bmc_DumpType const', dump_fname_template: 'char const *', use_extra_step: 'boolean') -> "int":
    """Bmc_GenSolveInvar_EenSorensson(Prop_ptr invarprop, int const max_k, Bmc_DumpType const dump_type, char const * dump_fname_template, boolean use_extra_step) -> int"""
    return _bmc.Bmc_GenSolveInvar_EenSorensson(invarprop, max_k, dump_type, dump_fname_template, use_extra_step)

def Bmc_check_psl_property(prop: 'Prop_ptr', dump_prob: 'boolean', inc_sat: 'boolean', single_prob: 'boolean', k: 'int', rel_loop: 'int') -> "int":
    """Bmc_check_psl_property(Prop_ptr prop, boolean dump_prob, boolean inc_sat, boolean single_prob, int k, int rel_loop) -> int"""
    return _bmc.Bmc_check_psl_property(prop, dump_prob, inc_sat, single_prob, k, rel_loop)

def Bmc_CheckFairnessListForPropositionalFormulae(wffList: 'node_ptr') -> "node_ptr":
    """Bmc_CheckFairnessListForPropositionalFormulae(node_ptr wffList) -> node_ptr"""
    return _bmc.Bmc_CheckFairnessListForPropositionalFormulae(wffList)

def Bmc_WffListMatchProperty(wffList: 'node_ptr', pCheck: 'BMC_PF_MATCH', pCheckOptArgument: 'void *', iMaxMatches: 'int', aiMatchedIndexes: 'unsigned int *', pAnswer: 'BMC_PF_MATCH_ANSWER', pAnswerOptArgument: 'void *') -> "int":
    """Bmc_WffListMatchProperty(node_ptr wffList, BMC_PF_MATCH pCheck, void * pCheckOptArgument, int iMaxMatches, unsigned int * aiMatchedIndexes, BMC_PF_MATCH_ANSWER pAnswer, void * pAnswerOptArgument) -> int"""
    return _bmc.Bmc_WffListMatchProperty(wffList, pCheck, pCheckOptArgument, iMaxMatches, aiMatchedIndexes, pAnswer, pAnswerOptArgument)

def Bmc_IsPropositionalFormula(wff: 'node_ptr') -> "boolean":
    """Bmc_IsPropositionalFormula(node_ptr wff) -> boolean"""
    return _bmc.Bmc_IsPropositionalFormula(wff)

def Bmc_CommandBmcSetup(argc: 'int', argv: 'char **') -> "int":
    """Bmc_CommandBmcSetup(int argc, char ** argv) -> int"""
    return _bmc.Bmc_CommandBmcSetup(argc, argv)

def Bmc_CommandBmcSimulate(argc: 'int', argv: 'char **') -> "int":
    """Bmc_CommandBmcSimulate(int argc, char ** argv) -> int"""
    return _bmc.Bmc_CommandBmcSimulate(argc, argv)

def Bmc_CommandBmcIncSimulate(argc: 'int', argv: 'char **') -> "int":
    """Bmc_CommandBmcIncSimulate(int argc, char ** argv) -> int"""
    return _bmc.Bmc_CommandBmcIncSimulate(argc, argv)

def Bmc_CommandBmcPickState(argc: 'int', argv: 'char **') -> "int":
    """Bmc_CommandBmcPickState(int argc, char ** argv) -> int"""
    return _bmc.Bmc_CommandBmcPickState(argc, argv)

def Bmc_CommandBmcSimulateCheckFeasibleConstraints(argc: 'int', argv: 'char **') -> "int":
    """Bmc_CommandBmcSimulateCheckFeasibleConstraints(int argc, char ** argv) -> int"""
    return _bmc.Bmc_CommandBmcSimulateCheckFeasibleConstraints(argc, argv)

def Bmc_CommandGenLtlSpecBmc(argc: 'int', argv: 'char **') -> "int":
    """Bmc_CommandGenLtlSpecBmc(int argc, char ** argv) -> int"""
    return _bmc.Bmc_CommandGenLtlSpecBmc(argc, argv)

def Bmc_CommandGenLtlSpecBmcOnePb(argc: 'int', argv: 'char **') -> "int":
    """Bmc_CommandGenLtlSpecBmcOnePb(int argc, char ** argv) -> int"""
    return _bmc.Bmc_CommandGenLtlSpecBmcOnePb(argc, argv)

def Bmc_CommandCheckLtlSpecBmc(argc: 'int', argv: 'char **') -> "int":
    """Bmc_CommandCheckLtlSpecBmc(int argc, char ** argv) -> int"""
    return _bmc.Bmc_CommandCheckLtlSpecBmc(argc, argv)

def Bmc_CommandCheckLtlSpecBmcOnePb(argc: 'int', argv: 'char **') -> "int":
    """Bmc_CommandCheckLtlSpecBmcOnePb(int argc, char ** argv) -> int"""
    return _bmc.Bmc_CommandCheckLtlSpecBmcOnePb(argc, argv)

def Bmc_CommandGenInvarBmc(argc: 'int', argv: 'char **') -> "int":
    """Bmc_CommandGenInvarBmc(int argc, char ** argv) -> int"""
    return _bmc.Bmc_CommandGenInvarBmc(argc, argv)

def Bmc_CommandCheckInvarBmc(argc: 'int', argv: 'char **') -> "int":
    """Bmc_CommandCheckInvarBmc(int argc, char ** argv) -> int"""
    return _bmc.Bmc_CommandCheckInvarBmc(argc, argv)

def Bmc_check_if_model_was_built(err: 'FILE *', forced: 'boolean') -> "int":
    """Bmc_check_if_model_was_built(FILE * err, boolean forced) -> int"""
    return _bmc.Bmc_check_if_model_was_built(err, forced)

def Bmc_cmd_options_handling(argc: 'int', argv: 'char **', prop_type: 'Prop_Type', res_prop: 'Prop_ptr *', res_k: 'int *', res_l: 'int *', res_a: 'char **', res_s: 'char **', res_o: 'char **', res_e: 'boolean *') -> "Outcome":
    """Bmc_cmd_options_handling(int argc, char ** argv, Prop_Type prop_type, Prop_ptr * res_prop, int * res_k, int * res_l, char ** res_a, char ** res_s, char ** res_o, boolean * res_e) -> Outcome"""
    return _bmc.Bmc_cmd_options_handling(argc, argv, prop_type, res_prop, res_k, res_l, res_a, res_s, res_o, res_e)

def Bmc_Conv_Be2Bexp(be_enc: 'BeEnc_ptr', be: 'be_ptr') -> "node_ptr":
    """Bmc_Conv_Be2Bexp(BeEnc_ptr be_enc, be_ptr be) -> node_ptr"""
    return _bmc.Bmc_Conv_Be2Bexp(be_enc, be)

def Bmc_Conv_Bexp2Be(be_enc: 'BeEnc_ptr', bexp: 'node_ptr') -> "be_ptr":
    """Bmc_Conv_Bexp2Be(BeEnc_ptr be_enc, node_ptr bexp) -> be_ptr"""
    return _bmc.Bmc_Conv_Bexp2Be(be_enc, bexp)

def Bmc_Conv_BexpList2BeList(be_enc: 'BeEnc_ptr', bexp_list: 'node_ptr') -> "node_ptr":
    """Bmc_Conv_BexpList2BeList(BeEnc_ptr be_enc, node_ptr bexp_list) -> node_ptr"""
    return _bmc.Bmc_Conv_BexpList2BeList(be_enc, bexp_list)

def Bmc_Conv_cleanup_cached_entries_about(be_enc: 'BeEnc_ptr', symbs: 'NodeList_ptr') -> "void":
    """Bmc_Conv_cleanup_cached_entries_about(BeEnc_ptr be_enc, NodeList_ptr symbs)"""
    return _bmc.Bmc_Conv_cleanup_cached_entries_about(be_enc, symbs)

def Bmc_Conv_get_BeModel2SymbModel(be_enc: 'BeEnc_ptr const', be_model: 'Slist_ptr const', k: 'int', convert_to_scalars: 'boolean', frozen: 'node_ptr *', states: 'array_t **', inputs: 'array_t **') -> "void":
    """Bmc_Conv_get_BeModel2SymbModel(BeEnc_ptr const be_enc, Slist_ptr const be_model, int k, boolean convert_to_scalars, node_ptr * frozen, array_t ** states, array_t ** inputs)"""
    return _bmc.Bmc_Conv_get_BeModel2SymbModel(be_enc, be_model, k, convert_to_scalars, frozen, states, inputs)
BMC_DUMP_NONE = _bmc.BMC_DUMP_NONE
BMC_DUMP_DIMACS = _bmc.BMC_DUMP_DIMACS
BMC_DUMP_DA_VINCI = _bmc.BMC_DUMP_DA_VINCI
BMC_DUMP_GDL = _bmc.BMC_DUMP_GDL

def Bmc_Dump_WriteProblem(be_enc: 'BeEnc_ptr const', cnf: 'Be_Cnf_ptr const', prop: 'Prop_ptr', k: 'int const', loop: 'int const', dump_type: 'Bmc_DumpType const', dump_fname_template: 'char const *') -> "void":
    """Bmc_Dump_WriteProblem(BeEnc_ptr const be_enc, Be_Cnf_ptr const cnf, Prop_ptr prop, int const k, int const loop, Bmc_DumpType const dump_type, char const * dump_fname_template)"""
    return _bmc.Bmc_Dump_WriteProblem(be_enc, cnf, prop, k, loop, dump_type, dump_fname_template)

def Bmc_Dump_DimacsInvarProblemFilename(be_enc: 'BeEnc_ptr const', cnf: 'Be_Cnf_ptr const', filename: 'char const *') -> "int":
    """Bmc_Dump_DimacsInvarProblemFilename(BeEnc_ptr const be_enc, Be_Cnf_ptr const cnf, char const * filename) -> int"""
    return _bmc.Bmc_Dump_DimacsInvarProblemFilename(be_enc, cnf, filename)

def Bmc_Dump_DimacsProblemFilename(be_enc: 'BeEnc_ptr const', cnf: 'Be_Cnf_ptr const', filename: 'char const *', k: 'int const') -> "int":
    """Bmc_Dump_DimacsProblemFilename(BeEnc_ptr const be_enc, Be_Cnf_ptr const cnf, char const * filename, int const k) -> int"""
    return _bmc.Bmc_Dump_DimacsProblemFilename(be_enc, cnf, filename, k)

def Bmc_Dump_DimacsInvarProblem(be_enc: 'BeEnc_ptr const', cnf: 'Be_Cnf_ptr const', dimacsfile: 'FILE *') -> "void":
    """Bmc_Dump_DimacsInvarProblem(BeEnc_ptr const be_enc, Be_Cnf_ptr const cnf, FILE * dimacsfile)"""
    return _bmc.Bmc_Dump_DimacsInvarProblem(be_enc, cnf, dimacsfile)

def Bmc_Dump_DimacsProblem(be_enc: 'BeEnc_ptr const', cnf: 'Be_Cnf_ptr const', k: 'int const', dimacsfile: 'FILE *') -> "void":
    """Bmc_Dump_DimacsProblem(BeEnc_ptr const be_enc, Be_Cnf_ptr const cnf, int const k, FILE * dimacsfile)"""
    return _bmc.Bmc_Dump_DimacsProblem(be_enc, cnf, k, dimacsfile)

def Bmc_Gen_InvarProblem(be_fsm: 'BeFsm_ptr const', wff: 'node_ptr const') -> "be_ptr":
    """Bmc_Gen_InvarProblem(BeFsm_ptr const be_fsm, node_ptr const wff) -> be_ptr"""
    return _bmc.Bmc_Gen_InvarProblem(be_fsm, wff)

def Bmc_Gen_LtlProblem(be_fsm: 'BeFsm_ptr const', ltl_wff: 'node_ptr const', k: 'int const', l: 'int const') -> "be_ptr":
    """Bmc_Gen_LtlProblem(BeFsm_ptr const be_fsm, node_ptr const ltl_wff, int const k, int const l) -> be_ptr"""
    return _bmc.Bmc_Gen_LtlProblem(be_fsm, ltl_wff, k, l)

def Bmc_Gen_InvarBaseStep(be_fsm: 'BeFsm_ptr const', wff: 'node_ptr const') -> "be_ptr":
    """Bmc_Gen_InvarBaseStep(BeFsm_ptr const be_fsm, node_ptr const wff) -> be_ptr"""
    return _bmc.Bmc_Gen_InvarBaseStep(be_fsm, wff)

def Bmc_Gen_InvarInductStep(be_fsm: 'BeFsm_ptr const', wff: 'node_ptr const') -> "be_ptr":
    """Bmc_Gen_InvarInductStep(BeFsm_ptr const be_fsm, node_ptr const wff) -> be_ptr"""
    return _bmc.Bmc_Gen_InvarInductStep(be_fsm, wff)

def Bmc_Gen_UnrollingFragment(arg1: 'BeFsm_ptr const', i: 'int const') -> "be_ptr":
    """Bmc_Gen_UnrollingFragment(BeFsm_ptr const arg1, int const i) -> be_ptr"""
    return _bmc.Bmc_Gen_UnrollingFragment(arg1, i)

def Bmc_Model_GetInit0(be_fsm: 'BeFsm_ptr const') -> "be_ptr":
    """Bmc_Model_GetInit0(BeFsm_ptr const be_fsm) -> be_ptr"""
    return _bmc.Bmc_Model_GetInit0(be_fsm)

def Bmc_Model_GetInitI(be_fsm: 'BeFsm_ptr const', i: 'int const') -> "be_ptr":
    """Bmc_Model_GetInitI(BeFsm_ptr const be_fsm, int const i) -> be_ptr"""
    return _bmc.Bmc_Model_GetInitI(be_fsm, i)

def Bmc_Model_GetInvarAtTime(be_fsm: 'BeFsm_ptr const', time: 'int const') -> "be_ptr":
    """Bmc_Model_GetInvarAtTime(BeFsm_ptr const be_fsm, int const time) -> be_ptr"""
    return _bmc.Bmc_Model_GetInvarAtTime(be_fsm, time)

def Bmc_Model_GetTransAtTime(be_fsm: 'BeFsm_ptr const', time: 'int const') -> "be_ptr":
    """Bmc_Model_GetTransAtTime(BeFsm_ptr const be_fsm, int const time) -> be_ptr"""
    return _bmc.Bmc_Model_GetTransAtTime(be_fsm, time)

def Bmc_Model_GetUnrolling(be_fsm: 'BeFsm_ptr const', j: 'int const', k: 'int const') -> "be_ptr":
    """Bmc_Model_GetUnrolling(BeFsm_ptr const be_fsm, int const j, int const k) -> be_ptr"""
    return _bmc.Bmc_Model_GetUnrolling(be_fsm, j, k)

def Bmc_Model_GetPathNoInit(be_fsm: 'BeFsm_ptr const', k: 'int const') -> "be_ptr":
    """Bmc_Model_GetPathNoInit(BeFsm_ptr const be_fsm, int const k) -> be_ptr"""
    return _bmc.Bmc_Model_GetPathNoInit(be_fsm, k)

def Bmc_Model_GetPathWithInit(be_fsm: 'BeFsm_ptr const', k: 'int const') -> "be_ptr":
    """Bmc_Model_GetPathWithInit(BeFsm_ptr const be_fsm, int const k) -> be_ptr"""
    return _bmc.Bmc_Model_GetPathWithInit(be_fsm, k)

def Bmc_Model_GetFairness(be_fsm: 'BeFsm_ptr const', k: 'int const', l: 'int const') -> "be_ptr":
    """Bmc_Model_GetFairness(BeFsm_ptr const be_fsm, int const k, int const l) -> be_ptr"""
    return _bmc.Bmc_Model_GetFairness(be_fsm, k, l)

def Bmc_Model_Invar_Dual_forward_unrolling(be_fsm: 'BeFsm_ptr const', invarspec: 'be_ptr const', i: 'int') -> "be_ptr":
    """Bmc_Model_Invar_Dual_forward_unrolling(BeFsm_ptr const be_fsm, be_ptr const invarspec, int i) -> be_ptr"""
    return _bmc.Bmc_Model_Invar_Dual_forward_unrolling(be_fsm, invarspec, i)

def Bmc_Init() -> "void":
    """Bmc_Init()"""
    return _bmc.Bmc_Init()

def Bmc_Quit() -> "void":
    """Bmc_Quit()"""
    return _bmc.Bmc_Quit()

def Bmc_InitData() -> "void":
    """Bmc_InitData()"""
    return _bmc.Bmc_InitData()

def Bmc_QuitData() -> "void":
    """Bmc_QuitData()"""
    return _bmc.Bmc_QuitData()

def Bmc_AddCmd() -> "void":
    """Bmc_AddCmd()"""
    return _bmc.Bmc_AddCmd()

def Bmc_init_opt() -> "void":
    """Bmc_init_opt()"""
    return _bmc.Bmc_init_opt()

def Bmc_Simulate(be_fsm: 'BeFsm_ptr const', bdd_enc: 'BddEnc_ptr', constraints: 'be_ptr', time_shift: 'boolean', k: 'int const', print_trace: 'boolean const', changes_only: 'boolean const', mode: 'Simulation_Mode') -> "int":
    """Bmc_Simulate(BeFsm_ptr const be_fsm, BddEnc_ptr bdd_enc, be_ptr constraints, boolean time_shift, int const k, boolean const print_trace, boolean const changes_only, Simulation_Mode mode) -> int"""
    return _bmc.Bmc_Simulate(be_fsm, bdd_enc, constraints, time_shift, k, print_trace, changes_only, mode)

def Bmc_StepWiseSimulation(be_fsm: 'BeFsm_ptr', bdd_enc: 'BddEnc_ptr', trace_manager: 'TraceManager_ptr', target_steps: 'int', constraints: 'be_ptr', time_shift: 'boolean', printtrace: 'boolean', changes_only: 'boolean', mode: 'Simulation_Mode', display_all: 'boolean') -> "int":
    """Bmc_StepWiseSimulation(BeFsm_ptr be_fsm, BddEnc_ptr bdd_enc, TraceManager_ptr trace_manager, int target_steps, be_ptr constraints, boolean time_shift, boolean printtrace, boolean changes_only, Simulation_Mode mode, boolean display_all) -> int"""
    return _bmc.Bmc_StepWiseSimulation(be_fsm, bdd_enc, trace_manager, target_steps, constraints, time_shift, printtrace, changes_only, mode, display_all)

def Bmc_simulate_check_feasible_constraints(be_fsm: 'BeFsm_ptr', bdd_enc: 'BddEnc_ptr', constraints: 'Olist_ptr', from_state: 'be_ptr') -> "Olist_ptr":
    """Bmc_simulate_check_feasible_constraints(BeFsm_ptr be_fsm, BddEnc_ptr bdd_enc, Olist_ptr constraints, be_ptr from_state) -> Olist_ptr"""
    return _bmc.Bmc_simulate_check_feasible_constraints(be_fsm, bdd_enc, constraints, from_state)

def Bmc_pick_state_from_constr(fsm: 'BeFsm_ptr', bdd_enc: 'BddEnc_ptr', constr: 'be_ptr', mode: 'Simulation_Mode', display_all: 'boolean') -> "int":
    """Bmc_pick_state_from_constr(BeFsm_ptr fsm, BddEnc_ptr bdd_enc, be_ptr constr, Simulation_Mode mode, boolean display_all) -> int"""
    return _bmc.Bmc_pick_state_from_constr(fsm, bdd_enc, constr, mode, display_all)

def Bmc_Tableau_GetNoLoop(be_fsm: 'BeFsm_ptr const', ltl_wff: 'node_ptr const', k: 'int const') -> "be_ptr":
    """Bmc_Tableau_GetNoLoop(BeFsm_ptr const be_fsm, node_ptr const ltl_wff, int const k) -> be_ptr"""
    return _bmc.Bmc_Tableau_GetNoLoop(be_fsm, ltl_wff, k)

def Bmc_Tableau_GetSingleLoop(be_fsm: 'BeFsm_ptr const', ltl_wff: 'node_ptr const', k: 'int const', l: 'int const') -> "be_ptr":
    """Bmc_Tableau_GetSingleLoop(BeFsm_ptr const be_fsm, node_ptr const ltl_wff, int const k, int const l) -> be_ptr"""
    return _bmc.Bmc_Tableau_GetSingleLoop(be_fsm, ltl_wff, k, l)

def Bmc_Tableau_GetAllLoops(be_fsm: 'BeFsm_ptr const', ltl_wff: 'node_ptr const', k: 'int const', l: 'int const') -> "be_ptr":
    """Bmc_Tableau_GetAllLoops(BeFsm_ptr const be_fsm, node_ptr const ltl_wff, int const k, int const l) -> be_ptr"""
    return _bmc.Bmc_Tableau_GetAllLoops(be_fsm, ltl_wff, k, l)

def Bmc_Tableau_GetAllLoopsDepth1(be_fsm: 'BeFsm_ptr const', ltl_wff: 'node_ptr const', k: 'int const') -> "be_ptr":
    """Bmc_Tableau_GetAllLoopsDepth1(BeFsm_ptr const be_fsm, node_ptr const ltl_wff, int const k) -> be_ptr"""
    return _bmc.Bmc_Tableau_GetAllLoopsDepth1(be_fsm, ltl_wff, k)

def Bmc_Tableau_GetLtlTableau(be_fsm: 'BeFsm_ptr const', ltl_wff: 'node_ptr const', k: 'int const', l: 'int const') -> "be_ptr":
    """Bmc_Tableau_GetLtlTableau(BeFsm_ptr const be_fsm, node_ptr const ltl_wff, int const k, int const l) -> be_ptr"""
    return _bmc.Bmc_Tableau_GetLtlTableau(be_fsm, ltl_wff, k, l)
UNKNOWN_OP = _bmc.UNKNOWN_OP
CONSTANT_EXPR = _bmc.CONSTANT_EXPR
LITERAL = _bmc.LITERAL
PROP_CONNECTIVE = _bmc.PROP_CONNECTIVE
TIME_OPERATOR = _bmc.TIME_OPERATOR

def Bmc_Utils_generate_and_print_cntexample(be_enc: 'BeEnc_ptr', solver: 'SatSolver_ptr', be_prob: 'be_ptr', k: 'int const', trace_name: 'char const *', symbols: 'NodeList_ptr') -> "Trace_ptr":
    """Bmc_Utils_generate_and_print_cntexample(BeEnc_ptr be_enc, SatSolver_ptr solver, be_ptr be_prob, int const k, char const * trace_name, NodeList_ptr symbols) -> Trace_ptr"""
    return _bmc.Bmc_Utils_generate_and_print_cntexample(be_enc, solver, be_prob, k, trace_name, symbols)

def Bmc_Utils_generate_cntexample(be_enc: 'BeEnc_ptr', solver: 'SatSolver_ptr', be_prob: 'be_ptr', k: 'int const', trace_name: 'char const *', symbols: 'NodeList_ptr') -> "Trace_ptr":
    """Bmc_Utils_generate_cntexample(BeEnc_ptr be_enc, SatSolver_ptr solver, be_ptr be_prob, int const k, char const * trace_name, NodeList_ptr symbols) -> Trace_ptr"""
    return _bmc.Bmc_Utils_generate_cntexample(be_enc, solver, be_prob, k, trace_name, symbols)

def Bmc_Utils_fill_cntexample(be_enc: 'BeEnc_ptr', solver: 'SatSolver_ptr', k: 'int const', trace: 'Trace_ptr') -> "Trace_ptr":
    """Bmc_Utils_fill_cntexample(BeEnc_ptr be_enc, SatSolver_ptr solver, int const k, Trace_ptr trace) -> Trace_ptr"""
    return _bmc.Bmc_Utils_fill_cntexample(be_enc, solver, k, trace)

def Bmc_Utils_IsNoLoopback(l: 'int const') -> "boolean":
    """Bmc_Utils_IsNoLoopback(int const l) -> boolean"""
    return _bmc.Bmc_Utils_IsNoLoopback(l)

def Bmc_Utils_IsNoLoopbackString(str: 'char const *') -> "boolean":
    """Bmc_Utils_IsNoLoopbackString(char const * str) -> boolean"""
    return _bmc.Bmc_Utils_IsNoLoopbackString(str)

def Bmc_Utils_IsSingleLoopback(l: 'int const') -> "boolean":
    """Bmc_Utils_IsSingleLoopback(int const l) -> boolean"""
    return _bmc.Bmc_Utils_IsSingleLoopback(l)

def Bmc_Utils_IsAllLoopbacks(l: 'int const') -> "boolean":
    """Bmc_Utils_IsAllLoopbacks(int const l) -> boolean"""
    return _bmc.Bmc_Utils_IsAllLoopbacks(l)

def Bmc_Utils_IsAllLoopbacksString(str: 'char const *') -> "boolean":
    """Bmc_Utils_IsAllLoopbacksString(char const * str) -> boolean"""
    return _bmc.Bmc_Utils_IsAllLoopbacksString(str)

def Bmc_Utils_GetNoLoopback() -> "int":
    """Bmc_Utils_GetNoLoopback() -> int"""
    return _bmc.Bmc_Utils_GetNoLoopback()

def Bmc_Utils_GetAllLoopbacks() -> "int":
    """Bmc_Utils_GetAllLoopbacks() -> int"""
    return _bmc.Bmc_Utils_GetAllLoopbacks()

def Bmc_Utils_GetAllLoopbacksString() -> "char const *":
    """Bmc_Utils_GetAllLoopbacksString() -> char const *"""
    return _bmc.Bmc_Utils_GetAllLoopbacksString()

def Bmc_Utils_RelLoop2AbsLoop(loop: 'int const', k: 'int const') -> "int":
    """Bmc_Utils_RelLoop2AbsLoop(int const loop, int const k) -> int"""
    return _bmc.Bmc_Utils_RelLoop2AbsLoop(loop, k)

def Bmc_Utils_Check_k_l(k: 'int const', l: 'int const') -> "Outcome":
    """Bmc_Utils_Check_k_l(int const k, int const l) -> Outcome"""
    return _bmc.Bmc_Utils_Check_k_l(k, l)

def Bmc_Utils_GetSuccTime(time: 'int const', k: 'int const', l: 'int const') -> "int":
    """Bmc_Utils_GetSuccTime(int const time, int const k, int const l) -> int"""
    return _bmc.Bmc_Utils_GetSuccTime(time, k, l)

def Bmc_Utils_ConvertLoopFromString(strValue: 'char const *', result: 'Outcome *') -> "int":
    """Bmc_Utils_ConvertLoopFromString(char const * strValue, Outcome * result) -> int"""
    return _bmc.Bmc_Utils_ConvertLoopFromString(strValue, result)

def Bmc_Utils_ConvertLoopFromInteger(iLoopback: 'int const', szLoopback: 'char *', _bufsize: 'int const') -> "void":
    """Bmc_Utils_ConvertLoopFromInteger(int const iLoopback, char * szLoopback, int const _bufsize)"""
    return _bmc.Bmc_Utils_ConvertLoopFromInteger(iLoopback, szLoopback, _bufsize)

def Bmc_Utils_ExpandMacrosInFilename(filename_to_be_expanded: 'char const *', table_ptr: 'SubstString const *', table_len: 'size_t const', filename_expanded: 'char *', buf_len: 'size_t') -> "void":
    """Bmc_Utils_ExpandMacrosInFilename(char const * filename_to_be_expanded, SubstString const * table_ptr, size_t const table_len, char * filename_expanded, size_t buf_len)"""
    return _bmc.Bmc_Utils_ExpandMacrosInFilename(filename_to_be_expanded, table_ptr, table_len, filename_expanded, buf_len)

def Bmc_Utils_apply_inlining(be_mgr: 'Be_Manager_ptr', f: 'be_ptr') -> "be_ptr":
    """Bmc_Utils_apply_inlining(Be_Manager_ptr be_mgr, be_ptr f) -> be_ptr"""
    return _bmc.Bmc_Utils_apply_inlining(be_mgr, f)

def Bmc_Utils_apply_inlining4inc(be_mgr: 'Be_Manager_ptr', f: 'be_ptr') -> "be_ptr":
    """Bmc_Utils_apply_inlining4inc(Be_Manager_ptr be_mgr, be_ptr f) -> be_ptr"""
    return _bmc.Bmc_Utils_apply_inlining4inc(be_mgr, f)

def Bmc_Utils_simple_costraint_from_string(be_enc: 'BeEnc_ptr', bdd_enc: 'BddEnc_ptr', str: 'char const *', node_expr: 'Expr_ptr *') -> "be_ptr":
    """Bmc_Utils_simple_costraint_from_string(BeEnc_ptr be_enc, BddEnc_ptr bdd_enc, char const * str, Expr_ptr * node_expr) -> be_ptr"""
    return _bmc.Bmc_Utils_simple_costraint_from_string(be_enc, bdd_enc, str, node_expr)

def Bmc_Utils_next_costraint_from_string(be_enc: 'BeEnc_ptr', bdd_enc: 'BddEnc_ptr', str: 'char const *', node_expr: 'Expr_ptr *') -> "be_ptr":
    """Bmc_Utils_next_costraint_from_string(BeEnc_ptr be_enc, BddEnc_ptr bdd_enc, char const * str, Expr_ptr * node_expr) -> be_ptr"""
    return _bmc.Bmc_Utils_next_costraint_from_string(be_enc, bdd_enc, str, node_expr)
# This file is compatible with both classic and new-style classes.


