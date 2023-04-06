# Generators
# We can create functions that do not just return one result but rather an
# entire sequence of results, by using the yield statement.
# Python contains generator functions, which are an easy way to create iterators and
# are especially useful as a replacement of unworkably long list.
# A generator yields items rather than build lists. 
# Compare the running time of a list compared to a generator
import time
# generator function creates an iterator of odd numbers between n and m
def oddGen(n,m):
    while n < m:
        yield n
        n+=2
        
        
# builds a list of odd numbers between n and m
def oddList(n,m):
    lst = []
    while n < m:
        lst.append(n)
        n+=2
        
    return lst

# the time it takes to perform sum of an iterator
t1 = time.time()
sum(oddGen(1,100000))
print("Time to sum an iterator: %f" % (time.time()-t1))
# the time it takes to build and sum a list
t1 =  time.time()
sum(oddList(1,1000000))
print("The time to build and sum a list: %f" % (time.time()-t1))

# Generators never return a value rather than None
# Typically, generator objects are used in for loops. For example, we can make use of the
# oddList generator function created in the preceding code to print out odd integers between 1 and 10
for i in oddList(1,10):print(i)

# we can also create a generator expression, which, apart from replacing square brackets with parentheses,
# uses the same syntax and carries out the same operation as list comprehension. Generator expressions, however,
# do not create a list; they create a generator object. This object does not create the data, but rather creates
# that data on demand. This means that generator objects do not support sequence methods such as append() and insert()

# Yo can, however, change a generator into a list using the list() function
lst1 = [1,2,3,4]
gen1 = (10**i for i in lst1)
print(gen1, end='\n\n')
for x in gen1:
    print(x)
