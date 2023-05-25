def binary_search(lst, target, start=0):
    end = len(lst) - 1

    while start <= end:
        mid = (start + end) // 2

        if lst[mid] == target:
            return (lst[mid], mid)

        if target < lst[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return None


def find_duplicate(nums):
    if not isinstance(nums, list):
        return False

    nums.sort

    for index, num in enumerate(nums):
        if not (isinstance(num, int) and num >= 0):
            return False

        next = index + 1
        exists = binary_search(nums, num, next)

        if exists:
            return exists[0]

    return False
