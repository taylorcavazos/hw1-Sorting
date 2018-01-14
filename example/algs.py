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

def quicksort(x):
    """
    Describe how you are sorting `x`
    """

    assert 1 == 1
    return

