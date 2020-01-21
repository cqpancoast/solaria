

# TEMPLATE CLASS for StoryViews.
# A StoryView must be able to show some representation of a StoryModel.
class StoryView:

    # Initializes the view with a reference to the model
    def __init__(self, story_model):
        # Require input to be graph story model
        self.story_model = story_model

    # Renders the model in some form
    def render(self):
        pass
