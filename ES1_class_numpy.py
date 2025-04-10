import numpy as np

class Array:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        
    def create_equidistant_array(self):
        arr = np.linspace(0, 1, self.rows * self.cols)
        self.equidistant_array = arr.reshape(self.rows, self.cols)

    def create_random_array(self):
        self.random_array = np.random.rand(self.rows, self.cols)

    def compute_sum(self):
        self.sum_matrix = self.equidistant_array + self.random_array

    def print_matrices(self):
        print("Equidistant Array:")
        print(self.equidistant_array)
        print("Random Array:")
        print(self.random_array)
        print("Sum Matrix:")
        print(self.sum_matrix)

# Uso della classe
processor = Array(rows=3, cols=4)
processor.create_equidistant_array()
processor.create_random_array()
processor.compute_sum()
processor.print_matrices()
