import numpy as np
from example import algs

def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    w, x, y, z = np.array([1,2,4,0,1]), np.array([]), np.array([0]), np.array([2,1,0,-1,-2])
    
    assert np.array_equal(algs.bubblesort(w), sorted(w))
    assert np.array_equal(algs.bubblesort(x), sorted(x))
    assert np.array_equal(algs.bubblesort(y), sorted(y))
    assert np.array_equal(algs.bubblesort(z), sorted(z))

def test_quicksort():
    w, x, y, z = np.array([1,2,4,0,1]), np.array([]), np.array([0]), np.array([2,1,0,-1,-2])
    assert np.array_equal(algs.quicksort(w, 0, len(w)-1), sorted(w))
    assert np.array_equal(algs.quicksort(x, 0, len(x)-1), sorted(x))
    assert np.array_equal(algs.quicksort(y, 0, len(y)-1), sorted(y))
    assert np.array_equal(algs.quicksort(z, 0, len(z)-1), sorted(z))
