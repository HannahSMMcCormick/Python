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
            
            
            
    def has_cycle(head):
        
        slow = head 
        fast = head 
        
        while fast and fast.next:
            
            slow = slow.next 
            fast = fast.next.next
            
            if slow == fast:
                return True
            
        return False
            
            


list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.print_list()

list1.prepend(0)
list1.print_list()

list1.delete_node(2)
list1.print_list()

cycle_list = LinkedList()
cycle_list.append(1)
cycle_list.append(2)
cycle_list.append(3)
cycle_list.append(4)

cycle_list.print_list()

#Create a cycle 
cycle_list.head.next.next.next.next = cycle_list.head

print(LinkedList.has_cycle(cycle_list.head))

