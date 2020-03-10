

class Interaction(object):
    """TEMPLATE CLASS for Interactions.

    An Interaction can present zero or more displayables and zero or
    more prompts, in any order. In the end, it will return a single
    object back to the caller, which is a Readthrough or Interpreter.
    """

    def interact(self):
        """ Interacts with the reader using a View.

        Combines reader responses to all Prompts in some manner to create a
        total result of the Interaction event, then returns that.

        Returns:
            The total result of the Interaction.
        """

        pass
