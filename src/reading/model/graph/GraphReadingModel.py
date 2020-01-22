from src.interpreter.graph.graph_string_interp import graph_string_interp
from src.reading.model import ReadingModel


# Represents a Reading as a Reader and a dictionary to active Paragraphs
# from the names of those Paragraphs' layers. A Reader is a  dictionary
# of zero or more variables. These change as a readthrough progresses to
# reflect its current state.
class GraphReadingModel(ReadingModel):

    # Creates GraphReadingModel. Generally called by GRMBuilder.
    def __init__(self, story_model, reader=None):
        if reader is None:
            reader = {}
        self.current_paragraphs = {}
        self.reader = reader

    # TODO process the damn user input!
    # Takes in the reader's input — could be a string, could be a screen touch
    # event. Outputs the story's response to that input given the Reader params
    # and the current Paragraphs.
    def interp_reader_input(self, reader_input):
        # Hand reader_input, self.reader (?), self.current_paragraphs off to
        # the appropriate interpreter for the type of reader_input.
        input_type = type(reader_input)
        interpreters = {
            "string": graph_string_interp
        }
        return interpreters[input_type](
            reader_input,
            self.reader,
            self.current_paragraphs
        )
