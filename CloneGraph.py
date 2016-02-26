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
            return 

        root_copy = UndirctedGrap(node.label)        
        frontier = [node]
        dic = {node:root_copy}
        while frontier:
            nextlnode = []
            for i in frontier:
                for v in i.neighbors:
                    if v not in dic:
                        neighbors_copy = UndirctedGrap(v.label)
                        dic[v] = neighbors_copy
                        dic[i].neighbors.append(neighbors_copy)
                        nextlnode.append(v)
                    else:
                        dic[i].neighbors.append(dic[v])
        return root_copy


# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node : 
            return None

        start = UndirectedGraphNode(node.label)        
        frontier = [node]
        dic = {node:start}
        while frontier:
            nextlnode = []
            for i in frontier:
                for v in i.neighbors:
                    if v not in dic:
                        nextlnode.append(v)
                        newnode = UndirectedGraphNode(v.label)
                        dic[v] = newnode
                    else:
                        newnode = dic[v]
                    dic[i].neighbors.append(newnode)
            frontier = nextlnode
        return start
                   

# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return
        front = [node]
        root = UndirectedGraphNode(node.label)
        dic = {node:root}
        while front:
            level = []
            for n in front:
                for nh in n.neighbors:
                    if nh not in dic:
                        node = UndirectedGraphNode(nh.label)
                        dic[nh] = node
                        dic[n].neighbors.append(node)
                        level.append(nh)
                    else:
                        dic[n].neighbors.append(dic[nh])
            front = level
        return  root
