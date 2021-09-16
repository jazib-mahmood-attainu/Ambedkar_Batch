class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node'):
        if root is None:
            return
        print(root.val)
        for i in root.children:
            self.preorder(i.val)

root = Node(5)

obj = Solution()
obj.preorder(root)