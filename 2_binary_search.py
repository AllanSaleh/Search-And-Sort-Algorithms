#50
#75
#67
#71
#73


def binary_search(alist, target): #requres that the list be sorted
    low = 0
    high = len(alist) - 1

    while low <= high:
        mid = (low + high) // 2
        if alist[mid] == target:
            return f'Found my target at index: {mid}'
        elif alist[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return 'Target not found'

nums = [4,8,6,2,0,47,3]

print(binary_search(nums, -5))