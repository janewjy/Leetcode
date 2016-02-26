def heapsort( aList ):
    # convert aList to heap
    length = len( aList ) - 1
    leastParent = length / 2
    for i in range ( leastParent, -1, -1 ):
        moveDown( aList, i, length )
        print aList

    # flatten heap into sorted array
    for i in range ( length, 0, -1 ):
        if aList[0] > aList[i]:
            swap( aList, 0, i )
            moveDown( aList, 0, i - 1 )
            print aList
    # print aList
 
def moveDown( aList, first, last ):
  largest = 2 * first + 1
  while largest <= last:
    # right child exists and is larger than left child
    if ( largest < last ) and ( aList[largest] < aList[largest + 1] ):
        largest += 1
 
    # right child is larger than parent
    if aList[largest] > aList[first]:
        swap( aList, largest, first )
        # move down to largest child
        first = largest;
        largest = 2 * first + 1
    else:
      return # force exit
 
 
def swap( A, x, y ):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

heapsort([6,2,5,3,7,4])



def max_heapify(li, i, heap_size):
  l = i * 2 #left(i)
  r = l + 1 #right(i)
  if l <= heap_size and li[l] > li[i]:
    largest = l
  else:
    largest = i
  if r <= heap_size and li[r] > li[largest]:
    largest = r
  if i != largest:
    li[i], li[largest] = li[largest], li[i]
    max_heapify(li, largest, heap_size)

def build_max_heap(li, heap_size):
  for i in range(heap_size/2 - 1, 0, -1):
    max_heapify(li, i, heap_size) 

def heap_sort(li, heap_size):
  build_max_heap(li, heap_size)
  for i in range(len(li[1:]), 1, -1):
    li[1], li[i] = li[i], li[1]
    heap_size = heap_size - 1
    max_heapify(li, 1, heap_size)

def main():
  # we shall consider the list from element 1, not 0
  li = [0, 16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
  heap_size = len(li[1:])
  heap_sort(li, heap_size)
  print li[1:]

if __name__ == "__main__":
  main()
 
 # my version
def heapsort(aList):
    length = len(aList) - 1
    leastParent = length//2
    for i in xrange(leastParent,-1,-1):
        max_heapify(aList,leastParent,length)


# def max_heapify(aList,first,last):
#     print aList
#     lc = first*2+1
#     largest = first
#     if lc<=last and aList[lc]>aList[largest]:
#         largest = lc
#     if lc+1<= last and aList[lc+1]>aList[largest]:
#         largest = lc+1
#     if largest != first:
#         aList[largest],aList[first] = aList[first], aList[largest]
#         max_heapify(aList,largest,last)
# a = [6,2,5,3,7,4]
# for i in xrange(2,-1,-1):
#     max_heapify(a,i,5)
    

# for i in xrange(5,0,-1):
#     a[0],a[i] = a[i],a[0]
#     max_heapify(a,0,i-1)
#     print a




   