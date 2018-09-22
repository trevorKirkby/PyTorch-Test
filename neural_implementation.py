#
# A basic neural network implementation written in numpy. Because I would prefer to understand how it works before using a library to do it.
# (also beause numpy arrays and torch tensors are largely compatible)
# Largely a product of this excellent explanation of how a basic neural net works: https://iamtrask.github.io/2015/07/12/basic-python-network/
#

import numpy as np

INPUT_SIZE = 10
EXAMPLE_COUNT = 100
LAYERS = 3
ITERS = 100000

def sigmoid(x, deriv=False):
	if deriv:
		return x * (x-1)
	return 1 / 1 + np.exp(-x)

def relu(x, deriv=False):
	if deriv:
		return 1 * (x > 0)
	return x * (x > 0)

np.random.seed(2)
data = np.random.randint(10,size=(EXAMPLE_COUNT, INPUT_SIZE)) #A bunch of randomly generated data.
out = data.min(axis=1) #Learning to take the minimum.
synapses = np.random.rand(LAYERS-1, INPUT_SIZE) #TODO: Allow a more complex shape control, ex 3:4-4:2-2:1

for i in xrange(ITERS):
	layers = np.zeros((LAYERS, EXAMPLE_COUNT))
	layers[0] = data
	for l in xrange(LAYERS-1):
		layers[l+1] = sigmoid(np.dot(layers[l], synapse[l+1]))
	for l in xrange(LAYERS-1, 0, -1):
		synapse[l]
