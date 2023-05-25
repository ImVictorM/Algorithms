def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    if high_index > low_index:
        if word[low_index] != word[high_index]:
            return False
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return True
