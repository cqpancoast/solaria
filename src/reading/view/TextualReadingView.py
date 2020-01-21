from src.reading.view import ReadingView


# Represents ReadingModel output textually, using any appendable object
# passed in during program initialization.
class TextualReadingView(ReadingView):

    # Initializes this object with a text-appendable object
    def __init__(self, appendable):
        # require that appendable is a text-appendable object
        self.ap = appendable

    # Parses the raw model output.
    # NOTE: will later have more features than just repetition
    def read_story(self, raw_model_output):
        self.ap.append(raw_model_output)

    # get_user_input!?!?!?
