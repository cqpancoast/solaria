# The Solaria Framework

### Points of Confusion
- The way that *read session*s are saved should be configurable; I wouldn't want to lock anyone into anything
- Does an `Environment` even need to exist? The data definitions for **write** seem arbitrary; make them smarter
- Are we actually sticking with the very slick and symmetrical *write session* data def, or does that not work in practice?
- Is a `Response` actually a thing?
- Are `Reading`s and `Writing`s classes? We've been using the fancy monospaced text for them, but I think they're just executable programs. After all, they're self-contained, so it's not like they talk with anything else in a class-y way
- Does it all have to be Python?
- Is an `Interpreter` literally just a function or are there actual honest-to-god restrictions on it?
- How does the `Draft` represent itself? Are there any restrictions on this? A `Draft` explicitly has to be editable, so it seems reasonable to hard-code that functionality in a method, but I can't think how to do it.

**The Solaria framework** *(sol-ARR-ree-uh)* is a component-based Python object framework for the creation and execution of software-based [interactive fiction](https://en.wikipedia.org/wiki/Interactive_fiction). This framework is not limited to interactive fiction (particularly the provided definition of "text-based"), and a further discussion of its capabilities can be found elsewhere (or here, but later).

The framework is separated into two halves: **write** and **read**.
Together, these form a complete creative pipeline from a *writer* of interactive fiction to a *reader*.

In a sentence (just add semicolons):
- A *writer* runs a `Writing`, a concatenation of a complete set of compatible implementations of **write** framework components, to begin a *write session*.
- The goal of the *write session* is then to create and configure a `Reading`, a concatenation of a complete set of compatible implementations of **read** framework components, which can be executed by the *reader* to begin a *read session*.
- A `Reading` and `Writing` are self-contained, executable programs with no dependency on one another.

Here's a (non-technical, non-specific) visual:

//[The Solaria Framework](/resources/framework.svg)

Now for the technical, specific part, which should explain what's in the visual.

### Writers and Readers

First, a point of clarification.

The *writer* and *reader* don't have to be the end-users themselves, but can be backends to other programs, interfacing between a `Writing` or `Reader` and, say, some domain-specific framework.
For example, the *reader* could be a video game that is using a `Reading` to keep track of a player-traversed consequence tree in a playthrough, running a new *read session* every time the game boots (as the vocab goes).

## Write

Implementations of **write** framework components 

The **write** section of the framework allows a *writer* to design a `Reading`, which is an executable implementation of the **read** package that can be used by a *reader*.

It uses an `Environment` to organize one or more `Editor`s, each of which is a different way of displaying and(/or?) editing the contents of one or more `Draft`s. The `Environment` also has access to implementations of elements of the **read** package, which it can put together (along with a `Story`, a finalized `Draft`) to produce a `Reading`.

### Environment

I dislike that this breaks that wonderful story-based naming scheme. Also, I was thinking that this could be outside of a "write session". What the fuck is a "write session", anyway?

### Publisher

Not sure yet. I was thinking that this could be the thing that has access to the software collections library. This could be "the concatenator".

### Editor

An `Editor` can edit a `Draft`, whatever that means. We'll start with the `Draft` first, and then have the `Editor` work from there.

#### Methods
- `edit(Draft)`???

### Draft

A `Draft` is an editable precursor to a `Story`. It can faithfully represent itself... somehow.

#### Methods
- `finalize() -> Story`: finalize this `Draft` to produce a `Story`.

## Read

Compatible implementations of **read** framework components can be put together by the `Publisher` to produce an executable, *reader*-usable `Reading`.

When a *read session* is begun, the `Reading` uses data stored in its `Story` to generate `Interaction`s consisting of `Displayable`s and `Prompt`s for its `View` to present. The `Interaction` constructs `Interprete(r)`-d responses to `Prompt`s into a `Response` for the `Storyteller` to pass along to the `Story`, which closes the cycle by generating another `Interaction`.

### Storyteller

The entry point into a *read session*.

#### Methods
- `read()`: begin a *read session*. Depending on parameters, query the `Story` for an `Interaction` or load stored data or... or something.

### Story

The `Story` turns a *reader*'s `Response` into another `Interaction`, driving forward the *read session*. If the *read session* stores any static or dynamic data, the `Story` is the only object that has access to it. It's the [Dungeon Master's screen](https://nerdarchy.com/dm-screen/), as it were. 

#### Methods
- `turn_page(Response) -> Interaction`: takes in a *reader*'s `Response` to an `Interaction`, uses whatever static or dynamic data is necessary to create the next `Interaction` for the `Storyteller` to send to the `View`.

### Interaction

An `Interaction` is a set of `Displayables` and `Prompts`, a logic to decide their order of presentation, and a method for taking output from whichever `Prompt`s are presented by the `View` and turning those into a `Response`.

#### Methods
- `interact(View) -> [anything]`: sends its components to be presented by a `View` and then collects the output into a `Response`.

### Displayable

Something to be displayed by the `View`. There are pretty much no restrictions on what this is; it could be something as simple as an integer. It's up to the `View` to interpret and display. Should be considered more as a collection of useful objects in a subpackage than an actual class with strict methods and stuff. These are just... data.

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
