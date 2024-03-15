from Domain.entities import Person
from Domain.entities import Event


def quicksort(array, key=None, reverse=False):
    """
    Sorts a list of events using QuickSort
    :param array: list of events
    :type array: [Event, Event, ...]
    :param key: the key after which it sorts
    :param reverse: whether it sorts ascending or descending
    """
    start = 0
    end = len(array) - 1
    quicksort_sorting(start, end, array, key, reverse)


def quicksort_sorting(start, end, array, key, reverse):
    """
    Function that implements QuickSort
    :param start: index of the first element
    :type start: int
    :param end: index of the last element
    :type end: int
    :param array: list of events
    :type array: [Event, Event, ...]
    :param key: the key after which it sorts
    :param reverse: whether it sorts ascending or descending
    """
    if start < end:
        p = quicksort_partition(start, end, array, key, reverse)
        quicksort_sorting(start, p - 1, array, key, reverse)
        quicksort_sorting(p + 1, end, array, key, reverse)


def quicksort_partition(start, end, array, key, reverse):
    """
    Sortiong part of the QuickSort algorithm
    :param start: index of the first element
    :type start: int
    :param end: index of the last element
    :type end: int
    :param array: list of events
    :type array: [Event, Event, ...]
    :param key: the key after which it sorts
    :param reverse: whether it sorts ascending or descending
    :return: end
    :rtype: int
    """
    # initialize the pivot index
    pivot_index = start 
    pivot = array[pivot_index]

    # this loop executes until start index becomes greater than or equal to end index,
    # and then it swaps the pivot and the end
    while start < end:
        # increment start index until it finds an element greather than or equal to pivot
        while start < len(array) and key(array[start], pivot, reverse):
            start += 1
        # decrement the end index until it find an element less than or equal to pivot
        while not key(array[end], pivot, reverse):
            end -= 1
        # if start and end didn't intersect, swaps them
        if start < end:
            array[start], array[end] = array[end], array[start]
    # swaps the pivot and the end to put the pivot in the right position (sorted)
    array[end], array[pivot_index] = array[pivot_index], array[end]
    # returns the end index to divide the list in two
    return end


def quicksort_compare(x, y):
    """
    Compares events x and y (description, date)
    :param x: first event
    :type x: Event
    :param y: second event
    :type y: Event
    :return: True if x <= y, otherwise False
    :rtype: bool
    """
    if x.get_description() == y.get_description():
        return x.get_date() <= y.get_date()
    else:
        return x.get_description() < y.get_description()


def compare_by_description(x, y, reverse):
    """
    Compares events x and y (description)
    :param x: first event
    :type x: Event
    :param y: second event
    :type y: Event
    :param reverse: whether it sorts ascending or descending
    """
    if reverse:
        return x.get_description() >= y.get_description()
    return x.get_description() <= y.get_description()


def compare_by_date(x, y, reverse):
    """
    Compares events x and y (date)
    :param x: first event
    :type x: Event
    :param y: second event
    :type y: Event
    :param reverse: whether it sorts ascending or descending
    """
    if reverse:
        return x.get_date() >= y.get_date()
    return x.get_date() <= y.get_date()


def compare_by_participants(x, y, reverse):
    """
    Compares events x and y (participants count)
    :param x: first event
    :type x: Event
    :param y: second event
    :type y: Event
    :param reverse: whether it sorts ascending or descending
    """
    if reverse:
        return len(x.get_participants()) >= len(y.get_participants())
    return len(x.get_participants()) <= len(y.get_participants())


def compare_by_events_count(x, y, reverse):
    """
    Compares people x and y by how many events they take part in
    :param x: first person
    :type x: Person
    :param y: second person
    :type y: Person
    :param reverse: whether it sorts ascending or descending
    """
    if reverse:
        return x.get_events_count() >= y.get_events_count()
    return x.get_events_count() <= y.get_events_count()


def gnomesort(array, key=None, reverse=False):
    """
    Sorts a list of people using GnomeSort
    :param array: list of people
    :type array: [Person, Person, ...]
    :param key: the key after which it sorts
    :param reverse: whether it sorts ascending or descending
    """
    index = 0
    while index < len(array):
        if index == 0:
            index += 1
        if key(array[index-1], array[index], reverse):
            index += 1
        else:
            array[index], array[index-1] = array[index-1], array[index]
            index -= 1
