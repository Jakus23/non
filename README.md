# Non Object Notation (NON) Programming Language

> A programming language that imitates the way we think using _frames_ to represent knowledge

The initial aim of the language is to reduce the overhead of using a mind-map. The tokens that should map naturally to your brain are:
* frames,
* slots,
* defaults,
* aliases, and
* terminals.

> **The ‘Hello World!’ example**: Save `Hello World` in a file with a `.non` extension.

You can make business motivation digital and consistent fast with _non_, and discuss implementation details with dev later.

More about each token...

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
    Person
````
Capitalise the first letter of each word in a “Frames”

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
A colon separates the slot from it's default. The default is the most likely value a slot can take. Each slot may also act as a selector between frames.
> Order the slots from most to least essential to help readers understand the frame

Terminal
--------

You sometimes have records that you want to present as examples.

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
 The terminal name becomes a “reserved word” and can be used as reference.
> You can do your task list as terminals

 Alias
 -----
 It doesn't have to be all the slots of a frame to be useful. You can also repeat slots if required. For example...
 ```
 Person
     - John Doe
        home language (language): Afrikaans
        business language (language): English
```
Now you have two slots of the same kind, but with two different defaults.

A slot can map to a frame and a default can map to a terminal.

```
Language
    - English
        first spoken: 1100 AD
    - Afrikaans
        first spoken: 1900 AD
Person
    language: English
    - John Doe
        home language (language): Afrikaans
        business language (language): English
```
> You can do graphs

[Here is the full Stakeholder file as an example](https://github.com/Jakus23/non/blob/main/Stakeholder.non)

Okay, enjoy. Other features not in the readme:

* how to setup a text editor to make writing and reading more enjoyable,
* _non_ idioms,
* the simple language engine (non.py) to lex and parse the language: you can provide a datastore to dev to use when implementing.

> An interesting use of *non* is to translate to and from Excel for version control.

Cheers!
