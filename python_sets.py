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
print('a.union(t)', a.union(t),end='\n\n')

# The `t` parameter can be any Python iterator object that supports iteration
# and all methods are available to both `set` and `frozenset` objects. It is
# important to be aware that the operator versions of these methods require their
# arguments to be sets, whereas  the methods themselves can accept any
# iterable type. For example,s-[1,2,3], for any set `s`, will generate unsupported
# operand type. Using the equivalent, s.difference([1,2,3]) will return a result. Example
s = {1,2,3,4,5}
print('s',s)
print("s.difference([1,2,3])",s.difference([1,2,3]),end='\n\n')
# print('s-[1,2,3]',s-[1,2,3]) => Unsupportes operand type

# Mutable set object have addtional methods.
# 1. s.add(item) => Adds an item to s; nothing happens if an item is already added.
s = {2,4,6,8}
print("add method")
print('s',s)
s.add(10)
print('s.add(10)',s)
s.add(4)
print('s.add(4)',s,end='\n\n') # nothing happen if an item is already added
# 2. s.clear() => Removes all elements from the set,s.
print("clear method")
print('s',s)
s.clear()
print('s.clear()',s,end='\n\n')
# 3. s.difference_update(t) => Removes those elements from the `s` set that are also in the other set,`t`.
s = {2,4,6,8}
t = {1,2,3,4,5,6}
print('difference_update method')
print('s',s)
print('t',t)
s.difference_update(t)
print('s.diffrence_update(t)',s,end='\n\n')
# 4. s.discard(item) => Removes item from the set,s.
s = {2,4,6,8}
print("discard method")
print('s',s)
s.discard(8)
print('s.discard(8)',s,end='\n\n')
# 5. s.intersection_update(t) => Romoves the items from the set,`s` which are not in the intersection of the sets,`s` and `t`
s = {1,2,3,4,5,6}
t = {2,4,6,8}
print("intersetion_update method")
print('s',s)
print('t',t)
s.intersection_update(t)
print('s.intersection_update(t)',s,end='\n\n')
# 6. s.pop() => Returns an arbitrary item from the set,`s` and it removes it from the `s` set
print('pop method')
s = {1,2,3,4,5}
print('s',s)
print('s.pop()',s.pop())
print('s',s,end='\n\n')
# 7. s.remove(item) => Deletes the item from the `s` set.
s = {1,2,3,4,5}
print('remove method')
print('s',s)
s.remove(3)
print('s.remove(3)',s,end='\n\n')
# 8. s.symmetric_difference_update(t) => Deletes all of the elements from the `s` set that are not in the symmetric difference of the sets,`s` and `t`
s = {1,2,3,4,5,6}
t = {2,4,6,8}
print('symmetric_difference_update method')
print('s',s)
print('t',t)
s.symmetric_difference_update(t)
print('s.symmetric_difference_update(t)',s,end='\n\n')
# 9. s.update(t) => Appends all of the items in an iterable object,t,to the set,s
s = {1,2,3,4,5}
print('update method')
print('s',s)
s.update([6,7,8,9,10])
print('s.update([6,7,8,9,10])',s,end='\n\n')

# Consider example below, showing addition, removal,discard and clear operations.
s1 = set()
s1.add(1)
s1.add(2)
s1.add(3)
s1.add(4)
print(s1)
s1.remove(4)
print('s1.remove(4)',s1)
s1.discard(3)
print('s1.discard(3)',s1)
s1.clear()
print('s1.clear()',s1,end='\n\n')

# The following example demonstrates some simple set operations and their result.
s1 = {'ab',3,4,(5,6)}
s2 = {'ab',7,(7,6)}
print('s1',s1)
print('s2',s2)
s = s1 - s2 # same as s1.difference(s2)
print('s1-s2',s)
print('s1.intersection(s2)',s1.intersection(s2))
print('s1.union(s2)',s1.union(s2),end='\n\n')

# Notice that the `set` object does not care that its members are not all of the same type,
# as long as they are all immutable. If you try to use a mutable object such as a list or dictionary in a set,
# you will receive an unhashable type error. Hashable types all have a hash value that does not change throughout
# the lifetime of the instance. All built-in mutable types are not hashable, so they can not be used as elements 
# of sets or keys to dictionaries.

# Notice also in the preceding code that when we print out the union of s1 and s2, there is only one element
# with the value 'ab'. This is a natural property of sets in that they do not include duplicates.
# In addtion to these built-in methods, there are a number of other operations we can perform on sets. Example to
# test for membership of a set use the following.

print("test membership")
print('ab in s1', 'ab' in s1)
print('ab not in s1','ab' not in s1,end='\n\n')

# We can loop through elements in set as follows.
print("loop set elements")
print('s1',s1)
for element in s1:
    print(element)



