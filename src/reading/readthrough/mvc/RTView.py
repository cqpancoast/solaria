from src.reading.readthrough.mvc.RTModel import RTModel


class RTView(object):
    """TEMPLATE CLASS for ReadthroughViews.

    An RTView must be able to take an item from an RTModel's display
    queue and then display it.
    """

    def __init__(self, model: RTModel):
        """
        Initializes this RTView with an RTModel that it can display.

        Args:
            model: an RTModel
        """

        self.model = model

    def display(self):
        """Displays all elements in an RTModel's displayable buffer."""

        pass
