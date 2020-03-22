from src.reading.storyteller.Storyteller import Storyteller


class SimpleStoryteller(Storyteller):
    """Runs a storytelling session."""

    def read(self):
        while True:
            # get initial state from Story
            # 
