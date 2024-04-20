class BST:
   
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def add_child(self,data):
        if self.data == data:
            return 
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left= BST(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BST(data)

    # calculate sum of lefts+right and then finally add the self root

    def calcSum(self):
        left_sum = self.left.calcSum() if self.left else 0
        right_sum = self.right.calcSum() if self.right else 0
        return self.data + left_sum + right_sum
        

        
        

def build_tree(elements):
    root=BST(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
        

if __name__ =="__main__":
    num=[1,324,54,3,25,342,53,23,3,3]
    
    tree_num = build_tree(num)
    # sum=0
    print(tree_num.calcSum())


            
