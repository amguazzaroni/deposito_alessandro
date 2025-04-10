import numpy as np

#definisco classe
class Array: 
    #costruttore con parametro size
    def __init__(self, size): 
        self.size = size

    #metodo per generare array linspace random.rand
    def generatore_arrays(self): 
        self.linspace_array = np.linspace(0, 10, self.size)
        self.random_array = np.random.rand(self.size)

    #metodo per somma di elemento per elemento (genera un altro array)
    def sum_elemento(self):
        self.sum_array = self.linspace_array + self.random_array

    #metodo somma totale su tutti elementi
    def total_sum(self):
        return np.sum(self.sum_array)

    #metodo somma totale su tutti elementi > 5
    def sum_maggiore_5(self):
        return np.sum(self.sum_array[self.sum_array > 5])

    #metodo stampa per print di tutto 
    def stampa(self):
        print("Array linspace:")
        print(self.linspace_array)
        print("Array random:")
        print(self.random_array)
        print("Array somma:")
        print(self.sum_array)
        print("Somma totale:", self.total_sum())
        print("Somma dei valori > 5:", self.sum_maggiore_5())

#creazione oggetto
oggetto = Array(50)
#chiamata metodi
oggetto.generatore_arrays()
oggetto.sum_elemento()
oggetto.stampa()
