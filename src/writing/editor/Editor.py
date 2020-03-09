from src.writing.draft.Draft import Draft


class Editor(object):
    """TEMPLATE CLASS for Editors.

    An editor must be able to construct, revise, and display a Draft.
    It also must be able to put a Readthrough, View, and Story together
    to produce an executable file.
    """

    def __init__(self, draft: Draft):
        """Initialize this editor with a Draft."""

        self.draft = draft

    def add(self, story_component, component_name):
        """Add a story component to the Draft."""

        pass

    def edit(self, component_name):
        """Edit a component of the Draft."""

        pass

    def remove(self, component_name):
        """Remove a component of the Draft."""

        pass

    def visualize(self, component_name, options):
        """Display a visual representation of the Draft."""

        pass

    def build(self):
        """Produce an executable file containing a Readthrough, View, and Story
        hooked up correctly.
        """

        pass

