from ..ply import lex
from ..elements import Element



class Lexer:

    tokens = (
        'STYLE_TARGET',
        'STRING',
        'LINE_SUFFIX',
        'PAIR_SEP',
        'STYLE_END',
        'STYLE_START'
    )

    @staticmethod
    def t_STYLETARGET(tok):
        '''([^:;{}\n\t ]+)'''
        for tag, cls in Element.element_tags().items():
            if cls.styleable:
                if tok.value == tag or tok.value.startswith(tag + '.'):
                    tok.type = 'STYLE_TARGET'
                    return tok
        tok.type = 'STRING'
        return tok

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
