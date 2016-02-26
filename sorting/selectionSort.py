def selectionSort(alist):
    for index in range(0, len(alist)):
        cur = alist[index]
        minium = alist[index]
        position = index
        minin = index
        while position + 1 < len(alist):
            if alist[position+1] < minium:
                minium = alist[position+1]
                minin = position+1

            position += 1

        alist[index] = minium
        alist[minin] = cur


alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist) 



