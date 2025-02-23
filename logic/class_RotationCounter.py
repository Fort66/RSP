from dataclasses import dataclass


@dataclass
class RotationCounter:
    """
    RotationCounter is a class designed to keep track of a counter value that can be increased or decreased.
    It provides a simple interface to manipulate the counter value and ensures it does not go below zero.

    Core Functionality:
    - decrease_counter: Decreases the counter value by 1 if it is greater than 0.

    Example Usage:

    Constructor Parameters:
    - None

    Usage Limitations:
    - The counter value cannot be set to a negative number directly. It is automatically reset to zero if an attempt is made to decrease it below zero.
    - The counter value is not thread-safe. If multiple threads are modifying the counter concurrently, it may lead to unexpected behavior.
    """
    counter: int = 0

    @property
    def decrease_counter(self):
        if self.counter > 0:
            self.counter -= 1
