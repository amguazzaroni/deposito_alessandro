import numpy as np

#array di numeri equidistanti tra un v_i e v_f
arr = np.linspace(0,1,5)
print(arr)

#matrice 3x3 con valori casuali tra 0 e 1
random_arr = np.random.rand(3,3)
print(random_arr)

#operazioni matematiche/statistica base
arr1 = np.array([1,2,3,4,5])

sum_value=np.sum(arr1)
mean_value=np.mean(arr1)
std_value=np.std(arr1)

print("sum: ",sum_value)
print("mean: ", mean_value)
print("standar deviation: ",std_value)
