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
        mname = '.'.join((pkg, '_plugins')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_plugins')
    _plugins = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_plugins', [dirname(__file__)])
        except ImportError:
            import _plugins
            return _plugins
        try:
            _mod = imp.load_module('_plugins', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _plugins = swig_import_helper()
    del swig_import_helper
else:
    import _plugins
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

PRIuPTR = _plugins.PRIuPTR
PRIdPTR = _plugins.PRIdPTR
LLU = _plugins.LLU
LLO = _plugins.LLO
LLX = _plugins.LLX
false = _plugins.false
true = _plugins.true
OUTCOME_GENERIC_ERROR = _plugins.OUTCOME_GENERIC_ERROR
OUTCOME_PARSER_ERROR = _plugins.OUTCOME_PARSER_ERROR
OUTCOME_SYNTAX_ERROR = _plugins.OUTCOME_SYNTAX_ERROR
OUTCOME_FILE_ERROR = _plugins.OUTCOME_FILE_ERROR
OUTCOME_SUCCESS_REQUIRED_HELP = _plugins.OUTCOME_SUCCESS_REQUIRED_HELP
OUTCOME_SUCCESS = _plugins.OUTCOME_SUCCESS

def Object_destroy(arg1: 'Object_ptr', arg: 'void *') -> "void":
    """Object_destroy(Object_ptr arg1, void * arg)"""
    return _plugins.Object_destroy(arg1, arg)

def Object_copy(arg1: 'Object_ptr const') -> "Object_ptr":
    """Object_copy(Object_ptr const arg1) -> Object_ptr"""
    return _plugins.Object_copy(arg1)

def TraceCompact_create() -> "TraceCompact_ptr":
    """TraceCompact_create() -> TraceCompact_ptr"""
    return _plugins.TraceCompact_create()

def TraceExplainer_create(changes_only: 'boolean') -> "TraceExplainer_ptr":
    """TraceExplainer_create(boolean changes_only) -> TraceExplainer_ptr"""
    return _plugins.TraceExplainer_create(changes_only)

def TracePlugin_action(arg1: 'TracePlugin_ptr const', trace: 'Trace_ptr const', opt: 'TraceOpt_ptr const') -> "int":
    """TracePlugin_action(TracePlugin_ptr const arg1, Trace_ptr const trace, TraceOpt_ptr const opt) -> int"""
    return _plugins.TracePlugin_action(arg1, trace, opt)

def TracePlugin_get_desc(arg1: 'TracePlugin_ptr const') -> "char *":
    """TracePlugin_get_desc(TracePlugin_ptr const arg1) -> char *"""
    return _plugins.TracePlugin_get_desc(arg1)
TRACE_TABLE_TYPE_ROW = _plugins.TRACE_TABLE_TYPE_ROW
TRACE_TABLE_TYPE_COLUMN = _plugins.TRACE_TABLE_TYPE_COLUMN

def TraceTable_create(style: 'TraceTableStyle') -> "TraceTable_ptr":
    """TraceTable_create(TraceTableStyle style) -> TraceTable_ptr"""
    return _plugins.TraceTable_create(style)

def TraceXmlDumper_create() -> "TraceXmlDumper_ptr":
    """TraceXmlDumper_create() -> TraceXmlDumper_ptr"""
    return _plugins.TraceXmlDumper_create()
# This file is compatible with both classic and new-style classes.


