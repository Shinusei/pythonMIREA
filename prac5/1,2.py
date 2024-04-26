import random
import unittest

def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr

def test_bucketsort():
    # Test empty array
    assert bucketsort([], 10) == []

    # Test array with one element
    assert bucketsort([5], 10) == [5]

    # Test array with multiple elements
    assert bucketsort([3, 1, 5, 2, 4], 6) == [1, 2, 3, 4, 5]

    # Test array with duplicate elements
    assert bucketsort([3, 1, 5, 2, 4, 1, 3, 2], 6) == [1, 1, 2, 2, 3, 3, 4, 5]

    # Test array with all elements equal
    assert bucketsort([2, 2, 2, 2, 2], 3) == [2, 2, 2, 2, 2]

    # Test array with negative elements
    assert bucketsort([-3, -1, -5, -2, -4], 5) == [-5, -4, -3, -2, -1]

    # Test array with mixed positive and negative elements
    assert bucketsort([-3, 1, -5, 2, -4], 7) == [-5, -4, -3, 1, 2]

    # Test array with zero elements
    assert bucketsort([0, 0, 0, 0, 0], 1) == [0, 0, 0, 0, 0]

    # Test large array with random elements
    random_arr = [random.randint(0, 100) for _ in range(1000)]
    assert bucketsort(random_arr, 101) == sorted(random_arr)

    print("All tests passed!")

test_bucketsort()