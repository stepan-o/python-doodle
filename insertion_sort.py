##########################################################################################################
#                                                                                                        #
#       Recursive implementation of an insertion sort algorithm on an unsorted array in Python           #
#                                                                                                        #
#                   Algorithm steps:                                                                     #
#                   ----------------                                                                     #
#             1. Divide array into two parts: sorted and unsorted                                        #
#                   (start by taking only the first element of N to the sorted side)                     #
#             2. Insert an element from the unsorted side to the sorted side using insertion sort        #
#             3. Repeat until there are no more unsorted elements                                        #
#                                                                                                        #
##########################################################################################################


def insertion_sort(N_x, x_pos=-1):
    if abs(x_pos) == len(N_x):
        return N_x
    elif N_x[x_pos] < N_x[x_pos - 1]:
        swap = N_x[x_pos - 1]
        N_x[x_pos - 1] = N_x[x_pos]
        N_x[x_pos] = swap
        x_pos -= 1
        return insertion_sort(N_x, x_pos=x_pos)
    else:
        return N_x


def sort_array(array):
    sorted_part = [array[0]]
    unsorted_part = array[1:]
    for unsrt_item in unsorted_part:
        sorted_part = insertion_sort(sorted_part + [unsrt_item])
    return sorted_part


N = [7, 5, 3, 15, 1, 25, 0]

N_sorted = sort_array(N)
print("Original array:\n{0}\nArray sorted using insertion sort:\n{1}".format(N, N_sorted))
