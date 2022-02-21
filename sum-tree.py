# https://practice.geeksforgeeks.org/problems/sum-tree/1
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


class Solution:
    def isSumTree(self, root):

        is_sum_tree = True

        def check_sum_tree(root):
            nonlocal is_sum_tree

            if(not root):
                return 0

            if(not root.left and not root.right):
                return root.data

            left_sum = check_sum_tree(root.left)
            right_sum = check_sum_tree(root.right)

            if(root.data != left_sum + right_sum):
                is_sum_tree = False

            return left_sum + right_sum + root.data

        check_sum_tree(root)

        return is_sum_tree
