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
    t_TEXT = r'[^<>]+'
    t_SELFCLOSINGTAG = r'<\w+ ([^>]*)\/>'

    @staticmethod
    def t_error(token):
        print(token)

    @staticmethod
    def lexer():
        return lex.lex(module=Lexer)
