from types import CodeType, FunctionType
from typing import Any, Dict


def load(function: str, globals_dict: Dict[str, Any] = None) -> FunctionType:
    """Loads the function specified by compiling it,
    creating a function in the current python shell
    and returning that callable function.

    The function string passed in MUST be a function
    definition only. Specifically, if any imports are
    required they MUST be done within the function definition,
    and there is no ability to declare global variables.

    The globals argument allows you to control the namespace
    of your loaded function. If empty, will use the module-local
    call to globals().
    """
    code = compile(function, "<string>", "exec")
    code_obj = code.co_consts[0]
    argdefs = None
    if not isinstance(code_obj, CodeType):
        argdefs = code.co_consts[-1:][0]
        for const in code.co_consts:
            if isinstance(const, CodeType):
                code_obj = const
                break
    return FunctionType(code_obj, globals_dict or globals(), argdefs=argdefs)


__all__ = ["load"]
