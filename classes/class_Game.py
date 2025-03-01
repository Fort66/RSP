import pygame as pg

from config.create_Objects import (
    screen,
    is_start,
    is_choice,
    rotation_counter,
    rounds_counter,
    player,
    computer,
    scores,
    sound_game,
)
from classes.class_CheckEvents import CheckEvents

from functions.function_start_screen import start_screen
from functions.function_choice_screen import choice_screen
from functions.function_rotation_screen import rotation_screen
from functions.function_round_screen import round_screen
from functions.function_win_screen import win_screen
from functions.function_create_text import create_text


class Game:
    """
    The Game class is responsible for managing the main game loop and handling the game's state.
    It initializes the game's clock, event checking mechanism, and starts playing background music.
    The main game loop runs until the game is over, handling different screens and game logic.

    Core functionalities:
    - Initializes game clock and event checking mechanism.
    - Plays background music.
    - Manages game loop to handle different screens and game logic.
    - Updates the game state based on user input and game rules.

    Example usage:
    game = Game()
    game.run_game()

    Constructor parameters:
    - None

    Usage limitations:
    - The class assumes that the necessary modules and classes (e.g., pg, CheckEvents, sound_game, etc.) are already imported and initialized.
    - The class assumes that the game's state is managed by external variables and classes (e.g., is_start, is_choice, rotation_counter, rounds_counter, scores, etc.).
    """

    def __init__(self):
        self.run = True
        self.clock = pg.time.Clock()
        self.check_events = CheckEvents(self)
        sound_game.play_background("sounds/back_music.mp3")

    def run_game(self):
        while self.run:
            screen.window.fill(screen.color)
            self.check_events.check_events()
            create_text()

            if not is_start.is_start:
                start_screen()

            elif is_start.is_start and not is_choice.is_choice:
                choice_screen()

            elif is_start.is_start and is_choice.is_choice:
                if rotation_counter.counter > 0:
                    if rotation_counter.counter % 2 == 0:
                        sound_game.play_sound_game("sounds/rotation.mp3")
                    rotation_screen()
                    rotation_counter.decrease_counter
                    pg.display.update()
                    pg.time.delay(500)
                else:
                    if rounds_counter.counter > 0:
                        rounds_counter.decrease_counter
                    rotation_counter.counter = 6
                    is_choice.change_is_choice
                    screen.window.fill(screen.color)
                    round_screen()
                    create_text()
                    pg.display.update()
                    pg.time.delay(2000)
                    player.player_choice = ""
                    computer.player_choice = ""

            if rounds_counter.counter <= 0:
                screen.window.fill(screen.color)
                pg.mixer.music.pause()
                sound_game.play_sound_game("sounds/win.mp3")
                win_screen()
                create_text()
                pg.display.update()
                pg.time.delay(3500)
                pg.mixer.music.unpause()
                rounds_counter.counter = 5
                is_start.change_is_start()
                scores.player_score = 0
                scores.computer_score = 0

            pg.display.update()
