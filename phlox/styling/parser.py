from .lexer import Lexer
from ..ply import yacc


class Parser(Lexer):
    @staticmethod
    def parser(*args, **kwargs):
        return yacc.yacc(*args, **kwargs)
