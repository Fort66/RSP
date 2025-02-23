from dataclasses import dataclass


@dataclass
class Scores:
    """
    A class to keep track of scores for a game between a player and a computer.

    Attributes:
        player_score (int): The score of the player.
        computer_score (int): The score of the computer.

    Methods:
        change_scores(player_score=0, computer_score=0): Updates the player and computer scores by the given amounts.
    """

    player_score: int = 0
    computer_score: int = 0

    def change_scores(self, player_score=0, computer_score=0):
        """
        Updates the player and computer scores by the given amounts.

        Args:
            player_score (int): The amount to add to the player's score. Defaults to 0.
            computer_score (int): The amount to add to the computer's score. Defaults to 0.
        """
        self.player_score += player_score
        self.computer_score += computer_score
