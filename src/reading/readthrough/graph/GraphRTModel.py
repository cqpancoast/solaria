from src.reading.readthrough.mvc.RTModel import RTModel


class GraphRTModel(RTModel):
    """Represents the current state of a read session as:
        - a dictionary mapping to current nodes from the names of
          different "layers" in a layered graph with nodes and edges. A
          full description of the GraphStory framework can be found in
          the GraphStoryModel documentation. Notably, nodes are called
          "Paragraphs" and edges are called "Phrases". One can inhabit
          multiple Paragraphs simultaneously, as long as they are from
          different layers.
        - a dictionary mapping to lists of names of traversable edges  # NOTE
          from the names of the layers of current nodes.
        - a free-form dictionary of variables called a "reader".
        These are collected in a single dictionary object that is passed
        to the Interpreter, which is the thing that changes this model's
        state.

        A GraphRTModel also has a queue of objects that can be displayed
        by an RTView. TODO which RTViews?
    """

    def __init__(self):
        """Default constructor. Initializes this GraphRTModel with an empty
        queue, no current Paragraphs, an empty list of traversable phrases, and
        an empty reader."""

        self.displayable_queue = []
        self.readthrough_state = {
            "current_paragraph": {},
            "traversable_phrases": {},
            "reader": {}
        }

    def get_readthrough_state(self):
        """See base class."""

        return self.readthrough_state

    def add_displayable(self, displayable):
        """See base class."""

        self.displayable_queue.append(displayable)

    def get_next_displayable(self):
        """See base class."""

        return self.displayable_queue.pop(0)

    def is_queue_empty(self):
        """See base class."""

        return len(self.displayable_queue) == 0
