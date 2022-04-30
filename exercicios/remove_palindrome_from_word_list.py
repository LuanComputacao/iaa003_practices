
def remove_palindrome_from_word_list(word_list):
    """
    Remove palindrome from word list.
    """
    return [word for word in word_list if word != word[::-1]]


if __name__ == '__main__':
    word_list = ['abc', 'xyz', 'aba', '1221']
    print(remove_palindrome_from_word_list(word_list))
