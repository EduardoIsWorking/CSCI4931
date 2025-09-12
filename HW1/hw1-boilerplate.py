import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# The Given Small Dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([[0], [1], [1], [1]])

# Sigmoid Activation Function
def sigmoid(x):
    '''
    This function actually compute sigmoid over input, x

    Inputs: 
        x: input data
    Returns:
        returns sigmoid of x
    '''
    return 1 / (1 + np.exp(-x))


# Initialize weights for visualization
# Please note the dimensions and data types of both weights between input and hidden layer, and
#  between hidden layer and output layer
np.random.seed(42)
hidden_size = 2
input_size = 2
output_size = 1

W1 = np.random.randn(input_size, hidden_size) * 0.01
b1 = np.zeros((1, hidden_size))
W2 = np.random.randn(hidden_size, output_size) * 0.01
b2 = np.zeros((1, output_size))


# Forward Propagation (for visualization)
def forward_propagation(X, W1, b1, W2, b2):
    '''
    This function computes forward propagation of the input X through the network.
    Inputs:
        X: input,
        W1: weights between input and hidden layer
        b1: bias weights between input and hidden layer.
        W2: weights between hidden layer and output layer
        b2: bias weights between hidden layer and output layer.

    Returns:
        Z1: net weighted sum at hidden layer neurons
        A1: activated outputs by the hidden layer neurons
        Z2: net weighted sum at output layer neuron
        A2: activated output by the output layer neuron.
    '''
    n = X.shape[0] #num of samples

    Z1 = np.zeros((n,hidden_size))
    A1 = np.zeros((n,hidden_size))
    Z2 = np.zeros((n,output_size))
    A2 = np.zeros((n,output_size))

    #@TODO: Your code begins here...
    




    return Z1, A1, Z2, A2

def backward(Z1, A1, Z2, A2, Y):
    '''
    This function computes derivatives of the error, E with respect to all the weights given the predicted outputs from a forward pass and 
      the corresponding target outputs.
    
    Inputs: 
        Z1: net weighted sum at hidden layer neurons
        A1: activated outputs by the hidden layer neurons
        Z2: net weighted sum at output layer neuron
        A2: activated output by the output layer neuron.
        Y: the target/ground true outputs for the inputs.
    
    Returns:
        dW1: derivative of error, E with respect to W1
        db1: derivative of error, E with respect to b1
        dW2: derivative of error, E with respect to W2
        db2: derivative of error, E with respect to b2
    '''
    m = X.shape[1] #number of features per sample

    dW1 = np.zeros((m,hidden_size))
    db1 = np.zeros((m,hidden_size))
    dW2 = np.zeros((m,output_size))
    db2 = np.zeros((m,output_size))
    

    #@TODO: Your code begins here...
    





    return dW1, db1, dW2, db2


def update_weights(W1, b1, W2, b2, dW1, db1, dW2, db2):
    '''
    This function updates given weights based on the derivatives of the error with respect to each weights. This is part of the gradient descent based optimization.

    Inputs:
        W1: weights between input and hidden layer
        b1: bias weights between input and hidden layer.
        W2: weights between hidden layer and output layer
        b2: bias weights between hidden layer and output layer.
        dW1: derivative of error, E with respect to W1
        db1: derivative of error, E with respect to b1
        dW2: derivative of error, E with respect to W2
        db2: derivative of error, E with respect to b2

    Returns:
        W1: updated weights between input and hidden layer
        b1: updated bias weights between input and hidden layer.
        W2: updated weights between hidden layer and output layer
        b2: updated bias weights between hidden layer and output layer.

    '''
    #@TODO: Your code begins here...

    


    return W1, b1, W2, b2

# The training loop for visualization
learning_rate = 0.1
epochs = 10000

for epoch in tqdm(range(epochs)):
    # Forward propagation
    Z1, A1, Z2, A2 = forward_propagation(X, W1, b1, W2, b2)
    
    # Backward propagation
    dW1, db1, dW2, db2 = backward(Z1, A1, Z2, A2, Y)

    # Update parameters
    W1, b1, W2, b2 = update_weights(W1, b1, W2, b2, dW1, db1, dW2, db2)
    

# Generate a grid of points to visualize decision boundary
x1 = np.linspace(-0.5, 1.5, 100)
x2 = np.linspace(-0.5, 1.5, 100)
xx1, xx2 = np.meshgrid(x1, x2)
grid = np.c_[xx1.ravel(), xx2.ravel()]

# Predict on the grid
_, _, _, Y_pred = forward_propagation(grid, W1, b1, W2, b2)
Y_pred = Y_pred.reshape(xx1.shape)

# Plot decision boundary
plt.figure(figsize=(8, 6))
plt.contourf(xx1, xx2, Y_pred, levels=[0, 0.5, 1], alpha=0.6, cmap="coolwarm")
plt.scatter(X[:, 0], X[:, 1], c=Y.ravel(), edgecolors="k", cmap="coolwarm", s=100)
plt.title("Decision Boundary for the Small Data Problem")
plt.xlabel("x1")
plt.ylabel("x2")
plt.colorbar(label="Prediction Confidence")
plt.show()


# @TODO: Please draw epoch-loss plot here...

