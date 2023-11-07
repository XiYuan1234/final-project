import numpy as np

arr = [2, 3, 4, 1, 7, 6, 5]


def find_sub_max(arr, n):
    for i in range(n - 1):
        arr_ = arr
        arr_[np.argmax(arr_)] = np.min(arr)
        arr = arr_
    return np.argmax(arr_) + 1


arr.append(9)
print(find_sub_max(arr, 4))
