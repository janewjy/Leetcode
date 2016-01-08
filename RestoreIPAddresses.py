class Solution(object):

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        res = []

        back_track(s, res, '', 3)
        return res


def back_track(s, res, subres, order):
    if order >= 0:
        for i in xrange(1, min(4, len(s)-order)+1):
            if order == 0 and 0 <= int(s) <= 255 and (len(s) == 1 or (len(s) == 2 and s[0] != "0") or (len(s) == 3 and s[0] != '0')):
                res.append(subres+s)
                return
            if 0 <= int(s[0:i]) <= 255 and (len(s[0:i]) == 1 or (len(s[0:i]) == 2 and s[0] != "0") or (len(s[0:i]) == 3 and s[0] != '0')):
                back_track(s[i:], res, subres+s[0:i]+'.', order-1)


a = Solution()
print a.restoreIpAddresses("010010")
