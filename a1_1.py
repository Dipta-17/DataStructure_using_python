class linearlist:
     def __init__(self,lineararray,datatype):
          self.lineararray=lineararray
          self.size=len(lineararray)
          self.datatype=datatype
          for i in lineararray:
               if type(i)!=datatype:
                    print("not similar datatype")
                    exit()
                    

            
     def display(self):
          print("the array is:",self.lineararray)


     def linearsearch(self,item):
          self.item=item
          for i in range(self.size):
             if self.lineararray[i]==item:
                  print (i)
             i+=1
          return -1
     
     
     def insert(self,new_item):
          self.new_item=new_item
          self.lineararray.append(new_item)
          print(self.lineararray)
     
     
     def delete(self,item):
          self.item=item
          self.lineararray.remove(item)
          print(self.lineararray)    

l=[10,20,30.5,70]
d=int
obj=linearlist(l,d)
obj.display()
obj.linearsearch(20)
obj.insert(60)
obj.delete(30)
