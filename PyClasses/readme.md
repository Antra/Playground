# Notes
These are my notes and writings from [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/runestone/books/published/pythonds/index.html).

# Writing proper classes
A proper class has:
- a `docstring` to provide some level of documentation on how to use it
- a `__str__` magic method to give it a meaningful string representation
- a `__repr__` magic method for representation in the interactive shell, the debugger, etc.
- at least a way to be comparable and sortable when compared to other instance; i.e. an __eq__ and __lt__
- been designed with consideration of which attributes are public, read-only, and which are controlled/value-checked before updating

If the class is a container for other classes, then also:
- supports `len` to figure out how many things are in the container
- is able to iterate over the items in the container
- consider allowing index access via the square bracket method

# Algorithm analysis
Analysis results are described with Big-O notitation, see [Big-O complexity chart](https://stackoverflow.com/questions/487258/what-is-a-plain-english-explanation-of-big-o-notation/487278#487278) and [Python's own timeits](https://wiki.python.org/moin/TimeComplexity).

## Lists
- Indexing and Assigning at an Index: O(1)
- Appending to a list: O(1)
- Concatenating a list of k elements to a list: O(k)
- pop(): O(1)
- pop(i): O(n)
- contains (in): O(n)
- iteration: O(n)
- sort: O(n * log n)
- reverse: O(n)
- get slice[x:y]: O(k)
- concatenate: O(k)

*See [lists](https://runestone.academy/runestone/books/published/pythonds/AlgorithmAnalysis/Lists.html)*

## Dictionaries
- copy: O(n)
- get item: O(1)
- set item: O(1)
- delete item: O(1)
- contains (in): O(1)
- iteration: O(n)

*See [dictionaries](https://runestone.academy/runestone/books/published/pythonds/AlgorithmAnalysis/Dictionaries.html)*

# Basic data structures
Some basic data structures that they keep items in the position they were added (*linear data structures*):
- [stack](https://runestone.academy/runestone/books/published/pythonds/BasicDS/TheStackAbstractDataType.html): Basic last-in-first-out, LIFO, structure. Oldest items at the base, newest items at the top. E.g. a stack of books.
  - *a stack is thus handy to reverse the order of items*
- [queue](https://runestone.academy/runestone/books/published/pythonds/BasicDS/TheQueueAbstractDataType.html): Basic first-in-first-out, FIFO, structure. Oldest item at the front of the queue, newest items at the back. E.g. a line-up at a supermarket.
  - *a queue is thus handy to maintain the ordering according to age*
- [deque](https://runestone.academy/runestone/books/published/pythonds/BasicDS/TheDequeAbstractDataType.html): Is a double-ended queue; and basically combines a Stack and a Queue in a single structure, although not bound to LIFO and FIFO operation.
  - *notice that the deque is e.g. O(1) for front operations and O(n) for rear operations*
- [unordered list](https://runestone.academy/runestone/books/published/pythonds/BasicDS/TheUnorderedListAbstractDataType.html): Is a basic collection of items, holding their relative position to the others, but unordered (and maybe just stored as a linked list)
  - *Python of course has a powerful list collection already, but not all languages do*
- [ordered list](https://runestone.academy/runestone/books/published/pythonds/BasicDS/TheOrderedListAbstractDataType.html): Is a collection of items, but this time ordered (sorted ascendingly) and holding their relative position
  - *but otherwise very similar to the unordered list*



# SQLAlchemy
This is just from playing around a bit with SQLAlchemy and sqlite; I needed to keep it somewhere where I could find it again. ;)