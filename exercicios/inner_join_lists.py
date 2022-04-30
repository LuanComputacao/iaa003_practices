def inner_join_lists(lst1, lst2):
    """
    Inner join two lists.
    """
    return [i for i in lst1 if i in lst2]


if __name__ == '__main__':
    lst1 = [1, 2, 3, 4, 5]
    lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(inner_join_lists(lst1, lst2))
