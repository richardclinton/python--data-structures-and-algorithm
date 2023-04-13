# Set
# Are unordered collections of unique items. Sets are themselves mutable, we can add and remove items
# from them; however, the items themselves must be immutable. An important distiction with sets is that they
# can not contain duplicate items. Sets are typically used to perform mathematical operations such as 
# intersection, union, difference, and complement.
# Unlike sequnce types, set types do not provide any indexing or slicing operations. There are two types 
# of set objects in Python, the mutable `set` object and immutable `frozenset` object.
# Set are created using comma-separated values within curly braces. By the way, we can not create an empty 
# set using `a={}`, because this will create a dictionary. To create an empty set, we write either `a=set()`
# or `a=frozenset()`.