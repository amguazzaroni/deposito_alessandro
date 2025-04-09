import numpy as np

arr = np.random.randint(10,50,20)
arr1 = arr[:10]
arr2 = arr[-5:]
arr3 = arr[5:15] 
arr4 = arr[0:20:3]

print(arr1)
print(arr2)
print(arr3)
print(arr4)
