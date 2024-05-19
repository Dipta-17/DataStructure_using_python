class Node:
    def __init__ (self,value):
        self.info=value
        self.next=None
start=Node(24)


start.next=Node(12)
print(start.info)
print(start.next)
print(start.next.info)
print(start.next.next)
start.next.next=Node(20)
print(start.info)
print(start.next.next.info)
