# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node : 
            return node
        newnode = UndirctedGrap
        
        nextlnode = node.neighbors
        while nextlnode:
            for i in nextlnode:
                
                