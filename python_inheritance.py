# Inheritance
# Is  one of most powerful features of object-oriented programming
# It allows us to inherit the functionality from other classes. It is possible to
# create a new class that modifies the behaviour of an existing class through inheritance.
# Inheritance means that if an object of one class is created by inheriting another class,
# the the object would have all functionality, methods and variables of both the classes;
# that is, the parent class and new class. The existing class from which we inherit the functionalities
# is called parent/base class, and the new class is called derived/child class.
# Inheritance in Python is done by passing the inherited class as an argument in the class definition
# It is often used to modify the behaviour of existing methods.

class Employee:
    numEmployee = 0
    
    def __init__(self, name, rate):
        self.owed = 0
        self.name = name
        self.rate = rate
        Employee.numEmployee +=0
        
    def delete(self):
        Employee.numEmployee -= 1
        
    def hours(self,numHours):
        self.owed += numHours * self.rate
        return ("%.2f hours worked" % numHours)
    
    def pay(self):
        self.owed = 0
        return ("payed %s" % self.name)
    

class SpecialEmployee(Employee):
    # For subclass to define new class variable, it needs to define an `__init__()` method
    def __init__(self, name, rate, bonus):
        Employee.__init__(self,name, rate)
        self.bonus = bonus
    
    def hours(self, numHours):
        self.owed += numHours * self.rate *2
        return ("%.2f hours worked" % numHours)
# An instance of `SpecialEmployee` class is identical to an `Employee` instance, except for
# changed `hours()` method
# Notice that the methods of the base class are not automatically invoked and it is necessary
# for the derived class to call them.
# We can test for the class membership using the built-in `isintance(obj1,obj2)` function. This returns
# `True` if `obj1` belongs to the class of `obj2
# issubclass() => to check whether a class is a subclass of another class
# isinstance() => to check if an object belongs to a class or not
print(issubclass(SpecialEmployee, Employee), end='\n\n')
print(issubclass(Employee, SpecialEmployee), end='\n\n')

d = SpecialEmployee('Packt',20, 100)
b = Employee('Packt', 20)
print(isinstance(b, SpecialEmployee),end='\n\n')
print(isinstance(b, Employee))

# Generally, all the methods operate on the instance of a class defined within a class.
# However, it is not a requirement. There are two types of methods, `static` methods and `class` methods.
# A static method is quite similar to a class method, which is mainly bound to the class, and not bound with the
# object of the class. It is defined within a class and does not require an instance of the class to execute.
# It does not perform any operations on the instance and it is defined using the `@staticmethod` class decorator
# Static methods can not access the attributes of an instance, so their common usage is as a convinience to group
# utility functions together.
        