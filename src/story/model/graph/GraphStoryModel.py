from src.story.model import StoryModel
import networkx as nx


# Represents a Story as a graph with nodes, organized into layers, and
# edges.
# - The nodes are called Paragraphs, which contain story content that
#   displays depending on the state of the Reader.
# - The edges are called Phrases, which connect Paragraphs to one
#   another as well as to themselves, which change the
#   state of the Reader.
# - The graph also has "layers", which are roughly causally-independent
#   sets of nodes that overlap one another. Layers are defined by a
#   field in the Paragraph class, and are used to access a paragraph
#   from a particular layer in this class.
class GraphStoryModel(StoryModel):

    # Default constructor. Creates a null Graph.
    def __init__(self):
        self.graph = nx.MultiDiGraph()

    # TODO Creation from EditableGSM? Or should this already be editable?

    # TODO Create from pickle file or something idk
