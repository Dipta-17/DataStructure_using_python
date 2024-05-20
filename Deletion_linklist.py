class Node:
    def __init__(self,value):
        self.info=value
        self.next=None
class linkedlist:
    def __init__(self):
        self.start=None
    def insertfrombeginning(self,v):
        n=Node(v)
        if self.start == None:
            self.start=n
        else:
            n.next=self.start
            self.start=n

    # Delete from bigining
    def deletefrombigining(self):
        temp=self.start
        self.start=temp.next
        del temp
    
    # Delete from middle
    def deletefrommiddle(self,item):
        temp=self.start
        while temp.info!=item:
            prev=temp
            temp=temp.next
        prev.next=temp.next
        del temp
        # b=temp.next
        # prev.next=b
        # del temp

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
        while a:
            print(a.info)
            a=a.next
        print(None)

l=linkedlist()
l.insertfrombeginning(36)
l.insertfrombeginning(57)
l.insertfrombeginning(34)
l.insertfrombeginning(90)
l.insertfrombeginning(89)
l.insertfrombeginning(42)
l.insertfrombeginning(12)
l.deletefrombigining()
l.deletefrommiddle(57)
l.deletefromend()
l.display()