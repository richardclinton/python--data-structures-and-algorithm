# Lists can store any number of different data types. They are simple representations
# of objects and are indexed by integers starting from zero.
# List methods
# 1. list(s) => returns list of sequence s.
s = 'abcd'
print('list method')
print(list(s), end='\n\n') # ['a','b','c','d']

# 2. s.append(x) => append element x at the end of the s.
s = ['a','b']
print('append method')
s.append('c')
print(s, end='\n\n') # ['a','b','c']

# 3. s.extend(x) => appends list x at the end of list s.
s = ['a','b']
x = ['c','d']
print('extend method')
s.extend(x)
print(s, end='\n\n') #['a','b','c','d']

# 4. s.count(x) => returns count occuence of  x in list s
s = [1,2,4,3,2,5,6,6,7,3,9]
print('count method')
print(s.count(2)) # 2
print(s.count(1)) # 1
print(s.count(3),end='\n\n') # 2

# 5 s.index(x, [start,end]) => returns the smallets index i, where s[i] == x.
s = [1,2,3,4,2,1]
print('index method')
print(s.index(2)) # 1
print(s.index(2,2),end='\n\n') # 4

# 6. s.insert(i, x) => insert x at index i
s = [2,4,6]
print('insert method')
s.insert(0,1)
print(s) # [1,2,4,6]
s.insert(2,3) 
print(s) # [1,2,3,4,6]
s.insert(4,5)
print(s,end='\n\n') # [1,2,3,4,5,6]

# 7. s.pop(i) => returns the element at index i and removes it from the list s.
s = [1,2,3,4,5]
print('pop method')
x = s.pop(3)
print(s,x,end='\n\n') # [1,2,3,5],4

# 8. s.remove(x) => removes element x from the list s.
s = [1,2,3,4]
print('remove method')
s.remove(4)
print(s) # [1,2,3]
s.remove(3)
print(s,end='\n\n') # [1,2]

# 9. s.reverse() => reverse the order of list s.
s = [1,3,5,4,2]
print('reverse method')
s.reverse()
print(s,end='\n\n') # [2,4,5,3,1]

# 10. s.sort(key, [reverse]) => sort list s with optional key and reverse it.
s = [1,3,5,4,2]
print('sort method')
s.sort()
print(s) # [1,2,3,4,5]
s.sort(reverse=True)
print(s) # [5,4,3,2,1]
fruit = ['mango','apple','banana','ovacado','pawpaw']
fruit.sort()
print(fruit) # ['apple','banana','mango','ovacado','pawpaw']
def my_func(e):
    return len(e)
fruit.sort(key=my_func)
print(fruit,end='\n\n') # ['apple','mango','banana','pawpaw','ovacado']

# In python list implementation is different compared to other languages.
# Python does not create multiple copies of variable. Fore xample, when we assign a value
# of one variable in another variable, both variables point to the same memory address where
# the value is stored. A copy would only be allocated if the variable changes their values.
# This feature makes python memory efficient, in the sense that it only creates multiple copies 
# when it is required.
x = 1; y = 2; z = 3
list1 = [x,y,z]
list2 = list1
print(list1,list2)
list2[1] = 4
print(list1,list2)