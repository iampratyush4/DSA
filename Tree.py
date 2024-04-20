class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level +=1
            p=p.parent
        return level
    
    def print_tree(self):
        spaces= '  ' * self.get_level() *3
        prefix =spaces + "|_ _ " if self.parent else ""
        print(prefix + self.data)
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
    
    return root
    
    
 
if __name__ == '__main__':
   root= build_product()

   root.print_tree()
   pass