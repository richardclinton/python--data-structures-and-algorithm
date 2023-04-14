# Deques
# Double-ended queues, deques (ussually pronounced decks), are list-like objects that supports
# thread safe, memory efficient appends.
# Deques are mutable and support some of the opeartions of lists, such as indexing. Deques can be
# assigned by index, for example dq[1] = z; however, we can not directly slice deques. For example
# dq[1:2], results in TypeError.

# The major advantage of deques over lists is that inserting items at the begining of a deque is much
# faster than inserting items at the begining of a list, although inserting items at the end of a deque
# is very slightly slower than the equivalent operation on a list.
# Deques are thread safe and can be serialized using the `pickle` module.

# A useful way of thinking about deques is in terms of populating and consuming items. Items
# in deques are ussually populated and consumed sequentially from either end.

from collections import deque
import itertools
dq =  deque('abc') # create deque(['a','b','c'])
print(dq)
dq.append('d') # adds the value 'd' to the right
print(dq)
dq.appendleft('z') # adds the value 'z' to the left
print(dq)
dq.extend('efg') # adds multiple items to the right
print(dq)
dq.extendleft('yxw') # adds multiple items to the left
print(dq,end='\n\n')

# We can use pop() and popleft() methods for consuming items in the deque.
print(dq.pop()) # returns and remove an item from the right
print(dq)
print(dq.popleft()) # returns and remove an item from the left
print(dq,end='\n\n')

# We can also use the rotate(n) method to move and rotate all items of n steps
# to the right for positive for positive values of n integer or negative values of
# n steps to the left, using positive integers as the argument.
print("rotate(n) method")
print(dq)
dq.rotate(2) # rotates all items 2 steps to the right
print(dq)
dq.rotate(-2) # rotates all items 2 steps to the left
print(dq,end='\n\n')

# Note that we can use the rotate(n) and pop() methods to delete selected elements.
# Also worth knowing is a simple way to return a slice of deque, as a list.
print('slicing deque')
print(dq)
print(list(itertools.islice(dq,3,9)),end='\n\n')

# The itertools.isslice() method works in the same way that slice works on a list,except
# rather than taking a list for an argument, it takes an iterable and returns selected values,
# by start and stop indeices, as list.

# A useful feature of deque is that they support a `maxlen` optional parameter that restricts the size
# of the deque. This makes it ideally suited to a data structure known as `circular buffer`. This is a fixed-size
# structure that is effectively connected end to end and they are typically used for buffering  data streams.
# The following is a basic example.
dq2 = deque([],maxlen=3)
for i in range(6):
    dq2.append(i)
    print(dq2)
    
# In this example above we are populating from the right and consuming from the left. Notice that
# once the buffer is full the oldest values are consumed first and values are replaced from the right
 
