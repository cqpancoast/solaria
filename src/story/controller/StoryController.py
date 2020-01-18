

# TEMPLATE CLASS for StoryControllers.
# A StoryController must be able to manage a StoryModel and StoryView.
class StoryController:

    def __init__(self, story_model, story_view):
        self.story_model = story_model
        self.story_view = story_view

    def go(self):
        return
