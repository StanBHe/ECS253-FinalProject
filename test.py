import pandas as pd
import numpy as np
import re

def count_matching_values(array1, array2):
    array1 = np.array(array1)
    array2 = np.array(array2)

    if array1.shape != array2.shape:
        return 0

    matching_count = np.sum(array1 == array2)
    return matching_count

# Example usage
array1 = [1, 0, 1, 0]
array2 = [0, 1, 0, 1]
matching_count = count_matching_values(array1, array2)
print(matching_count)  # Output: 0

array3 = [1, 0, 1, 0]
array4 = [1, 0, 1, 0]
matching_count = count_matching_values(array3, array4)
print(matching_count)  # Output: 4