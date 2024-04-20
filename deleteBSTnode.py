
"""Conditions for deletion
    condtions 1 - deleting node is leaf node
        then there is no issue we can directly delete it.
    condition 2- non leaf with single child.
        we can join its child directly to its grandparent node

    condition 3 - if deleting node has 2 childs
        we can either take the maximum value in this nodes left subtree and place it on its position or we can take the minimum
        value from right subtree and place it in place of deleting node.
"""






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

        

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()



        
            




    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self
    
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


def build_tree(elements):
    root= BST(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__ =="__main__":
    num=[1,324,54,3,25,342,53,23,3,3]
    
    tree_num = build_tree(num)
    print(tree_num.Inorder())
  
    print(tree_num.delete(324))
    print(tree_num.Inorder())





        

        