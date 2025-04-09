import numpy as np #qualsiasi import sempre prima riga (prime righe per più import)

#creazione di un array unidimensionale
arr = np.array([1,2,3,4,5]) #è un metodo e la classe è numpy
print(arr)

#creazione di un array bidimensionale
arr2d= np.array([[1,2,3],[4,5,6]])
print(arr2d)

# Utilizzo di alcuni metodi
print("Forma dell'array:", arr.shape)  # Output: (5,)
print("Dimensioni dell'array:", arr.ndim)  # Output: 1
print("Tipo di dati:", arr.dtype)  # Output: int64 (varia a seconda della piattaforma)
print("Numero di elementi:", arr.size)  # Output: 5
print("Somma degli elementi:", arr.sum())  # Output: 15
print("Media degli elementi:", arr.mean())  # Output: 3.0
print("Valore massimo:", arr.max())  # Output: 5
print("Indice del valore massimo:", arr.argmax())  # Output: 4

#crea array contenente una sequenza di numeri (simile a range)
arr1=np.arange(10)
print(arr1)

#cambia la forma senza modificarne i dati
reshaped_arr1 = arr1.reshape((2,5))
print(reshaped_arr1)
