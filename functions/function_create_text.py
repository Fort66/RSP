from UI.class_DrawText import DrawText
from UI.class_TextGroup import TextGroup

from config.create_Objects import (
    screen,
    fonts,
    colors,
    rounds_counter,
    scores
    )


def create_text():
    """
    Creates a text group with two DrawText objects to display the remaining rounds and the player's and computer's scores.

    The text group consists of two DrawText objects:
    1. Displays the remaining rounds counter.
    2. Displays the player's and computer's scores.

    The positions of the text objects are calculated based on the screen size.
    """
    text_group = TextGroup(
        group=[
            DrawText(
                screen=screen.window,
                font=fonts.roboto,
                color=colors.yellow,
                pos=(screen.size[0] // 2 - 190, 50),
                text=f"Осталось раундов: {rounds_counter.counter}",
            ),
            DrawText(
                screen=screen.window,
                font=fonts.roboto,
                color=colors.yellow,
                pos=(screen.size[0] // 2 - 30, screen.size[1] - 100),
                text=f"{scores.player_score} : {scores.computer_score}",
            ),
        ]
    )

    text_group.update()
