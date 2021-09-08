def convert():
    pass


def prioritize_converters():
    pass


def converters():
    yield Converter
    yield from Converter.__subclasses__()

class Converter:
    name = 'Default'
    regex = r'[^\n]+'
    priotity = 0

    def convert(self, value: str) -> str:
        return value
