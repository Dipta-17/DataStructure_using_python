'''1. Write a program of Linear Search. Define a class for LinearList, containing the data members
Lineararray, datatype, and size of the list, and the following methods:
• __init__() initialize the object, it should contain homogeneous data.
• display() display the list of items
• LinearSearch() search the given item
• Inert() insert new item
• Delete delete the specified item'''

class linearlist:
    def __init__(self,lineararray,datatype):
        self.lineararray=lineararray
        self.size=(len(lineararray))
        self.datatype=datatype
        for i in self.lineararray:
            if type(i)!=datatype:
                print("not similar datatype")
                exit()

    def display(self):  
        print("the array is:",self.lineararray)  

    def linearsearch(self,item):
        self.item=item
        for i in range(self.size):
            if self.lineararray[i]==item:
                print(i)
            
        return -1
    
    def insert(self,new_item):
       self.new_item=new_item
       self.lineararray.append(new_item)
       print(self.lineararray)
    
    def delete(self,item):
        self.item=item
        self.lineararray.remove(item)
        print(self.lineararray) 
    

l=[10,20,30.5,40,50,70]
d=int
obj=linearlist(l,d)
obj.display()
obj.linearsearch(40)
obj.insert(60)
obj.delete(70)


    



       
