import numpy as np

arr = np.arange(10,50)
print(arr)
print(arr.dtype)
arr_ft= arr.astype('float64') #ho utilizzato il metodo .astype
arr_ft1 = np.array(arr,dtype='float64') #impongo con dtype
print(arr_ft)
print(arr_ft.dtype)
print(arr_ft1.dtype)
