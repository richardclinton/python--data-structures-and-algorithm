# We can user the `dir(object)` to get a list of attributes of a particular object.
# The methods that begin and end with two underscores are called apecial methods.
# Apart from the following exception, special methods are generally called by python
# interpreter rather than the programmer; for example when we use the `+` operator,
# we are actually invoking to `__add__()` call. For example, rather than using `my_object.__len__()`,
# we can use `len(my_object)`; using `len()` on string object is actually much faster, because it
# returns the value representing object's size in the memory, rather making a call to the object's `__len__()` 
# method. The only special method we actually call in our program as common practice, is the `__init__()` method.
# to invoke the initializer of the superclass in our own class definition. It is strongly advised not to use
# the double underscore syntax for your own objects because potential current or future conflicts with Python's
# special methods.
# We may, however, want to implement special methods in custom objects, to give them some of the behaviour
# of built-in types.
# In the following code we create a class that implements `__repr__()` method. This method creates string
# representation of our object that is useful for inspection purposes.

class MyClass:
    def __init__(self, greet):
        self.greet = greet
        
    def __repr__(self):
        return 'a custom object (%r)' % self.greet
    
    # Notice the use the `%r` forma placeholder to return the standard representation of the object
    # This is useful and best practice because, in this case, it shows us that the `greet` object is
    # a string indicated by the quation mark
    
a = MyClass('Clinton')
print(a)
 