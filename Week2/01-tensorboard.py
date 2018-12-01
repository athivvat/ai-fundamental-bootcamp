"""
TensorBoard
1. Visualizing the graph
2. Writing summaries
"""

import tensorflow as tf

a = tf.constant(2, name="a")
b = tf.constant(4, name="b")
x = tf.add(a, b, name="add")

# Print session output
with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(x))

"""
# "with" in Python
# Ref: http://effbot.org/zone/python-with-statement.htm

session = tf.Session()
print(session.run(x))
session.close()
"""

# close the writer when you're done using it
writer.close()
