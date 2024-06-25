# Here we are creating a general tree:
# Electronics
#    |__Laptop
#       |__Mac
#       |__Surface
#       |__Thinkpad
#    |__cellphone
#       |__iPhone
#       |__Pixel
#       |__Vivo
#    |__Tv
#       |__Samsung
#       |__LG

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
            

    def print_tree(self):
        spaces = " "*self.get_level()*3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()   

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("cellphone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("Tv")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root



if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
    pass