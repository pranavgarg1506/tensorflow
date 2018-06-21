#!/usr/bin/python3

# MAINLY FOR THE LARGE DATA SETS
# karas and pytorch are made upon on the basic model of tensorflow

import tensorflow as tf

# creating constants
x = tf.constant([5])
y = tf.constant([7])

# add two numbers
z = tf.add(x,y)

'''
METHOD 1
# need to create the session to process the data
session = tf.Session()

# run the session
result = session.run(z)
print(result)

# closing the session
session.close()
'''

# METHOD 2
# no need to close the session manually

with tf.Session() as session:
	result = session.run(z)
	print(result)