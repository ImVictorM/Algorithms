def is_palindrome_iterative(word):
    if not word:
        return False

    left, right = 0, len(word) - 1
    for _ in word:
        if word[right] != word[left]:
            return False
        else:
            right -= 1
            left += 1

    return True
