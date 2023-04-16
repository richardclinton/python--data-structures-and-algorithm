# The defaultdict object is a subclass of dict, and therefor they share methods and operations.
# It acts as a convinient way to initialize dictionaries. With `dict`, will throw KeyError when
# attempting to access a key that is not already in the dictionary. The `defaultdict` overrides one
# method, `missing(key)`, and creates a new instance variable, `default_factory`. With defaultdict
# rather than throw an error, it will run the function supplied as default_factory argument, which
# will generate a value. A simple use of defaultdict is to set default_factory to `int` and use it 
# to quickly tally the counts of items in the dictionary,as in the following example.