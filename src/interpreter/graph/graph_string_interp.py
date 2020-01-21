

# Accepts the current state of the story and the reader's string input.
# Returns the story's response to this, which can be of any type.
# NOTE can it really be of any type? Make sure to be consistent here.
def graph_string_interp(reader_input, reader, current_paragraphs):
    return "Thanks! I was given:\n" \
           + reader_input.str() + "\n" \
           + reader.str() + "\n" \
           + current_paragraphs.str() + ".\n" \
           + "Have a nice day!"
