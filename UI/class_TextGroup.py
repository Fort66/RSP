from dataclasses import dataclass, field


@dataclass
class TextGroup:
    """
    TextGroup is a class designed to manage a collection of text objects. It provides a way to update all the text objects
    contained within the group.

    Attributes:
        group (list): A list that holds the text objects.

    Methods:
        update(): Updates all the text objects in the group.
    """

    group: list = field(default_factory=list)

    def update(self):
        """
        Updates all the text objects in the group.

        This method iterates over the list of text objects and calls their update method. This allows for a centralized
        way to update all the text objects at once.
        """
        for obj in self.group:
            obj.update()
