class Node:
    id = 0
    nodes = []

    def __init__(self, parents, parent_dists):
        self.id = Node.id
        Node.nodes.append(self) 
        self.parents = parents
        self.connected_to = []
        self.is_visited = False
        self.table = {self:0}
        for i,parent in enumerate(self.parents):
            self.connected_to.append(parent)
            if parent:
                self.table[parent] = parent_dists[i]
                parent.connected_to.append(self)
                parent.table[self] = parent_dists[i]
        Node.id+=1
    
    def __str__(self):
        return f"{self.id}"
    
    def __repr__(self):
        return f"{self.id}"
    
    @staticmethod
    def reset_is_visited():
        for node in Node.nodes:
            node.is_visited = False
    
    @staticmethod
    def check_if_all_visited():
        for node in Node.nodes:
            if node.is_visited==False:
                return False
        return True
    
    @staticmethod
    def get_min_dist_node(node):
        min_val = None
        min_obj = None
        for child in node.connected_to:
            if child:
                if not(child.is_visited):
                    if min_val is None or node.table[child]<min_val:
                        min_val = node.table[child]
                        min_obj = child
        return min_obj
    
    def calculate(self):
        start_node = self
        while not(Node.check_if_all_visited()):
            start_node.is_visited = True
            min_obj = Node.get_min_dist_node(start_node)
            if min_obj:
                for child in min_obj.connected_to:
                    if child and not(child.is_visited):
                        if self.table.get(child) is None:
                            self.table[child] = self.table[min_obj]+min_obj.table[child]
                        else:
                            self.table[child] = min(self.table[child],self.table[min_obj]+min_obj.table[child])
                start_node = min_obj
            else:
                start_node = self
        return self.table
        


if __name__=='__main__':
    A = Node([None],[0])
    B = Node([A],[2])
    C = Node([B],[5])
    D = Node([A],[3])
    E = Node([D,B],[5,4])
    F = Node([E,C],[2,4])
    G = Node([F,C],[1,3])
    for node in Node.nodes:
        table = node.calculate()
        Node.reset_is_visited()
        print(f"{node.id}: {table}")
        