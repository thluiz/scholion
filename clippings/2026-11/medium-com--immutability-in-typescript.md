---
url: "https://medium.com/@ezequiel/immutability-and-builders-with-typescript-b69a51c94e8c"
captured_at: "2026-11-16T05:50:14+00:00"
title: "Immutability in TypeScript. Since I learnt Scala, immutability has… | by Ezequiel Foncubierta | Medium"
domain: "medium-com"
---

Typescript
Programming
Serverless
Development
JavaScript
Immutability in TypeScript
Ezequiel Foncubierta
4 min read
·
Nov 18, 2017

Since I learnt Scala, immutability has been top priority in my code. Immutability leads to much simpler and less error prone code. No matter whether it is with Java at work or with TypeScript at Hyperdoc, I always encourage developers to use immutable objects and data structures.

Photo by Kelly Sikkema on Unsplash

Javascript is a highly dynamic and flexible language. You can set attributes to any object, even if they haven’t been declared.

class Person {
constructor (name, surname) {
this.name = name
this.surname = surname
}
}
var person = new Person('Ezequiel', 'Foncubierta')
person.country = 'Spain'

Implementing immutable code in Javascript is really difficult. But in TypeScript, there are workarounds for it. We can enforce immutable code in compile time.

Let’s start defining our immutable Person object in TypeScript:

export default class Person {
readonly name: string
readonly surname: string
readonly city: string

constructor (name: string, surname: string, city: string) {
this.name = name
this.surname = surname
this.city = city
}
}

Our Person class has three attributes: name, surname and city. These attributes have been declared as readonly, so they can only be assigned once, when the object is constructed.

We can now work with an immutable Person object in TypeScript as following:

const me = new Person('Ezequiel', 'Foncubierta', 'Cádiz')
// ERROR: Property 'country' does not exist on type 'Person'
me.country = 'Spain'
// ERROR: Cannot assign to 'city' because it is a constant or a
// read-only property.
me.city = 'London'

So far, so good. We’ve got an immutable object. If you want to set an attribute in an immutable object, you will have copy it.

const britishMe = new Person(me.name, me.surname, 'London')

Done! However, if we had an object with lots of properties, this will be painful. Also, adding a new attribute to Person will break this code. That’s not good. How can we set attributes in immutable objects like a boss? Object builders to the rescue.

Photo by David Noe on Unsplash
Object builders

An object builder is used to build objects… really. So rather than instantiating a Person object through Person.constructor(), we will use a PersonBuilder.

export type PersonJson = {
name: string
surname: string
city: string
}
export class PersonBuilder {
private json: PersonJson
constructor(person?: Person) {
this.json = person ? person.toJSON() : <PersonJson>{}
}
name(name: string): PersonBuilder {
this.json.name = name
return this
}
surname(surname: string): PersonBuilder {
this.json.surname = surname
return this
}
city(city: string): PersonBuilder {
this.json.city = city
return this
}
build(): Person {
return Person.fromJSON(this.json)
}
}

export default class Person {
readonly name: string
readonly surname: string
readonly city: string

private constructor (name: string, surname: string, city: string)
{
this.name = name
this.surname = surname
this.city = city
}
toJSON(): PersonJson {
return {
name: this.name,
surname: this.surname,
city: this.city
}
}

static fromJSON(json: PersonJson): Person {
return new Person(json.name, json.surname, json.city)
}
static builder(person?: Person): PersonBuilder {
return new PersonBuilder(person)
}
}

First thing to notice, is that Person cannot be instantiated. Its constructor is private. We don’t want other ways to construct a Person than using its builder. Also, we have created a PersonBuilder class that is used to construct a Person object based on another Person. Let’s see how this works.

// ERROR: Constructor of class 'Person' is private and only
// accessible within the class declaration.
const me = new Person('Ezequiel', 'Foncubierta', 'Cádiz')
// OK
const me = Person.builder()
.name('Ezequiel')
.surname('Foncubierta')
.city('Cádiz')
.build()
// OK
const britishMe = Person.builder(me)
.city('London')
.build()

Awesome! Mission accomplished. We’ve got a Person class, which produces immutable Person objects, and a PersonBuilder to build and copy Person objects. But, what if Person had a mutable attribute like an array?

export default class Person {
readonly name: string
readonly surname: string
readonly cities: string[]

// ...
// constructor, fromJSON, toJSON and builder
// ...
}

The cities attribute is readonly, but not immutable. We can push, and pop, values to it.

// OK
const me = Person.builder()
.name('Ezequiel')
.surname('Foncubierta')
.cities(['Cádiz'])
.build()
// :-(
me.cities.push('London')

That’s not good! Don’t worry. There is a solution for this problem too… Immutable data structures.

Photo by William Bout on Unsplash
Immutable data structures

We are not going to implement an immutable data structure, but use an existing library open sourced by Facebook: Immutable.js. This library provides many immutable data structures including: List, Stack, Map, OrderedMap, Set, OrderedSet and Record.

import { Set } from 'immutable'
// ...
// PersonJson and PersonBuilder
// ...
export default class Person {
readonly name: string
readonly surname: string
readonly cities: Set<string>

// ...
// constructor, fromJSON, toJSON and builder methods
// ...
}

Our Person.cities attributes is now an immutable set of strings. Let’s see how it works.

// OK
const cities = Set(['Cádiz'])
const me = Person.builder()
.name('Ezequiel')
.surname('Foncubierta')
.cities(cities)
.build()
// this has no effect.
// me.cities.size == 1
me.cities.add('London')
// OK
const cities2 = me.cities.add('London')
const britishMe = Person.builder(me)
.cities(cities2)
.build()

I know, right? It is awesome.

Do you use immutable objects/data structures?

What’s your approach in TypeScript?

What’s next?

I am using this approach in Hyperdoc to build immutable objects. So next week I am going to define more types (i.e. User, Account, Group, Schema, SchemaProperty and so on) in the data model.

What can you do to help me right now?

Follow me on Medium: ezequiel
Follow me on Twitter: efoncubierta
Email me your thoughts to ezequiel.foncubierta@gmail.com
Clap this story.
Comment on this story.
Share this story on your social networks.
