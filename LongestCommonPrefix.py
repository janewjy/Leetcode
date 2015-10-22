def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix = ""
        for i in range(len(strs[0])):
            letter = strs[0][i]

            for s in strs:
                if i >= len(s) or s[i] != letter:
                    return prefix
            prefix += letter
        return prefix
        

