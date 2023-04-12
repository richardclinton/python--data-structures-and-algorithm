# Tuples
# Are immutable sequences of arbitrary objects. A tuple is a comma-separated sequence of values; however,
# it is common practice to enclose them in parentheses. Tuples are very useful when we want to set up multiple 
# variables in one line or to allow a function to return multiple values of different objects. Tuple is an ordered
# sequence of items similar to the `list` data type. The only difference is this, tuples are immutable; hence, once
# created they ca not be modified, unlike list. Tuples are indexed by integers greater than zero. Tuples are
# hashbale, which means we can sort lists of them and they ca be used as keys to dictionaries.
# We can also create tuple using the built-in function: `tuple()`. With no argument this create an empty tuple
# If the argument to `tuple()` is a sequence then this creates a tuple of elements of that sequence. It is 
# important to remember to use a trailing comma when creating a tuple with one element-without a trailing comma,
# this will be interpreted as string. An important use of tuples is to allow us to assign more than one variable
# at a time by placing tuple on the left-hand side of an assignment. Example
t = tuple()
print(type(t))
t = ('a',)
print(t)
print('type is',type(t))
tp1 = ('a','b','c')
print(tp1)
t = tuple('clinton')
print(t)
x,y,z = tp1
print(x)
print(y)
print(z)
print('a' in tp1) # testing membership
print('z' in tp1)

# Most operators, such as those for slicing and indexing, work as they do on lists.
# However, because tuples are immutable, trying to modify an element of a tuple will give you a `TypeError`
# We can compare tuples in the same way tha we compare other sequences, using the ==, > and < operators.
tp1 = 1,2,3,4,5 # braces are optional
print(tp1)
print('tuple value at index 1 is', tp1[1])
print('tuple[1:3] is', tp1[1:3])
tup12 = (11,12,13)
tup13 = tp1 + tup12 # tuple concatenation
print(tup13)
print(tp1*2) # repetition for tuples
print(5 in tp1) # membership test
print(tp1[-1]) # negative indexing
print(len(tp1)) # length function of tuple
print(max(tp1))
print(min(tp1))
# tp1[1] = 5 # modification in tuple is not allowed
print(tp1 == tup12)
print(tp1 > tup12)
print(tp1 < tup12)

# We can use multiple assignment to swap values in a tuple.
l = ['one','two']
x,y = l # ('one','two')
x,y = y,x # ('two', 'one')

