from config.create_Objects import (
    player,
    computer,
    scores
    )


def win_screen():
    """
    Updates the game screen to reflect the winner of the game.

    This function checks the scores of the player and the computer and updates
    their respective signs to indicate the winner. If the player's score is
    greater than the computer's, the player's sign is updated to "win" and the
    computer's sign is updated to "start". If the computer's score is greater
    than the player's, the computer's sign is updated to "win" and the player's
    sign is updated to "start". If the scores are equal, both the player and
    the computer's signs are updated to "win".
    """
    if scores.player_score > scores.computer_score:
        computer.update(sign="start")
        player.update(sign="win")
    elif scores.player_score < scores.computer_score:
        computer.update(sign="win")
        player.update(sign="start")
    else:
        computer.update(sign="win")
        player.update(sign="win")
