

class Readthrough(object):
    """TEMPLATE CLASS for Readthroughs.

    A Readthrough is the center of a read session - it's what keeps
    things moving and what keeps track of the read session's state. It
    must be able to use the current read session state to produce an
    Interaction, and send that Interaction out to a View. Then, it must
    use the output of that interaction to update its state, often by
    querying its Story.
    """

    def start_reading(self):
        """ Runs a read session. """

        pass
