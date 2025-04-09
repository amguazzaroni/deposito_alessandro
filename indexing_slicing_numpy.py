import numpy as np

arr = np.array([1,2,3,4,5])

#indexing
print(arr[0])

#slicing
print(arr[1:3])

#boolean indexing (vede sia valori che indici)
print(arr[arr>2])

arr_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

#slicing su righe
print(arr_2d[1:3])

#slicing su colonne
print(arr_2d[:,1:3])

#slicing misto
print(arr_2d[1:,1:3])
