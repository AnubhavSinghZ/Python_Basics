#  CREATING AN ARRAY
import numpy as np

x=[1,2,3,4] # by assigning the value to variable
y=np.array([1,2,3,4,5,6]) # by direct in np.array
print(y)


l=[]
for i in range(1,5):
    int_1=int(input("enter:"))
    l.append(int_1)
print(np.array(l))