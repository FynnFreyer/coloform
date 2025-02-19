"""
Colorado is based on the colorama_ package by Jonathan Hartley.
It extends the available colors but entirely drops support for Windows.

.. colorama_: https://pypi.org/project/colorama/
"""
from colorama.ansi import BEL, Cursor

from colorado.ansi import Back, Fore, Style

__all__ = ["Fore", "Back", "Style", "Cursor", "BEL"]
