# The Solaria Framework

*The Solaria Framework* is a two-piece component-based structure for developers to follow to design programs that allow users (writers or readers) to write or read interactive storytelling. In particular, implementations of this structure will typically reside inside other programs, keeping track of their interactive-storytelling parts.

From the [wikipedia page](https://en.wikipedia.org/wiki/Interactive_storytelling):

> Interactive storytelling […] is a form of digital entertainment in which the storyline is not predetermined. The author creates the setting, characters, and situation which the narrative must address, but the user (also reader or player) experiences a unique story based on their interactions with the story world.

After that, their definition gets way too specific, neglecting to separate function from implementation. (Even this part of the definition is a little implementation-specific for me (who says there’s characters?), but it will serve.)

There are three users at play here: the developer, the writer, and the reader. The choice of an *embeddable framework* as a central data structure was made for the benefit of the developer and writer — as it is *embeddable*, it can be nestled inside other programs for little cost, freeing a developer to design a reading or writing program unrestricted by this framework, or a writer to use existing "enclosing programs" that already understand the framework. As it is a *framework*, strict roles have been delegated to each component that make up a writing or reading framework, making implementation easy for the developer, and configuring and linking easy for the writer.

Yet the most important user is the reader, without whom all of this would be pointless. By placing program design into the hands of a community (or potentially just me) instead of relying on some pre-baked IDE like [Twine](https://twinery.org), you free up configurability, while the framework keeps the books tidy. The dream is that there be an internet library of component implementations of varying mutual compatibilities that writers can grab to make their own custom story program, as if with Legos. Then, if a writer feels like the current options are insufficient, they become a developer, or perhaps put a request up on a forum!

So, in order to realize my dream, I need three things: a framework that's as general as possible, a framework that's as specific as possible, and a community of people willing to spend lots of their time working with something I came up with. In other words, I have already resigned myself to failure, but this is something I care about enough to give a shot anyway.

---

### Data Definition: Embeddable Framework

An *embeddable framework* is a set of definite, implementable (as per Java interfaces) *components* whose *implementations* can be instantiated, linked, and run to create a *session*, which continuously waits for input from one or more sources and sends output to one or more destinations.

* **“Definite”**: This is a key word. When working with an embeddable framework, what the components are is not up in the air — only how those components will be implemented.
* **Implementation compatibility**: A given implementation of some component need not be compatible with all implementations of other components.
  * While implementations of course have the same methods as their respective components, those methods may expect input or produce output that implementations of other components aren’t set up to handle.
  * There is no framework-based, catch-all way of checking implementation compatibility; that is done as needed by implementations or external process. If incompatible frameworks are put together, any consequent exceptions will be thrown mid-session. (Or, even scarier, maybe no exceptions will be thrown at all.)
* **Execution**: An embeddable framework is called such because a set of pre-linked implementations (called a dormant session) on their own cannot run — a session is only begun when an external process runs it.
  * **Linker**: Imps cannot link themselves on their own and require an external process to put them together. This is called a *linker*.
  * **Entry point**: Each embeddable framework must have reserved method in one of its components that functions as an entry point to run a session.
  * **Complete set**: Linking and running a framework does not necessarily require every component to be implemented and linked. Depending on the framework, perhaps only a subset of the components need to be implemented and linked, and other implementations are added dynamically, according to the needs of the session.
* **I/O**: Each session can accept input at any time from one or more sources and send output to one or more destinations.
  * A session never does anything without receiving input, and always produces output as quickly as possible — if some presentational delay is necessary, it is the recipient’s responsibility to manage that.

Queasy Points:
- “Framework daemon” is a potentially more apt (and certainly much cooler) name, but I don’t know if what I’m making is actually a daemon because I don’t know very much about computing.
- I’ve left out the “interpretation” section of the data design recipe, but I don’t feel like this needs one, as it isn’t domain-specific data representing some definite information. It really is just data.

---

And now for the main event. I decided to split this into two separate sections: one where I go over the framework without looking at the individual components, and another when I focus on them, as starting with the components is just a bit much, particularly with the examples section.

Sorry for butchering the design recipie, by the way.

## Design Recipe: Solaria Framework (Component-Agnostic Overview)

### Data Definition

*The Solaria Framework* (or just “*the framework*”) is a “chain” of two disparate embeddable frameworks called `write` and `read`. A *write session* can acquire, configure (if necessary), and link `read` component implementations to create a *dormant read session*.

* **End Users**: If a read session or write session has an end user, they are called a *reader* or *writer* respectively.

Queasy Points:
- Should the “end users” bit go in the purpose statement? Does it matter?
- I want to implement the framework in Python. Would it be a good idea to go for something language-agnostic, though?
  - If we do have to be language-gnostic, would something other than Python be better than this? I chose Python because it’s widely known and it lets people make packages easily, which is my goal, but I’m inexperienced with programming languages.
- Should I add an additional embeddable framework called develop whose function is to configure and link a dormant write session? That would be very much in the spirit of Solaria. But I'm tabling this ’til implementation, as

### Purpose Statement(s)

The framework is an interactive storytelling pipeline from a writer to a reader. A writer can use the `write` framework to write a (typically) non-linear story encoded in a dormant read session, and a reader can run the read session (perhaps as a part of some other storytelling program, like a video game) to experience the writer's story.

* **`read`**: a read session manages how a reader’s interactions with a story world affect the path of a narrative.
  * **I/O**: The inputs to a read session should represent a reader’s choice or action, and its outputs should represent the future path of the narrative, be that some representation of the changes an interaction caused or simply the next paragraph.
  * **Enclosing program, or lack thereof**: A read session could tell a story pretty much on its own, or it can be a small module managing a reader’s path through a narrative told by a much larger program. If the second case is true, then `read` components should be implemented to fit the needs of the enclosing program, not the other way around.
* **`write`**: A write session allows a writer to access `read` component implementations, configure them, and link them together into a dormant read session.
  * **I/O**: The inputs to a write session should reflect a writer’s desired actions, be they selecting implementations, writing the manuscript, or creating a dormant read session. The outputs should represent the curent state of a write session after these alterations.
  * **Enclosing program, or lack thereof**: Hmm can't talk about a draft.

Queasy Points:
- I don't like the amount of choice that a developer has in deciding what goes in the read session and what goes in an enclosing program. Should I place additional restrictions on the form and content of read session output? This feels squishy.

### Examples

#### `read`

For ease of reference, most of these examples show pre-existing games reimplemented in terms of the framework.

**_Zork_**: The classic text adventure game [*Zork*](https://en.wikipedia.org/wiki/Zork), an inspiration for this framework, could be implemented in terms of a read session.
* **I/O**: The input source would be the keyboard, from which text would be read into the read session. The output would be the program's response text, which would be somehow written to the screen.
* **Enclosing program, or lack thereof**: As this implementation of *Zork* returns text directly, there wouldn't need to be an enclosing program - the read session could simply output text to a command line. However, for extra bells and whistles, all input and output could be routed through an enclosing program to accomplish non-narrative functionality like saving the game or adjusting display preferences like text size.

**_Skyrim_**: Or insert-your-favorite-open-world-adventure-game-here. This is a more complicated example than the basic *Zork*, as this shows how a read session can be embedded into a larger storytelling program.
* **I/O**: The inputs to the read session would be some representation of any action that the reader (player) performs in the game world that could influence the course of a narrative. Say that the reader picked up a golden carrot that can grant sight to the blind, I don't know. The read session might receive that inventory update, check with its internal model of the story, and then output something to the larger Skyrim program telling it to make some quest available somewhere. I don't know; I'm tired.
  * You could also decide to implement a read session that stores player inventory. Then, the input would be some representation of the player picking up an object, causing some change in the internal state of the read session. This wouldn't cause immediate output — that would happen later, when the read session is loading conversational trees and deciding that one dialogue path can only be traversed if the user has the golden carrot.
* **Enclosing program**: The enclosing program would be Skyrim, although it would gain and lose functionality as less or more is delegated to the read session.

#### `write`

**_SCALE: The Solaria CommAnd Line Environment_**: A simple example of write sessions controllable from the command line.
* **I/O**: The input source are commands from the command line performing the actions associated with a write session: accessing, configuring, and linking read components.

**_Bonsai: The Solaria GUI Environment_**: More complex example, with more complex enclosing program, but sits on top of SCALE.

**_Skyrim_**: What; again?

## Design Recipie: The Solaria Framework (Component-Gnostic Overview)

### Data Definition

Let's get into those components now.
* **`read`**: 
  * `Manuscript`:
* **`write`**:
  * `Draft`:

### Purpose Statement(s)

* **`read`**: 
  * `Manuscript`: The `read` framework has one particular component from whose implementations information about a narrative is accessible, called `Manuscript`. An instance of a `Manuscript` implementation is simply called a *manuscript*. Other components’ implementations, such as ones for display or reader response processing, should carry as little information about a narrative as possible — ideally none.
* **`write`**: A write session allows a writer to access `read` component implementations, produce a manuscript, configure implementations of the other `read` components, and link them all together into a dormant read session.
  * **Draft component**: The `write` framework has one particular component to whose implementations information about a narrative is imparted, called the *draft component*. An instance of a draft component implementation is called a *draft*. A draft can produce a manuscript. A manuscript might simply be a read-only version of a draft, or it might be something more sophisticated.

### Examples

---

## Conclusion

### For Blerner in particular

* I am also looking for critiques on the quality of my technical writing. This is intended to be a technical document, and if you have any advice on how to improve that, it would be welcome.
  * In writing this, I followed the [Google Dev Docs Style Guide](https://developers.google.com/style/text-formatting), but I don't feel like proper text formatting is sufficient.
* Yes, I intend to figure out what the frameworks are at some point, but I think that more important is building these requirements around them.
  * Nah, fuck that. This weekend I'm diving into the components.
