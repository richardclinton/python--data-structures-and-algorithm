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
print('c3',c3)


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
