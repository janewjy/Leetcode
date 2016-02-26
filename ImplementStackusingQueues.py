class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q.append(x)
        for _ in xrange(len(self.q)-1):
            self.q.append(self.q.pop(0))

    def pop(self):
        """
        :rtype: nothing
        """
        return self.q.pop(0)
        
        

    def top(self):
        """
        :rtype: int
        """
        return self.q[0]
            

    def empty(self):
        """
        :rtype: bool
        """
        if not self.q:
            return True
        else:
            return False