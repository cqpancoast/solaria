

# TEMPLATE CLASS for Controllers.
# A Controller must be able to manage a Model and View.
class ReadingController:

    def __init__(self, reading_model, reading_view):
        self.reading_model = reading_model
        self.reading_view = reading_view

    def go(self):
        return
