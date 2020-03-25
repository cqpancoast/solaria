from src.reading.story.StringBuilderStory import StringBuilderStory
from src.reading.storyteller.SimpleStoryteller import SimpleStoryteller
from src.reading.view.StringOptionView import StringOptionView


SimpleStoryteller(StringBuilderStory(), StringOptionView()).read()
