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
# configuration settings.