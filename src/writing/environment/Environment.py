

class Environment(object):
    """TEMPLATE CLASS for Environments.

    An Environment must be able to put a Readthrough, Interpreter, and
    Story together and produce an executable file. It also must be able
    to put Drafts and their Editors together to form controllable Draft-
    Editor complexes.
    """

    def build(self):
        """Produce an executable file containing a Readthrough, Interpreter,
        and Story hooked up correctly.
        """

        pass

    def add_story_editor(self, draft_story, editor):
        """Wire up Editor to Draft and add the complex to the Environment.
        Depending on the Environment, this can kick out the previous
        Draft-Editor or add it to some sort of list.

        Args:
            draft_story:
            editor:

        """

        pass
