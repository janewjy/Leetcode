class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        resl = [1]*len(ratings)
        lbase = rbase = 1
        for i in xrange(1,len(ratings)):
            if ratings[i] > ratings [i-1]:
                lbase += 1
            else:
                lbase = 1
            resl[i] = lbase
        for i in xrange(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                rbase += 1
            else:
                rbase = 1
            resl[i] = max(rbase,resl[i])

        return sum(resl)





