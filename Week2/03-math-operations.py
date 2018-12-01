"""
TensorFlow math ops are pretty standard, quite similar to NumPy. Visit
https://www.tensorflow.org/api_docs/python/math_ops/arithmetic_operators for more because listing
math ops is boring.
"""

import tensorflow as tf

a = tf.constant([2, 4])
b = tf.constant([3, 6])

ex1 = tf.add(a, b)  # Output: [5 10]
ex2 = tf.add_n([a, b, b])  # Output: [8 16]
ex3 = tf.multiply(a, b)  # Output: [6, 24]
# ex4 = tf.matmul(a, b)
# Output:
# ValueError: Shape must be rank 2 but is rank 0 for 'MatMul' (op: 'MatMul') with input shapes: [], [].

# tf.reshape(a, [1, 2]) = [[2 4]]
# tf.reshape(b, [2, 1]) = [[3] [6]]
ex5 = tf.matmul(tf.reshape(a, shape=[1, 2]), tf.reshape(b, shape=[2, 1]))
# Output: [[30]]
ex6 = tf.div(a, b)  # Divides x / y
# Output: [0 0]
ex7 = tf.mod(a, b)
# Output: [2 4]

# Print session output
with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(ex7))

# close the writer when you're done using it
writer.close()

