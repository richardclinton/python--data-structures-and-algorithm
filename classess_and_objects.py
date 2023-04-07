# Classes
# Are a way to create new kinds of objects, and they are central to object-oriented programming.
# A class defines a set of attributes that are shared across instances of that class.Typically, classess are sets
# of functions, variables and properties.
# The functions defined inside a class are called instance methods. They apply some operations
# to the class instance by passing an instance of that class as the first argument. This argument is
# called `self` by convention, but it can be any legal identifier.

class Employee(object):
    numEmployee=0
    
    def __init__(self, name, rate):
        self.owed = 0
        self.name = name
        self.rate = rate
        Employee.numEmployee += 1
        
    def delete(self):
        Employee.numEmployee -= 1
        
        
    def hours(self,numHours):
        self.owed += numHours * self.rate
        return ("%.2f hours worked" % numHours)
    
    def pay(self):
        self.owed = 0
        return ("payed %s" % self.name)
    
    # Class variables, such as `numEmployee`, share value among all the instances of the class.
    # In the above example `numEmployee` is used to count the number of employee instances.
    # Note that the `Employee` class implements the __init__ and __del__, special methods.
    
emp1 = Employee("Jill", 18.50)
emp2 = Employee("Jack", 15.50)

print(Employee.numEmployee)
print(emp1.hours(20))
print(emp1.owed)
print(emp1.pay())