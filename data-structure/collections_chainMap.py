# The `collections.chainmap` class was added in Python 3.2,and it provides as way to link
# a number of dictionaries, or other mappings, so that they can be treated as one object.
# In addition, there is a `maps` attribute, a `new_child()` method, and a `parents` property.
# The underlying mappings for `chainMap` objecs are stored in a list and are accessible using
# the `maps[i]` attribute to retrieve the ith dictionary. Note that, even though dictionaries
# themselves are unordered, chainMap objects are ordered lists of dictionaries.

# ChainMap is useful in applications where we are using a number of dictionaries containing
# related data. The consuming application expects data in terms of a priority, where the same key
# in two dictionaries is given priority if it occurs at the begining of the underlying list.
# ChainMap is typically used to simulated nested contexts such as when we have multiple overriding
# configuration settings. The following example demonstrates a possible use case for chainMap.

import collections

dict1 = {'a':1,'b':2,'c':3}
dict2 = {'d':4,'e':5}
chainMap = collections.ChainMap(dict1,dict2) # linking two doctionaries
print('dict1',dict1)
print('dict2',dict2)
print('chainMap', chainMap)
print('chainMap.maps',chainMap.maps)
print('chainMap.values',chainMap.values)
print("chainMap['b']", chainMap['b']) # accesing values
print("chainMap['e]",chainMap['e'], end='\n\n')

# The advantage of using chainMap objects, rather than just a dictionary, is that we
# retain previously set values. Adding a child context overrides values from the same key,
# but it does not remove it from the data structure.This can be useful when we may need to keep
# a record of changes so that we can easily roll back to a previous settings.

# We can retrieve and change any value in any of the dictionaries by providing the `map()`
# method with an appropriate index. This index represents dictionary in chainMap. Also we can retrive
# the parent settings, that is, the default settings, by using the `parents()` method

defaults = {'theme':'default','language':'eng','showIndex':True,'showFooter':True}
cm = collections.ChainMap(defaults) # creates a chainMap with defaults configuration
print('cm.maps',cm.maps)
print('cm.values()',cm.values())
cm2 = cm.new_child({'theme':'bluesky'}) # creates a new chainMap with a child overrides a parent
print('cm2[theme]', cm2['theme']) # returns the overriden theme'bluesky'
print('cms2.pop[theme]',cm2.pop('theme')) # removes the child theme'bluesky'
print('cm2[theme]',cm2['theme'])
print('cm2.maps',cm2.maps)
print('cm2.parents',cm2.parents)