print("----Zeros----")

import numpy as np
ar_zero=np.zeros(4) # np.zeros is used to create Array filled with Zero
# ar_zero1=np.zeros((3,4))  this line is used to create the dimension we want
print(ar_zero)
#print(ar_zero1)

print("-----Ones------")
ar_one=np.ones(3)
print(ar_one)

print("------Empty------")
ar_emp=np.empty(3)
print(ar_emp)

print("-------RANGE-------")
ar_rng=np.arange(3) # it is same as range function in python. like it give the output which you have taken in the function
print(ar_rng)


print("DIAGONAL")
ar_dia=np.eye(3) # eye function is used to create diagonal elements filled with 1's
print(ar_dia)
ar_dia1=np.eye(3,5)  
print(ar_dia1)