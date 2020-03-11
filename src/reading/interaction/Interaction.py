

class Interaction(object):
    """TEMPLATE CLASS for Interactions.

    An Interaction is a sequence of displayables and prompts that
    display on a View in order. Interactions are created by Readthroughs
    using the current read session state, but are not able to reference
    that data themselves, nor are they able to reference the Story. This
    class's single method returns instructions of some sort that tell
    the Readthrough how to update its state.
    """

    def interact(self, view):
        """Interacts with the reader using a View.

        Uses reader responses to zero or more of this Interaction's prompts to
        construct an instruction set informing a Readthrough how to update its
        state.

        Returns:
            State-update instructions for a Readthrough.
        """

        pass
