from .lexer import Lexer
from ..ply import yacc


class Parser(Lexer):
    @staticmethod
    def p_stylesheet(p):
        '''stylesheet : stylesheet style
                      | style
                      | '''
        if len(p) > 1:
            p[0] = p[1]
            if len(p) > 2:
                p[0].update(p[2])
        else:
            p[0] = {}

    @staticmethod
    def p_style(p):
        '''style : STYLE_TARGET STYLE_START style_lines STYLE_END'''
        p[0] = {tuple(p[1].split('.')): dict(p[3])}

    @staticmethod
    def p_style_lines(p):
        '''style_lines : style_lines style_line
                       | style_line'''
        if len(p) > 2:
            p[0] = p[1] + p[2]
        else:
            p[0] = p[1]

    @staticmethod
    def p_style_line(p):
        '''style_line : STRING PAIR_SEP STRING LINE_SUFFIX'''
        p[0] = [(p[1], p[3])]

    @staticmethod
    def p_error(p):
        # TODO: Added extensive error reporting system to setup error logging to a relative user log file
        pass

    @staticmethod
    def parser(*args, **kwargs):
        return yacc.yacc(*args, **kwargs, module=Parser)
