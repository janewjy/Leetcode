def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    num = 0
    l = len(digits)
    for digit in digits:
        l -= 1
        num += digit * (10 ** (l))        
  
    num += 1
    
    list_ = []
    while num > 0:
        list_ = [num % 10] + list_
        num //= 10
    
    return list_

print plusOne([1,0])


    for ind, val in enumerate(alist):
        num *= ind * val

    for key, val in adict.iteritems():

    for key in sorted(adict.keys()):

  

        