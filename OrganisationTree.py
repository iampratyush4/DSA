class TreeNode:
    def __init__(self,data1,data2):
        self.data1=data1
        self.data2=data2
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
        prefix = spaces + "|_ _ " if self.parent else ""
        print(prefix + self.data1 + "("+ self.data2+ ")")
        if self.children:
        
            for child in self.children:
                child.print_tree()
        
def build_product():
    root=TreeNode("Pratyush","CEO")

    CTO = TreeNode("Anu","CTO")
    CTO.add_child(TreeNode("Vishwa","Infra head"))
    CTO.add_child(TreeNode("dhaval","app maangaer"))
    # laptop.add_child(TreeNode("Thinkpad"))
   
    HR_Head=TreeNode("Nishant","HR Head")
    HR_Head.add_child(TreeNode("Peter","recuritor"))
    HR_Head.add_child(TreeNode("henry","policy matters"))
    # Cellphone.add_child(TreeNode("nokia"))

    root.add_child(CTO)
    root.add_child(HR_Head)
    
    return root
    
    
 
if __name__ == '__main__':
   root= build_product()

   root.print_tree()
   pass