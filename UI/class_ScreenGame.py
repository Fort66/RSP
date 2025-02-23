import pygame as pg
from pygame.display import set_mode, set_caption, set_icon, get_desktop_sizes
from pygame.locals import RESIZABLE, FULLSCREEN
from pygame.image import load

from dataclasses import dataclass

pg.init()


@dataclass
class ScreenGame:
    """
    The ScreenGame class is designed to initialize and configure a game window with customizable properties such as size,
    color, caption, and icon. It supports resizable and fullscreen modes.

    Attributes:
        size (tuple): The dimensions of the game window (width, height).
        color (str | tuple): The background color of the game window.
        caption (str): The title of the game window.
        icon (str): The path to the icon file for the game window.
        is_resizable (bool): Indicates whether the game window should be resizable.
        is_fullscreen (bool): Indicates whether the game window should be fullscreen.
    """

    size: tuple = (0, 0)
    color: str | tuple = "SteelBlue"
    caption: str = "Game"
    icon: str = ""
    is_resizable: bool = False
    is_fullscreen: bool = False

    def __post_init__(self):
        """
        Initializes the game window based on the provided configuration.

        This method sets the window mode (resizable or fullscreen), sets the window caption, and sets the window icon if
        provided. It also retrieves the window rectangle for further use.

        Note:
            This method assumes that the necessary Pygame functions (`set_mode`, `get_desktop_sizes`, `set_caption`,
            `set_icon`, `load`, and `get_rect`) are available and properly imported.
        """
        if self.is_resizable:
            self.window = set_mode(self.size, RESIZABLE)
        elif self.is_fullscreen:
            self.window = set_mode(get_desktop_sizes()[0], FULLSCREEN)
        else:
            self.window = set_mode(self.size)

        set_caption(self.caption)

        if self.icon:
            set_icon(load(self.icon))

        self.rect = self.window.get_rect()
