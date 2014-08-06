BFPython
========

Class based BrainFuck interpreter in Python.

Implemented:

- Operators
- Moving the tape pointer
- Printing out
- Getting a character in

To-Do:
- loops
- better input


Basic syntax:
- +,- Increasing/Decreasing the number, at the data pointer.
- <,> Moving the data pointer left or right one unit.
- .   Writing out the number, at the pointer.
- ,   Getting a character and writing it into at the pointer.

(
- []  The loop. If the number at the pointer is zero jump to the command right after ], else loop between [] and the       commands inside until, the the number becomes zero.
 


You can learn about brainfuck here: http://en.wikipedia.org/wiki/Brainfuck
Usage in test.py file.