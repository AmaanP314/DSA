class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
# class  LinkedList:
#     def __init__(self,value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length  = 1


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
        
       

    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if  self.length == 0:
            self.head = None
            self.tail = None
        return temp
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length  -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self,index):
        if  index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True 
        return False
    
    def insert(self,index,value):
        if  index < 0 or index > self.length:
            return True
        if  index == 0:
            return self.prepend(value)
        if index == self.length:
            return  self.append(value)
        
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self,index):
        if  index < 0 or index >= self.length:
            return None
        if  index == 0:
            return self.pop_first()
        if index == self.length-1:
            return  self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next =  temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        
        while temp is not None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
    def arr(self,arr):
        for item in arr:
            self.append(item)
    
    
    
    ############################### QUESTIONS ###############################
    
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
    
    def partition_list(self, x):
        temp1 = LinkedList()
        temp2 = LinkedList()
        for i in range(self.length):
            if(self.get(i).value == x or self.get(i).value > x):
                temp2.append(self.get(i).value)
            else:
                temp1.append(self.get(i).value)
        
        # temp1.pop_first()
        # temp2.pop_first()
                
        temp1.tail.next = temp2.head
        
        return temp1
    
    def remove_duplicates(self):
        temp = self.head
        mySet = set()
        myLL = LinkedList()

        while temp:
            mySet.add(temp.value)
            temp = temp.next
        for item in mySet:
            myLL.append(item)
        return myLL
    
    
    



def find_kth_from_end(ll, k):
    if ll.head is None or k <= 0:
        return None
    
    slow = ll.head
    fast = ll.head
    
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
   
    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow.value if slow is not None else None

        
            

# Example usage:
# ll = LinkedList(0)
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.append(5)
# ll.append(6)
# ll.append(7)
# ll.insert(3,2.718)
# ll.insert(5,3.14)
# ll.remove(2)
# print(ll.length)

# ll.print_list() 

# print(find_kth_from_end(ll,-1))

# print(ll.find_middle_node().value)


# ll.reverse()


# ll2 = LinkedList(1)
# ll2.append(4)
# ll2.append(3)
# ll2.append(2)
# ll2.append(5)
# ll2.append(2)


ll = LinkedList()

# for item in [3, 1, 4, 2, 5]:
#     ll.append(item)

# ll.partition_list(5).print_list()

ll.arr([3,1,4,1,5,9])
ll.print_list()
# print("\n")
# ll.reverse()
# ll.print_list()
print("\n")
ll.remove_duplicates().print_list()




# ll.partition_list(3).print_list()



    

            
            
            
            
        

   








