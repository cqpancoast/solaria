

class RTModel(object):
    """TEMPLATE CLASS for ReadthroughModels.

    An RTModel must be able to store displayable output in a queue, to
    be displayed by the view when the controller decrees. When a queue
    item is displayed, this removes it from the queue. The queue also
    must be able to be incremented.

    This also must be able to return a current state, if it has one.
    If it doesn't have one, it will return None.
    """

    def get_readthrough_state(self):
        """
        Returns:
            The current state of this readthrough.
        """

        pass

    def add_displayable(self, displayable):
        """Adds a displayable to this RTModel's queue."""

        pass

    def get_next_displayable(self):
        """
        Returns:
            The next displayable object in this RTModel's queue.
        """

        pass

    def is_queue_empty(self):
        """
        Returns:
            Whether this RTModel's queue is empty.
        """

        pass
