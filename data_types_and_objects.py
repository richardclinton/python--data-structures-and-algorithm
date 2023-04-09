# Numeric types
#   1. int
#   2. float
#   3. complex
#   4. bool
# Sequence types
#   1. str
#   2. list
#   3. tuple
#   4. range
# Mapping type
#  1. dict
# Two set types

# It is also possible to create user defined objects such as fucntions or classes.
# All data types in python are objects. In fact, pretty much everything is an object in python, including
# modules, classes and fucntions, as well as literals such as `strings` and `integers`.
# Each object in python has a `type`, a `value` and an `identity`
# Example great = "helloworld", we are creating an instance of a `string` object with the value `helloworld`
# and the identity of `great`. The identity of an object act as a pointer to the object's location in memory.
# The type of object, also known as the object's class, describes the object internal representation as well as
# the methods and operations it supports. Once an instance of an object is created, its identity and type cannot be 
# changed. We can get the identity of an object by using the built-in function `id()`. This returns  an
# identifying integer and on most systems, this refers to its memory location, althought you should not rely on
# this in any of your code.

# Also there are number of ways to compare objects
a = 4; b = 5
if a == b: # `a` and `b` have the same value
    pass
if a is b: # `a` and `b` are the same object
    pass
if type(a) is type(b): # `a` and `b` are the same type
    pass

# Mutable objects
# => such as `lists` can have their values changed. They have methods, such as `insert()` or `append()`,
#    that change an object's value.
# Immutable objects
# => such as `strings` cannot have their value changed, so when we run their methods,
#    they simply return a value rather than change a value of underlying object.


# Python data types can be devided into three categories: numeric, sequence and mapping.
# There is also None object that represents Null, or the absence of a value. It should not forgotten
# that other objects such as classes, files and exceptions can also properly be considered `types`.
# Python build-in data types are outlined below
# a. None
# 1. None => It is a null object
# b. Numeric
# 1. int => This is an integer data type
# 2. float => This data type can store a floating-point number.
# 3. complex => It stores a complex number
# 4. bool => It is boolean type and returns True or False
# c. Sequence
# 1. str => It is used to store a string of characters
# 2. list => It can store a list of arbitrary objects
# 3. tuple => It can store a group  of arbitrary items.
# 4. range => It is used to create a range of integers.
# d. Mapping
# 1. dict => It is a dictionery data type that stores data in key/value pairs.
# 2. set => It is a mutable and unordered collection of unique items.
# 3. frozenset => It is an immutable set.

