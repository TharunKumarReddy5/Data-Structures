class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def addBeginning(self,new_data):
        nd = Node(new_data)
        nd.next = self.head
        self.head = nd

    def addLast(self,new_data):
        nd = Node(new_data)
        if self.head==None:
            self.head=nd
            return

        last = self.head
        while (last.next):
            last = last.next
        last.next = nd

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def rotate(self,k):
        if k==0:
            print('No rotation required as k = 0')
            return
        current=self.head
        i=1
        while i<k and current!=None:
           current = current.next
           i+=1

        if current==None:
            print('Number of rotations is more than the Linked List size')
            return

        kNode=current
        while current.next!=None:
            current=current.next

        current.next=self.head
        self.head = kNode.next
        kNode.next = None

if __name__=='__main__':
    llist = LinkedList()
    for i in range(10,60,10):
        llist.addLast(i)
    llist.printList()
    llist.rotate(3)
    llist.printList()
