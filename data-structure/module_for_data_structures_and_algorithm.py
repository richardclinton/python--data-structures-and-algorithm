# In addtion to the built-in data type,there are several Python modules that we can use
# to extend the built-in types and functions. In many cases these, these Python modules
# offer efficiency and programming advantages that allow us to simplify our code.
# The built-in data type, we have looked so far,strings,lists,dictionaries,tuples,sets as well as
# the decimal and fraction modules. They are often described by the term Abstarct Data Types (ADTs)
# ADT(s) can be considered mathematical specifications for the set of operataions that can be
# performed on data. They are defined by their behaviour rather than their implementation. In addition
# to the ADTs that we have looked at, there are several Python libraries that provide extensions to the
# built-in data-types.

# Collections
# This module provides more specialized, high performance alternatives for the built-in data types
# as well as the utility function to create a named tuples.
# Below shows datatypes and operations of the collections module and their description.
# 1. namedtuple() => Creates tuple subclasses with named fields
# 2. deque => Lists with fast appends and pops either end.
# 3. chainMap => Dictionary-like class tp create a single view of multiple mapping
# 4. Counter => Dictionary subclass for counting hashable objects
# 5. OrderedDict => Dictionary subclass that remembers the entry order.
# 6. defaultdict => Dictionary subclass that calls a function to supply missing values.
# 7. UserDict,UserDict,UserString => These three data types are simply wrappers for their
#    underlying base classes. Their use has largely been supplanted by the ability to subclass
#    their respective base class directly. Can be used to access the underlying objects as an attribute.