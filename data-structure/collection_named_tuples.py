# The `namedtuple` method returns a tuple-like objects that has fields accessible 
# with named indexes as well as the integer indexes of normal tuple. This allows for code
# that is, to a certain extent, self-documenting and more readable. It can especially
# useful in an application where there are a large number of tuples and we need to easily keep track
# of what each tuple represent.
# Futhermore, `namedtuple` inherits method from tuple and it is backward-compactible with tuple.

# The field names are passed to the namedtuple method as comma and/or whitespace-separated values.
# They can also be passed as a sequnce of strings. Field names are single strings, and they can be any legal
# Python identifier that does not begin with a digit or an underscore. A typical example is shown below.

from collections import namedtuple
space = namedtuple('space','x y z') 
s1 = space(x=2.0,y=4.0,z=10) # we can also use space(2.0,4.0,10)
print('s1',s1)
print('s1.x*s1.y*s1.z',s1.x*s1.y*s1.z,end='\n\n') # calculate the volume

# In addition to the inherited tuple methods, the namedtuple also defines three
# methods for its own,`_make()`,`asdict()` and `replace()`. These methods begin with
# an underscore to prevent potential conflicts with field names. The `_make()` method takes 
# an iterable as an argument and turns it into a namedtuple object, as in the following example.
s1 = [4,5,6]
s1 = space._make(s1)
print('s1',s1)
print('s1._1',s1._1)