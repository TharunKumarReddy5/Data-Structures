class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class circularLinkedList():
    def __init__(self):
        self.last = None

    def addToEmpty(self,data):
        if (self.last!=None):
            return
        temp = Node(data)
        self.last = temp
        self.last.next = self.last
        return self.last

    def addBegin(self,data):
        if (self.last==None):
            return self.addToEmpty(data)
        temp = Node(data)
        temp.next = self.last.next
        self.last.next = temp
        return self.last

    def addAfter(self,data,item):
        if self.last==None:
            return
        temp = Node(data)
        p = self.last.next
        while p!=None:
            if p.data == item:
                temp.next = p.next
                p.next = temp
                if p==self.last:
                    self.last = temp
                    return self.last
                else:
                    return self.last
            p = p.next

        if p==None:
            print('Item not found in Linked List')
            return

        temp.next = Node(data)


    def addLast(self,data):
        if (self.last==None):
            return self.addToEmpty(data)
        temp = Node(data)
        temp.next = self.last.next
        self.last.next = temp
        self.last = temp

    def sortInsert(self,dt):
        temp = self.last.next
        prev = self.last
        while (temp.next!=self.last.next and temp.data<=dt):
            prev = temp
            temp=temp.next

        if temp==self.last:
            if temp.data > dt:
                self.addAfter(dt, prev.data)
            else:
                self.addLast(dt)

        elif temp==self.last.next:
            if temp.data > dt:
                self.addBegin(dt)
            else:
                self.addAfter(dt, prev.data)

        else:
            self.addAfter(dt, prev.data)

    def traverse(self):
        if (self.last==None):
            print ('List is empty')
            return
        temp = self.last.next
        while(temp):
            print(temp.data,end = " ")
            temp=temp.next
            if (temp==self.last.next):
                break

if __name__=='__main__':
    clist = circularLinkedList()
    last = clist.addLast(3)
    last = clist.addLast(7)
    last = clist.addLast(9)
    last = clist.addLast(11)
    last = clist.sortInsert(5)
    clist.traverse()