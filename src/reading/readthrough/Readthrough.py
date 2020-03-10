

class Readthrough(object):
    """TEMPLATE CLASS for Readthroughs.

    A Readthrough is the center of a read session - it's what keeps
    things moving and what keeps track of the read session's state. It
    must be able to query a particular Story implementation for
    information and use that information to update the current state of
    the read session. Then, it must be able to use that current read
    session state to produce an Interaction, and send that Interaction
    out to a View. This dude's got a lot on its plate!
    """

    def start_reading(self):
        """
        Runs a read session.
        NOTE might add params (for loading saves, perhaps?)
        """

        pass
