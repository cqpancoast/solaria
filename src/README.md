# The Solaria Framework

This framework is separated into two components: **write** and **read**.
Together, these form a complete creative pipeline from a *writer* of interactive fiction to a *reader*.

In short, a *writer* runs a `Writing`, a complete set of compatible implementations of **write** package components, to begin a *write session*.
The goal of the *write session* is then to create and configure a `Reading`, a complete set of compatible implementations of **read** package components, which can be executed by the *reader* to begin a *read session*.

Here's a (non-technical, non-specific) visual:

![The Solaria Framework](/resources/framework.svg)

Now for the technical, specific part, which should explain what's in the visual.

### Writers and Readers

First a point of clarification.

The *writer* and *reader* don't have to be end-users, but can be backends to other programs, interfacing between an implementation of the **write** or **read** package and, say, a domain-specific framework.
For example, the *reader* could be a video game that is using a `Reading` to keep track of a player-traversed consequence tree in a playthrough.

## Write

The **write** section of the framework allows a *writer* to design a *reading*, which is an executable implementation of the **read** package that can be used by a *reader*.

It uses an `Environment` to organize one or more `Editor`s, each of which is a different way of displaying and(/or?) editing the contents of a `Draft`. The `Environment` also has access to implementations of elements of the **read** package, which it can put together (along with a `Story`, a finalized `Draft`) to produce a *reading*.

### Environment

### Editor

### Draft

## Read

The **read** section of this framework is everything that is needed for the `Environment` to produce a *reader*-usable *reading*. 

When run, the *read session* uses data stored in its `Story` to generate `Interaction`s consisting of `Displayable`s and `Prompt`s for its `View` to display. The `Interaction` constructs `Interpreted` responses to `Prompt`s into a `Response` for the `Storyteller` to pass along to the `Story`, which completes the cycle by generating another `Interaction`.

### Story

### Storyteller

### Interaction

#### Displayable

#### Prompt

#### Interpreter

### View
