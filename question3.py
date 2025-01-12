import numpy as np 
B = np.array ([[1,2],[3,4]])
U,D,Vt=np.linalg.svd(B)
print(U)
print(Vt)
print(D)

B_remark=(U @np.diag(D)@Vt)
print(B_remark)