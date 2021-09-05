from ..ply import lex


class Lexer:
    tokens = (
        'TOKEN',
    )

    @staticmethod
    def lexer(*args, **kwargs):
        return lex.lex(*args, **kwargs, module=Lexer)
