class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackin = []
        self.stackout = []
        
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        
        self.stackin.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.move()
        self.stackout.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.stackout[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return (not self.stackin) and (not self.stackout)
    def move(self):
        if not self.stackout:
            while self.stackin:
                self.stackout.append(self.stackin.pop())

x = Queue()
x.push(3)
x.push(4)
x.push(6)
print x.empty(),x.peek(),x.stackin,x.stackout

# 1-31
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.empty():
            self.peek()
            self.stack2.pop()
            
        

    def peek(self):
        """
        :rtype: int
        """
        if not self.empty():
            if self.stack2:
                return self.stack2[-1]
            else:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
                return self.stack2[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack1 and not self.stack2
