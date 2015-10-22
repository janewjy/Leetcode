a = [2,7,5,3,11,8,4,6,5,2]
# for i in range(0,len(a)):
#     for j in range()
print a 
def mergeSort(alist):
    l = len(alist)
    mid = l//2
    if l > 1:
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1 
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            # i, k += 1, 1
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1 
            k += 1
            
mergeSort(a)
print a 



# def mergeSort(alist):
#     print("Splitting ",alist)
#     if len(alist)>1:
#         mid = len(alist)//2
#         lefthalf = alist[:mid]
#         righthalf = alist[mid:]

#         mergeSort(lefthalf)
#         mergeSort(righthalf)

#         i=0
#         j=0
#         k=0
#         while i < len(lefthalf) and j < len(righthalf):
#             if lefthalf[i] < righthalf[j]:
#                 alist[k]=lefthalf[i]
#                 i=i+1
#             else:
#                 alist[k]=righthalf[j]
#                 j=j+1
#             k=k+1

#         while i < len(lefthalf):
#             alist[k]=lefthalf[i]
#             i=i+1
#             k=k+1

#         while j < len(righthalf):
#             alist[k]=righthalf[j]
#             j=j+1
#             k=k+1
#     print("Merging ",alist)

# alist = [54,26,93,17,77,31,44,55,20]
# mergeSort(alist)
# print(alist)
