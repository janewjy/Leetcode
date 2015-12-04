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
        
                
        