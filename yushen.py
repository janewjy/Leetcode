class Solution(object):
    i = ['werwe']
    def lala(self):
        print self.i
        self.i += ['e']
        print self.i

    @classmethod
    def baba(cls):
        print cls.i
        cls.i += ['e3']



# Solution().baba()
# Solution().baba()
Solution().lala()
Solution().lala()