class Node:
    def __init__(self,value):
        self.info=value
        self.next=None
        self.prev=None
class doubly_linkedlist:
    def __init__(self):
        self.start=None
        # self.tail=None (optional   for backword print)
    # insert at begining
    def insertatbegining(self,v):
        n=Node(v)
        if self.start==None:
            self.start=n
            # self.tail=n  (optional for backword print)
        else:
            n.next=self.start
            self.start.prev=n
            self.start=n
    # insert at end
    def insertatend(self,v):
        n=Node(v)
        if self.start==None:
             self.start=n
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=n
            n.prev=temp

    # insert at middle
    def insertatmiddle(self,v,item):
        n=Node(v)
        if self.start==None:
            self.start=n
        else:
            temp=self.start
            while temp.info!=item:
                temp=temp.next
            n.next=temp.next
            temp.prev=n
            temp.next=n
            n.prev=temp      

    #display code
    def display(self):
        a=self.start
        while a:
            print(a.info, end="-->")
            a=a.next
        print(None)

    # It is a another way to print backword
    # def display2(self):
    #     a=self.tail
    #     while a:
    #         print(a.info ,end="-->")
    #         a=a.prev
    #     print(None)

d=doubly_linkedlist()
d.insertatbegining(20)
d.insertatbegining(34)
d.insertatbegining(67)
d.insertatend(40)
d.insertatmiddle(80,34)
d.display()