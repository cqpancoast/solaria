

class RTModel(object):
    """TEMPLATE CLASS for ReadthroughModels.

    An RTModel must be able to accept user input provided by the
    RTController and store displayable output in a queue, to be
    displayed by the view when the controller decrees. When a queue
    item is displayed, this removes it from the queue.

    Note that this ties the model implementation to the view
    implementation, as the view must be such that it can display the
    output stored in this model's buffer.

    If an Interpreter is being used, that interpreter is accessed within
    this class.
    """

    def accept_reader_input(self, reader_input):
        """Accepts reader input from the controller and returns an output
        displayable by a view.

        Args:
            reader_input: input from the reader. Implementations of this class
            fix the type of the input.

        Returns:
            displayable: data displayable by the RTView.
        """

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
