def bubble_sort(list):
    for i in range(len(list)):
        print('PASS', i)
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j] #swapping values from current to next and vice versa
    return list

mylist = [12,45,86,37,84,51,966]

print(bubble_sort(mylist))