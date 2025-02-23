from config.create_Objects import computer, player, scores


def round_screen():
    """
    This function updates the player and computer choices, and adjusts the scores based on the game rules.
    """
    player.update(sign=player.player_choice)
    computer.update(sign=computer.player_choice)

    if player.player_choice == computer.player_choice:
        scores.change_scores()

    elif player.player_choice == "rock" and computer.player_choice == "scissors":
        scores.change_scores(1, 0)

    elif player.player_choice == "paper" and computer.player_choice == "rock":
        scores.change_scores(1, 0)

    elif player.player_choice == "scissors" and computer.player_choice == "paper":
        scores.change_scores(1, 0)

    else:
        scores.change_scores(0, 1)
