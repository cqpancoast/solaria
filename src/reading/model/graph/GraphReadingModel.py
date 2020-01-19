from src.reading.model import ReadingModel


# Represents a Reading as a graph with nodes and edges. A Reader is a
# set of variables, including the current Node. These change as a
# readthrough progresses to reflect its current state.
# - The nodes are called Paragraphs, which contain story content that
#   displays depending on the state of the Reader.
# - The edges are called Phrases, which connect Paragraphs to one
#   another as well as to themselves, which change the
#   state of the Reader.
# - The graph also has "layers", which are roughly causally-independent
#   sets of nodes that overlap one another. Layers are defined by a
#   field in the Paragraph class, and are used to access a paragraph
#   from a particular layer in this class.
class GraphReadingModel(ReadingModel):

    # TODO use builder pattern to load GRM
    def __init__(self, story_model, reader=None):
        if reader is None:
            reader = {}
        self.current_paragraphs = {}
        self.reader = reader

    def interp_reader_input(self, reader_input):
        # TODO process the damn user input!
        return None
