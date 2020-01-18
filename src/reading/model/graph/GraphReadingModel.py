from src.reading.model import ReadingModel


# Represents a Reading as a graph with nodes and edges. A Reader is a set of variables, including the current Node,
# which changes as the story progresses to reflect its state.
# - The nodes are called Paragraphs, which contain story content that displays depending on the state of the Reader
# - The edges are called Phrases, which connect Paragraphs to one another as well as to themselves, which change the
#   state of the Reader.
class GraphReadingModel(ReadingModel):

    # TODO add references to fields:
    #   - current_paragraph
    #   - reader

    # TODO use builder pattern to load GRM
    def __init__(self):
        return

    def process_user_input(self, user_input):
        # TODO process the damn user input!
        #   Keep in mind that these can be any objects being taken in and being returned
        #   How do we structure our project knowing that processing user input is easily the most complicated part?
        return None
