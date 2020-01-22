from src.story.view.StoryView import StoryView


# Represents a GraphStoryModel textually by listing its Paragraphs and
# Phrases. NOTE might be used in saving Stories?
class TextualGraphStoryView(StoryView):

    def render(self):
        print(self.story_model.str())
        # TODO make this more representative of the data structure:
        #   A command line editor for this shit would actually be really
        #   nice before I make a full GUI.
        # NOTE use appendable to control where this prints... or return?
