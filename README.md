## Introduction to Python

Github Classroom Assignment Link : https://classroom.github.com/a/oUE_Og9m

Tasks Definition : https://docs.google.com/document/d/1V1gYEKLtOPYzZL7F9koaDVdgIlOXl_ALspjyzOZJN7Q/edit?usp=sharing

## Understanding solid principles
Solid Principles are the structures meant for Object Oriented Design, these principles were designed to make programmers
design write classes that are flexible,robust,maintainable and resueable software.
SOLID is an acronmy for 
S: SRP-Single Responsibility Principle
O: OCP-Open-Closed Principle
L: LSP-Liskov Substitution Principle
I: ISP-Interface Segrgation Principle
D: DIP-Dependency Inverted Principle

Single Responsibility Principle States that a class must perform only one reponsibility the reason it because 
1.it makes testing easier to perform and will require only few tests
2.it requires very few functions and lower dependencies
3.it makes organization of smaller classes easy to search
Example 
A. A class of a list of book should not implement print method
B. A class of vehicle should not implement flying method

Open-Closed Principle States that a class is open for extention and closed for modification this is so that an already functioning class will be affected and this can be done by simpily extending the class. AN exception to this rule is if there is a bug in the 
existing class
Example 
A. class of Users with a method of add user if there is an additional information to keep login and logout the class can be extended and
the new method added to it 
B. class of guitar with a knob if there is a new design parttern to be added then we can just expend the class

LSP-Liskov Substitution Principle is the ability to replace any instance of a parent with an instance of one of its child without breaking the system
Example:
A. If the son of a farmer inherits the skills of farming from his father then in the absence of this father he should be able to have the same artributes as his father and deliver the same functions as his father
B. A rectangle has a height and a width which can be any positive integer if a square class inherits from rectangle because it has  height and width property this will violate the law because the a square will always have the same height and width.

Interface Segregation Principle states that a client should not interface with fat interfaces they don't need rather there should be small interfaces/methods that they can use 
Example:
A. A Customer coming to a resturant and a vegetarian should not be made to look at the general menu that contains all foods avaliable in the resturant
B. A Vehicle Class Should not combine too many methods such as start engine,play radio,open hood,open roof these method should be broken down into interfaces that can be used seperately

DIP-Dependency Inversion Principle this pronciple states that high level classes or Modules should not depend on low level classes or module they should both depend on abstraction and abstraction should not depend on details details should depend on abstraction.
Example
A. A Remote control battery should not depend on the type of battery to function
B. 