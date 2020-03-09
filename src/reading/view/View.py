

class View(object):
    """TEMPLATE CLASS for Views.

    Displays an Interaction's displayable, if it has one, and then its
    Prompt, if it has one. Must be able to accept reader input to
    "answer" the prompt. A good View supports as many kinds of
    displayables and Prompts as possible.
    """

    def present_interaction(self, interaction):
        pass
