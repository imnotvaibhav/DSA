# Probelem: https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root):
        # Go BST
        # if not root.left and not root.right:
        #     return True
        # if root.left.val>=root.val or root.right.val<=root.val:
        #     return False
                
        # return (self.isValidBST(root.left) and self.isValidBST(root.right))
        # Why was this wrong?
        # bcz even a late descendant node could have value that defaults the value of root node
        # e.g. 5->2,8  but then, 8-->6,9. Here, 6 defaults root value of 5
        
        def valid(node,left,right):
            if not node:
                return True

            if not (node.val<right and node.val>left):
                return False
            
            return (valid(node.left,left,node.val) and valid(node.right,node.val,right))

        return valid(root,float("-inf"),float("inf"))