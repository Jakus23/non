# non
Non Object Notation (NON) Programming Language
==============================================
> A framing language that imitates the way we think

The initial aim of the laugauge is to reduce the overhead of using a mindmapping tool, especially in quantitative finance. Over time it became more consequential to the point where my business modeling is digital, before the first line of implementation code, or spreadsheet.

This example is valid:

`Hello World`

Save in a file with a `.non` extension and you are done.

It is a langauge for thinking and not for implementing. The tokens you can maps are:
* frames,
* slots,
* defaults,
* aliases, and
* terminals.

More about each...

Frame
-----
A simple mindmap, using just frames:

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
                    Sole Propriator
                    Trading As
                    Partnership
                    Trust
                    Practice
                Closed Corporation
        Non Profit
            Non Government Organisation
                Charity
                Foundation
                Political Party
                Trade Union
            Goverment
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
This mindmap is cool. You should have already learned something about stakeholders (and about the _non laugauge_).

There is no markdown or brackets required. You'll see all “Frames” are capitalised and there is no special characters. It is to keep things uniform for you to focus on the domain only.

Slot and default
----------------
Each of these stakeholders should have “Slots” that can distingish one record from another.
Let's do “Person” as an example:
```
Person
    home lauguage: Engish
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
You'll see that some slots may have defaults to help you understand what data can be slotted in for a record while others do not. A semicolon is used to seperate the slot from the default. Each slot may also act as a selecter for some frames. We also should order the slots from most essential to least descriptive.

Terminal
--------
You sometimes have records of your frames. Maybe for testing, once you have used an implemenation tool like Excel.

Let's also use person for this example
```
Person
   - John Doe
      home language: Afrikaans
      nationality: South Africa
      first name: John
      birthdate: 1986-10-11
      gender: Male
 ```
 Alias
 -----
 You'll see the name of the record is “John Doe”. It doesn't have to be all the slots of a frame to be useful. You can also repeat slots if required. For example
 ```
 Person
     - Jakus van Rooyen
        home language (language): Afrikaans
        business language (language): English
```
Now you have two slots that is of the same kind, but with two different defaults.

Lastly, but very importantly a slot can map to a frame.

```
Laugauge
    - English
        first spoken: 1100 AD
    - Afrikaans
        first spoken: 1900 AD
Person
     - Jakus van Rooyen
        home language (language): Afrikaans
        business language (language): English
```
You'll find this natural to the relational mappings.

Okay, enjoy. If I get motivation; I'll also show you:
*how to setup a text editor to make reading the document a whole lot easier,
*what rules will help your notation map to your brain better,
*you the simple laugauge engine works to lex and parse the lauguage: it is important as an asset to use when you are actually implementing.
*I haven't created any tools to translate code to non (please do, if you are skilled in a specific lauguage)

Cheers!
        
