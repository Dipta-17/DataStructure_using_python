class Node:
    def __init__(self,value):
        self.info=value
        self.next=None
        self.prev=None
class circular_doublylinkedlist:
    def __init__(self):
        self.start=None
    
    def insertion(self,v):
        n=Node(v)
        if self.start==None:
            self.start=n
            self.start.next=n
            self.start.prev=n
        else:
            n.next=self.start
            temp=self.start
            temp.prev=n
            while temp.next!=self.start:
                temp=temp.next
            temp.next=n
            n.prev=temp
            self.start=n

    # delete from beginning
    def deletefrombeginning(self):
        temp=self.start
        while temp.next!=self.start:
            temp=temp.next
        self.start=self.start.next
        temp.next=self.start
        self.start.prev=temp
        del temp

    # delete from middle
    def deletefrommiddle(self,item):
        temp=self.start
        while temp.info!=item:
            prev=temp
            temp=temp.next
        prev.next=temp.next
        temp.next.prev=prev
        del temp

    # delete from end
    def deletefromend(self):
        temp=self.start
        while temp.next!=self.start:
            prev=temp
            temp=temp.next
        prev.next=self.start
        self.start.prev=prev
        del temp
        
    


    def display(self):
        if self.start==None:
            print("The list is empty")
            return
        else:
            a=self.start
            while a:
                print(a.info,end="-->")
                a=a.next
                if a==self.start:
                    break
            print("start")




d=circular_doublylinkedlist()
d.insertion(78)
d.insertion(64)
d.insertion(34)
d.insertion(21)
d.insertion(96)
d.insertion(20)
d.deletefrombeginning()
d.deletefrommiddle(34)
d.deletefromend()
d.display()


    