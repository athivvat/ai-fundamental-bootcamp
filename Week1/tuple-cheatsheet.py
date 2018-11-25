"""
- By convention, we generally use tuple for different datatypes
and list for similar datatypes
- Since tuple are immutable, then iterating through tuple
is faster than with list !!!
- Tuples that contain immutable elements can be used as key for a
dictionary. With list, this is NOT possible.
- If you have data that doesn't change, implementing
it as tuple will GUARANTEE that it remains write-protected
"""

# Empty tuple
tuple1 = ()
print(tuple1)

# Tuple containing integers
tuple1 = (1, 2, 3)
print(tuple1)

# Tuple with mixed datatuypes
tuple1 = (1, "Hello", 3.4)
print(tuple1)

# Nested tuple
tuple1 = ('mouse', [8, 4, 5], (1, 2, 3))
print(tuple1)

# How to check 'type' in Python
print(type(tuple1))

# Creating a tuple is not necessary to use '()'
tuple2 = 1, 2, 3
print(tuple2)
print(type(tuple2))

# Creating a tuple with one element
tuple3 = (1, )
print(tuple3)
print(type(tuple3))

# or without '()'
tuple4 = 1,
print(tuple4)
print(type(tuple4))