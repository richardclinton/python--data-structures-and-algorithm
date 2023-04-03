# Strings are immutable sequence object, with each character representing an element in the sequence.
# Strings, being immutable, do not change the instance; each method simply returns a value.
# String methods
#  1. capitalize => Only first character capitalized, the rest remaining lowercase. 
name = "clinton joseph"
print('capitalize method')
value = name.capitalize() 
print(value) # Clinton joseph

name = 'CLINTON JOSEPH'
value = name.capitalize()
print(value,end='\n\n') # Clinton joseph

# 2. count(substring, [start,end]) => counts occurances of a substring
s = 'Juma Mgunda' 
print('count method')
print(s.count('u')) # 2
print(s.count('u',4,-1),end='\n\n') # 1

# 3. expandtabs([tabsize]) => replaces tabs with spaces.
s = 'Clinton\tJoseph'
print('expandtabs method')
print(s)
print(s.expandtabs())
print(s.expandtabs(2))
print(s.expandtabs(10), end='\n\n')

# 4. endswith(substring, [start, end]) => return TRUE if a string ends with specified substring
s = 'Juma Aweso'
print('endswith method')
print(s.endswith('o')) # True
print(s.endswith('a'), end='\n\n') # False

# 5. find(substring, [start, end]) => Returns index of first presence of a substring.
s = 'abcdabcd'
print('find method')
print(s.find('a')) # 0
print(s.find('a',2), end='\n\n') # 4

# 6. isalnum() => returns True if all characters are alphanumeric of string s. ie a-z and 0-9
s = 'abc12hd'
print('isalnum method')
print(s,s.isalnum()) # True
s = s +'#'
print(s,s.isalnum(), end='\n\n') # False

# 7. isalpha() => returns True if all characters are alphabetic of string s. ie a-z
s = 'abcd'
print('isalpha method')
print(s,s.isalpha()) # True
s = s + '2'
print(s,s.isalpha()) # False
s = 'abcd#'
print(s,s.isalpha(),end='\n\n') # False

# 8. isdigit() => returns True if all characters are digits in the string. ie 0-9
s = '1234'
print('isdigit method')
print(s,s.isdigit()) # True
s = s + 'a'
print(s,s.isdigit()) # False
s = '123*'
print(s,s.isdigit(), end='\n\n') # False

# 9. split([separator],[maxsplit]) => Splits a string separated by white space or an optional seprator.Returns a list.
name = 'Clinton Joseph'
print('split method')
print(name, name.split()) # ['Clinton','Joseph']
s = 'a,b,c,d,e,f'
print(s,s.split(',')) # ['a','b','c','d','e','f']
print(s.split(',',0)) # ['a,b,c,d,e,f']
print(s.split(',',1)) # ['a','b,c,d,e,f']
print(s.split(',',2)) # ['a','b','c,d,e,f']
print(s,s.split(',',3), end='\n\n') # ['a','b','c','d,e,f']

# 10. join(t) => join the string in sequence t.
s = 'abcd'
print('join method')
print(','.join(s), end='\n\n') # 'a,b,c,d'

# 11. lower() => converts the string to all lower case.
s = 'ABCD'
print('lower method')
print(s.lower(), end='\n\n') # 'abcd'

# 12. replace(old,new[maxreplace]) => replaces old substring with a new substring
s = 'abcdabcdabcd'
print('replace method')
print(s.replace('a','1')) # '1bcd1bcd1bcd'
print(s.replace('b','1',1)) # '1bcdabcdabcd'
print(s.replace('a','1',2), end='\n\n') # '1bcd1bcdabcd'

# 13. startwith(substring, [start,end]) => returns True if the string starts with specified substring
s = 'abcdefgh'
print('startwith method')
print(s.startswith('a')) # True
print(s.startswith('b')) # False
print(s.startswith('c',2), end='\n\n') # True

# 14. swapcase() => returns a copy of the string with a swapped case in the string.
name = 'Clinton Joseph'
print('swapped method')
print(name.swapcase(), end='\n\n') # cLINTON jOSEPH

# 15. strip([characters]) => renoves white spaces or optional characters.
name = ' Clinton Joseph'
print('strip method')
print(name,name.strip()) # Clinton Joseph
s = 'abcd'
print(s.strip('d'), end='\n\n') # abc

# 16. lstrip([characters]) => returns a copy of the string with leading characters removed
s = 'abcd'
print('lstrip method')
print(s, s.lstrip()) # abcd
print(s.lstrip('a')) # bcd
print(s.lstrip('b')) # abcd
print(s.lstrip('ab'),end='\n\n') # cd

# Strings, like all sequence types, support indexing and slicing.
# 1. indexing => s[i] 
greet = 'hello world'
print('string indexing')
print(greet[0]) # h
print(greet[1]) # e
print(greet[-1], end='\n\n') # d

# 2. slicing[i:j]
print('string slicing')
print(greet[0:6]) #hello
print(greet[:6]) # hello
print(greet[6:], end='\n\n') #world

# 3. striding[i:j:k]
print('string striding')
print(greet[0:6:2]) # hlo
print(greet[0::2]) # hlowrd








