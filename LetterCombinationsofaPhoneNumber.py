class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'1':'*', '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        additional = mapping[digits[-1]]
        return [s + c for s in prev for c in additional]
# 1-25
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        res = []
        bk(digits,res,'')
        return res

def bk(digits,res,subres):
    if digits == '':
        return res.append(subres)
    mapping = {'1':'*', '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    
    for i in mapping[digits[0]]:
        bk(digits[1:],res,subres+i)
