def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_div = lst[:mid]
    right_div = lst[mid:]

    left = merge_sort(left_div)
    right = merge_sort(right_div)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return (first_string, second_string, False)

    sorted_first = merge_sort(list(first_string.lower()))
    sorted_second = merge_sort(list(second_string.lower()))

    return (
        "".join(sorted_first),
        "".join(sorted_second),
        sorted_first == sorted_second,
    )
