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
    """

    while len(my_list) < list_size:
        number = random.randint(0, list_size)
        my_list.append(number)

    return my_list


def python_sort(my_list, start, gap):
    """Calls sort function on input list

    Args:
        my_list (list): list that is to be sorted

    Returns:
        my_list (list): original list but sorted
    """

    for i in range(start + gap, len(my_list), gap):
        current_value = my_list[i]
        position = i

        while position >= gap and my_list[position - gap] > current_value:
            my_list[position] = my_list[position - gap]
            position = position - gap

        my_list[position] = current_value


def insert_sort(my_list, list_size):
    """Sorts list with randomly generated values.

    Args:
        my_list (list): empty list to be filled with random integers
        list_size(int): value to determine size of list

    Returns:
        my_list(list): list of sorted values with size determined by list_size value
        str: average time spent on sorting
    """

    random_list(my_list, list_size)

    start = time.time()

    for index in range(1, len(my_list)):
        current_value = my_list[index]
        position = index

        while position > 0 and my_list[position - 1] > current_value:
            my_list[position] = my_list[position - 1]
            position = position - 1

        my_list[position] = current_value

    end = time.time()

    return 'Insert sort requires {:.7f} seconds to run on average'.format(end-start)


def shell_sort(my_list, list_size):
    """Sorts the list with random values.

    Args:
        my_list (list): empty list to be populated
        list_size (int): value of size of list
    Returns:
        my_list (list): list of sorted values
        str: average time spent on sort
    """

    random_list(my_list, list_size)

    start = time.time()
    sublist_count = len(my_list) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            python_sort(my_list, start_position, sublist_count)

        sublist_count = sublist_count // 2

    end = time.time()
    return 'Shell sort requires {:.7f} seconds to run on average'.format(end-start)


if __name__ == '__main__':
    for i in range(100):
        for list_size in (500, 1000, 10000):
            print(i, list_size, insert_sort(my_list, list_size))
            print(i, list_size, shell_sort(my_list, list_size))
