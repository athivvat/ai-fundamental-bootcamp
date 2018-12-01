import tensorflow as tf
import numpy as np

a = tf.constant(2, name="a")
b = tf.constant(4, name="b")
x = tf.add(a, b, name="add")

# Example 4:
# constant of 1d tensor (vector)
c = tf.constant([2, 2], name="vector")

# constant of 2x2 tensor (matrix)
e = tf.constant([[2, 2], [3, 3]], name="matrix")

# Example 5:
# Create a tensor of shape and all elements are zeros
tf.zeros([2, 3], tf.int32)
# Output: [[0 0 0] [0 0 0]]

# Example 6:
# create a tensor of shape and type (unless type is specified) as the input_tensor
# but all elements are zeros.
input_tensor = [[0, 1], [2, 3], [4, 5]];
ex6 = tf.zeros_like(input_tensor)
# Output: [[0 0] [0 0] [0 0]]

# Example 7:
# create a tensor of shape and all elements are ones
ex7 = tf.ones([2, 3], tf.int32)
# Output: [[1 1 1] [1 1 1]]

# Example 8:
# create a tensor of shape and type (unless type is specified) as the input_tensor
# but all elements are ones.
ex8 = tf.ones_like(input_tensor)
# Output: [[1 1] [1 1] [1 1]]

# Example 9:
# create a tensor filled with a scalar value.
ex9 = tf.fill([2, 3], 8)
# Output: [[8 8 8] [8 8 8]]

# Example 10:
# create a sequence of num evenly-spaced values are generated beginning at start. If
# num > 1, the values in the sequence increase by stop - start / num - 1, so that the
# last one is exactly stop.
# start, stop, num must be scalars
# comparable to but slightly different from numpy.linspace
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
ex10 = tf.linspace(10.0, 13.0, 5, name="linspace")
# Output: [10.0 10.75 11.50 12.25 13.0]

# Example 11:
# create a sequence of numbers that begins at start and extends by increments of
# delta up to but not including limit
# slight different from range in Python
# tf.range(start, limit=None, delta=1, dtype=None, name="range")
ex11_1 = tf.range(1)
# Output: [0]
ex11_2 = tf.range(1, 5)
# Output: [1 2 3 4]
ex11_3 = tf.range(1, 5, 0.5)
# Output: [1.  1.5 2.  2.5 3.  3.5 4.  4.5]

# Example 12:
# Tensor objects are only iterable when eager execution is enabled.
for x in np.linspace(0.0, 10.0, 4):
    print(x)
ex12 = tf.linspace(0.0, 10.0, 4)
# with tf.Session() as session:
#     for x in ex12: # Error: Tensor objects are only iterable when eager execution is enabled.
#         print(session.run(x))

# Example 13:
# Generate random constants from certain distributions.
ex13_1 = tf.random_normal([2, 2], mean=0.0, stddev=1.0, dtype=tf.float32)
# Output: [[-1.1151633 0.15495828] [0.98194677 0.97437686]]

# ex13_2 = tf.truncated_normal([2, 2], mean=0, stddev=1, dtype=tf.int32)
# Output:
# TypeError: Value passed to parameter 'dtype' has DataType int32 not in list of allowed values:
# float16, bfloat16, float32, float64

ex13_3 = tf.truncated_normal([2, 2], mean=0.0, stddev=1.0, dtype=tf.float32)
# Output: [[-1.7611743  -0.5191109] [-0.96332175 -0.60741574]]

ex13_4 = tf.random_uniform([2, 2], minval=0, maxval=None, dtype=tf.float32)
# Output: [[0.28795278 0.680246] [0.566113 0.67732]]

# Random in tensor
ex13_5 = tf.random_shuffle([12, 35, 64, 5, 16])
# Output 1: [64 35 16  5 12]
# Output 2: [64 12 35  5 16]

# Print session output
with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(ex13_5))

"""
# "with" in Python
# Ref: http://effbot.org/zone/python-with-statement.htm

session = tf.Session()
print(session.run(x))
session.close()
"""

# close the writer when you're done using it
writer.close()
