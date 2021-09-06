import re

from .element import Element
from .lexer import Lexer
from ..ply import yacc


def parse_tag_arguments(string):
    tag, *_ = re.findall(r'<(\w+)', string)
    return {
        'tag': tag,
        'attrs': dict(re.findall(r'(\w+)="([^"]*)"', string))
    }


class Parser(Lexer):
    @staticmethod
    def p_page(p):
        '''page : elements'''
        p[0] = Element(children=p[1])

    @staticmethod
    def p_elements(p):
        '''elements : elements element
                    | element'''
        if len(p) > 2:
            p[0] = p[1] + [p[2]]
        else:
            p[0] = [p[1]]

    @staticmethod
    def p_element(p):
        '''element : OPENTAG elements CLOSETAG
                   | TEXT
                   | OPENTAG CLOSETAG
                   | SELFCLOSINGTAG'''
        if len(p) > 2 or not isinstance(p[1], str):
            kwargs = parse_tag_arguments(p[1])
            if isinstance(p[2], list):
                kwargs.update(children=p[2])
            p[0] = Element.create_element(**kwargs)
        else:
            p[0] = p[1]

    @staticmethod
    def parser():
        return yacc.yacc(module=Parser)

    @staticmethod
    def p_error(token):
        pass # print(token)
