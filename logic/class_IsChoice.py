from dataclasses import dataclass

@dataclass
class IsChoice:
    """
    A simple class to represent a boolean choice.

    This class provides a single boolean attribute `is_choice` and a property
    to toggle its value. It is useful for scenarios where a simple boolean
    flag is needed that can be easily toggled.

    Attributes:
        is_choice (bool): A boolean attribute that can be toggled.

    Methods:
        change_is_choice: A property that toggles the value of `is_choice`.

    Usage:
        >>> choice = IsChoice()
        >>> choice.is_choice
        False
        >>> choice.change_is_choice
        >>> choice.is_choice
        True
    """

    is_choice: bool = False

    @property
    def change_is_choice(self):
        """
        Toggles the value of `is_choice`.

        This property changes the value of `is_choice` from `True` to `False`
        or from `False` to `True`, effectively toggling its state.

        Returns:
            None
        """
        self.is_choice = not self.is_choice
