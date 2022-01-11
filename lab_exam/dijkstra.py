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
        self.routes = {}
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
        d_done = False
        f_done = False
        path = f"{self.id}"
        while not(Node.check_if_all_visited()):
            start_node.is_visited = True
            min_obj = Node.get_min_dist_node(start_node)
            if min_obj:
                for child in min_obj.connected_to:
                    if child and not(child.is_visited):
                        if self.table.get(child) is None:
                            self.table[child] = self.table[min_obj]+min_obj.table[child]
                            path+=f" {min_obj.id} {child.id}"
                        else:
                            self.table[child] = min(self.table[child],self.table[min_obj]+min_obj.table[child])
                            path+=f" {min_obj.id} {child.id}"
                        if(self.id==2 and min_obj.id in [3,5]):
                            if min_obj.id==3:
                                if not(d_done):
                                    print(f"C's table After visiting D: {self.table}\n")
                                    d_done = True
                            else:
                                if not(f_done):
                                    print(f"C's table After visiting F: {self.table}\n")
                                    f_done = True
                start_node = min_obj
            else:
                for child in start_node.connected_to:
                    if child:
                        start_node = child
                        break
        # print(f"Path: {path}")
        return self.table
        


if __name__=='__main__':
    A = Node([None],[0])
    B = Node([A],[4])
    C = Node([A,B],[5,2])
    D = Node([A,C],[3,6])
    E = Node([D,C],[3,4])
    F = Node([E,C,B],[2,4,3])
    G = Node([F,B],[5,4])
    for node in Node.nodes:
        table = node.calculate()
        Node.reset_is_visited()
        print(f"{node.id}: {table}\n")
    # table = B.calculate()
    # print(f"{table}")
        