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

    def addMiddle(self,previous_node,new_data):
        if previous_node==None:
            print('Node must be in Linked List')
        nd = Node(new_data)
        nd.next = previous_node.next
        previous_node.next = nd

    def swapNodes(self, x, y):
        if x == y:
            return

        # Search for x (keep track of prevX and CurrX)
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next

        # Search for y (keep track of prevY and currY)
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next

        # If either x or y is not present, nothing to do
        if currX == None or currY == None:
            return
        # If x is not head of linked list
        if prevX != None:
            prevX.next = currY
        else:  # make y the new head
            self.head = currY

        # If y is not head of linked list
        if prevY != None:
            prevY.next = currX
        else:  # make x the new head
            self.head = currX

        # Swap next pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    def deleteNode(self,key):
        temp = self.head
        if temp!=None:
            if temp.data==key:
                self.head = temp.next
                temp = None
                return

        while (temp!=None):
            if temp.data==key:
                break
            prev = temp
            temp=temp.next

        if temp==None:
            print('Node not found in Linked List to delete')
            raise Exception("Can't delete Node")
            return

        prev.next = temp.next
        temp = None

    def deleteNodeByPosition(self,position):
        if self.head==None:
            return
        temp = self.head

        if position==0:
            self.head=temp.next
            temp=None
            return

        i=0

        while (temp!=None):
            if (i==position):
                break
            i = i + 1
            prev = temp
            temp=temp.next

        if temp==None:
            print('Position not found in Linked List')
            raise Exception("Can't delete Node")

        prev.next = temp.next
        temp = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def listLength(self):
        temp = self.head
        count=0
        while (temp!=None):
            count=count+1
            temp=temp.next
        return count

if __name__=='__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    llist.printList()
    llist.addBeginning(0)
    llist.printList()
    llist.addLast(4)
    llist.printList()
    llist.addMiddle(second,2.5)
    llist.printList()
    llist.swapNodes(1,4)
    llist.printList()