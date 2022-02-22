# Question: https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1

class Solution:
    ans = []
    stack = []

    def printBoundaryView(self, root):
        if(not root):
            return None

        if(not root.left and not root.right):
            return [root.data]

        self.ans = []
        self.stack = []

        self.ans.append(root.data)

        # left traversal
        # always send root.left not just root else it work work for skew tree
        self.leftBoundaryTrav(root.left)

        self.getLeafNodes(root)  # get leaf nodes

        self.rightBoundaryTrav(root.right)  # right traversal in reverse

        while(self.stack):
            self.ans.append(self.stack.pop())

        return self.ans

    def leftBoundaryTrav(self, root):
        if(not root):
            return

        if(not root.left and not root.right):
            return

        self.ans.append(root.data)

        if(root.left):
            self.leftBoundaryTrav(root.left)
        else:
            self.leftBoundaryTrav(root.right)

    def getLeafNodes(self, root):
        if(not root):
            return

        if(not root.left and not root.right):
            self.ans.append(root.data)
            return

        self.getLeafNodes(root.left)
        self.getLeafNodes(root.right)

    def rightBoundaryTrav(self, root):
        if(not root):
            return

        if(not root.left and not root.right):
            return

        self.stack.append(root.data)

        if(root.right):
            self.rightBoundaryTrav(root.right)
        else:
            self.rightBoundaryTrav(root.left)
