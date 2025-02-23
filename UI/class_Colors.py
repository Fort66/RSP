from dataclasses import dataclass


@dataclass(frozen=True)
class Colors:
    """
    The Colors class provides predefined color constants in both string and tuple formats.

    This class is designed to simplify the usage of color constants by providing them in both
    string and tuple formats. This can be useful for applications that require colors in different
    formats or for applications that need to support both string and tuple color representations.

    Core Functionality:
    - Provides predefined color constants in both string and tuple formats.

    Example Usage:

    Constructor:
    - No constructor parameters are required.

    Usage Limitations:
    - This class is a static class and does not have a constructor. All color constants are
      available as class attributes.

    Potential Side Effects:
    - None.
    """

    white: str | tuple = "white"
    yellow: str | tuple = "yellow"
