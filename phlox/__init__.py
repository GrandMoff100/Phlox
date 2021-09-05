import colorama

from .rendering import render
from .styling import Style
from .scripting import Script
from .elements import (
    Body,
    Color,
    Div,
    Element,
    Page,
    LineDivider,
    Hidden,
    Blink,
    Bold,
    Dim,
    Underline
)

colorama.init()

__name__ = "Phlox"
__version__ = "1.0.0"
__description__ = "The terminal webbrowser"
__author__ = "GrandMoff100"
__author_email__ = "nlarsen23.student@gmail.com"
