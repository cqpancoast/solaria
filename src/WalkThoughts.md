# Things I Thought Up On My Walk

## Issues
- Are actions and events restricted to discrete packets of information, or can they be continuous streams?
- It seems that output text a la Zork no longer fits in with what an event is — "something that could have happened some other way".
- An action is "something done by a reader that can have an effect on the narrative path". Does this support on-the-fly alterations being made by what I'm termind writer-readers? There should absolutely be support for this. What is an action? Does it have to occur in the story world?
- Can read sessions have listeners injected into an enclosing program? This would be a nice way of having read sessions choose what data they're looking for dynamically, but on the other hand, this breaks the separation between an enclosing program and a read session.

## Actions and Events

Solaria should be expanded to support the most general kind of game: multi-agent, real-time, multi-user-type.
It should be able to create the example of "the interrupted conversation", where the reader is having a conversation with an NPC at the moment that another reader causes a volcano to erupt in the distance.
If coded correctly, the NPC should be able to remember the point in the conversation that they left off, remember that the volcano interruped them, and respond accordingly.

An I/O scheme that I came up with for a read session solves a few of these problems, but leaves some others unclear.
`Action`s go in, `Event`s come out.

An action (doing away with the fancy monospaced text) is anything done by a reader that could have an effect on the narrative path.

Examples of actions:
- having a conversation with an NPC
- adding an item to their inventory
- a "writer-reader" making on the fly edits to the read session, such as directly triggering an event or decreasing enemy spawn rate
  - Note that different types of actions would be submitted to the read session by different types of users. This is how "permissions" are dealt with: your permissions are percisely the kinds of actions you are capable of submitting to the read sessiion
- entering an area/crossing a boundary

Examples of *not* actions: (or perhaps examples of *bad* actions?)
- A reader pressing (a)
  - The read session should only know about occurrences in the story world
- 

An enclosing program is logging actions like these (specifically which depends on the program) and sending them along to its read session.

Something that makes me feel really queasy about the action-event model is that it's general as shit.
As I'm writing this, I am (or should be) searching for ways to say anything definite about them.

An event is some occurence in the story world that manifests itself in a potentially observable way to a reader.
Loosely, an event is something that could have happened some other way.

Examples of events:
- A volcano exploding at a particular time
- A trapdoor opening for a character as opposed to not opening depending on narrative beats
- An NPC appearing sad as opposed to cheerful
- The next paragraph in an interactive fiction session

Examples of *bad* events:
- Gravity, in a world where gravity is deterministic
  - Gravity is something that always happens, so it is a waste of time for a read session to produce an event causing a character to fall. (It is generally inadvisable to base physics systems off of actions and events; they are more designed for narrative structure and story beats.)
- A volcano exploding at a particular time when there was no way it was going to explode at any other time

Here's something that came up below, in the "art for art's sake" example: are actions and events discrete? Can they be streams?

## Scalability of Solaria

It is very appealing to me to be able to nestle smaller sessions inside of larger ones in a delegatory pattern.
I want the framework to be scalable between small projects like *Zork* and huge projects like *OASIS* from *Ready Player One*, and scalability can be created by having larger versions of the project contain smaller versions.

Maybe it would go like this: the top-level read session receives input either directly from the reader or through an enclosing program.
Then, the read session can create other read sessions on the fly that can handle a particular type of input.

Here's an example: a reader is walking around in an RPG, and then enters a cavern.
The top-level read session dynamically runs a cavern-specific read session that takes input from the top level one.
Maybe the top-level input was looking for one type of event, while the cavern-specific one is looking for another type.

Also, how do listeners play into this? That's a form of input, but the agency is taken out of the sender.

## Examples of Read Sessions

These are all read sessions that should be implementable in terms of the read framework, whatever the fuck that even means anymore.
- **Zork**: you should always be able to make Zork, my simple example for a read session. In Zork, actions are everything that the reader types in, and events are text output.
- **MMORPG: The Interrupted Conversation**: a conversation with an NPC is interrupted by a volcano eruption instigated by a PC, and the NPC acts believably following the explosion and can remember when the conversation left off and what information was and wasn't imparted. This example highlights how capital-I Interactions cannot be restricted to having to take time. The framework must be able to support the story turning on a dime, in real time.
- **MMORPG: The Big Bad**: a worldwide event is instigated (perhaps even by the readers!) in which they storm a castle with a bunch of really nasty enemies in it. The actions created by normal readers are things like "enemy X killed", "threshold Y crossed by player Z", etc. However, there is in this example a "reader-writer" who can submit custom actions to the story, such as "enemy group A difficulty increased by B%"...
  - ...hm. Wait, does this fit with how we defined an action?
- **Art for art's sake**: a good example for testing generality. There are no characters or setting in this read session, there's just dreamlike output, and maybe the input is output from a neural net indicating how relaxed the reader is. Are actions and events discrete? Can they be streams?
