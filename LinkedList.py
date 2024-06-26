class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)
        # commets

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


    def reverse(self):
        if self.head is None:
            return "LinkedList is Empty"
        if self.get_length==1:
            return self.head.data
        
        itr =self.head

        l=""

        while itr:
            l=( "<--" + str(itr.data)  + l ) if itr.next else (str(itr.data)  + l )
            itr=itr.next

        return l
    
    def reverselinks(self):
        if self.head is None:
            return "LinkedList is Empty"
        if self.get_length==1:
            return self.head.data
        
        itr =self.head
        prev=None

        while (itr is not None ):
            front=itr.next
            itr.next=prev
            prev=itr
            itr=front
           

        self.head=prev
        
        return prev
    

    def print(self):
        
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        # print("Recursive approch is ",ll.reverseLinkedList(self.head))
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        
        print(llstr)
    
    def reverseLinkedListusingrecursion(self,head):

        if head.next is None or head is None:
            return head
        newhead = self.reverseLinkedListusingrecursion(head.next)
        front=head.next
        front.next=head
        head.next=None
        self.head=newhead   #this will set the head for overall linkedlist to newhead.
        return newhead
    
    def deleteduplicate(self):
        pointer= self.head
        pointer = self.head
        if self.head is not None:
            while pointer.next is not None:
                if pointer.data == pointer.next.data:
                    pointer.next = pointer.next.next
                else:
                    pointer = pointer.next
        return self.head
        

        





if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_values(["banana","mango","grapes","orange"])
    # ll.insert_at(1,"blueberry")
    # ll.remove_at(2)
    # ll.print()

    ll.insert_values([1,1,2,3,4,4,5,5,5,6,6])

    # ll.insert_at_end(67)
    ll.print()
    print(ll.reverse())
    print(ll.reverselinks())
    ll.print()
    ll.reverseLinkedListusingrecursion(ll.head)
    ll.print()
    print(ll.deleteduplicate())
    ll.print()


