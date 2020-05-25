# The Solaria Framework

## Preamble, I guess

### For the masses

* Designed for ease of implementation by developers.
  * Only the absolute bare minimum of requirements to run the sessions are hard requirements.
  * The framework structure was designed for developers to design intentional cross-compatibility between implementations.
  * The framework structure was (will be) designed for both generality and ease of use.

### For Blerner in particular

* I am also looking for critiques on the quality of my technical writing. This is intended to be a technical document, and if you have any advice on how to improve that, it would be welcome.
  * In writing this, I followed the [Google Dev Docs Style Guide](https://developers.google.com/style/text-formatting), but I don't feel like proper text formatting is sufficient.
* Yes, I intend to figure out what the frameworks are at some point, but I think that more important is building these requirements around them.

---

For what follows, it will be useful to define what I have chosen to call an embeddable framework.

### Data Definition: Embeddable Framework

An *embeddable framework* is a set of definite, implementable (as per Java interfaces) *components* whose *implementations* can be instantiated, linked, and run to create a *session*, which continuously waits for input from one or more sources and sends output to one or more destinations.

* **“Definite”**: This is a key word. When working with an embeddable framework, what the components are is not up in the air — only how those components will be implemented.
* **Implementation compatibility**: A given implementation of some component need not be compatible with all implementations of other components.
  * While implementations of course have the same methods as their respective components, those methods may expect input or produce output that implementations of other components aren’t set up to handle.
  * There is no framework-based, catch-all way of checking implementation compatibility; that is done as needed by implementations. If incompatible frameworks are put together, any consequent exceptions will be thrown mid-session. (Or, even scarier, maybe no exceptions will be thrown at all.)
* **Execution**: An embeddable framework is called such because a set of pre-linked implementations (called a dormant session) on their own cannot run — a session is only begun when an external process runs them.
  * Linker: Imps cannot link themselves on their own and require an external process to put them together.
  * Entry point: Each embeddable framework must have reserved method in one of its components that functions as an entry point to run a session.
* **I/O**: Each session can accept input at any time from one or more sources and send output to one or more destinations.
  * A session never does anything without receiving input, and always produces output as quickly as possible — if some presentational delay is necessary, it is the recipient’s responsibility to manage that.

Queasy Points:
- “Framework daemon” is a much cooler (and potentially more apt) name, but I don’t know if what I’m making is actually a daemon because I don’t know very much about computing.
  - If I do end up calling this a framework daemon, I could refer to the implementations as imps and get all hell-themed with my terminology. But as fun as that would be, I do want people to read this, so I don’t want to sacrifice an intuitive naming scheme at the expense of fun.
  - …But come on:
    - Session —> daemon
    - Components —> still components, but ritual components. Hmm…
    - Implementations —> imps
    - Calling process —> summoner
    - Dormant session —> unsummoned daemon
- I’ve left out the “interpretation” section of the data design recipe, but I don’t feel like this needs one, as it isn’t domain-specific data representing some definite information. It really is just data.

And now for the main event. Sorry for butchering the design recipe.

## Design Recipe: Solaria Framework (Component-Agnostic Overview)

### Data Definition

*The Solaria Framework* (or just “*the framework*”) is a “chain” of two disparate embeddable frameworks called `write` and `read`. A *write session* can acquire, configure (if necessary), and link `read` component implementations to create a *dormant read session*.

  * **End Users**: If a read session or write session has an end user, they are called a *reader* or *writer* respectively.

Queasy Points:
- Should the “end users” bit go in the purpose statement? Does it matter?
- I want to implement the framework in Python. Would it be a good idea to go for something language-agnostic, though?
  - Also, if we do have to be language gnostic, would something other than Python be better than this? I chose Python because it’s widely known and it lets people make packages easily, which is my goal, but I’m inexperienced with programming languages.
- Should I add an additional embeddable framework called develop whose function is to configure and link a dormant write session? That would be very much in the spirit of Solaria. Tabling this ’til implementation.
  - Yes, I should do something like this, but I’m not sure what form it will take. Barebones program? Another embeddable framework? Will there be a “develop develop” package? How deep does the rabbit hole go?

### Purpose Statement(s)

The Solaria Framework is an interactive storytelling pipeline from a writer to a reader. From the [wikipedia page](https://en.wikipedia.org/wiki/Interactive_storytelling):

> Interactive storytelling […] is a form of digital entertainment in which the storyline is not predetermined. The author creates the setting, characters, and situation which the narrative must address, but the user (also reader or player) experiences a unique story based on their interactions with the story world.

After that, their definition gets way too specific, neglecting to separate function from implementation. (Even this part of the definition is a little implementation-specific for me (who says there’s characters?), but it will serve.)

* **`read`**: a read session manages how a reader’s interactions with a story world affect the path of a narrative.
  * **I/O**: The inputs to a read session should represent a reader’s choice or action, and its outputs should represent the future path of the narrative, be that the changes an interaction caused or simply the next paragraph.
    * The inputs and outputs of a read session can take what ever form they need to to fit the needs of the enclosing program, if there is one.
  * **Enclosing program, or lack thereof**: A read session could tell a story pretty much on its own, or it can be a small module managing a reader’s path through a narrative told by a much larger program. If the second case is true, then `read` components should be implemented to fit the needs of the enclosing program, not the other way around.
  * **Story Component**: The `read` framework has one particular component from whose implementations information about a narrative is accessible, called the *story component*. ~~An implementation of a story component is called a story.~~ Other components’ implementations, such as ones for display or reader response processing, should carry as little information about a narrative as possible. This will clarify the structure of a write session, which is given below.
* **`write`**: A write session allows a writer to access `read` component implementations, write a non-bold story encoded in a bold story, configure implementations of other `read` components, and link them all together.
  * **I/O**: The inputs to a write session should reflect a writer’s desired actions, be they selecting implementations, writing the story, or creating a dormant read session. The outputs should represent the curent state of a write session after these alterations.
  * **Enclosing program, or lack thereof**: A single write session can perform its function if using appropriate implementations (by definition), but just by the nature of a write session vs. a read session, a writer may want to “dynamically link” write sessions and run them simultaneously, perhaps to get different looks at the story. 

Queasy Points:
- Should the “story component” bit go in the data definition? I put it here because I’m singling out a component based off of its purpose statement, not on anything definite about its inputs and outputs.
  - Let's define a story implementation as something, but let's not use the word *story*.
- I don't like the amount of choice that a developer has in deciding what goes in the read session and what goes in an enclosing program. Should I place additional restrictions on the form and content of read session output? This distinction feels squishy.

### Examples

#### `read`

For ease of reference, most of these examples show pre-existing games reimplemented in terms of the framework.

**_Zork_**: The classic text adventure game [*Zork*](https://en.wikipedia.org/wiki/Zork) (an inspiration for this framework) could be implemented in terms of a read session.
* **I/O**: The input source would be the keyboard, from which text would be read into the read session. The output would be the program's response text.
* **Enclosing program, or lack thereof**: As this implementation of *Zork* returns text directly, there wouldn't need to be an enclosing program - the read session could simply output text to a command line. However, for extra bells and whistles, all input and output could be routed through an enclosing program to accomplish non-narrative functionality as saving the game or adjusting display preferences like text size.

**_Skyrim_**: Or insert-your-favorite-open-world-adventure-game-here. This is a more complicated example than the basic *Zork*, as this shows how a read session can be embedded into a larger storytelling program.
* **I/O**: The inputs to the read session would be some representation of any action that the reader (player) performs in the game world that could influence the course of a narrative. Say that the reader picked up a golden carrot that can grant sight to the blind, I don't know. The read session might receive that inventory update, check with its internal model of the story, and then output something to the larger Skyrim program telling it to make some quest available somewhere. I don't know; I'm tired.
  * You could also decide to implement a read session that stores player inventory. Then, the input would be some representation of the player picking up an object, causing some change in the internal state of the read session. This wouldn't cause immediate output — that would happen later, when the read session is loading conversational trees and deciding that one dialogue path can only be traversed if the user has the golden carrot.

**_Irritatium: Your Personal Narrative Hell_**: A continuously written story that uses neural networks to irritate you in real time!
* **I/O**: The input to the read session is video of your face. A neural network uses this to figure out how irritated you are at a particular moment, and then outputs text onto the screen that is more like the text that makes you irritated. Has some internal restrictions that force it to tell a coherent story.

#### `write`

**_SCALE: The Solaria CommAnd Line Environment_**: Simple example.

**_Bonsai: The Solaria GUI Environment_**: More complex example, with more complex enclosing program, but sits on top of SCALE.

**_Skyrim_**: What; again?

### Tests

As much as I would like to write tests for this stuff, I am still at too high a level to do so.

## Design Recipe: Solaria Framework Components

