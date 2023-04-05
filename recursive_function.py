# Recursion
# Function takes one or more calls to itself during execution.
# Loop iterations and recursion are different in the sense that loops execute
# statements repeatedly through a boolean condition or through a series of elements,whereas recursion
# repeatedly calls a function.

# Iteration example
def iterTest(low, high):
    while low <= high:
        print(low)
        low = low+1
        
# Recursion example
def recuTest(low, high):
    if low <= high:
        print(low)
        recuTest(low+1,high)
        
# In general, iteration is more efficient; however recursive functions are often easier
# to understand and write. Recursive functions are also useful for manipulating recursive data structures
# such as linked lists and trees