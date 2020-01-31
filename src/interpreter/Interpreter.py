

class Interpreter(object):
    """TEMPLATE CLASS for Interpreters.

    An Interpreter must be able to accept the reader's input, along with
    the current state of the Reading, and return output. If the
    Interpreter needs more data to produce output, it must query the Story
    appropriately."""

    def interpret(self, reader_input, reading_state):
        """Accept reader input and current Reading state, return response."""
        pass
