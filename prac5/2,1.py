import pytest


def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr


@pytest.fixture
def unsorted_array():
    return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

@pytest.fixture
def sorted_array():
    return [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_bucketsort(unsorted_array, sorted_array):
    assert bucketsort(unsorted_array, max(unsorted_array)+1) == sorted_array

@pytest.mark.parametrize("unsorted_array, k, expected", [
    ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 10, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]),
    ([0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 11, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
])
def test_bucketsort_parametrized(unsorted_array, k, expected):
    assert bucketsort(unsorted_array, k) == expected