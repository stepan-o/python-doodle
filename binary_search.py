##########################################################################################################
#                                                                                                        #
#          Recursive implementation of a binary search algorithm on a sorted array in Python             #
#                                                                                                        #
#                   Algorithm steps:                                                                     #
#             1. Compare x to the middle element m of a sorted array N                                   #
#             2. If x matches m, return m's index                                                        #
#             3. Else:                                                                                   #
#                   3a: If x is greater than m, recur for sub-array [m:end_of_N]                         #
#                   3b: If x is less than m, recur for sub-array [start_of_N:m]                          #
#                                                                                                        #
##########################################################################################################
from time import time


def binary_search_rec(array, target, iteration_=0, start_idx_=0, verbose=False):
    """
    ignore half of the elements after one comparison
    :param iteration_: int

    :param array:
        sorted array
    :param target:
        element to find in the sorted array
    :param iteration_: int
        current iteration of the search algorithm
    :param start_idx_: int
        starting index after discarding elements
    :param verbose: Boolean
        print details of each iteration
    :return: -1
                    if target is not found in array
             start idx + mid_idx: int
                    if target found, index of target in array
             iteration_: int
                    total number of iterations
    """
    mid_idx = len(array) // 2
    if verbose:
        print("Iteration {0}: Length of array to search: {1}, comparing element at index {2} to target..."
              .format(iteration_, len(array), mid_idx))
    iteration_ += 1
    if array[mid_idx] == target:
        # if middle element is target, return index of middle element
        return start_idx_ + mid_idx, iteration_
    elif len(array) == 1:
        # if middle element is not target and only 1 element left, return -1 (not found)
        return -1, iteration_
    elif x >= array[mid_idx]:
        # if more than 1 element left and target is greater than middle, discard lower half
        start_idx_ = start_idx_ + mid_idx
        return binary_search_rec(array[mid_idx:], target, start_idx_=start_idx_, verbose=verbose, iteration_=iteration_)
    else:
        # if more than 1 element left and target is less than middle, discard upper half
        return binary_search_rec(array[:mid_idx], target, start_idx_=start_idx_, verbose=verbose, iteration_=iteration_)


N = [2, 3, 4, 10, 40]
x = 40

t = time()
target_idx, iteration = binary_search_rec(N, x, verbose=True)
elapsed = time() - t
if target_idx == -1:
    print("Search completed in {0} steps, took {1} seconds. Element {2} not found in array {3}"
          .format(iteration, elapsed, x, N))
else:
    print("Search completed in {0} steps, took {1:.7f} seconds. Target element x={2} found in array {3} at index {4}"
          .format(iteration, elapsed, x, N, target_idx))
