import pygame as pg
from pygame.locals import MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame.font import Font, SysFont

from dataclasses import dataclass, field, InitVar


@dataclass
class Button:
    """
    A class representing a button with customizable properties and event handling.

    This class provides a way to create a button with various properties such as position,
    size, text, font, colors, and event handling for mouse interactions. It supports
    hover and click events and can execute a callback function when clicked.

    Attributes:
        pos (tuple): Position of the button on the screen (x, y).
        size (tuple): Size of the button (width, height).
        text (str): Text displayed on the button.
        font (pygame.font.Font): Font used for the button text.
        font_size (int): Size of the font.
        bg_color (str | tuple): Background color of the button.
        text_color (str | tuple): Color of the text.
        hover_color (str | tuple): Color of the button when hovered.
        click_color (str | tuple): Color of the button when clicked.
        is_hovered (bool): Whether the mouse is currently hovering over the button.
        is_clicked (bool): Whether the button is currently clicked.
        on_click_references (object): Callback function to execute when the button is clicked.
        reference_args (tuple): Arguments to pass to the callback function.
        reference_kwargs (dict): Keyword arguments to pass to the callback function.
    """

    pos: tuple = (0, 0)
    size: tuple = (0, 0)

    text: str = ""
    font: InitVar[Font] = None
    font_size: int = 26

    bg_color: str | tuple = (118, 172, 218)
    text_color: str | tuple = "white"
    hover_color: str | tuple = (23, 74, 117)
    click_color: str | tuple = (73, 107, 135)

    is_hovered: bool = False
    is_clicked: bool = False

    on_click_references: object = None
    reference_args: tuple = field(default_factory=tuple)
    reference_kwargs: dict = field(default_factory=dict)

    def __post_init__(self, font: str):
        """
        Post-initialization method to set up the button's properties.

        Args:
            font (str): Font name to use for the button text.
        """
        self.rect = pg.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.font = (
            Font(font, self.font_size) if font else SysFont("Arial", self.font_size)
        )

    def handle_event(self, event):
        """
        Handle events related to the button.

        Args:
            event (pygame.event.Event): Event to handle.
        """
        if event.type == MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)

        elif event.type == MOUSEBUTTONDOWN:

            if event.button == 1 and self.is_hovered:
                self.is_clicked = True

                if self.on_click_references:
                    self.on_click_references(
                        *self.reference_args, **self.reference_kwargs
                    )

        elif event.type == MOUSEBUTTONUP:
            self.is_clicked = False

    def update(self, surface):
        """
        Update the button's appearance based on its state.

        Args:
            surface (pygame.Surface): Surface to draw the button on.
        """
        if self.is_clicked:
            self.color = self.click_color

        elif self.is_hovered:
            self.color = self.hover_color

        else:
            self.color = self.bg_color

        pg.draw.rect(surface, self.color, self.rect, border_radius=20)

        if self.text:
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)
