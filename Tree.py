class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.children.append(child)


def build_product():
    root=Treenode("Electronice")
    laptop = TreeNode("Laptop")
    root.add_child(laptop)

if __name__ = '__main__':
    build_product()