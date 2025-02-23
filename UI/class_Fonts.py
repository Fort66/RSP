from pygame.font import SysFont
from dataclasses import dataclass


@dataclass(frozen=True)
class Fonts:
    """
    Fonts class provides access to system fonts with specified sizes.

    This class is designed to simplify the process of accessing system fonts with predefined sizes.
    It currently supports two fonts: Arial and Roboto, with specific sizes of 36 and 55 respectively.

    Example usage:
    >>> fonts = Fonts()
    >>> fonts.arial
    <pysdl2.font.Font object at 0x7f8e3a0b7a90>
    >>> fonts.roboto
    <pysdl2.font.Font object at 0x7f8e3a0b7b10>
    """

    arial: object = SysFont("Arial", 36)
    roboto: object = SysFont("Roboto", 55)
