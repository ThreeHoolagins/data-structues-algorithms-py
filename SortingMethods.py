import math

def merge_sort_outer(array):
    low = 0
    high = len(array)

    merge_sort(array, low, high)

def merge_sort(array, low, high):
    if low < high:
        middle = math.floor(low + (high - low )/2)
        print (f"Low:{low} Middle:{middle} High:{high}")
        merge_sort(array, low, middle)
        merge_sort(array, middle+1, high)
        merge(array, low, middle, high)

def merge(array, low, middle, high):
    #finish later
    # run through array
    helper_arr = array.copy()
    curr = low
    helper_left = low
    helper_right = middle

    while pointer1 < middle or pointer2 < high:
        if array[pointer1] < array[pointer2]:
            print(array[pointer1])
            array[pointer1] = helper_arr[pointer1]
            pointer1 += 1
        else:
            print()
            var = array[pointer2]
            pointer2 += 1
            array.insert(pointer1)

    print(array)
