# The `namedtuple` method returns a tuple-like objects that has fields accessible 
# with named indexes as well as the integer indexes of normal tuple. This allows for code
# that is, to a certain extent, self-documenting and more readable. It can especially
# useful in an application where there are a large number of tuples and we need to easily keep track
# of what each tuple represent.
# Futhermore, `namedtuple` inherits method from tuple and it is backward-compactible with tuple.

# The field names are passed to the namedtuple method as comma and/or whitespace-separated values.
# They can also be passed as a sequnce of strings. Field names are single strings, and they can be any legal
# Python identifier that does not begin with a digit or an underscore. A typical example is shown below. 