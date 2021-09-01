from ..ply import lex

EXCLUDE_REGEX = r'[^\.:;{}\n\t ]'


class Lexer:
    # precedence = ()

    tokens = (
        'STYLE_TARGET',
        'STRING',
        'LINE_SUFFIX',
        'PAIR_SEP',
        'STYLE_END',
        'STYLE_START'
    )



    t_STRING = rf'{EXCLUDE_REGEX}+'
    t_STYLE_TARGET = rf'({t_STRING}\.?)+'
    t_STYLE_START = r'{'
    t_STYLE_END = r'}'
    t_PAIR_SEP = ':'
    t_LINE_SUFFIX = ';'

    t_ignore = '\n\t '

    @staticmethod
    def t_error(tok):
        pass

    @staticmethod
    def lexer(*args, **kwargs):
        return lex.lex(*args, module=Lexer, **kwargs)
