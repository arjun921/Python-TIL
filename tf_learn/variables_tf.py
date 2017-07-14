import time
import tensorflow as tf

start_time = time.clock()
#x = tf.constant(1234567890, name='x')
#z = 1
#for i in range(10000):
#        z = tf.Variable(x+z, name='z')

x = tf.constant(35, name='x')
y = tf.Variable(x + 5, name='y')
model = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(model)
    print(session.run(y))

end_time = start_time - time.clock()
print("Finished in :{} Seconds".format(end_time))
