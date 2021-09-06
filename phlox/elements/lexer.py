from ..ply import lex


class Lexer:
    tokens = (
        'OPENTAG',
        'CLOSETAG',
        'TEXT',
        'SELFCLOSINGTAG'
    )

    t_OPENTAG = r'<\w+ ([^>]*)>'
    t_CLOSETAG = r'<\/\w+>'

    def t_TEXT(t):
        r'[^<>]+'
        for char in Lexer.t_ignore:
            t.value = t.value.replace(char, '')
        t.value = t.value.replace('    ', '')
        return t

    t_SELFCLOSINGTAG = r'<\w+ ([^>]*)\/>'

    t_ignore = '\n\t'

    @staticmethod
    def t_error(token):
        pass # print(token)

    @staticmethod
    def lexer():
        return lex.lex(module=Lexer)
