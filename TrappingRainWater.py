a = [0,1,0,2,1,0,1,3,2,1,2,1]

def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if not height:
        return 0
    dim = []
    first = height[0]
    i = 1
    count = 0
    while i < len(height):
        mark = height[i-1]

        while i < len(height) and height[i] < mark :
            dim.append(height[i])
            i += 1
        print dim
        while dim:            
            print mark - dim.pop()
        if height[i+1] and height[i+1]


        i += 1
   


trap(a)




