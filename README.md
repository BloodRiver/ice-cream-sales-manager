# Ice-cream Sales Manager
### By Sajeed Ahmed Galib Arnob

This project Simulates the operations of a ice-cream sales shop/business/startup.

I only created this project as a means to teach my student the basic concepts of software development using Python.

## Changelogs

### v0.1
- Currently does not support database
- Broken down into modules:

  - `main.py` - consists of the main interface and different menus written as user-defined functions for a workflow that is easier for beginners to understand and maintain.

  - `predefined_values.py` - as the name suggests, this file consists of predefined values. This file will have a lot of content removed later when database using SQL is implemented.
  If necessary, the file may be removed entirely.

  - `utility_functions.py` - as the name suggests, this file consists of user defined functions meant to be re-used to reduce redundancy (repetition of the same code).
  
    Upon implementing database functions, this file may also lose a lot of content.

  - `database_functions.py` - only serving as a placeholder for functions such as `save_order()` to be called without throwing an error. This same function call will later on save ice-cream orders to database.
