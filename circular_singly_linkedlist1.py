class Node:
    def __init__(self,value):
        self.info=value
        self.next=None
class circular_linkedlist:
    def __init__(self):    
        self.start=None

    def insertatbeginning(self,v):
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
    def insertatend(self,v):
        n=Node(v)
        if self.start==None:
            self.start=n
            self.start.next=n
        else:
            temp=self.start
            while temp.next!=self.start:
                  temp=temp.next
            temp.next=n
            n.next=self.start
    
    def insertbeforespecifieditem(self,v,item):
        n=Node(v)
        if self.start==None:
            self.start=n
            self.start.next=n
        else:
            temp=self.start
            while temp.info!=item:
                 prev=temp
                 temp=temp.next
            n.next=temp
            prev.next=n

    def insertafterspecifieditem(self,v,item):
        n=Node(v)
        if self.start==None:
            self.start=n
            self.start.next=n
        else:
            temp=self.start
            while temp.info!=item:
                 prev=temp
                 temp=temp.next
            n.next=temp.next
            temp.next=n
                    
             
    def display(self):
        if self.start==None:
         print("list is empty")
         return
        a=self.start
        while a:
            print(a.info,end="-->")
            a=a.next
            if a==self.start:
                break
        print("start")    
        

c=circular_linkedlist()
c.insertatbeginning(49)
c.insertatbeginning(56)
c.insertatbeginning(12)
c.insertatend(90)
c.insertbeforespecifieditem(78,56)
c.insertafterspecifieditem(78,56)
c.display()