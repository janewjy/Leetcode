def partition(alist,size):
    if size < 2:
        return
    pivot = alist[size//2]
    lower = 0
    upper = size - 1
    while lower < upper:
        while alist[lower] < pivot:
            lower += 1
        while alist[upper] > pivot:
            upper -= 1
            alist[lower], alist[upper] = alist[upper], alist[lower]
    

def quickSort(alist):
