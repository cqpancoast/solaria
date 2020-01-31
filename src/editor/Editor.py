

# TEMPLATE CLASS for editors. An editor must be able to construct,
# revise, and display a story. TODO responsible for build?
class Editor:

    # Initialize this editor along with the editing environment.
    def __init__(self):
        pass

    # Add a story component to the story.
    def add(self, story_component):
        pass

    # Edit a component of the story.
    def edit(self, story_component):
        pass

    # Remove a component of the story.
    def remove(self, story_component):
        pass

    # Produce a visual representation of the story.
    def visualize(self, story_component, options):
        pass
