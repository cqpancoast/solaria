

class Editor(object):
    """TEMPLATE CLASS for editors.

    An editor must be able to construct, revise, and display a set of
    data. It must then be able to compile that data down into a Story.
    """

    def add(self, story_component, component_name):
        """Add a story component to the Story."""
        pass

    def edit(self, component_name):
        """Edit a component of the Story."""
        pass

    def remove(self, component_name):
        """Remove a component of the Story."""
        pass

    def visualize(self, component_name, options):
        """Display a visual representation of the story."""
        pass

    def build(self):
        """Produce a read-only version of the currently edited Story."""
        pass
