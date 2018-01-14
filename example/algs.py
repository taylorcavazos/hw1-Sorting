import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(x):
    """
    Sort array by looping through array, swapping unordered 
    adjacent elements until the array is sorted
    """
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(0, len(x)-1):
            if x[i] > x[i+1]:
                temp = x[i]
                x[i], x[i+1] = x[i+1], temp
                swapped = True
    return x

def partition(x, left, right):
    pivot = x[right]
    i = left-1
    for j in range(left, right):
        if x[j] <= pivot:
            i = i+1
            temp = x[i]
            x[i], x[j] = x[j], temp
    temp = x[i+1]
    x[i+1], x[right] = x[right], temp
    return i+1

def quicksort(x, left, right):
    """
    Describe how you are sorting `x`
    """
    if len(x) <= 1:
        return x

    if left < right:
        p = partition(x, left, right)
        quicksort(x, left, p-1)
        quicksort(x, p+1, right)
        return x
