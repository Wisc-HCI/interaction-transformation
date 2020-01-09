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
        mname = '.'.join((pkg, '_loaders')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_loaders')
    _loaders = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_loaders', [dirname(__file__)])
        except ImportError:
            import _loaders
            return _loaders
        try:
            _mod = imp.load_module('_loaders', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _loaders = swig_import_helper()
    del swig_import_helper
else:
    import _loaders
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

PRIuPTR = _loaders.PRIuPTR
PRIdPTR = _loaders.PRIdPTR
LLU = _loaders.LLU
LLO = _loaders.LLO
LLX = _loaders.LLX
false = _loaders.false
true = _loaders.true
OUTCOME_GENERIC_ERROR = _loaders.OUTCOME_GENERIC_ERROR
OUTCOME_PARSER_ERROR = _loaders.OUTCOME_PARSER_ERROR
OUTCOME_SYNTAX_ERROR = _loaders.OUTCOME_SYNTAX_ERROR
OUTCOME_FILE_ERROR = _loaders.OUTCOME_FILE_ERROR
OUTCOME_SUCCESS_REQUIRED_HELP = _loaders.OUTCOME_SUCCESS_REQUIRED_HELP
OUTCOME_SUCCESS = _loaders.OUTCOME_SUCCESS

def Object_destroy(arg1: 'Object_ptr', arg: 'void *') -> "void":
    """Object_destroy(Object_ptr arg1, void * arg)"""
    return _loaders.Object_destroy(arg1, arg)

def Object_copy(arg1: 'Object_ptr const') -> "Object_ptr":
    """Object_copy(Object_ptr const arg1) -> Object_ptr"""
    return _loaders.Object_copy(arg1)

def TraceLoader_load_trace(arg1: 'TraceLoader_ptr const', st: 'SymbTable_ptr', symbols: 'NodeList_ptr') -> "Trace_ptr":
    """TraceLoader_load_trace(TraceLoader_ptr const arg1, SymbTable_ptr st, NodeList_ptr symbols) -> Trace_ptr"""
    return _loaders.TraceLoader_load_trace(arg1, st, symbols)

def TraceLoader_get_desc(arg1: 'TraceLoader_ptr const') -> "char *":
    """TraceLoader_get_desc(TraceLoader_ptr const arg1) -> char *"""
    return _loaders.TraceLoader_get_desc(arg1)

def TraceXmlLoader_create(xml_filename: 'char const *', halt_on_undefined_symbols: 'boolean', halt_on_wrong_section: 'boolean') -> "TraceXmlLoader_ptr":
    """TraceXmlLoader_create(char const * xml_filename, boolean halt_on_undefined_symbols, boolean halt_on_wrong_section) -> TraceXmlLoader_ptr"""
    return _loaders.TraceXmlLoader_create(xml_filename, halt_on_undefined_symbols, halt_on_wrong_section)
# This file is compatible with both classic and new-style classes.


