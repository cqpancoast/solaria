

class Environment(object):
    """TEMPLATE CLASS for Environments.

    An Environment must be able to put a Reading, Interpreter, and Story
    together and produce an executable file. It also must be able to
    put Stories and their Editors together to form controllable Story-
    Editor complexes.
    """

    # Produce an executable file containing a Reading, Interpreter, and Story
    # hooked up correctly.
    def build(self):
        pass

    # Wire up Editor to Story and add the complex to the environment. Depending
    # on the Environment, this can kick out the previous Story-Editor or add
    # it to some sort of list.
    def add_story_editor(self, story, editor):
        pass
