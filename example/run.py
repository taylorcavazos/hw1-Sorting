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

    print("Bubble sort output: ", bubblesort(x)[0])
    print("Quick sort output: ", quicksort(x, 0, len(x)-1, 0, 0)[0])

    """
    Plot time complexities for bubble and quick sort
    """
    time_bubble,time_quick = [],[] # arrays to track times
    cond_bubble, cond_quick = [],[] # arrays to track num conds
    assign_bubble, assign_quick = [],[] # arrays to track num assigns
    # Loop through different sized arrays
    for s in np.arange(100, 1100, 100):
        # Track variables for each size
        bubble, quick = np.array([]), np.array([])
        b_c, q_c = np.array([]), np.array([])
        b_a, q_a = np.array([]), np.array([])
        # For each size of array compute 100 times
        for i in range(100):
            x = np.random.rand(s) # random array of size s
            # Run bubble sort and record outputs
            start_b = time.time() 
            arr,a,c = bubblesort(x)
            bubble=np.append(bubble,time.time()-start_b)
            b_a, b_c = np.append(b_a, a), np.append(b_c, c)
            # Run quick sort and record outputs
            start_q = time.time()
            arr,a,c = quicksort(x, 0, len(x)-1,0,0)
            quick=np.append(quick, time.time()-start_q)
            q_a, q_c = np.append(q_a, a), np.append(q_c, c)
        # Calculate mean of outputs over 100 random arrays
        time_bubble.append(np.mean(bubble))
        time_quick.append(np.mean(quick))
        cond_bubble.append(np.mean(b_c))
        assign_bubble.append(np.mean(b_a))
        cond_quick.append(np.mean(q_c))
        assign_quick.append(np.mean(q_a))
    
    # Plot time taken for each array of size s for quicksort and bubblesort
    plt.plot(np.arange(100, 1100, 100), time_bubble, label = "BubbleSort: O(n2)", color = "green")
    plt.plot(np.arange(100,1100,100), time_quick, label = "Quicksort: O(nlog(n))", color = "blue")
    plt.title("Time Complexity")
    plt.xlabel("Size")
    plt.ylabel("Time")
    plt.legend()
    plt.savefig("/Users/student/Desktop/alg_time.png", type = "png")
    plt.close()

    # Plot number of conditionals and assignments of array size s for quicksort and bubblesort
    plt.plot(np.arange(100,1100, 100), cond_bubble, label = "# conditions", color = "green")
    plt.plot(np.arange(100,1100,100), assign_bubble, label = "# assignments", color = "green", ls = "--" )
    plt.title("Number of Conditions and Assignments for BubbleSort")
    plt.xlabel("Size")
    plt.ylabel("Count")
    plt.legend()
    plt.savefig("/Users/student/Desktop/alg_counts_b.png", type = "png")
    plt.close()

    plt.plot(np.arange(100,1100, 100), cond_quick, label = "# conditions", color = "blue")
    plt.plot(np.arange(100,1100,100), assign_quick, label = "# assignments", color = "blue", ls = "--" )
    plt.title("Number of Conditions and Assignments for Quicksort")
    plt.xlabel("Size")
    plt.ylabel("Count")
    plt.legend()
    plt.savefig("/Users/student/Desktop/alg_counts_q.png", type = "png")
    plt.close()

