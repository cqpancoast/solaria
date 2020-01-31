

# TEMPLATE CLASS for editors. An editor must be able to construct,
# revise, and display a Story. It also must be able to produce a read-
# only version of the Story.
class Editor:

    # Initialize this editor by giving it a Story to edit.
    def __init__(self, story):
        self.story = story

    # Add a story component to the Story.
    def add(self, story_component):
        pass

    # Edit a component of the Story.
    def edit(self, story_component):
        pass

    # Remove a component of the Story.
    def remove(self, story_component):
        pass

    # Display a visual representation of the story.
    def visualize(self, story_component, options):
        pass

    # Produce a read-only version of the currently edited Story.
    def build(self):
        pass
