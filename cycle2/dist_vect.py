class Node:
    id = 0
    nodes = []
    def __init__(self, parents, parent_dists):
        self.id = Node.id
        self.parents = parents
        self.connected_to = []
        self.table = {str(self.id):0}
        Node.nodes.append(self)
        for i,parent in enumerate(self.parents):
            self.connected_to.append(parent)
            if parent!=None:
                self.table[str(parent.id)] = parent_dists[i]
                parent.table[str(self.id)] = parent_dists[i]
                parent.connected_to.append(self)
        Node.id+=1
    
    def update_neighbors(self):
        for child in self.connected_to:
            if child:
                for k,v in self.table.items():
                    if child.table.get(k) is None:
                        child.table[k] = v
                    else:
                        child.table[k] = min(child.table[k],child.table[str(self.id)]+v)
    
if __name__=='__main__':
    A = Node([None],[0])
    B = Node([A],[2])
    C = Node([B],[5])
    D = Node([A],[3])
    E = Node([D,B],[5,4])
    F = Node([E,C],[2,4])
    G = Node([F,C],[1,3])
    for _ in range(2):
        for node in Node.nodes:
            node.update_neighbors()
    for node in Node.nodes:
        print(f"Node {node.id} - {node.table}")
