---
url: "https://dev.to/lankinen/neural-network-from-scratch-using-tensorflow-1kc8"
captured_at: "2026-11-16T19:47:37+00:00"
title: "Neural Network from Scratch Using Tensorflow"
domain: "dev-to"
---

[![Cover image for Neural Network from Scratch Using Tensorflow](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fd4lz71xu99ka09x55m23.png)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fd4lz71xu99ka09x55m23.png)

[![Lankinen](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F272848%2F659a5a3d-df4b-46e7-891d-0c3dcc9d0e99.png)](https://dev.to/lankinen)

[Lankinen](https://dev.to/lankinen)

Posted on Apr 17, 2020 Edited on Apr 24, 2020

In this article I show how to build a neural network from scratch. The example is simple and short to make it easier to understand but I haven’t took any shortcuts to hide details.

Looking for PyTorch version of this same tutorial? [Go here.](https://dev.to/lankinen/neural-network-from-scratch-using-pytorch-457k)  

```
import tensorflow as tf
import matplotlib.pyplot as plt
```

Enter fullscreen mode Exit fullscreen mode

First we create some random data. x is just 1-D tensor and the model will predict one value y.  

```
x = tf.Variable([[1.,2.]])
x.shape

CONSOLE: TensorShape([1, 2])

y = 5.
```

Enter fullscreen mode Exit fullscreen mode

The parameters are initialized using normal distribution where mean is 0 and variance 1.  

```
def initalize_parameters(size, variance=1.0):
    return tf.Variable((tf.random.normal(size) * variance))

first_layer_output_size = 3

weights_1 = initalize_parameters((x.shape[1], first_layer_output_size))
weights_1

CONSOLE: <tf.Variable 'Variable:0' shape=(2, 3) dtype=float32, 
          numpy=array([
                [ 0.0535108 ,  1.1256728 ,  0.19349864],
                [-0.8206305 ,  1.8411716 , -0.18347588]],   
                dtype=float32)>

bias_1 = initalize_parameters([1])
bias_1

CONSOLE: <tf.Variable 'Variable:0' shape=(1,) dtype=float32,
          numpy=array([-1.7967013], dtype=float32)>

weights_2 = initalize_parameters((first_layer_output_size,1))
weights_2

CONSOLE: <tf.Variable 'Variable:0' shape=(3, 1) dtype=float32,
          numpy=array([[-0.68191385],
               [-1.3771404 ],
               [-0.59087867]], dtype=float32)>

bias_2 = initalize_parameters([1])
bias_2

CONSOLE: <tf.Variable 'Variable:0' shape=(1,) dtype=float32, 
          numpy=array([-0.93876433], dtype=float32)>
```

Enter fullscreen mode Exit fullscreen mode

The neural network contains two linear functions and one non-linear function between them.  

```
def simple_neural_network(xb):
    # linear (1,2 @ 2,3 = 1,3)
    l1 = xb @ weights_1 + bias_1
    # non-linear
    l2 = tf.math.maximum(l1, tf.Variable([0.]))
    # linear (1,3 @ 3,1 = 1,1)
    l3 = l2 @ weights_2 + bias_2
    return l3
```

Enter fullscreen mode Exit fullscreen mode

Loss function measures how close the predictions are to the real values.  

```
def loss_func(preds, yb):
    # Mean Squared Error (MSE)
    return tf.math.reduce_mean((preds-yb)**2)
```

Enter fullscreen mode Exit fullscreen mode

Learning rate reduces gradient making sure parameters are not changed too much in each step.  

```
lr = tf.constant([10E-4])
```

Enter fullscreen mode Exit fullscreen mode

Training contains three simple steps:

1.  Make prediction
2.  Calculate how good the prediction was compared to the real value (When calculating loss it automatically calculates gradient so we don’t need to think about it)
3.  Update parameters by subtracting gradient times learning rate

The code continues taking steps until the loss is less than or equal to 0.1. Finally it plots the loss change.  

```
losses = []

while(len(losses) == 0 or losses[-1] > 0.1):
    with tf.GradientTape() as tape:
    # 1. predict
        preds = simple_neural_network(x)
        # 2. loss
        loss = loss_func(preds, y)
    dW1, db1, dW2, db2 = tape.gradient(loss, 
                                       [weights_1, bias_1, 
                                        weights_2, bias_2])

    # 3. update parameters
    weights_1.assign_sub(dW1 * lr)
    bias_1.assign_sub(db1 * lr)

    weights_2.assign_sub(dW2 * lr)
    bias_2.assign_sub(db2 * lr)

    losses.append(loss)

plt.plot(list(range(len(losses))), losses)
plt.ylabel('loss (MSE)')
plt.xlabel('steps')
plt.show()
```

Enter fullscreen mode Exit fullscreen mode

[![Loss plot](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fi041pidbsbw6tupnfdic.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fi041pidbsbw6tupnfdic.png)

It changes a lot how many steps it takes to get to loss under 0.1.

[Source Code on Github](https://github.com/RealLankinen/machine-learning-from-scratch/blob/master/neural-network/Tensorflow%20Neural%20Network.ipynb)
