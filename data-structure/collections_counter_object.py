# Counter is a subclass of a dictionary where each dictionary key is a hashable object
# and the associated value is an integer count of that object. There are three ways to initilize 
# a counter. We can pass it as any sequence object, a dictionary of key:alue pairs, or a tuple of
# the format (object=value,...), as in the example below.
from collections import Counter
ct = Counter('Anysequence')
print(ct)
c1 = Counter('Anysequence')
c2 = Counter({'a':1,'c':2,'e':3})
c3 = Counter(a=1,c=1,e=3)
print('c1',c1)
print('c2',c2)
print('c3',c3, end='\n\n')


# We can also create an empty counter object and populate it passing its `update` method
# an iterable or a dictionary. Notice how the `update` method adds the count rather replacing them
# with new values. Once the counter is populated, we can access the stored values in the same way
# we would do for dictionaries.
ct = Counter()
print('ct',ct)
ct.update('abca')
print('ct',ct)
ct.update({'a':3}) # update the value of `a`
print("ct.update({'a':3})",ct)
for item in ct:
    print("%s:%d" % (item,ct[item]))
print(end='\n\n')   
    
# The most notable difference between counter objects and dictionaries is that counter
# objects return a zero count for missing items rather than raising a key error. We can create
# an iterator out of a `Counter` object by using its `elements()` method. This return an iterator
# where counts below one are not included and the order is not guaranteed. In the following code,
# we performs some update, creates an iterator from `Counter` elements and use `sorted()` to the
# keys alphabetically.
print(ct)
print('ct[x]',ct['x'])
ct.update({'a':-3,'b':-2,'e':2})
print("ct.update({'a':-3,'b':-2,'e':2})", ct)
print("sorted(ct.elements())",sorted(ct.elements()),end='\n\n')

# Tow other Counter methods worth mentioning are `most_common()` and `substract()`.
# The most common method takes a positive interger argument that determines the number of 
# most common elements to return. Elements are returned as a list of (key,value) tuples.
# The substract method works exactly like update except,instead of adding values, it substract them.
print('most_common method')
print('ct',ct)
print('ct.most_common()', ct.most_common(),end='\n\n')
print('substract method')
print('ct',ct)
ct.subtract({'e':2})
print("ct.subtract({'e':2})",ct)

