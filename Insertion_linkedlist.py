class Node:
 def __init__(self,value):
    self.info=value
    self.next=None
class linkedlist:
  def __init__(self):
    self.start=None

  # insert at bigining
  def insertatbegining(self,v):
    n=Node(v)
    if self.start==None:
        self.start=n
    else:
       n.next=self.start
       self.start=n 

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
      temp.next=n 

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
        
  # Display code
  def display(self):
    a=self.start
    while a:
      print(a.info, end="-->")
      a=a.next
    print("None")  


l=linkedlist()
l.insertatbegining(36)
l.insertatbegining(70)
l.insertatbegining(56)    
l.insertatmiddle(63,70)
l.insertatend(90)
l.display()


