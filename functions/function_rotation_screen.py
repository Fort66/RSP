from config.create_Objects import (
    computer,
    player
    )


def rotation_screen():
    """
    Rotates the screen for the player and computer.

    This function rotates the player's screen by -45 degrees and the computer's screen by 45 degrees.
    It then updates the player and computer's screen with the new rotation.

    Returns:
        None
    """
    player.rotation(angle=-45)
    computer.rotation(angle=45)

    player.update(sign="start")
    computer.update(sign="start")
