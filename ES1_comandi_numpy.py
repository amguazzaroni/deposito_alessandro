import numpy as np

arr= np.linspace(0,1,12) #creazione array equidistante
arr_reshaped = arr.reshape(3,4) #reshape array precedente in 3x4

random_arr= np.random.rand(3,4) #creazione 
sum_matrix  = arr_reshaped+random_arr
print(sum_matrix)

