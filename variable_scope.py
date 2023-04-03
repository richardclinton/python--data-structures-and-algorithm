# Example 1
a = 15; b = 25

def my_function():
    global a
    a = 11; b = 21
    
    
my_function()
print(a,b) # 11 25

# Example 2
a = 10

def my_next_function():
    print(a)
    
my_next_function() # 10

# Example 3
a = 10

def my_new_function():
    print(a)
    a = a + 1
    
my_new_function() # UnboundLocalError: local variable `a` referenced before assignment
# The preceeding code gives an error because assignment to a variable in a scope makes that
# variable a local variable to that scope.

# Example 4
d = 10

def my_function_new():
    global d
    print(d)
    d = d + 1
    
my_function_new() # 10
print(d) # 11