def insertionSort(alist):
    if alist:
        l = len(alist)
        for index in range(1,l):
            cur = alist[index]
            position = index 
            while position > 0 and cur < alist[position - 1]:
                alist[position] = alist[position - 1]
                position -= 1
            alist[position] = cur


alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)