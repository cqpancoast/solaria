from src.story.view.StoryView import StoryView


# Represents a GraphStoryModel textually by listing its Paragraphs and
# Phrases.
class TextualGraphStoryView(StoryView):

    def render(self):
        print(self.story_model.str())
        # NOTE use appendable to control where this prints, or return?
