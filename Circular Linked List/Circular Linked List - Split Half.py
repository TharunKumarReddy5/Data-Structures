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

    def splitHalf(self,a,b):
        if self.last==None:
            return
        i,j = 1,0
        temp1 = self.last
        print("")
        temp = self.last.next
        while temp!=self.last:
            i=i+1
            temp=temp.next
        if i%2==0:
            while j<i//2:
                j+=1
                temp1 = temp1.next
            a.last = temp1
            lst = temp1.next
            a.last.next = self.last.next
            a.traverse()
            print("")
            b.last = self.last
            b.last.next = lst
            b.traverse()

        if i % 2 != 0:
            while j < (i // 2)+1:
                j += 1
                temp1 = temp1.next
            a.last = temp1
            lst = temp1.next
            a.last.next = self.last.next
            #a.traverse()
            #print("")
            b.last = self.last
            b.last.next = lst
            #b.traverse()

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
    last = clist.addToEmpty(6)
    last = clist.addBegin(2)
    last = clist.addBegin(1)
    last = clist.addLast(8)
    last = clist.addLast(10)
    last = clist.addAfter(4,2)
    last = clist.addAfter(7,6)
    clist1 = circularLinkedList()
    clist2 = circularLinkedList()
    clist.traverse()
    clist.splitHalf(clist1,clist2)
    clist1.traverse()
    print("")
    clist2.traverse()