def square_of_list(lst):
    """
    Returns the square of the list.
    """
    return [i ** 2 for i in lst]


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    print(square_of_list(numbers))
