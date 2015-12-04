class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern and not str:
            return True
        
            
        words = str.split()
        chars = list(pattern)
        if len(words) != len(chars):
            return False
        
        dic = {}
        dic2 = {}
        
        for char, word in zip(chars, words):
            if char not in dic:
                dic[char] = word
            else:
                if dic[char] != word:
                    return False
            if word not in dic2:
                dic2[word] = char
            else:
                if dic2[word] != char:
                    return False
        return True

        
# better version

def wordPattern(self, pattern, str):
    s = pattern
    t = str.split()
    return map(s.find, s) == map(t.index, t)

