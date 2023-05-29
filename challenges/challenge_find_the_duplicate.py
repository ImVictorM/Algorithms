def find_duplicate(nums):
    if not isinstance(nums, list):
        return False

    nums_count = {}

    for num in nums:
        if not (isinstance(num, int) and num >= 0):
            return False

        if num in nums_count:
            return num
        else:
            nums_count[num] = 1

    return False
