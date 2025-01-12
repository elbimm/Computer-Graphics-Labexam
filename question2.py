# import numpy library 
import numpy as np 
  
# initialize X and Y matrices 
X = np.array([[1,2,3], 
              [2,5,6], 
              ]) 
Y = np.array([[-5, 5,-10], 
              [ 1, 2, 8], 
              ]) 
Z = np.cross(X,Y)
print(Z) 