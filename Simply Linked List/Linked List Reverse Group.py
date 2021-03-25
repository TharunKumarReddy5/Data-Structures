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

    def reverse(self,head,k):
        if head==None:
            return None
        current = head
        next = None
        prev = None
        i=0
        while (i<k and current!=None):
            nxt = current.next
            current.next=prev
            prev = current
            current = nxt
            i=i+1

        if nxt!=None:
            head.next = self.reverse(nxt,k)
        return prev


if __name__=='__main__':
    llist = LinkedList()
    for i in range(10,60,10):
        llist.addLast(i)
    llist.printList()
    llist.head = llist.reverse(llist.head,3)
    llist.printList()
