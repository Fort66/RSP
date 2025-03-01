from config.create_Objects import (
    screen,
    btn_group,
    player,
    computer,
    is_choice
    )


def choice_screen():
    """
    This function handles the choice screen of the game.
    It updates the buttons, players' choices, and changes the state of the game.
    """
    for btn in btn_group[1:]:
        btn.update(screen.window)

    player.update(sign="start")
    computer.update(sign="start")

    if player.player_choice:
        if not computer.player_choice:
            computer.set_choice()
        is_choice.change_is_choice
