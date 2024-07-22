class Graph:
    def __init__(self):
        self.adj_list = {}
        
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])
    
    def add_vertex(self,v):
        if v not in self.adj_list.keys():
            self.adj_list[v] = []
            return True
        return False
    
    def add_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and  v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v1].append(v2)
            return True
        return False
    
    def remove_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and  v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v1].remove(v2)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self,v):
        if  v in self.adj_list.keys():
            for others in self.adj_list[v]:
                self.adj_list[others].remove(v)
            del self.adj_list[v]
            return True
        return False
        
            
    
    
            
    
