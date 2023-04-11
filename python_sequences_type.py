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

# 2. min(s, [,default=obj],key=func) => Return the minimum value in s(alphabetically for strings).
print("min method")
s = [3,5,7,1,8]
print(min(s))
s = "clinton"
print(min(s))
s = ['Asha','Juma','Ali','Amina','Absa']
print(min(s))
print(min(s, key=len),end='\n\n')

# 3. max(s,[,default=obj], key=func) => Returns the maxmum value in s (Alphabetically for strings).
print("max method")
s = [1,2,3,4,5,6,7,8,9]
print(max(s))
s = "clinton"
print(max(s))
s = ['Asha','Juma','Ali','Amina','Absa','Zahoro','Mwantumu']
print(max(s))
print(max(s,key=len),end='\n\n')

# 4. sum(s,[,start=0]) => Returns the sum of elemts (returns TypeError id if s in not numeric)
print("sum method")
s = [1,2,3,4,5]
print(sum(s))
print(sum(s,start=10))
print(sum(range(10)))
print(sum([1,2,3,4,5,6,7,8,9]))
s = (4,5,1)
print(sum(s))
