

# Represents a Story as a graph with nodes and edges.
# - The nodes are called Paragraphs, which contain story content that displays depending on the state of the Reader.
# - The edges are called Phrases, which connect Paragraphs to one another as well as to themselves, which change the
#   state of the Reader.
# TODO Should I code my own stuff for graphs or should I use software from somewhere else?
class GraphStoryModel:  # TODO should GSM have a parent class StoryModel?

    # Default constructor. Creates a GraphStoryModel with a single empty node.
    def __init__(self):  # TODO do when you know how you'll represent graphs
        return
