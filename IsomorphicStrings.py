class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # dic = {}
        # for a, b in zip(s,t):
        #     if a in dic:
        #         if b != dic[a]:
        #             return False
        #     else:
        #         dic[a] = b
        # return True
                
        return map(s.find, s) == map(t.find, t)
        
                
def isIsomorphic(self, s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        table1 = {}
        table2 = {}
        
        if len(s)!=len(t):
            return False
        table1 = {}
        table2 = {}
        
        for i,j in zip(s,t):
            if i not in table1:
                table1[i] = j
            if j not in table2:
                table2[j] = i
            if table1[i] != j or table2[j]!= i:
                    return False
        return True

            
Solution().isIsomorphic('ac','aa')
                
