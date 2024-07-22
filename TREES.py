class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# class BinarySearchTree:
#     def __init__(self,value):
#         new_node  = Node(value)
#         self.root = new_node
        
### OR ###

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
    def contains(self,value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
############################ rBST  ############################
    def __r_contains(self,node,value):
        if node == None:
            return False
        elif value == node.value:
            return True
        elif value < node.value:
            return self.__r_contains(node.left,value)
        elif value > node.value:
            return self.__r_contains(node.right,value)
        pass
        
        
    def r_contains(self,value):
        return self.__r_contains(self.root,value)
    
    def __r_insert(self,node,value):
        if node == None:
            return Node(value)
        if value < node.value:
            node.left = self.__r_insert(node.left,value)
        if value > node.value:
            node.right = self.__r_insert(node.right,value)
        return node
        pass
    
    def r_insert(self,value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root,value)
        
    def __delete_node(self,node,value):
        if node.value == None:
            return None
        if value < node.value:
            node.left = self.__delete_node(node.left,value)
        if value > node.value:
            node.right = self.__delete_node(node.right,value)
        else:
            if node.left == None and node.right == None:
                return None
            elif node.left == None:
                node = node.left
            elif node.right == None:
                node = node.right
            else:
                subtree_min = self.min_value(node.right)
                node.value = subtree_min
                node.right = self.__delete_node(node.right,subtree_min)
        return node
    
    def min_value(self,node):
        while node.left is not None:
            node = node.left
        return node

    def delete_node(self,value):
        self.__delete_node(self.root,value)
        
    ##### BFS #####    
    def BFS(self):
        current = self.root
        queue = []
        results = []
        queue.append(current)
        while len(queue) > 0:
            current = queue.pop(0)
            results.append(current.value)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
            return results
        
    ##### DFS #####
    def DFS_pre(self):
        results = []
        
        def traverse(node):
            results.append(node.value)
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
            
        traverse(self.root)
        return results
    
    def DFS_post(self):
        results = []
        
        def traverse(node):
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
            results.append(node.value)
            
        traverse(self.root)
        return results
        
    def DFS_in(self):
        results = []
        
        def traverse(node):
            if node.left is not None:
                traverse(node.left)
            results.append(node.value)
            if node.right is not None:
                traverse(node.right)
            
        traverse(self.root)
        return results    
                 
mytree = BinarySearchTree()
mytree.insert(50)
mytree.insert(25)
mytree.insert(75)
mytree.insert(7)
mytree.insert(80)

print(mytree.root.value)
print(mytree.root.left.value)
print(mytree.root.right.value)

# print(mytree.contains(2521))  
print(mytree.r_contains(50))

print(mytree.DFS_pre())
print(mytree.DFS_post())
print(mytree.DFS_in())

      