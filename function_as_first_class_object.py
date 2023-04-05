# In python, it is not only data types that are treated as objects.
# Both functions and classes are what are known as first class objects, allowing
# them to be manipulated in the same ways as built-in data types.
# By definition, first class objects are
#  1. Created at runtime
#  2. Assigned as variable or in a data structure
#  3. Passed as argument to a function
#  4. Returned as result of a function

# Example


def greeting(language):
    if language == 'eng':
        return 'hello world'
    if language == 'fr':
        return 'Bonjour le monde'
    else:
        return 'language not supported'
    
# Since user-defined functions are objects, we can do things such as include them 
# in other objects, such as lists.
l = [greeting('eng'),greeting('fr'),greeting('ger')]
print(l[1])

# Function can also be used as arguments for other functions.
def call(f):
    lang = 'eng'
    return (f(lang))

result = call(greeting)
print(result)
