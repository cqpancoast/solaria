

class Editor(object):
    """TEMPLATE CLASS for editors.

    An editor must be able to construct, revise, and display a Story.
    It also must be able to produce a read-only version of the Story.
    """

    def __init__(self, story):
        """Initialize this editor by giving it a Story to edit."""
        self.story = story

    def add(self, story_component):
        """Add a story component to the Story."""
        pass

    def edit(self, story_component):
        """Edit a component of the Story."""
        pass

    def remove(self, story_component):
        """Remove a component of the Story."""
        pass

    def visualize(self, story_component, options):
        """Display a visual representation of the story."""
        pass

    def build(self):
        """Produce a read-only version of the currently edited Story."""
        pass
