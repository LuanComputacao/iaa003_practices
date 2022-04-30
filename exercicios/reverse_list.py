def reverse_list(lst):
    """
    Reverse the order of a list.
    """
    if len(lst) == 0:
        return []

    return [lst[-1]] + reverse_list(lst[:-1])


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    print(reverse_list(numbers))
