# use dictionary, my version
class Solution(object):

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(s)
        n = len(t)
        if m < n:
            return ''
        lt = {}
        for i in t:
            if i not in lt:
                lt[i] = 1
            else:
                lt[i] += 1
        missing = n
        i = I = J = 0
        for j, c in enumerate(s, 1):

            if c in lt and lt[c] > 0:
                missing -= 1
            if c in lt:
                lt[c] -= 1
            print missing,i,j
            while i < j and not missing:
                if not J or j-i < J-I:
                    I, J = i, j
                if s[i] not in lt:
                    i += 1
                    continue
                else:
                    lt[s[i]] += 1
                    if lt[s[i]] > 0:
                        missing += 1
                    i += 1
        return s[I:J]
print Solution().minWindow("a","a")


# using counter

class Solution(object):

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            print j, c
            print missing, need[c]
            missing -= need[c] > 0
            print missing, need
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(s)
        n = len(t)
        
        if m < n:
            return ""
        dic = {}
        for char in t:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1

        missing = n
        i = 0
        I = J = 0

        for j in xrange(m):
            if s[j] in dic and dic[s[j]] > 0:
                missing -= 1 
            if s[j] in dic:
                dic[s[j]] -= 1
            while not missing and i < j+1:
                if not J or j-i<J-I:
                    I,J = i,j+1
                if s[i] not in dic:
                    i += 1
                    continue
                else:
                    dic[s[i]] += 1
                    if dic[s[i]] > 0:
                        missing += 1
                    i += 1
        return s[I:J]
print Solution().minWindow("a","a")