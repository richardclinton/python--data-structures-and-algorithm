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
print(sum(s),end='\n\n')

# 5. all(s) => Returns True if all element in s are True(that is, not 0, False or Null)
print("all method")
s = [1,2,3,4,5]
print(all(s))
s = [1,2,3,0]
print(all(s))
s = ["a","b"]
print(all(s))
s = ["a","b",None]
print(all(s))
s = [True,True]
print(all(s))
s = [False, True]
print(all(s))
print(all(range(0,3)), end='\n\n')

# any(s) => Checks whether any item in s is True
print("any methods")
s = [1,2,3]
print(any(s))
s = [0,1]
print(any(s), end='\n\n')

# In addition, all sequences support the following operations
# 1. s+r => concatenates two sequnces of the same type
print("s+r operation")
s = [1,2,3]
r = [4,5,6]
print(s+r)
s = "clin"
r ="ton"
print(s+r)
s = (1,2,3)
r = (4,5,6)
print(s+r,end='\n\n')

# 2. s*n => make n copies of s, where n is an integer.
print("s*n operation")
s = [1,2,3]
n = 3
print(s*n)
s = "paw"
n = 2
print(s*n, end="\n\n")

# 3. v1, v2, ..., v n=s => unpacks n variables from s to v1, v2 and so on.
print("unpack operation, v1, v2,...v n=s")
a,b,c,d = [1,2,3,4]
print(a,d, end='\n\n')

# 4. s[i] => Indexing returns the i element of s.
print("s[i] indexing operation")
s = [1,2,3]
print(s[1])
s = "clinton"
print(s[4])
s = range(10)
print(s[5])
s = (1,4,7,9,10)
print(s[-1],end='\n\n')

# 5. s[i:j:stride] => Slicing returns element between i and j with optional stride
print("s[i:j:stride] operation")
s = [1,2,3,4,5,6,7,8,9]
print(s[1:7])
print(s[2:7:2],end='\n\n')

# 6. x in s => Returns True if x element is in s
print("x in s operation")
s = [1,2,3,4,5]
print(2 in s)
print(11 in s)
print('a' in s)
s = range(9)
print(0 in s)
print(9 in s)
s = "clinton"
print('l' in s)
print("a" in s)
s = (1,2,3,4,5,6)
print(6 in s)
print('6' in s, end='\n\n')

# 7. x not in s => Returns True if the x element is not in s.
print("x not in s operation")
s = [1,2,3,4]
print(5 not in s)
print(1 not in s)

