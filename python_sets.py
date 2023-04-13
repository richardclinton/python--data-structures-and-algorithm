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
print(a.intersection(t),end='\n\n')
# 5. a.isdisjoint(t) => Returns True if no element is common in both sets,`a` and `t`
print("isdisjoint method")
print('a',a)
print('t',t)
print(a.isdisjoint(t))
k = {6,7,8}
print('k',k)
print(a.isdisjoint(k),end='\n\n')
# 6. a.issubset(t) => Returns True if all of the elements of the `a` set are also in the `t` set.
print("issubset method")
print('a',a)
print('t',t)
print(a.issubset(t))
k = {1,2,3,4,5,6,7,8,9}
print('k',k)
print('a.issubset(k)',a.issubset(k))
print('k.issubset(a)',k.issubset(a),end='\n\n')
# 7. a.issuperset(t) => Returns True if all of the elements of the `t` set are also in the `a` set
print("issuperset method")
print('a',a)
print('t',t)
print('a.issuperset(t)',a.issuperset(t))
print('k',k)
print('a.issuperset(k)',a.issuperset(k))
print('k.issuperset(a)',k.issuperset(a),end='\n\n')
# 8. a.symmetric_difference(t) => Returns a set of elements that are in either the `a` or `t` sets,but not both
print("symmetric_difference method")
print('a',a)
print('t',t)
print(a.symmetric_difference(t),end='\n\n')
# 9. a.union(t) => Returns a set of elements that are in either the `a` or `t` sets.
print('union method')
print('a',a)
print('t',t)
print('a.union(t)', a.union(t))
