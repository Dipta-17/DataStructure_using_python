class Node:
    def __init__(self,value):
        self.info=value
        self.next=None
        self.prev=None
class dubbly_linkedlist:
    def __init__(self):
        self.start=None
    # for insert value in doubbly linklist
    def insertion(self,v):
        n=Node(v)
        if self.start==None:
            self.start=n
        else:
            n.next=self.start
            self.start.prev=n
            self.start=n
    # delete from begining
    def deletefrombegining(self):
        temp=self.start
        self.start=temp.next
        self.start.prev=None
        del temp

    #delete from middle
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
        while temp.next!=None:
            prev=temp
            temp=temp.next
        prev.next=None
        del temp

    def display(self):
        a=self.start
        while a :
            print(a.info,end="-->")
            a=a.next

d=dubbly_linkedlist()
d.insertion(20)
d.insertion(60)
d.insertion(76)
d.insertion(30)
d.insertion(56)
d.insertion(43)
d.deletefrombegining()
d.deletefrommiddle(76)
d.deletefromend()
d.display()

    