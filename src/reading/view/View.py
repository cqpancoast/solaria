

class View(object):
    """TEMPLATE CLASS for Views.

    Displays Displayables and presents Prompts. Must be able to accept
    reader input to "answer" a prompt. A good View supports as many
    kinds of Displayables and Prompts as possible. A View can also
    support meta-level operations like saving and quitting, but does not
    have to.
    """

    def display(self, displayable):
        """ Displays a displayable.

        Args:
            displayable: The displayable to be Displayed.

        Raises:
            NOTE [some exception] if this View does not support the
            Displayable.
        """

        pass

    def prompt(self, prompt):
        """ Prompts the reader with the given Prompt. Processes the Prompt such
        that the processed reader response does not depend on the View, then
        calls back to the Prompt for Interpretation. Finally, returns the
        interpreted response.

        Args:
            prompt: The Prompt to be used to prompt the reader.

        Returns:
            Reader response as interpreted by the Prompt.

        Raises:
            NOTE [some exception] if this View does not support the Prompt.
        """

        pass
