class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if maxWidth<2:
            return words
        result = []
        line = []
        n = len(words)
        i = 0
        count = 0
        while i < n:
            count += len(words[i])
            if count <= maxWidth:
                line.append(words[i])
                if count < maxWidth:
                    count += 1
                    line.append(" ")
                else:
                    result.append(line)
                    line = []
                    count = 0

                i += 1
                if i == n and count != 0:
                    extra = maxWidth - count
                    line.append(" "*extra)
                    result.append(line)

            else:

                if len(line) > 2:
                    line.pop()
                    extra = maxWidth - ( count-len(words[i])-1)
                else:
                    extra = maxWidth - ( count-len(words[i]))

                needSpace = 1
                while  extra > 0:
                    line[needSpace] = line[needSpace] + " "
                    needSpace += 2
                    if needSpace >= len(line):
                        needSpace = 1
                    extra -= 1
                result.append(line)
                line = []
                count = 0
        f = []
        for i in result:
            f.append("".join(i))

        return f

l = ["Listen","to","many,","speak","to","a","few."]
m = 6
["a","b","c","d","e"]
3
["Here","is","an","example","of","text","justification."]
14
# l=["This", "is", "an", "example", "of", "text", "justification."]
# m=16
r =  Solution().fullJustify(l,m)

print r