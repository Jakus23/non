# Non Object Notation (NON) Programming Language

> A framing language that imitates the way we think

The initial aim of the language is to reduce the overhead of using a mind-mapping tool. It is aimed for managers in the finance sector. Over time it became more consequential to the point where my business modeling is digitised using _non_ before any real discussions or implementation started. It is a superpower.

This example is valid:

`Hello World`

Save in a file with a `.non` extension. You're done with your first (not useful) program.

It is a language for thinking and not for implementing. The tokens that should map naturally to your brain are:
* frames,
* slots,
* defaults,
* aliases, and
* terminals.

More about each...

Frame
-----
A simple mind-map, using frames:

```
Stakeholder
    Organisation
        Business
            Corporate
                Company
                    Public Company
                    Private Company
                    Section 54B Company
                Professional
                    Sole Proprietor
                    Trading As
                    Partnership
                    Trust
                    Practice
                Closed Corporation
        Nonprofit
            Non Government Organisation
                Charity
                Foundation
                Political Party
                Trade Union
            Government Organisation
               Department
               Ministry
               Commission
               Agency
               Body
               Institution
        Social Group
            Team
            Club
    Person
````
This mind-map is cool. You should have already learned something about stakeholders (and about the _non_ language).

There is no markdown or brackets required.

> Capitalise the “Frames”
> No special characters

Slot and default
----------------
Each of these stakeholders should have “Slots” that can distinguish one record from another.
Let's do “Person” as an example:
```
Person
    home language: English
    nationality: American
    first name: John
    birthdate: 1986-10-11
    gender: Male
        Male
        Female
    surname: Doe
    title: Mnr
        Mnr
        Miss
        Mrs
        Ms
        Dr
        Prof
    social security number
    initials: J
    is living: Yes
    marital status: Married
        Married
        Divorced
        Single
        Widow
        Widower
    occupation status: Employed
      Employed
        Contributor
        Manager
        Executive
        Non Executive
        Independent
      Self Employed
      Unemployed
      Retired
    residential status: Renting
      Renting
      Home Owner
    education standard classification: Masters
      Childhood
      Primary
      Lower Secondary
      Upper Secondary
      Postsecondary Non Tertiary
      Short Cycle Tertiary
      Bachelors
      Masters
      Doctors
    minor child count
```
You'll see that some slots may have defaults to help you keep your slots consistent. A colon separates the slot from the default. Each slot may also act as a selector for some frames.
> Order the slots from most essential to least descriptive

Terminal
--------

You sometimes have records of your frames. It is to group cases to a specific frame.

Let's use person for this example...
```
Person
   - John Doe
      home language: Afrikaans
      nationality: South Africa
      first name: John
      birthdate: 1986-10-11
      gender: Male
 ```
> When you go-pro, you're to-do list will be terminals

 Alias
 -----
 You'll see the name of the record is “John Doe”. It doesn't have to be all the slots of a frame to be useful. You can also repeat slots if required. For example...
 ```
 Person
     - Jakus van Rooyen
        home language (language): Afrikaans
        business language (language): English
```
Now you have two slots of the same kind, but with two different defaults.

Lastly, a slot can map to a frame.

```
Language
    - English
        first spoken: 1100 AD
    - Afrikaans
        first spoken: 1900 AD
Person
    language: English
    - Jakus van Rooyen
        home language (language): Afrikaans
        business language (language): English
```
> It's to do relational mappings

Okay, enjoy. If I'm motivation; I'll also show you:
*how to setup a text editor to make writing reading the document more enjoyable,
*idioms that will help your notation map to your brain better,
*you the simple language engine (non.py) to lex and parse the language: you can provide a datastore for your direct reports to use when implementing.

> Please create tools to translate your code to non object notation

Cheers!
        
