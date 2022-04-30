def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == '__main__':
    print("Enter a number: ")
    n = int(input())
    print("The factorial of", n, "is", factorial(n))
