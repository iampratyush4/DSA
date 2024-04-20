class BTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data==self.data:
            return
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BTreeNode(data)


    def Inorder(self):
        elements=[]

        # visit left tree first
        if self.left:
            elements +=self.left.Inorder()

        # visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:

            elements += self.right.Inorder()
        return elements
    
            
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

            


    
def build_tree(elements):
    root=BTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
        

if __name__ =="__main__":
    num=[1,324,54,3,25,342,53,23,3,3]
    
    tree_num = build_tree(num)
    print(tree_num.Inorder())
    print(tree_num.search(324))
    # print(tree_num.Inorder())
