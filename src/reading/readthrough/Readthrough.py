

class Readthrough(object):
    """TEMPLATE CLASS for Readthroughs.

    A Readthrough must accept reader input and present prompt output.
    These methods are separated so that a single input can present any
    number of outputs, rather than just one.

    In any read session but the simplest, a Readthrough should store the
    state of the read session, which could mean many different things
    for each read session.
    """

    def accept_reader_input(self, reader_input):
        """Accept reader input in whatever form the implementation
        requires.
        """

        pass

    def present_output(self):
        """Produce output in whatever manner is specified by the implementing
        class.
        """

        pass
