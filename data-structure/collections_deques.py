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