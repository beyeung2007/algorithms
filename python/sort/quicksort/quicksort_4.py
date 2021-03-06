# quicksort


def quicksort(array):
    """

    Quicksort chooses an element as the pivot and split the remaining n-1
    elements into 2 sublists. Left sublist contains elements to the left of
    pivot in sorted position and right sublist contains elements to the right
    of pivot in sorted position. Then we merge left and right sublists by
    placing pivot element in between them. We then move on the same sequence
    for left and right sublists recursively until all elements are sorted.

    """
    return _quicksort(array, 0, len(array))


def _quicksort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        _quicksort(array, low, pivot)
        _quicksort(array, pivot+1, high)
    return array


def partition(array, low, high):
    # initialize pivot
    # initialize first high index
    # traverse the array from low to high
    #   if current element less than pivot element
    #       swap current with first high index element
    #       increment first high index
    # swap pivot element and first high element
    # return first high index
    pivot = high-1
    first_high = low
    for i in xrange(low, high):
        if array[i] < array[pivot]:
            array[i], array[first_high] = array[first_high], array[i]
            first_high += 1
    array[pivot], array[first_high] = array[first_high], array[pivot]
    return first_high
