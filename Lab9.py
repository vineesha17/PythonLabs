import pandas as pd
import numpy as np

# a) 
print("a) Arithmetic operations on two Series")
s1 = pd.Series([10, 20, 30, 40, 50])
s2 = pd.Series([2, 4, 6, 8, 10])

print("Series 1:")
print(s1)
print("Series 2:")
print(s2)

print("Addition:\n", s1 + s2)
print("Subtraction:\n", s1 - s2)
print("Multiplication:\n", s1 * s2)
print("Division:\n", s1 / s2)
print("\n----------------------------------------\n")

# b) 
print("b) Dictionary to Series")
data = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
series_from_dict = pd.Series(data)
print(series_from_dict)
print("\n----------------------------------------\n")

# c)
print("c) Series from list, numpy array, and dict")
list_data = [1, 2, 3, 4, 5]
array_data = np.array([10, 20, 30, 40, 50])
dict_data = {'x': 111, 'y': 222, 'z': 333}

series_from_list = pd.Series(list_data)
series_from_array = pd.Series(array_data)
series_from_dict = pd.Series(dict_data)

print("Series from list:\n", series_from_list)
print("Series from numpy array:\n", series_from_array)
print("Series from dictionary:\n", series_from_dict)
print("\n----------------------------------------\n")

# d) 
print("d) Stack two Series vertically and horizontally")
s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([5, 6, 7, 8])

# Vertically
stacked_vertical = pd.concat([s1, s2])

# Horizontally 
stacked_horizontal = pd.concat([s1, s2], axis=1)
stacked_horizontal.columns = ['s1', 's2'] 

print("Vertical stacking:\n", stacked_vertical)
print("\nHorizontal stacking:\n", stacked_horizontal)
