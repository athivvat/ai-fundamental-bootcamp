import array as arr

a = arr.array('d', [1.1, 2.5, 4.5]) # arr.array('Type code', Value)
print(a)

'''
Type code   C Type             Minimum size in bytes 
'b'         signed integer     1 
'B'         unsigned integer   1 
'u'         Unicode character  2 (see note) 
'h'         signed integer     2 
'H'         unsigned integer   2 
'i'         signed integer     2 
'I'         unsigned integer   2 
'l'         signed integer     4 
'L'         unsigned integer   4 
'q'         signed integer     8 (see note) 
'Q'         unsigned integer   8 (see note) 
'f'         floating point     4 
'd'         floating point     8 
'''

# How to access elements in an array
print('First element:', a[0])
print('Second element:', a[1])

print('Last element:', a[-1])

print('3nd to 5tf elemetns', a[2:5])
print('3rd to last emlements', a[2:])

# Append and extend in an array
numbers = arr.array('i', [1, 2, 3])
numbers.append(4)
print(numbers)

numbers.extend([5, 6, 7])
print(numbers)

# Concatenate two arrays using +
odd = arr.array('i', [1, 3, 5, 7])
even = arr.array('i', [2, 4, 6, 8])

numbers = arr.array('i')
numbers = odd + even
print(numbers)

# Delete a specific element
del numbers[2]
print(numbers)

del numbers

# Remove an element in an array
numbers = arr.array('i', [2, 4, 6])
numbers.remove(4)
print(numbers)

# Pop a given index
print(numbers.pop(0))