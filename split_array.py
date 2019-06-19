"""
Simple module that takes a list of numbers and a positive integer N
and splits the original list into a list of lists each N long
"""

from math import ceil

def split_array(original_array, array_count):
    """
    Splits the list original_array into a number of list in a list. The number
    returned is equal to the array_count passed in

    If given an empty array or an array_count less than 0 it returns an empty list
    """
    new_array = []

    if not original_array or array_count < 0:
        return []

    try:
        len_arrays = ceil(len(original_array)/array_count)     #Work out how many whole elements are in each list
    except StandardError:
        return []

    for i in range(0, len(original_array), len_arrays):
        sub_array = original_array[i:i+len_arrays]
        new_array.append(sub_array)

    return new_array


if __name__ == "__main__":
    print(split_array([1,2,3,4,5], 3))
