class TreeNode:
    def __init__(self,data):
        self.data=data
        salf.children=[]
        self.parent=None
        
    def add_child(self,child):
        child.parent=self
        self.children.append(child)