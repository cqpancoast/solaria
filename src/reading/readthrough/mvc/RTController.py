from src.reading.readthrough.Readthrough import Readthrough
from src.reading.readthrough.mvc.RTModel import RTModel
from src.reading.readthrough.mvc.RTView import RTView


class RTController(Readthrough):
    """Keeps chosen RTView and RTModel in lockstep for Readthroughs
    organized into an MVC architecture. This is the front-facing
    component of the trio that interacts with the reader directly.
    """

    def __init__(self, model: RTModel, view: RTView):
        """Initializes this RTController with an appropriate model and view.

        Args:
            model: an RTModel
            view: an RTView
        """

        self.model = model
        self.view = view

    def go(self):
        """Runs and manages a read session. Generally, the cycle will look like
        this:
        - Accepts user input from the view,
        - passes it to the model,
        - displays model output via the view, and
        - waits for user input.
        """

        pass

    def accept_reader_input(self, reader_input):
        """See base class."""

        pass

    def present_output(self):
        """See base class."""

        pass
