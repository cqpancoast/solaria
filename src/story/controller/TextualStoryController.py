from src.story.controller import StoryController


# Provides a text-based controller for interacting with a Story editing
# session. Accepts info from the user and confers that to the model,
# renders view in appropriate ways when necessary.
class TextualStoryController(StoryController):

    def __init__(self, rd, ap):
        self.rd = rd;
        self.ap = ap;
        super.__init__()  # TODO how to do?
