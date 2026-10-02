#  CREATING AN ARRAY
import numpy as np

x=[1,2,3,4] # by assigning the value to variable
y=np.array([1,2,3,4,5,6]) # by direct in np.array
print(y)
print(y.ndim) # to check which dimension array is


l=[]

for i in range(1,5):
    int_1=int(input("enter:"))
    l.append(int_1)
    
print(np.array(l))



# 2d arraay
ar2=np.array([[7,7,7], [8,8,8]])
print(ar2)
print(ar2.ndim)