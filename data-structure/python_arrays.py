# The `array` module defines a data type array that is similar to the list data type
# except fot the constraint that their contents must be of a single type of the
# underlying representation, as is determined by the machine architecture or underlying
# C implementation.
# The type of `array` is determined at creation time and it is indicated by one of the
# following type codes.
# 1. Code => 'b' C type => signedchar Python type => int Minimum bytes => 1
# 2. Code => 'B' C type => unsignedchar Python type => int Minimum bytes => 1
# 3. Code => 'u' C type => Py_UNICODE Python type => Unicodecharacter Minimum bytes => 2
# 4. Code => 'h' C type => sigleshort Python type => int Minimum bytes => 2
# 5. Code => 'H' C type => unsignedshort Python type => int Minimum bytes => 2
# 6. Code => 'i' C type => signedint Python type => int Minimum bytes => 2
# 7. Code => 'I' C type => unsignedint Python type => int Minimum bytes => 2
# 8. Code => 'l' C type => signedlong Python type => int Minimum bytes => 4
# 9. Code => 'L' C type => unsignedlong Python type => int Minimum bytes => 8
# 10. Code => 'q' C type => signedlonglong Python type => int Minimum bytes => 8
# 11. Code => 'Q' C type => unsignedlonglong Python type => int Minimum bytes => 8
# 12. Code => 'f' C type => float Python type => float Minimum bytes => 4
# 13. Code => 'd' C type => double Python type => double Minimum bytes => 8

# The `array` objects supports methods and attributes.
# 1. a.itemsize => The size of one array item in bytes.
# 2. a.append(x) => Appends an x element at the end of `a` array
# 3. a.buffer_into() => Returns a tuple containing the current memory location and length of the buffer used to store the array
# 4. a.byteswarp() => Swarps the byte order of each item in `a` array
# 5. a.count(x) => Returns the occurrences of x in array `a`
# 6. a.extend(b) => Appends all the elements from iterable `b` at the end of `a` array
# 7. a.frombytes(s) => Appends elements from an `s` string, where the string is an array of machine values
# 8. a.fromfile(a,f) => Read `n` machine values from the file and append them at the end of the array
# 9. a.fromlist(l) => Appends all of the elements from the `l` list to the array
# 10. a.fromunicode(s) => Extends an array of `u` type with the Unicode string,`s`.
# 11. index(x) => Returns the first (smallest) index of the x element.
# 12. a.insert(i,x) => Inserts an item of which the value is x, in the array at i index position.
# 13. a.pop([i]) => Returns the item at index, i, and remove it from the array
# 14. a.remove(x) => Removes the first occurence of the x item from the array
# 15. a.reverse() => Reverses the order of items in the `a` array.
# 16. a.tofile(f) => Writes all the element to the f file object
# 17. a.tolist() => Converts the array into list.
# 18. a.tounicode() => Converts an array of the `u` type into a unicode string

# Array objects support all of the normal sequence oparations such as indexing, slicing,
# concatenation and multiplication.

# Using arrays, as opposed to lists, is much more efficient way of storing data that
# is of the same type. In the following example, we have created an interger array from 0
# to one million minus 1, and an identical list. String one million integers in an integer array
# requires around 90% of the memory of an equivalent list.

import array
import sys
ba = array.array('i', range(10**6))
bl = list(range(10**6))
my_size = 100*sys.getsizeof(ba)/sys.getsizeof(bl)
print(my_size, end='\n\n')

# Because we are interested in saving space, that is, we are dealing with large
# datasets and limited memory size, we ussuanly perform in-place operations on arrays
# and only creates copies when we need to.
# Typically, enumarate is used to perform an operation on each element. In the following 
# snippet, we perform the simple operation of adding one to each item in the array.

# It should be noted that when performing operations on arrays that creates lists, such as
# list comprehension, the memory efficiency gains of using an array in the first place
# will be negated. When we need to create a new data object, a solution is to use generator
# expression to perform the operation.

# Arrays created with this module are unsuitable for work that requires a matrix of vector
# operations
