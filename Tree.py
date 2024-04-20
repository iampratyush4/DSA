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
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))
   
    Cellphone=TreeNode("Cell phone")
    Cellphone.add_child(TreeNode("Iphone"))
    Cellphone.add_child(TreeNode("samsung"))
    Cellphone.add_child(TreeNode("nokia"))

    root.add_child(laptop)
    root.add_child(Cellphone)

    
    root.add_child(laptop)
 
if __name__ == '__main__':
    build_product()