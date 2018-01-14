# You can do all of this in the `__main__.py` file, but this file exists
# to shows how to do relative import functions from another python file in
# the same directory as this one.
import numpy as np
import time
import matplotlib.pyplot as plt
import sys
from .algs import quicksort, bubblesort

def run_stuff():
    sys.setrecursionlimit(1500)
    """
    This function is called in `__main__.py`
    """
    print("This is `run()` from ", __file__)

    x = np.random.rand(10)
    print("Unsorted input: ", x)

    print("Bubble sort output: ", bubblesort(x))
    print("Quick sort output: ", quicksort(x, 0, len(x)-1))

    """
    Plot time complexities for bubble and quick sort
    """
    time_bubble,time_quick = [],[]
    for s in np.arange(100, 1100, 100):
        bubble, quick = np.array([]), np.array([])
        for i in range(100):
            x = np.random.rand(s)
            start_b = time.time()
            bubblesort(x)
            bubble=np.append(bubble,time.time()-start_b)
            start_q = time.time()
            quicksort(x, 0, len(x)-1)
            quick=np.append(quick, time.time()-start_q)
        time_bubble.append(np.mean(bubble))
        time_quick.append(np.mean(quick))
    
    plt.plot(np.arange(100, 1100, 100), time_bubble, label = "BubbleSort: O(n2)", color = "green")
    plt.plot(np.arange(100,1100,100), time_quick, label = "Quicksort: O(nlog(n))", color = "blue")
    plt.title("Time Complexity")
    plt.xlabel("Size")
    plt.ylabel("Time")
    plt.legend()
    plt.savefig("/Users/student/Desktop/alg_time.png", type = "png")
    plt.close()
