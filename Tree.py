class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    
    def print_tree(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
                


def build_product():
    root=TreeNode("Electronice")
    laptop = TreeNode("Laptop")
    root.add_child(laptop)
 
if __name__ == '__main__':
    build_product()