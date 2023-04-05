# Higher order functions
# Functions that take other functions as arguments, or that return functions
# Python 3 contains two built-in higher order function, `filter()` and `map()`
# In python three this functions return an iterator, making them much more efficient.
# The map() function provides an easy way to transform each item into an iterable object.
# For example, here is an efficient, compact way to perform an operation on sequence.
# Note the use of the `lambda` anonymous function.

lst = [1,2,3,4]
for item in map(lambda n: n*2, lst):
    print(item)