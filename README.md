# Neural-Network
implement of a Self Organizing Map neural network.
input data size is (m,n) where m is the number of training examples and n is the number of features in each example.First, it initializes the weights of size (n, C) where C is the number of clusters. Then iterating over the input data, for each training example, it updates the winning vector (weight vector with the shortest distance) from training example). Weight updation rule is given by : 
wij = wij(old) + alpha(t) *  (xik - wij(old))
where alpha is a learning rate at time t, j denotes the winning vector, i denotes the ith feature of training example and k denotes the kth training example from the input data. After training the SOM network, trained weights are used for clustering new examples. A new example falls in the cluster of winning vectors. 
