def is_palindrome(word):
    """
    Checks if a word is a palindrome
    """
    return word == word[::-1]

if __name__ == '__main__':
    word = string(input("Enter a word: "))
    if is_palindrome(word):
        print("The word is a palindrome")
    else:
        print("The word is not a palindrome")