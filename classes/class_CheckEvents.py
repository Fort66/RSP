import pygame as pg
from pygame.locals import QUIT, K_ESCAPE, KEYDOWN

from config.create_Objects import btn_group


class CheckEvents:
    """
    The CheckEvents class is responsible for handling events in a game loop.
    It checks for specific events such as quitting the game or pressing the escape key.
    Additionally, it delegates event handling to a group of buttons.

    Attributes:
        game (Game): The game instance associated with this event checker.

    Methods:
        __init__(game=None): Initializes the CheckEvents instance with an optional game instance.
        check_events(): Processes events and updates the game state accordingly.
    """

    def __init__(self, game=None):
        """
        Initializes the CheckEvents instance.

        Args:
            game (Game, optional): The game instance to associate with this event checker. Defaults to None.
        """
        self.game = game

    def check_events(self):
        """
        Processes events and updates the game state accordingly.

        This method checks for events such as quitting the game or pressing the escape key.
        It also delegates event handling to a group of buttons.
        """
        for event in pg.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.game.run = False

            for btn in btn_group:
                btn.handle_event(event)
