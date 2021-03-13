# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import *

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        queue = collections.deque()
        queue.append(node)
        nodeDict = dict()
        nodeDict[node.val] = Node(node.val, [])
        while queue:
            theirNode = queue.popleft()
            myNode = nodeDict[theirNode.val]
            for n in theirNode.neighbors:
                if n.val not in nodeDict:
                    nodeDict[n.val] = Node( n.val, [])
                    queue.append(n)
                myNode.neighbors.append(nodeDict[n.val])
        return nodeDict[1]