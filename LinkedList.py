class Node:
    def _init_(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def _init_(self):
        self.head = None
        
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insertEnd(self,data):
        node=Node(data,None)
        if self.head is None:
            self.head=node
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=node
            
    def getlength(self):
        count=0
        n=self.head
        while n:
            count+=1
            n=n.next
            
        return count
        
            
    def insertlist(self,listll):
        self.head=None
        for data in listll:
            self.insertEnd(data)
            
    def Deleteatindex(self,ind):
        if ind<0 or ind >= self.getlength():
            return
        if ind==0:
            self.head=self.head.next
            
        count=0
        n=self.head
        while n:
            if (count== ind-1):
                n.next=n.next.next
            n=n.next
            count+=1
        
   
        
    
    def Printll(self):
        if self.head is None:
            print("linkedList is empty")
        
        n=self.head
        lstr=""
        while n is not None:
            lstr += str(n.data) + "-->"
            n=n.next
        print(lstr)
    

if _name=="main_":
    
# n=int(input("enter number of links"))
    ll= LinkedList()
    
    ll.insert_at_begining(20)
    ll.insert_at_begining(45)
    ll.insertEnd(10)
    ll.insert_at_begining(67)
    # ll.insertlist([1,4,56,4,35,6])
    ll.Printll()
    print( ll.getlength())
    ll.Deleteatindex(40)
    ll.Printll()
    ll.insertat(2,56)
    ll.Printll()