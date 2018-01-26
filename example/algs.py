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
    assign, cond = 0, 0 # track assignments and conditionals
    swapped = True # variable to determine whether elements in array have been swapped
    assign += 1
    # continue sorting until array is looped through once and no swap is made
    while swapped == True:
        swapped = False
        assign += 1
        # loop through array 
        for i in range(0, len(x)-1):
            cond += 1
            # if elements are unordered swap them
            if x[i] > x[i+1]:
                temp = x[i]
                x[i], x[i+1] = x[i+1], temp
                swapped = True
                assign += 4
    return x, assign, cond

def partition(x, left, right, assign, cond):
    """
    Pivot element is chosen to be the rightmost element in 
    the array. If array element is less than pivot place it before,
    if array element is greater place it after the pivot. 
    """
    pivot = x[right]
    i = left-1
    assign += 2
    for j in range(left, right):
        cond += 1
        if x[j] <= pivot:
            i = i+1
            temp = x[i]
            x[i], x[j] = x[j], temp
            assign += 4
    temp = x[i+1]
    x[i+1], x[right] = x[right], temp
    assign += 3
    return i+1, assign, cond

def quicksort(x, left, right, assign, cond):
    """
    Sort array by partitioning into two subarrays at a pivot element (p),
    then recursively sort the two subarrays.
    """
    # base case
    cond += 1
    if len(x) <= 1:
        return x, assign, cond
    # recursion
    cond += 1
    if left < right:
        p, assign, cond  = partition(x, left, right, assign, cond)
        temp, assign, cond = quicksort(x, left, p-1, assign, cond)
        temp, assign, cond = quicksort(x, p+1, right, assign, cond)
        return x, assign, cond
    return x, assign, cond

