import pygame as pg

pg.init()


class SoundGame:
    """
    SoundGame is a class designed to handle sound playback in a game environment using the Pygame library.

    Core functionalities include:
    - Playing background music.
    - Playing sound effects.

    Parameters:
    - sound: The path to the sound file to be played.

    Usage:
    To play background music, call the `play_background` method with the path to the sound file.
    To play sound effects, call the `play_sound_game` method with the path to the sound file.
    """

    def play_background(self, sound):
        """
        Plays background music.

        Parameters:
        - sound: The path to the background music file.

        Usage:
        >>> game = SoundGame()
        >>> game.play_background('path/to/music/file.mp3')
        """
        if sound:
            self.sound = pg.mixer.music.load(sound)
            pg.mixer.music.set_volume(0.2)
            pg.mixer.music.play(-1)

    def play_sound_game(self, sound):
        """
        Plays sound effects.

        Parameters:
        - sound: The path to the sound effect file.

        Usage:
        >>> game = SoundGame()
        >>> game.play_sound_game('path/to/sound/file.wav')
        """
        if sound:
            self.sound = pg.mixer.Sound(sound)
            pg.mixer.Sound.set_volume(self.sound, 0.4)
            pg.mixer.Sound.play(self.sound)
