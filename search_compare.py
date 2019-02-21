import time
import random

my_list = []


def random_list(my_list, list_size):
    """Generate a list with random numbers.

    Args:
        my_list (list): empty list to be filled
        list_size (int): value to determine size of list

    Returns:
        my_list (list): list of random value with size determined by list_size value

    Example:
        >>>random_list(my_list, 6)
        [4, 6, 1, 3, 7, 2]
    """

    while len(my_list) < list_size:
        number = random.randint(0, list_size)
        my_list.append(number)

    return my_list


def sequential_search(my_list, item, list_size):
    """Performs item search on a list and returns bool and string.

    Args:
        my_list (list): list of random integers
        item (int): value used for search on my_list
        list_size (int): value used to determine size of list

    Returns:
        bool: logic value if value is found
        str: average time spent on search

    """

    random_list(my_list, list_size)

    pos = 0
    found = False
    start = time.time()

    while pos < len(my_list) and not found:
        if my_list[pos] == item:
            found = True
        else:
            pos += 1

    end = time.time()

    return found, 'Sequential Search took {:.7f} seconds to run'.format((end-start))


def ordered_sequential_search(my_list, item, list_size):
    """Performs search on ordered list, returning logic and string

    Args:
        my_list (list): list of generated integers
        item (int): value of number to search for
        list_size (int): value to determine list size

    Returns:
        bool: logic indicating item existence
        str: average time spent on search
    """

    random_list(my_list, list_size)

    pos = 0
    found = False
    stop = False

    newlist = sorted(my_list)

    start = time.time()

    while pos < len(newlist) and (not found) and (not stop):
        if newlist[pos] == item:
            found = True
        elif newlist[pos] > item:
            stop = True
        else:
            pos += 1

    end = time.time()

    return found, "Ordered sequential search tool {:.7f} seconds to run on average".format(end-start)


def binary_search_iterative(my_list, item, list_size):
    """Performs item search on ordered list and returns bool logic and string.

    ARgs:
        my_list (list): list of random integers
        item(int): value to be searched
        list_size(int): size of list

    Returns:
        bool: logic of value existing in list
        str: average time spent on search
    """

    random_list(my_list, list_size)

    first = 0
    last = len(my_list) - 1
    found = False
    newlist = sorted(my_list)
    start = time.time()

    while first <= last and not found:
        midpoint = (first + last) // 2
        if newlist[midpoint] == item:
            found = True
        elif item < newlist[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

    end = time.time()

    return found, 'Binary search iterative search took {:.7f} seconds to run on average'.format(end-start)


def binary_search_recursive(my_list, item, list_size):
    """Performs item search on orderd list and returns logic and string

    Args:
        my_list (list): list of random integers
        item (int): value for search on list
        list_size (int): value to determine size of list

    Returns:
        bool: bool logic for item existing in list
        str: average time spent on search.
    """

    random_list(my_list, list_size)

    newlist = sorted(my_list)
    start = time.time()

    if len(newlist) == 0:
        return False
    else:
        midpoint = len(newlist) // 2

    if newlist[midpoint] == item:
        end1 = time.time()
        return True, 'Binary search recursive took {:.7f} to run on average'.format(end1-start)
    else:
        end2 = time.time()
        print('Binary search recursive took {:.7f} seconds to run on average'.format(end2 - start))
        if item < newlist[midpoint]:
            return binary_search_recursive(newlist[:midpoint], item, midpoint),
        else:
            return binary_search_recursive(newlist[midpoint + 1:], item, midpoint),


if __name__ == '__main__':
    for i in range(100):
        for list_size in (500, 1000, 10000):
            print(i, list_size, sequential_search(my_list, -1, list_size))
            print(i, list_size, ordered_sequential_search(my_list, -1, list_size))
            print(i, list_size, binary_search_iterative(my_list, -1, list_size))
            print(i, list_size, binary_search_recursive(my_list, -1, list_size))
