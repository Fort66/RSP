from dataclasses import dataclass


@dataclass
class RoundsCounter:
    """
    RoundsCounter is a class designed to keep track of the number of rounds.

    Core functionality:
    - Decrease the counter by 1 if it is greater than 0.

    Example usage:
    >>> counter = RoundsCounter()
    >>> counter.counter = 5
    >>> counter.decrease_counter
    >>> counter.counter
    4

    Constructor:
    - No constructor parameters.

    Limitations and side effects:
    - The counter can only be decreased, it cannot be increased directly.
    - The counter is a class variable, so it is shared across all instances of the class.
    """

    counter: int = 0

    @property
    def decrease_counter(self):
        if self.counter > 0:
            self.counter -= 1
