# Definition for a binary tree node.
class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def add_child(self,data):
        if data == self.data:
            return
        
        if data < self.data:
            #add data in left sub tree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = TreeNode(data)
        else:
            #add data in right sub tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = TreeNode(data)
    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    

class Solution:
    def invertTree(self, root):
        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    


def build_tree(elements):
    root = TreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == "__main__":
    sol = Solution()
    numbers = [17,1,20,9,23,18,34]
    numbers_tree = build_tree(numbers)
    sol.invertTree(numbers_tree)

    print(numbers_tree.in_order_traversal())