try:
    import colorama

    from .rendering import render
    from .styling import Style
    from .scripting import Script
    from .elements import (
        Body,
        Div,
        Element,
        Page,
        Break,
        Resource,
        Text,
        Link
    )

    colorama.init()
except ImportError as err:
    print('Running with imports because of:', err)

__name__ = "Phlox"
__version__ = "1.0.0"
__description__ = "The terminal webbrowser"
__author__ = "GrandMoff100"
__author_email__ = "nlarsen23.student@gmail.com"
