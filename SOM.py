
""" self organization map neural network"""

import math

class SOM:
    """ Function here computes the winning vector
    by Euclidean distance"""
    def winner(self, weights, sample):
        D0 = 0
        D1 = 0
        for i in range(len(sample)):
             D0 += math.pow((sample[i] - weights[0][i]),2)
             D1 += math.pow((sample[i] - weights[1][i]),2)
             if D0 > D1 :
                 return 0
             else:
                 return 1
    def update(self, weights, sample, J , alpha):
        """update the winning vector"""
        for i in range(len(weights)):
            weights[J][i] += +alpha * (sample[i]-weights[J][i])
        return weights
    
def main():
    """driver code"""
    #training examples=(m,n)
    T = [[1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1]]
    m, n = len(T), len(T[0])
    #weight initialization n, C
    weights = [[0.2, 0.6, 0.5, 0.9], [0.8, 0.4, 0.7, 0.3]]
    #training
    ob = SOM()
    epochs = 3
    alpha = 0.5
    for i in range(epochs):
        for j in range(m):
        #training sample
            sample = T[j]
            #compute winner vector
            J = ob.winner(weights,sample)
            #update winning vector
            weights = ob.update(weights, sample, J, alpha)
# classify test sample
    s = [0, 0, 0, 1]
    J = ob.winner(weights, s)
 
    print("Test Sample s belongs to Cluster : ", J)
    print("Trained weights : ", weights)
 
 
if __name__ == "__main__":
    main()
    