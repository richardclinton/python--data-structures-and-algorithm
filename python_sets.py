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

# Methods and operations of sets
# 1. len(a) => Provides the total number of element in the `a` set.
a = {1,2,3,4,5}
print("len method")
print(len(a))
print(type(a),end='\n\n')
# 2. copy(a) => Provides another copy of the `a` set.
print("copy method")
print(a)
b = a.copy()
print(b,end='\n\n')
# 3. a.difference(t) => Provides a set of elements that are in the `a` set but not in `t`
t = {2,4,6,8,10}
print("difference method")
print('a',a)
print('t',t)
print(a.difference(t),end='\n\n')
# 4. a.intersection(t) => Provides a set of elements that are in both set,`a` and `t`
print("intersection method")
print('a',a)
print('t',t)
print(a.intersection(t))
