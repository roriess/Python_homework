class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes: 
            self.nodes[node] = []

    def add_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            self.nodes[node1].append(node2)

    def get_neighbors(self, node):
        return self.nodes.get(node, [])
    
    def dfs(self) -> list:
        visited = []
        stack = []

        start_node = list(self.nodes.keys())[0]
        stack.insert(0, start_node)

        while stack:
            node = stack.pop(0)
            if node not in visited:
                visited.append(node)
                
            for neighbor in self.get_neighbors(node):
                if neighbor not in visited and neighbor not in stack:
                    stack.insert(0, neighbor)

        return visited  
