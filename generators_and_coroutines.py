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
