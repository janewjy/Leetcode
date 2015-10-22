class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s
            
        
        output = []
        i = 0 
        l = len(s)
        while i < l:
            output.append(s[i])
            i += (numRows-1)*2
        
        
        for j in range(1,numRows-1):
            i  = j
            tal = numRows*2 - 2

            while i < l:
                output.append(s[i])
                k  = tal - i
                if k < l:
                    output.append(s[k])
                i += (numRows-1)*2
                tal += (numRows-1)*4
                
        i = numRows-1
        while i < l:
            output.append(s[i])
            i += (numRows-1)*2
                
        return ''.join(output)
            
            
        