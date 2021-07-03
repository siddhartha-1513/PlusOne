#here we do plus 1 to the linked list last item , first we make linked list , then we print the linkedlist after that we reverse that linkedlist for our convience and print that reverse list . after that add  1 to the first item of the node.data and take care of carry too.after finsh operation we again reverse the last linkedlist to get our output. 
class Node:
    def __init__(self,d,n=None):
        self.data=d 
        self.next_node=n 
        
    def get_data(self):
        return self.data 
    
    def set_data(self,d):
        self.data=d 
        
    def set_next(self,n):
        self.next_node=n 
        
    def get_next(self):
        return self.next_node
        
    def to_string(self):
        return "Node value :" + str(self.data)
        
    def has_next(self):
        if self.get_next() is None:
            return False
        return True
        
    
        
        
class LinkedList:
    def __init__(self,r=None):
        self.root= r  
        self.size=0 
        
    def get_size(self):
        return self.size 
    
    def reverse(self):
        temp=self.root
        prev_node=None
        current=None
        while temp is not None:
            current=temp.get_next()
            temp.set_next(prev_node)
            prev_node=temp
            temp=current
            
        self.root=prev_node
        return self.root
        
    def add(self,d):
        new_node=Node(d,self.root)
        self.root=new_node
        self.size+= 1  
        
        
        
    def plusone(self):
        temp=self.root
        prev_node=None
        if temp.get_data()!=9:
            temp.set_data(temp.get_data()+1)
            return
        while temp and temp.get_data()==9:
            temp.set_data(0)
            prev_node=temp
            temp=temp.get_next()
            
        if temp is None:
            new_node=Node(1)
            prev_node.set_next(new_node)
        elif prev_node is not None:
            prev_node.get_next().set_data(prev_node.get_next().get_data()+1)
        
            
            
            
            
    def remove(self,d):
        temp=self.root
        prev_node=None
        while temp:
            if temp.get_data()==d:
                if prev_node:
                    prev_node.set_next(temp.get_next())
                else:
                    self.root=temp.get_next()
                    
                self.size=self.size-1
                return True
            else:
                prev_node=temp
                temp=temp.get_next()
        return False
        
    def find(self,d):
        temp=self.root
        while temp:
            if temp.get_next()==d:
                return d  
            else: 
                temp=temp.get_next()
        return None
        
    def print_list(self):
        if self.root is None:
            return 
        temp=self.root
        print(temp.to_string())
        while temp.has_next():
            temp=temp.get_next()
            print(temp.to_string())
            

            
            
        
myList = LinkedList()
myList.add(9)
myList.add(2)
myList.add(8)
myList.add(7)
myList.add(9)
print("our list is here before reverse operation.")
myList.print_list()
print("-------Our reversed list is here ------")

myList.reverse()
myList.print_list()
print("we apply plus one operation before print the output")
myList.plusone()
print("-----------------")
myList.print_list()
print("--------------again we reversed the last linkedlist to get our final output. ------------------")
myList.reverse()
myList.print_list()
#myList.remove(8)
print("size="+str(myList.get_size()))
#print("Remove 15", myList.remove(15))
print("size="+str(myList.get_size()))
print("Find 25", myList.find(25))
myList.print_list() 
