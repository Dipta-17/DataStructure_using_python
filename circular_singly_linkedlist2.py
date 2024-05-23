# Deletion oparation of circular singly linkedlist
class Node:
    def __init__(self,value):
        self.info=value
        self.next=None

class circularlinklist:
    def __init__(self):
        self.start=None
    
    def insetion(self,v):
        n=Node(v)
        if self.start==None:
            self.start=n
            self.start.next=n
        else:
            n.next=self.start
            temp=self.start
            while temp.next!=self.start:
                temp=temp.next
            temp.next=n
            self.start=n

    # Delete from begining
    def deletefrombegining(self):
        temp=self.start
        while temp.next!=self.start:
            temp=temp.next
        self.start=self.start.next
        temp.next=self.start

    # delete from middle
    def deletefrommiddle(self,item):
        temp=self.start
        while temp.info!=item:
            prev=temp
            temp=temp.next
        prev.next=temp.next
        del temp

    # delete from end
    def deletefromend(self):
        temp=self.start
        while temp.next!=self.start:
            prev=temp
            temp=temp.next
        prev.next=self.start
        del temp
        


    def display(self):
        if self.start==None:
            print("The list is empty")
            return
        a=self.start
        while a:
            print(a.info,end="-->")
            a=a.next
            if a==self.start:
                break
        print("start")

q=circularlinklist()
q.insetion(30)
q.insetion(45)
q.insetion(30)
q.insetion(70)
q.insetion(89)
q.insetion(34)
q.deletefrombegining()
q.deletefrommiddle(70)
q.deletefromend()
q.display()
