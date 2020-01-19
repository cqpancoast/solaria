from src.reading.model import ReadingModel


# Represents a Reading as a Reader and a set of current Paragraphs. A
# Reader is a dictionary of zero or more variables. These change as a
# readthrough progresses to reflect its current state. The current
# Paragraphs are the set of
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
