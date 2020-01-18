

# TEMPLATE CLASS for StoryViews.
# A StoryView must be able to show some representation of a StoryModel.
class StoryView:

    def __init__(self, story_model):
        self.story_model = story_model
