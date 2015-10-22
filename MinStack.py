class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        # NEED TO BE MODIFIED FOR BETTER ORGNIZED
        self.minimum = None
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.minimum == None or x < self.minimum:
            self.minimum = x
        self.stack.append((x,self.minimum))
        

    def pop(self):
        """
        :rtype: nothing
        """
        
        self.stack.pop()
        if len(self.stack) == 0:
            self.minimum = None
        else:
            self.minimum = self.getMin()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        
        return self.stack[-1][1]

        
x = MinStack()
x.push(0)
x.push(1)
x.push(0)
x.pop()
print x.getMin(),x.top()
