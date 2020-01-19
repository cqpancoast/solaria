from src.story.model import StoryModel
import networkx as nx


# Represents a Story as a graph with nodes and edges.
# - The nodes are called Paragraphs, which contain story content that
#   displays depending on the state of the Reader.
# - The edges are called Phrases, which connect Paragraphs to one
#   another as well as to themselves, which change the state of the
#   Reader.
class GraphStoryModel(StoryModel):

    # Default constructor. Creates a null Graph.
    def __init__(self):
        self.graph = nx.MultiDiGraph()

    # TODO write other constructors using Builder pattern and NX prescription
