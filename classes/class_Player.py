from pygame.transform import (
    rotozoom,
    flip,
    scale_by
    )
from pygame.image import load

from random import choice
from collections import OrderedDict

from dataclasses import (
    dataclass,
    field
    )


@dataclass
class Player:
    """
    The Player class represents a player in a game, managing their choices and visual representation.

    Attributes:
        name (str): The name of the player.
        scale_value (float): The scaling factor for the player's images.
        center_pos (tuple): The center position of the player's images on the screen.
        screen (object): The screen object where the player's images are drawn.
        is_start (bool): Indicates if the game has started.
        is_rotation (bool): Indicates if the player's image is currently rotating.
        is_win (bool): Indicates if the player has won.
        auto_game (bool): Indicates if the game is in automatic mode.
        player_choice (str): The player's current choice (rock, paper, scissors).

    Methods:
        __post_init__(): Initializes the player's images based on the game mode.
        set_choice(value="auto"): Sets the player's choice to a specified value or randomly selects one.
        rotation(angle=0): Rotates the player's image by a specified angle.
        update(sign=None): Updates the screen with the player's current image.
    """

    name: str = ""
    scale_value: float = 1.0
    center_pos: tuple = (0, 0)
    screen: object = None

    is_start: bool = False
    is_rotation: bool = False
    is_win: bool = False
    auto_game: bool = False

    player_choice: str = ""
    sign_dict: dict = field(default_factory=OrderedDict)

    def __post_init__(self):
        self.sign_dict["rock"] = (
            scale_by(load("images/rock.png").convert_alpha(), self.scale_value)
            if not self.auto_game
            else flip(
                scale_by(load("images/rock.png").convert_alpha(), self.scale_value),
                True,
                False,
            )
        )

        self.sign_dict["paper"] = (
            scale_by(load("images/paper.png").convert_alpha(), self.scale_value)
            if not self.auto_game
            else flip(
                scale_by(load("images/paper.png").convert_alpha(), self.scale_value),
                True,
                False,
            )
        )

        self.sign_dict["scissors"] = (
            scale_by(load("images/scissors.png").convert_alpha(), self.scale_value)
            if not self.auto_game
            else flip(
                scale_by(load("images/scissors.png").convert_alpha(), self.scale_value),
                True,
                False,
            )
        )

        self.sign_dict["start"] = (
            scale_by(load("images/start.png").convert_alpha(), self.scale_value)
            if not self.auto_game
            else flip(
                scale_by(load("images/start.png").convert_alpha(), self.scale_value),
                True,
                False,
            )
        )

        self.common_rect = self.sign_dict["start"].get_rect(center=self.center_pos)
        self.sign_rotation = self.sign_dict["start"].copy()

        self.sign_dict["win"] = (
            scale_by(load("images/win.png").convert_alpha(), self.scale_value)
            if not self.auto_game
            else flip(
                scale_by(load("images/win.png").convert_alpha(), self.scale_value),
                True,
                False,
            )
        )

    def set_choice(self, value="auto"):

        if value != "auto":
            self.player_choice = value
        else:
            self.player_choice = choice(list(self.sign_dict.keys())[:3])

    def rotation(self, angle=0):
        if self.is_rotation:
            self.is_rotation = False
            self.sign_rotation = self.sign_dict["start"].copy()
            self.common_rect = self.sign_dict["start"].get_rect(center=self.center_pos)

        else:
            self.is_rotation = True
            self.common_rect = self.sign_rotation.get_rect(
                center=(self.center_pos[0] - 50, self.center_pos[1] + 50)
            )
            self.sign_rotation = rotozoom(self.sign_dict["start"], angle, 1)

    def update(self, sign=None):
        if not self.is_rotation:
            self.screen.window.blit(self.sign_dict[sign], self.common_rect)
        else:
            self.screen.window.blit(self.sign_rotation, self.common_rect)
