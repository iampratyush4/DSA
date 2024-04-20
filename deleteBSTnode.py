class BST:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if self.data ==data:
            return
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BST(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right= BST(data)

def build_tree(elements):
    root= BST(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root





        

        