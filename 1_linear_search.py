def linear_search(alist, target):
    for index, item in enumerate(alist):
        if item == target:
            return index
    return 'Target not found'

some_stuff = [4,8,6,2,0,47,3]

print(linear_search(some_stuff, 2))

print(some_stuff.index(2))