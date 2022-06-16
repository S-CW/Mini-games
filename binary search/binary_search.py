import random, time
# Implementation of binary search algorith

# Binary search vs Naive search

def naive_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1


def binary_search(list, target, low=None, high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(list) -1
    
    if high < low:
        return -1

    midpoint = (low + high) // 2

    if list[midpoint] == target:
        return midpoint
    elif target < list[midpoint]:
        return binary_search(list, target, low, midpoint-1)
    else:
        # target > list[midpoint]
        return binary_search(list, target, midpoint+1, high)


if __name__ == '__main__':
    length = 10000
    sorted_list = set()

    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start)/length, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start)/length, "seconds")