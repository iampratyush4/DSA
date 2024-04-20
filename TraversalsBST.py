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
    
    def Preorder(self):
        elements=[]

        # visit base node

        elements.append(self.data)

        # visit left tree first

        if self.left:
            elements +=self.left.Preorder()
        # visit right tree  
        if self.right:

            elements += self.right.Preorder()
        return elements
    
    def PostOrder(self):
        elements=[]

        

        # visit left tree first

        if self.left:
            elements +=self.left.PostOrder()
        # visit right tree  
        if self.right:

            elements += self.right.PostOrder()

        # visit base node

        elements.append(self.data)
        return elements

    


            
    
def build_tree(elements):
    root=BTreeNode(elements[0])
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
    
