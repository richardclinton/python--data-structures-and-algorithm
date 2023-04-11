# Number types include the follwoing
# 1. Integers(int), whole number of unlimited range
# 2. Floating-point numbers(float)
# 3. Complex numbers(complex), which are represente by two float numbers 
# 4. Boolean (bool)
# Python provides the `int` data type that allows standard arthmetic operators (+,*,- and /) to work on them.
# The boolean data type has two possible values, `True` and `False`. These values are mapped to 0 and 1, respectively.

a=4; b=5 # operator `=` assigns the value to variable
print(a, "is of type", type(a))
print(9/5)
c = b/a # devidion return a floating point number
print(c,"is of type", type(c))
print(c)

# The devision operator (/) always returns a float type; however if you want to get the `int`
# type after devision, you can use the floor devision operator (//), which discards any fractional part
# and will return the largest integer value that is less than or equal to x
a = 4; b = 5
d = b //  a
print("\n\n")
print(d, "is of type", type(d))
print(7/5) # true devision
print(-7//5,end='\n\n') # floor devision operator

# The exponent operator (**) can be used to get the power of a number (for example x**y),
# and the modulus operator (%) returns the reminder of the of the devision(for example a%b retuens the reminder of a/b)
a = 7; b = 5

e = b**a # The operator (**) calculate the power
print(e)
print(a%b,end='\n\n')


# Complex numbers are represented by two floating-pint numbers. They are assigned using the `j` operator
# to signify the imaginary part of the complex number. We can access the real and imaginary part with
# `f.real` and `f.imag`, respectively. Complex numbers are generally used for scientific computations.
# Python supports addition, substraction, multiplication, power, conjugates, and so forth on complex numbers.

f = 3 + 5j
print(f, "is of type",type(f))
print(f.real)
print(f.imag)
print(f*2)
print(f+3)
print(f-1,end='\n\n')

# Boolean
# Are represented using truth values, that is, `True` and `False`; it is similar to `0` and `1`.
# There is a `bool` class in python, which returns True or False. Boolean values can be combined
# with logical operators such as `and`, `or` and `not`.
print("Boolean")
print(bool(2))
print(bool(-2))
print(bool(0),end='\n\n')

# A Boolean operation returns either True or False. Boolean oparations are ordered in priority, so if more
# than one Boolean operation occurs in an expression, the operation with the highest will occur first.
# Below are three boolean operators in descending order of priority.
# 1. not x => It returns False if x is True, and returns True if x is False.
# 2. x and y => it returns True if x and y are both True; otherwise it returns False.
# 3. x or y => It returns True if either x or y is True; otherwise it retuens False.


# Python is very efficient when evaluating a Boolean expressions as it will only evaluate an
# operator if it needs to. For example if x is True in an expression x or y, there is no need to
# evaluate y since the expression is True anyway,that is why in Python y is not evaluated.
# Similarly, in an expression `x and y`, if x is False, the interpreter will simply evaluate x and
# return False, without evaluating y.

# Comparison operators (<,<=,>,>=,==,!=)
# This operators works with numbers, lists, and other collection objects and return True if the
# condition holds. For collection objects,comparison operators compare the number of elements and
# the equivalence operator (==) returns True if each collection object is structurally equivalent, and 
# the value of each element is identical

see_boolean = (4 * 3 > 10) and (6 + 5 >= 11) 
print("Comparison operator")
print(see_boolean)

if (see_boolean):
    print("Boolean expression returned True",end='\n\n')
else:
    print("Boolean expression returned False",end='\n\n')


# Representation Error  
# It should be that native double precision representation of floatin-point numbers leads to
# some unexpected result. Example
a = 1 - 0.9
print("representation error")
print("1-0.9=>",a)
print(1-0.9 == .1,end='\n\n')
# This is a result of the fact that most decimal fractions are not exactly representable as
# binary fraction, which is how most underlying hardware represents floating-point numbers.
# For algorithms or application where this may be an issue,Python provides a decimal module. This
# module allows for the exact representation of decimal numbers and facilitates greater control of properties,
# such as rounding behaviour, number of significant digits, and precision.
# It defines two object, a `Decimal` type, representing decimal numbers and a `Context` type, representing 
# various computational parameters such as precision, rounding and error handling. Example

import decimal
print("Decimal module")
x = decimal.Decimal(3.14)
y = decimal.Decimal(2.74)
z = x * y
print(z)
decimal.getcontext().prec = 4
z = x * y
print(z,end='\n\n')
# Here we have created a global context and set the precision to 4. The `Decimal` objects can
# be treated pretty much as you would treat `int` and `float`. They are subject to all to of the same mathematical
# operations and can be used as dictionery keys, placed in sets, and so on. In additon `Decimal` objects
# also have several methods for mathematical operations, such as natural exponents, `x.exp()`, natural logarithms,`x.ln()`,
# and base 10 logarithms, `x.log10()`. Python also has fractions module that implements a rational number type.
import fractions

a = fractions.Fraction(3,4)
print("fractions.module")
print(a)
b = fractions.Fraction(0.5)
print(b)
c = fractions.Fraction("0.25")
print(c)

# It is also worth mentioning here the NumPy extension. This has types for
# mathematical objects, such as arrays, vectors,and matrices, and capabilties for linear algebra,calculation 
# of Fourier transforms, eigenvectors, logical operations, and much more.