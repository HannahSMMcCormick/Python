class Node:
    
    def __init__(self,data):
        
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None 
        
    def append(self,data):
        
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
        
    def prepend(self, data):
        
        #Create a new node
        new_node = Node(data)
        
        #Set the next(reference/pointer) of the new node to the current head
        new_node.next = self.head
        
        #set the head of the linked list to the new node
        self.head = new_node
        
    def delete_node(self,key):
        
        temp = self.head
        
        if temp and temp.data == key:
            
            self.head = temp.next 
            
            temp = None 
            
            return 
        
        prev = None
        
        while temp and temp.data != key:
            
            prev = temp
            temp = temp.next
            
            
        if temp is None:
            
            return
        
        
        prev.next = temp.next 
        temp = None
        
    def print_list(self):
        
        temp = self.head
        while temp:
            
            print(temp.data)
            temp = temp.next
            
            


list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.print_list()

list1.prepend(0)
list1.print_list()

list1.delete_node(2)
list1.print_list()

