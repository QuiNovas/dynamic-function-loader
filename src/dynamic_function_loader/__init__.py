from types import CodeType, FunctionType


def load(function: str) -> FunctionType:
    code = compile(function, "<string>", "exec")
    code_obj = code.co_consts[0]
    argdefs = None
    if not isinstance(code_obj, CodeType):
        argdefs = code.co_consts[-1:][0]
        for const in code.co_consts:
          if isinstance(const, CodeType):
            code_obj = const
    return FunctionType(code_obj, globals(), argdefs=argdefs)


__all__ = ["load"]
