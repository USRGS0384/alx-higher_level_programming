#!/usr/bin/python3

def find_peak(list_of_integers):
    """
    Finds a peak element in a list of unsorted integers.
    """

    Args:
        list_of_integers (list[int]): The input list of integers.

    Returns:
        int: The peak element (an element greater than its neighbors).
    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]

    # Check the first and last elements
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[n - 1] >= list_of_integers[n - 2]:
        return list_of_integers[n - 1]

    # Traverse the array to find the peak
    for i in range(1, n - 1):
        if list_of_integers[i] >= list_of_integers[i - 1] and list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]

print("Peak element:", find_peak(arr))
