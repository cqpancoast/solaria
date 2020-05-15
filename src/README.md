# The Solaria Framework

### Unresolved Points
- I'm uncomfortable with the "it can be anything" Python typing that I've taken advantage of with responses, `Displayable`s, and `Prompt` data. Or, on the function-al side, `Interpreter`s. If something has no type restrictions, is there any sense in, like, calling these things anything?
- Is Python a good choice for what I'm doing here?
- How does the `Draft` represent itself? Are there any restrictions on this? A `Draft` explicitly has to be editable, so it seems reasonable to hard-code that functionality in a method, but I can't think how to do it in a way that preserves the freedom of `Draft` implementations.
- Should I add a **develop** package? This would assist those disinclined towards coding with putting together custom linkings of **read** and **write** implementations.
- (`Storyteller`, `Environment`) == (`Reading`, `Writing`)? Hm. This would mess with the current definition of a **reading** and **writing**, but would also eliminate two classes that seem like they are fat to be cut out.
- **write** package unfinished. Simple as that.

**The Solaria framework** *(sol-ARR-ree-uh)* is a component-based Python object framework for the creation and execution of software-based [interactive fiction](https://en.wikipedia.org/wiki/Interactive_fiction). This framework is not limited to interactive fiction (particularly given the provided definition of "text-based"), and a further discussion of its capabilities can be found elsewhere (or here, but like, later).

The framework is separated into two halves: **write** and **read**.
Together, these form a complete creative pipeline from a *writer* of interactive fiction to a *reader*.

Terms:
- **write**: the **write** package, a collection of implementations of Solaria framework components focused on writing.
- *writer*: an end user of a **writing**.
- **writing**: an executable program that can run one or more *write session*s.
- *write session*: a linking of a complete set of compatible implementations of **write** framework components.
- **read**: the **read** package, a collection of implementations of Solaria framework components focused on reading.
- *reader*: an end user of a **reading**.
- **reading**: an executable program that can run one or more *read session*s.
- *read session*: a linking of a complete set of compatible implementations of **read** framework components.

Here's a (non-technical, non-specific) visual:

//[The Solaria Framework](/resources/framework.svg)

Now for the technical, specific part, which should explain what's in the visual.

### Writers and Readers

First, a point of clarification.

The *writer* and *reader* don't have to be the end-users themselves, but can be backends to other programs, interfacing between a **writing** or **reading** and, say, some domain-specific framework.
For example, the *reader* could be a video game that is using a **reading** to keep track of a player-traversed consequence tree in a playthrough, running a new *read session* every time the game boots (as the vocab goes).

## Write

The **write** section of the framework allows a *writer* to design a **reading**.

It uses an `Environment` to organize one or more `Editor`s, each of which is a different way of displaying and(/or?) editing the contents of one or more `Draft`s. The `Environment` also has access to implementations of elements of the **read** package, which it can put together (along with a `Story`, a finalized `Draft`) to produce a **reading**.

### Environment

An `Environment` is an entry point to a **writing** capable of linking and running its three suboordinate classes to create a *write session*. I dislike that this is the only class in **write** that breaks the naming scheme.

### Publisher

Not sure yet. I was thinking that this could be the thing that has access to the software collections library. This could be the "linker" in the publishing process.

#### Methods
- `publish(???) -> [reading]`: link together **read** framework components with a finalized `Draft` to produce a **reading**.

### Editor

An `Editor` can edit/revise a `Draft`, whatever that means. We'll start with the `Draft` first, and then have the `Editor` work from there.

#### Methods
- `revise(Draft)`???
- `represent(Draft)`???

### Draft

A `Draft` is an editable precursor to a `Story`. It can faithfully represent itself somehow and has some method for changing its contents, although what a `Draft` is can vary so much that there are no required methods for this component on those fronts. However, there are some soft requirements: a good `Draft` represents itself in such a way that the `Story` it will finalize to is intuitive so as to make the *writer*'s job as easy as possible.

#### Methods
- `isFinalizable() -> bool`: returns whether this `Deaft` is finalizable.
- `finalize() -> Story`: finalize this `Draft` to produce a `Story`.

## Read

The **read** section of the framework provides the *reader* with an interactive experience.

When a *read session* is begun, the **reading** uses data stored in its `Story` to generate `Interaction`s consisting of `Displayable`s and `Prompt`s for its `View` to present. The `Interaction` constructs `Interprete(r)`-d responses to `Prompt`s into a `[response]` for the `Storyteller` to pass along to the `Story`, which closes the cycle by generating another `Interaction`.

### Storyteller

The entry point into a *read session*. Deals with meta-level commands like saving and quitting, if that functionality is provided.

#### Methods
- `read(???)`: begin a *read session*. Depending on parameters, query the `Story` for an `Interaction` or load stored data or... or something.

### Story

The `Story` turns a *reader*'s `Response` into another `Interaction`, driving forward the *read session*. If the *read session* stores any static or dynamic data, the `Story` is the only object that has access to it. It's the [Dungeon Master's screen](https://nerdarchy.com/dm-screen/), as it were. 

#### Methods
- `turn_page([response]) -> Interaction`: takes in a *reader*'s `Response` to an `Interaction`, uses whatever static or dynamic data is necessary to create the next `Interaction` for the `Storyteller` to send to the `View`.

### Interaction

An `Interaction` is a set of `Displayables` and `Prompts`, a logic to decide their order of presentation, and a method for taking output from whichever `Prompt`s are presented by the `View` and formulating those into a `Response`.

#### Methods
- `interact(View) -> [response]`: sends its components to be presented by a `View` and then collects the output into a `Response`.

### Displayable

Something to be displayed by the `View`. There are no restrictions on what this is; it could be something as simple as an integer. It's up to the `View` to interpret and display. Should be considered more as a collection of useful objects in a subpackage than an actual class with strict methods and stuff. These are just... data.

### Prompt

A `Prompt` is responsible for providing data to the `View`, which in turn is responsible for turning that data into a form that a *reader* can interact with. The `Prompt` is then responsible for processing the *reader*'s response (already having been processed into a "`View`-agnostic" form by the `View`) into the form expected (if any) by its calling `Interpreter`.

#### Methods
- `get_prompt_data() -> [anything]`: returns the data associated with this `Prompt`. The `View` is responsible for being able to process and present data of the `Prompt`'s form.
- `process_view_output([anything]) -> [anything]`: accepts a "`View`-agnostic" reader response, processes it into a form expected by this `Prompt`'s calling `Interaction`.

### Interpreter

Literally any function that turns something into something else. So, I guess more of a subpackage of useful things than an actual class with methods. Maybe I should start thinking of some of these things more in terms of subpackages with a collection of things than actual classes.

### Response

Similar to the `Displayable`, there are no restrictions on what this is; it could be something as simple as an integer or string. It's up to the `Story` to interpret this and produce sensible output. (After all, it was what produced the `Interaction` in the first place.)

### View

The `View` displays `Displayables` and prompts the reader with `Prompt`s. As the `Story` is ultimately what produces `Displayable`s and `Prompt`s, *it is the job of the `View`* to present these in a satisfactory manner. It is *not* the job of the `Story` to produce `Displayable`s and `Prompt`s that conform to the `View`'s specifications.

#### Methods
- `display(Displayable)`: display a `Displayable` according to the demands of the `Story`. A `View` has no hard-coded requirements here, as it doesn't return anything, so what constitutes a good `View` is simply that it displays the data in the way that the *writer* intends.
- `prompt(Prompt) -> [view-agnostic response]`: uses data stored in the `Prompt` to prompt the *reader* for input. The `View` has the additional responsibility here of returning a "view-agnostic" response, meaning that the `Prompt` should not have to know anything about the `View` when processing the response.
