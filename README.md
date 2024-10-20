## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

### 2.1 what refactoring signs (code smells) suggest this refactoring?
There should be no mixing of movie-specific data and the pricing strategies for rentals.
SRP says that a class should not have more than one reason to change.
The classes Movie and Rental handle responsibilities which belong to other classes.
Movie handles data of type movie (the title).
Rental handles data of type rental pricing and points logic - it uses the price_code to handle this
### 5.2 Document the reason(s) for your choice in README.md.
Tight Coupling: The function may be implemented on Rental; this might make classes of Rental and Movie tightly coupled. In that case, changes to be performed in any class may affect the whole code and it may not be that flexible or maintainable.

Information Expert: All information required to determine the price code, like year and genre, is contained in the Movie class. Placing logic inside the Movie class will align better with the principle of information expert.
Which means that it should be the class itself that is responsible to handle data with respect to its own attributes.