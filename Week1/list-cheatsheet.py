# Empty list
list1 = []

list1 = ['mouse', [2, 4, 6], ['a']]
print(list1)

# How to access elements in list
list2 = ['p', 'r', 'o', 'b', 'l','e','m']
print(list2)

list1 = ['mouse', [2, 4, 6], ['a']]
print(list1[1][1])

# Slicing in a list
list2 = ['p', 'r', 'o', 'b', 'l','e','m']
print(list2[:-5])

# List is mutable !!!
even = [2, 4, 6, 8]
even[0] = 0

print(even)

odd = [2, 4, 6, 8]
odd[1:4] = [3, 5, 7]
print(odd)

# Append and extend ca be also done in list
odd.append(9)
print(odd)

odd.extend([11, 13])
print(odd)

# Insert an element into a list
odd = [1, 9]
odd.insert(1, 3)
print(odd)

odd[2:2] = [5, 7]
print(odd)

# How to delete or remove elements from a list?
del odd[0]
print(odd)

del odd

odd = [1, 3, 5, 7, 9]
print(odd)
odd.remove(1)
print(odd)

# Clear
odd.clear()
print(odd)

odd = [3, 5, 9, 1, 7]
print(odd)
odd.sort()
print(odd)

# An elegant way to create a list
pow2 = [2 ** x for x in range(10)]
print(pow2)

# Membership in list
print(2 in pow2)
print(2 not in pow2)

# Iterate through in a list
for fruit in ['apple', 'banana', 'orage']:
    print("I like ", fruit)
