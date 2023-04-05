# Higher order functions
# Functions that take other functions as arguments, or that return functions
# Python 3 contains two built-in higher order function, `filter()` and `map()`
# In python three this functions return an iterator, making them much more efficient.
# The map() function provides an easy way to transform each item into an iterable object.
# For example, here is an efficient, compact way to perform an operation on sequence.
# Note the use of the `lambda` anonymous function.

lst = [1,2,3,4]
print('map function')
for item in map(lambda n: n*2, lst):
    print(item)
print('\n\n')
    
# Similarly, we can use thefilter() built-in function to filter items in a list
lst = [1,2,3,4]
print('filter function')
for item  in filter(lambda m: m<4,lst):
    print(item)
    
# Note that both filter() and map() functions perform the same functions similar to
# what can be archieved by list comprehension.
# Creating our own higher order function is the one of the hallmarks of functional programming style.
# A practical example of how higher order functions can be useful is demostrated by the following.
words = str.split("The longest word in this sentence")
result = sorted(words, key=len)
print("sorted function")
print(result,end='\n\n')

# Example for case-insensitive sorting
sl = ['A','b','a','C','c']
print('Case-insensitive sorting')
sl.sort(key=str.lower)
print(sl)
print('Case sensitive sort')
sl.sort()
print(sl, end='\n\n')

# Note the difference between list.sort() method and the sorted() built-in
# function. The list.sort() method, a method of the list object, sorts the existing instance of a list
# without copying it. This method changes the target object and returns None. It is an important convention in Pyhthon
# that functions or methods that change the object return None, to make it clear that no new object was created
# and that the object itself was changed.
# On the other hand, the sorted() built-in function returns a new list. It actually accepts any iterable
# object as an argument, but it will always return a list. Both `list sort` and `sorted` take two optional keyword
# arguments as key.