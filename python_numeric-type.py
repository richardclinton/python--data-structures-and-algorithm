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
print(-7//5) # floor devision operator