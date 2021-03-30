class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class circularLinkedList():
    def __init__(self):
        self.last = None

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
    clist.traverse()