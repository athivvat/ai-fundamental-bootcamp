# How to create a string in Python
# all are equivalent

my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

my_string = """Hello"""
print(my_string)

# format string in Python
name = "Ohm"
print(f"Hello {name}".format(name=name))

# How to access characters in a string?
my_string = "Python programming"

print('my_string[0]', my_string[0])
print('my_string[1]', my_string[1])
print('my_string[2]', my_string[2])

# Index backward
print('len of my_string', len(my_string))
print('my_string[-1]', my_string[len(my_string)-1])
print('my_string[-2]', my_string[len(my_string)-2])

# Slice
print('Slice my_string 2:5', my_string[2:5])

# Slicing 6th to 2nd character
print('my_string[5:-2]', my_string[5:-2])

# String is immutable
my_string = 'Hello'
# my_string[0] = 'a' # Can't immutable

# Delete the entire string
# del my_string

# Iterate through a string
count = 0
for letter in 'Hello world':
    if letter == 'l':
        count += 1

print(count, 'letters found')

# string membership test
print('a' in 'programming')

print('pr' not in 'programming')


# Built-in functions of Python
print('len(my_string) = ', len(my_string))

# enumerate a string
print('list(enumerate(my_string))', list(enumerate(my_string)))


# Escape special symbols
# He said, "What's there?"

print('He said, \"what\'s there?\"')
print('''He said, "what's there?"''')


# Formatting integers
print("Binary representation of {0} is {0:b})".format(12))

# Document string

"""
No install necessary—run the TensorFlow tutorials directly in the browser with Colaboratory, 
a Google research project created to help disseminate machine learning education and research. 

It's a Jupyter notebook environment that requires no setup to use and runs entirely in the cloud.
"""
