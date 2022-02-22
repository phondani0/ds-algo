# Problem: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

from queue import PriorityQueue


class Solution:
    pq = None

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.pq = PriorityQueue()
        self.traverseTree(root, 0, 0)

        ans = []
        temp = []
        prev_vert_level = None

        while(not self.pq.empty()):
            node = self.pq.get()

            if(prev_vert_level != None and prev_vert_level != node[0]):
                ans.append(temp)
                temp = []

            temp.append(node[2])
            prev_vert_level = node[0]

        if(temp):
            ans.append(temp)

        return ans

    def traverseTree(self, root, level, vertical_level):
        if(not root):
            return

        # insert elements to priority queue
        self.pq.put((vertical_level, level, root.val))

        self.traverseTree(root.left, level+1, vertical_level-1)
        self.traverseTree(root.right, level+1, vertical_level+1)
