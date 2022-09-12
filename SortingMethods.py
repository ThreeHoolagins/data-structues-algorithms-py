
def merge_sort(array):
    low = 0
    high = len(array) -1

    merge_sort(array, low, high)

def merge_sort(array, low, high):
    if low < high:
        middle = int(low + (high - low )/2)
        merge_sort(array, low, middle)
        merge_sort(array, middle, high)
        merge(array, low, middle, high)

def merge(array, low, middle, high):
    #finish later
