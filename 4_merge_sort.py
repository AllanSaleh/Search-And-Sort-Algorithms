# Break lists in half recursively, base case (arrive at single element lists)

# Left and right half, both need to broken
# Break down left side first, once you manage the left, then deal with the right side

# Merging two lists
#  -- compare elements of each list, gradually draining both, until one is empty
#  -- empty the list that still has elements

def merge_sort(list):
    if len(list)>1:
        print(list)
        mid = len(list) // 2
        left_side = list[:mid]
        print(left_side)
        right_side = list[mid:]
        print(right_side)

        merge_sort(left_side)
        merge_sort(right_side)
        print(f'Merging {left_side} and {right_side}')

        i = 0 # main
        j = 0 # left half
        k = 0 # right

        while j < len(left_side) and k < len(right_side):
            if left_side[j]['title'].lower() < right_side[k]['title'].lower():
                list[i] = left_side[j]
                i += 1
                j += 1
            else:
                list[i] = right_side[k]
                i += 1
                k += 1
        
        while j < len(left_side):
            list[i] = left_side[j]
            i += 1
            j += 1

        while k < len(right_side):
            list[i] = right_side[k]
            i += 1
            k += 1
        print(f'MERGED {list}')
    else:
        print('BASE CASE')


# alist = [3,1,5,2]

# merge_sort(alist)
# print(alist)

playlist = [
    {"title": "ANNIE", "duration": 180, "upload_date": "2022-01-01"},
    {"title": "annie Fandoura", "duration": 240, "upload_date": "2021-12-15"},
    {"title": "Ben the Einstein", "duration": 200, "upload_date": "2022-01-10"},
]

merge_sort(playlist)
print('~'*50)
print(playlist)
