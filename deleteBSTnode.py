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

    def delete(self, val):
        if self.data == val:
            r

        if val < self.data:
            if self.left:
                self.left= self.left.delete(val)
            else:
                return False

        if val > self.data:
            if self.right:
                self.right= self.right.delete(val)
            else:
                return False
        if self.left is None and self.right is None:
            return None
        if self.left is None:
            return self.right
        if self.right is None:
            return self.left

def build_tree(elements):
    root= BST(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__ =="__main__":
    num=[1,324,54,3,25,342,53,23,3,3]
    
    tree_num = build_tree(num)
    print(tree_num.Inorder())
    # print(tree_num.search(324))
    print(tree_num.Preorder())
    print(tree_num.PostOrder())





        

        