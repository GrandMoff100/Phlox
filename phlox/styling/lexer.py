from ..ply import lex


class Lexer:
    tokens = []

    @staticmethod
    def lexer(*args, **kwargs):
        return lex.lex(*args, module=Lexer, **kwargs)
