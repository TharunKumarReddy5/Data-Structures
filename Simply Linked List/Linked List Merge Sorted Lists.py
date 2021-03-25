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

def mergeLists(a,b):
    dummy=Node(0)
    tail = dummy
    while True:
        if a==None:
            tail.next=b
            break
        if b==None:
            tail.next=a
            break
        if a.data<=b.data:
            tail.next=a
            a=a.next
        else:
            tail.next=b
            b=b.next
        tail=tail.next
    return dummy.next

if __name__=='__main__':
    llistA = LinkedList()
    llistB = LinkedList()
    llistA.addLast(1)
    llistA.addLast(3)
    llistA.addLast(7)
    llistB.addLast(2)
    llistB.addLast(10)
    llistB.addLast(20)
    llistA.printList()
    llistB.printList()
    llistA.head = mergeLists(llistA.head,llistB.head)