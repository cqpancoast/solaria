# Solaria

Solaria is a package and procedure for creating modules that keep track of non-linear narratives.

The modules, called *reading modules* or *readings*, can either sit inside larger storytelling programs, such as an RPG like Skyrim or an MMO like World of Warcraft, or tell a story pretty much on their own, as with a text-based game like [Zork](http://textadventures.co.uk/games/view/5zyoqrsugeopel3ffhz_vq/zork).

While half of the package is for the direct creation of readings, the other half is an object-oriented framework for making modules that create reading modules.
These "creator modules", called *writing modules* or *writings*, abstract the creation of a reading from bare code into a workflow centered around narrative beats.
In much the same way as with a reading, a writing can be interfaced with directly by a writer, or it can be an automated process that builds a reading module for some larger storytelling program.

As there are many different types of each module for a variety of purposes and with a variety of implementations, modules and module components can be put online in a manner similar to how [PyPI](https://pypi.org) works.
Pulling code from this library makes it accessible from the Solaria package.

## Reading

A reading tells a story, or assists in telling a story, by managing a non-linear narrative.
It takes in *actions*, which are representations of reader actions that might affect the path of a narrative, and outputs *events*, representations of events that occur in the story world that might not have happened if not for the "action-history".

### Form of I/O data

While what actions and events mean is (hopefully) clear, the data they are composed of can be anything.
Generally, a reading should fit the needs of an enclosing storytelling program, or the reader, if there is none.

#### Actions

For a complex enclosing program like Skyrim, an action might have some internal grammar (player X killed spider Y) parsable by the reading.
An action in Zork could be player input text.

#### Events

Again for Skyrim, an event might be some update to the world (perhaps spider queen Z is enraged, as spider Y was her fiancé).
An event in Zork might be prompt text.

### I/O scheme

While readings can act simply as functions, in the case of a single-user, non-real-time game like Zork, the most general reading follows an input/output scheme whereby any number of actions can be accepted at any time and events must return as soon as they are certain.

To see why this scheme is useful, let's say there is volcano in some [MMORPG](https://en.wikipedia.org/wiki/Massively_multiplayer_online_role-playing_game) that is on the brink of eruption.
Some players fight to prevent the eruption, while others fight to ensure it.

The reading takes in player actions that influence the status of the volcano, perhaps the press of a button or capturing a flag, but once it returns the volcano event, the fate of the volcano is certain.
This event would then update the story-world state (volcano is erupted), and the altered world state would cause different actions to come from players (gathering precious metals that came from the eruption), which would cause different events to come from the reading (subterranean fire giants dislike such flagrant theft of their property).

By using this timing scheme for events, a reading can handle non-linear narratives with real-time, multi-user stories.

#### Multi-user-type

The action-event scheme also supports multiple types of readers/players.
These types and their permissions are defined by the types of actions they can submit.
For example, maybe a standard player in the MMORPG example above can only submit (usually without knowing) actions like "crossed over threshold" or "killed monster X".

However, say there was a world event where the players were to attack a castle filled with baddies.
A different type of player, acting as a dungeon master rather than as a character, could submit custom actions to alter the strengths and attack/response patterns of monsters to create a more immersive experience.

### Nesting

Creating reading modules is cheap, and nesting them is encouraged.
Below are some common ways one might go about doing this.
These are certainly not the only ways.

#### Delegation Tree

In a "delegation tree", each module in the tree is responsible for its own section of a story.

Let's say a player accepts a quest that requires them to enter a cave.
Some of their actions might go towards a reading module nested within the "main" reading that controls the narrative of the quest taking place in the cave.
Other actions, such as the umbrella they collect off of a mysterious red-robed skeleton, might have consequences extending beyond the cave, and so would be delegated to the "main" reading, potentially for transport to some other appropriate reading, or as a parameter in the creation of that reading when its scene comes up.

This brings up another important point: use of a delegation tree allows readings to be created and destroyed *dynamically*. [That sounds like a job for a writing, doesn't it?](#writings-within-readings)

#### Processing Stack

In a "processing stack", each module in the stack is responsible for a particular kind of processing.

Perhaps Zork could be created by two modules:
- One on top may accept and return text, with the purpose of turning that text into concrete actions and doing the reverse for events, all depending on story context. It might have the I/O scheme of a function: return ASAP after accepting arguments.
- The one on bottom may accept these more concrete actions, update its model of the store, and then produce an event. It… hm. Don't know.

## Writing

A writing writes a story, or assists in writing a story, by abstracting the creation of a reading module into information about the story the reading will tell.
It accepts commands to create or configure a reading and either returns the result of some configuration or produces a valid reading.

### Components

### Writings within readings
