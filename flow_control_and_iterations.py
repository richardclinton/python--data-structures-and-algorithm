# Conditional statement
x = 'one'

if x == 0:
    print('False')
elif x == 1:
    print('True')
else:
    print('Something else')
    
# Loops
# 1. while => repeat executing statement until a boolean condition is True
x = 0
while x < 3:
    print(x)
    x += 1
    
# 2. for => provides a way of repating execution into the loop through a series of elements.
words = ['cat','dog','elephant']
for w in words:
    print(w)