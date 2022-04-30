
def sum_of_sqares_of_numbers_list(numbers):
    """
    Sum of squares of numbers in a list
    """
    return sum([i**2 for i in numbers])


if __name__ == '__main__':

    more_numbers = 'y'
    numbers = []
    while more_numbers.lower() == 'y':
        number = int(input("Enter a number: "))
        numbers.append(number)
        more_numbers = input("Do you want to enter more numbers? (y/n) ")
    print("The sum of squares of numbers is:", sum_of_sqares_of_numbers_list(numbers))
