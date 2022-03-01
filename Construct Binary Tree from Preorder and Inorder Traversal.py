# Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        dict_ = {}
        for i, x in enumerate(inorder):
            dict_[x] = i

        def solve(preorder, inorder, pre_start, pre_end, in_start, in_end):
            if(pre_start > pre_end or in_start > in_end):
                return None

            root = TreeNode(preorder[pre_start])

            # find root index in inorder
            in_root = dict_[preorder[pre_start]]

            nums_left = in_root - in_start

            root.left = solve(preorder, inorder, pre_start+1,
                              pre_start + nums_left, in_start, in_root-1)
            root.right = solve(preorder, inorder, pre_start +
                               nums_left+1, pre_end, in_root+1, in_end)

            return root

        return solve(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)
