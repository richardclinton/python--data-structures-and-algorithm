# The important thing about ordered dictionary is that they remember ther insertion
# order, so when we iterate over them, they return values in the order they were inserted.
# This is in contrast to a normal dictionary, where the order is arbitrary. When we test to see 
# whether two dictionaries are equal, this equality is only based on their keys and values; however
# with `OrderedDict`, the insertion order is also considered an equality test between two OrderedDict
# objects with the same keys and values, but a different insertion order will return False.
import collections
odt1 = collections.OrderedDict()
odt1['one'] = 1
odt1['two'] = 2
print('odt1',odt1)
odt2 = collections.OrderedDict()
odt2['two'] = 2
odt2['one'] = 1
print('odt2',odt2)
print('odt1==odt2',odt1==odt2,end='\n\n')

# Similarly, when we add values from a list using `update`, OrderedDict will retain the same order
# as the list. This is the order that is returned when we iterate the values,as in the following example.

kvs = [('three',3),('four',4),('five',5)]
print('odt1',odt1)
odt1.update(kvs)
print('odt1.update(kvs)',odt1)
for k,v in odt1.items():
    print(k,v)
print(end='\n\n')

# OrderedDict is often used in conjuction with the `sorted` method to create a sorted dictionary
# In the following example, we use a lambda function to the values, and here we use a numarical expression
# to sort the integer values.
odt3 = collections.OrderedDict(sorted(odt1.items(), key=lambda t: (4*t[1]-t[1]**2)))
print('odt3',odt3)
print('odt3.values()', odt3.values())