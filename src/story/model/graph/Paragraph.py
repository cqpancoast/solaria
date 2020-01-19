

# A Paragraph is a "position" in a GraphStory that a Reader can be in.
#
# Paragraphs display prompts upon reader entry depending upon the Reader
# state. A Paragraph has zero or more directed edges, called Phrases,
# that direct to a destination Paragraph. This new Paragraph can be the
# origin Paragraph. A Paragraph also has zero or more Phrases that feed
# into it.
#
# The inhabiting  of a Paragraph never deviates from this prescription:
#   - The Paragraph accepts the Reader, and prints out a prompt
#     depending on the Reader's state.
#   - The reader (lowercase L) types in or chooses an input.
#   - The Paragraph sends that input off to the interpreter, along with
#     some information about itself. TODO clarify this and below
#   - Based on the response from the interpreter, the Paragraph either
#     prints out some kind of error-style message or sends a user down
#     a Phrase.
#
# A Paragraph also has the additional layer property. Layers are a field
# in a Paragraph that allows a Reader to inhabit multiple Paragraphs at
# once. This is accomplished by two or more Phrases pointing away from
# the same Paragraph having the same name, all pointing to Paragraphs
# from different layers. It is illegal to have two Phrases of the same
# name and source paragraph directed towards Paragraphs on the same
# layer.
class Paragraph:

