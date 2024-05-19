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


     def binarysearch(self,item):
          self.item=item
          self.beg=0
          self.end=self.size-1
          for i in range(self.size):
              mid=(self.beg+self.end)//2
              if  self.lineararray[mid]==item:
                   return mid
              elif(item>=mid):
                   self.beg=mid+1
              else:
                   self.end=mid-1
          return -1
              
     
     
     def insert(self,new_item):
          self.new_item=new_item
          self.lineararray.append(new_item)
          print(self.lineararray)
     
     
     def delete(self,item):
          self.item=item
          self.lineararray.remove(item)
          print(self.lineararray)    

l=[10,20,30,70]
d=int
obj=linearlist(l,d)
obj.display()
obj.binarysearch(20)
obj.insert(60)
obj.delete(30)