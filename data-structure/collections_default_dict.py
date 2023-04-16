# The defaultdict object is a subclass of dict, and therefore they share methods and operations.
# It acts as a convinient way to initialize dictionaries. With `dict`, will throw KeyError when
# attempting to access a key that is not already in the dictionary. The `defaultdict` overrides one
# method, `missing(key)`, and creates a new instance variable, `default_factory`. With defaultdict
# rather than throw an error, it will run the function supplied as default_factory argument, which
# will generate a value. A simple use of defaultdict is to set default_factory to `int` and use it 
# to quickly tally the counts of items in the dictionary,as in the following example.
from collections import defaultdict
dd = defaultdict(int)
words = str.split("red blue green red yellow blue red green green red")
for word in words:
    dd[word] += 1
    
print('dd',dd,end='\n\n')

# You will notice that if we tried to do this with an ordinary dictionary, we would get
# a key error when we tried to add the first key.The `int` we supplied as an argument to the
# `defaultdict` is realy the int() function that simply returns a zero.


# We can, of course, create a function that will determine the dictionary's value.
# For example, the following function returns True if the supplied argument is a primary color,
# that is red,green or blue, or returns false otherwise.
def isprimary(c):
    if (c == 'red') or (c == 'blue') or (c == 'green'):
        return True
    else:
        return False