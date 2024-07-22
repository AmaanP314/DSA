class HashTable:
    def __init__(self,size = 7):
        self.data_map = [None] * size
    
    def __hash(self,key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*23 % len(self.data_map))
        return my_hash
    
    def print_list(self):
        for i,value in enumerate(self.data_map):
            print(f"{i}: {value}")
            
    def set_table(self,key,value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])
        
    def get_item(self,key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if  self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
        
    def keys(self):
        keys = []
        for data in self.data_map:
            if data is not None:
                for item in range(len(data)):
                    keys.append(data[item][0])
        return keys
    
    
ht = HashTable()
ht.set_table("a",1)
ht.set_table("b",2)
ht.set_table("c",3)
ht.set_table("d",4)

ht.print_list()
print("\n")
print(ht.keys()) # should return 1



# print(ord("a"))
        