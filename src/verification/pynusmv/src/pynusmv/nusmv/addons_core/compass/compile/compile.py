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
        mname = '.'.join((pkg, '_compile')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_compile')
    _compile = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_compile', [dirname(__file__)])
        except ImportError:
            import _compile
            return _compile
        try:
            _mod = imp.load_module('_compile', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _compile = swig_import_helper()
    del swig_import_helper
else:
    import _compile
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

PRIuPTR = _compile.PRIuPTR
PRIdPTR = _compile.PRIdPTR
LLU = _compile.LLU
LLO = _compile.LLO
LLX = _compile.LLX
false = _compile.false
true = _compile.true
OUTCOME_GENERIC_ERROR = _compile.OUTCOME_GENERIC_ERROR
OUTCOME_PARSER_ERROR = _compile.OUTCOME_PARSER_ERROR
OUTCOME_SYNTAX_ERROR = _compile.OUTCOME_SYNTAX_ERROR
OUTCOME_FILE_ERROR = _compile.OUTCOME_FILE_ERROR
OUTCOME_SUCCESS_REQUIRED_HELP = _compile.OUTCOME_SUCCESS_REQUIRED_HELP
OUTCOME_SUCCESS = _compile.OUTCOME_SUCCESS

def ProbAssign_create(assigns: 'node_ptr', value: 'node_ptr') -> "ProbAssign_ptr":
    """ProbAssign_create(node_ptr assigns, node_ptr value) -> ProbAssign_ptr"""
    return _compile.ProbAssign_create(assigns, value)

def ProbAssign_destroy(arg1: 'ProbAssign_ptr') -> "void":
    """ProbAssign_destroy(ProbAssign_ptr arg1)"""
    return _compile.ProbAssign_destroy(arg1)

def ProbAssign_get_assigns_expr(arg1: 'ProbAssign_ptr const') -> "node_ptr":
    """ProbAssign_get_assigns_expr(ProbAssign_ptr const arg1) -> node_ptr"""
    return _compile.ProbAssign_get_assigns_expr(arg1)

def ProbAssign_get_prob(arg1: 'ProbAssign_ptr const') -> "node_ptr":
    """ProbAssign_get_prob(ProbAssign_ptr const arg1) -> node_ptr"""
    return _compile.ProbAssign_get_prob(arg1)
# This file is compatible with both classic and new-style classes.


