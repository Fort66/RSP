from config.create_Objects import screen, btn_group, player, computer


def start_screen():
    """
    Updates the start screen of the game.

    This function updates the button group and the player and computer objects
    to reflect the start screen state. It is called when the game starts or
    when the player returns to the start screen from another screen.
    """
    btn_group[0].update(screen.window)
    player.update(sign="start")
    computer.update(sign="start")
