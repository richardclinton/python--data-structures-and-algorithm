# Unless otherwise specified, all attributes and methods are accessible without restriction.
# This also means that everything defined in a base class is accessible from a derived class.
# This may cause problems when we are building object-oriented applications where we may want to hide
# the internal implementation of an object. This can lead to namespace conflict bweteen objects defined 
# in the derived classes with the base class. To prevent this, the methods we define private attributes
# with have a double underscore, such as `__privatemethod()` .
# These method names are automatically changed `__classname_privatemethod()` to prevent name conflicts with
# methods defined in base classes. Be aware that this does not strictly private attributes, rather it just provides
# a mechanism for preventing name conflicts.
# It is recommended to use private attributes when using a class property to define mutable attributes. A property is a
# kind of attribute that rather returning a stored value computes its value its value when called.
# For example we could redefined the `exp()` property with the following.