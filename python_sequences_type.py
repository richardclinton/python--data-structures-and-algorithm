# Sequnce
# Are ordered sets of objects inexed by non-negative intergers.
# Sequences include `list`, `string`, `tuple` and `range` objects.
# Lists and tuples are sequnces of arbitrary objects, whereas strings are
# sequnces of characters. However `string`, `tuple` and `range` are immutable, whereas
# list object is mutable. All sequence types have number of operations in common. Note that
# for the immutable types, any operation will only return a value rather than actually change the value.
# For all sequences, the indexing and slicing operators apply as described in the previous chapter.
# Below we present, some of the important methods and operations that are common to all of the sequence 
# types (list, tuple, string and range objects)
# 1. len(s) => Returns the number of element in s.
s = [1,2,3]
print("len method")
print(len(s))
s = "clinton"
print(len(s))
s = (1,2,3,4)
print(len(s))
s = range(5)
print(len(s),end='\n\n')

# 2. min(s, [,default=obj],key=func) => Return the minimum value in s(alphabetically for strings)
print("min method")
s = [3,5,7,1,8]
print(min(s))
s = "clinton"
print(min(s))
s = ['Asha','Juma','Ali','Amina','Absa']
print(min(s))
print(min(s, key=len))