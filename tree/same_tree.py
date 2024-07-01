# Problem: https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q):
        # if both p and q does not exist
        if not p and not q:
            return True
        # if either p or q does not exist or their values are not equal
        if not p or not q or p.val!=q.val:
            return False

        return ( self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) )