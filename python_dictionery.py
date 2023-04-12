# Dictionary
# Is the one of the most popular and useful data types. Dictionary stores data in a mapping
# of key and value pair. Dictionary are mainly a collection of objects; they are indexed by numbers, strings
# or any other immutable objects. Keys should be unique in the dictionaries; however, the values in the dictionary
# can be changed. Python dictionaries are the only built-in mapping type; they can be thought of as a mapping
# from a set of keys to a set of values. They are created using `{key:value}` syntax. Example
a = {'Monday':1,'Tuesday':2,'Wednesday':3} # creates a dictionary
b = dict({'Monday':1,'Tuesday':2,'Wednesday':3})
print(a)
print(b)
c = dict(zip(['Monday','Tuesday','Wednesday'],[1,2,3]))
print(c)
d = dict([('Monday',1),('Tuesday',2),('Wednesday',3)])
print(d)

# We can add keys and values. We can also update multiple values, and test for membership or
# occurrence of a value using the `in` operator
d['Thursday'] = 4 # add an item
d.update({'Friday':5,'Saturday':6}) # add multiple items
print(d)
print('Wednesday' in d) # membership test (only in keys)
print(5 in d) # membership do not check in values

# The `in` oparator to find an element in a list takes too much time if the list is long.
# The running time required to look up an element in a list increases linearly with an increase
# in the size of the list. Whereas, the `in` operator in dictionaries uses a hashing function, which
# enables dictionaries to be very efficient, as the time taken in looking up an element is independent
# of the size of the dictionary.
# Notice, when we print out the {key:value} pairs of the dictionary, it does so in no particular order. This is 
# not a problem since we use specified keys to look up each dictionary value rather than an ordered sequence of
# integers, as is the case for strings and lists.
a = dict(zip('packt', range(5)))
print(a)
print(len(a))
print(a['c']) # to check the value of a key
print(a.pop('a'))
print(a)
b = a.copy() # make a copy  of the dictionary
print(b)
print(a.keys())
print(a.values())
print(a.items())
a.update({'a':1}) # add item in the dictionary
print(a)
a.update(a=22) # update the value of key `a`
print(a,end='\n\n')

# Dictionary methods
# 1. len(d) => Returns total number of items in the dictionary,d.
d = dict(zip('joseph',range(6)))
print(d)
print("len method")
print(len(d), end='\n\n')
# 2. d.clear() => Removes all of the items of dictionary,d.
print("clear method")
print(d)
d.clear()
print(d,end='\n\n')

# 3. d.copy() => Returns a shallow copy of the dictionary, d.
d = dict(zip('abcd',range(3)))
print("copy method")
print(d)
e = d.copy()
print(d,end='\n\n')

# 4. d.fromkeys(s, [,values]) => Returns a new dictionary with keys from the `s` sequence and values set to value
print("fromkeys method")
x = ('a','b','c')
y = 2
z = dict.fromkeys(x,y)
print(z)
x = {'a','b','c'}
z = dict.fromkeys(z,y)
print(z)
z = dict.fromkeys(x)
print(z)
x = ['a','b','c']
z= dict.fromkeys(x,y)
print(z)
y = (10,11,12)
z = dict.fromkeys(x,y)
print(z,end='\n\n')
# 5. d.get(k[,value]) => Returns d[k] if it is found; otherwise it `v`.(None if v is not given)
print("get method")
print(d)
print(d.get('a'))
print(d.get('z',10))
print(d.get('z'),end='\n\n')
# 6. d.items() => Returns all of the `key:value` pair of the dictionary,d.
print("items() method")
print(d)
print(d.items())
print(type(d.items()),end='\n\n')
# 7. d.keys() => Returns all of the keys defined in the dictionary,d.
print("keys() method")
print(d)
print(d.keys())
print(type(d.keys()),end='\n\n')

# 8. d.pop(k[,default]) => Returns d['k'] and removes it from d.
print("pop method")
print(d)
print(d.pop('a'))
print(d,end='\n\n')

# 9. d.popitem() => Removes a random key:value from the dictionary, d, and return it as a tuple.
print("popitem method")
print(d.popitem())
print(d,end='\n\n')
# 10. d.setdefault(k[,v]) => Returns d[k]. If it is not found, it returns v and sets d[k] to v
print("setdefault method")
print(d)
print(d.setdefault('b'))
print(d.setdefault('a',1))
print(d,end='\n\n')

# 11. d.update(b) => Adds all of the object from the b dictionary to the d dictionary.
print("update method")
print(d)
d.update({'c':3,'d':4})
print(d)
d.update(b=2)
print(d,end='\n\n')
# 12. d.values() => Returns all of the values in the dictionary, d.
print("values method")
print(d)
print(d.values())
print(type(d.values()))
