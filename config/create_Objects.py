"""
Module for creating game objects.

This module contains classes and functions for creating game objects such as ScreenGame, Button, Colors, Fonts, Player, SoundGame, IsStart, IsChoice, RotationCounter, Scores, RoundsCounter.

Classes:
    - ScreenGame: Class for creating game screen.
    - Button: Class for creating game buttons.
    - Colors: Class for defining game colors.
    - Fonts: Class for defining game fonts.
    - Player: Class for creating game players.
    - SoundGame: Class for managing game sounds.
    - IsStart: Class for managing game start state.
    - IsChoice: Class for managing game choice state.
    - RotationCounter: Class for managing game rotation counter.
    - Scores: Class for managing game scores.
    - RoundsCounter: Class for managing game rounds counter.

Functions:
    - create_objects: Function for creating game objects.
"""

from UI.class_ScreenGame import ScreenGame
from UI.class_Button import Button
from UI.class_Colors import Colors
from UI.class_Fonts import Fonts

from classes.class_Player import Player
from classes.class_SoundGame import SoundGame

from logic.class_IsStart import IsStart
from logic.class_IsChoice import IsChoice
from logic.class_RotationCounter import RotationCounter
from logic.class_Scores import Scores
from logic.class_RoundsCounter import RoundsCounter

colors = Colors()
fonts = Fonts()
is_start = IsStart()
is_choice = IsChoice()
rotation_counter = RotationCounter(6)
scores = Scores()
rounds_counter = RoundsCounter(5)
sound_game = SoundGame()


screen = ScreenGame(
    size=(800, 600),
    color="SteelBlue",
    caption="Камень Ножницы Бумага",
    icon="images/win.png",
)

player = Player(
    name="Игрок", scale_value=0.16, center_pos=(100, screen.size[1] // 2), screen=screen
)

computer = Player(
    name="Компьютер",
    scale_value=0.16,
    center_pos=(screen.size[0] - 100, screen.size[1] // 2),
    auto_game=True,
    screen=screen,
)

btn_group = [
    Button(
        pos=(screen.size[0] // 2 - 100, screen.size[1] // 2),
        size=(200, 50),
        text="Старт",
        on_click_references=is_start.change_is_start,
    ),
    Button(
        pos=(screen.size[0] // 2 - 175, screen.size[1] // 2 + 100),
        size=(100, 50),
        text="Камень",
        reference_kwargs=dict(value="rock"),
        on_click_references=player.set_choice,
    ),
    Button(
        pos=(screen.size[0] // 2 - 50, screen.size[1] // 2 + 100),
        size=(100, 50),
        text="Ножницы",
        reference_kwargs=dict(value="scissors"),
        on_click_references=player.set_choice,
    ),
    Button(
        pos=(screen.size[0] // 2 + 75, screen.size[1] // 2 + 100),
        size=(100, 50),
        text="Бумага",
        reference_kwargs=dict(value="paper"),
        on_click_references=player.set_choice,
    ),
]
