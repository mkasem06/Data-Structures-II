class Graph:
    def __init__(self):
        # We use a dictionary to act as our Adjacency List.
        # Keys will be the nodes, values will be lists of (neighbor, weight) tuples.
        self.graph = {}

    def add_node(self, node):
        """Helper to initialize a node in the dictionary if it doesn't exist."""
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, u, v, weight=0, directed=False):
        """Adds an edge to the graph."""
        self.add_node(u)
        self.add_node(v)

        # Add the connection from u to v
        self.graph[u].append((v, weight))

        # If it's an undirected graph (like Prim's), add the connection from v back to u
        if not directed:
            self.graph[v].append((u, weight))

    def display(self):
        """Prints the adjacency list so you can verify the structure."""
        for node, edges in self.graph.items():
            print(f"{node}: {edges}")

# ==========================================
# MK'S TEST MASTER SETUP (From Assignment Images)
# ==========================================

if __name__ == "__main__":
    
    # ---------------------------------------------------------
    # 1. SETUP FOR EYAD (Topological Sort)
    # Directed Acyclic Graph, No Weights
    # ---------------------------------------------------------
    print("--- Testing Topological Sort Graph (Eyad's Task) ---")
    topo_graph = Graph()
    
    # Edges extracted directly from Image 1 
    edges_topo = [
        (7, 5), (7, 6),
        (5, 2), (5, 4),
        (6, 4), (6, 3),
        (2, 1), (3, 1),
        (1, 0)
    ]
    
    # Add all directed edges to Eyad's graph
    for u, v in edges_topo:
        topo_graph.add_edge(u, v, directed=True)

    topo_graph.display()
    print("\n[Eyad's function will run here later]")
    # Eyad will write his function and test it like this:
    # result = topological_sort(topo_graph.graph)
    # print(f"Expected: 7 6 5 4 3 2 1 0")
    # print(f"Actual:   {result}\n")


    # ---------------------------------------------------------
    # 2. SETUP FOR PRIM'S ALGORITHM (Teammate's Task)
    # Undirected Graph, Weighted Edges
    # ---------------------------------------------------------
    print("--- Testing Prim's MST Graph (Teammate's Task) ---")
    mst_graph = Graph()
    
    # Edges and weights extracted directly from Image 2
    edges_mst = [
        ('a', 'b', 4), ('a', 'h', 8),
        ('b', 'c', 8), ('b', 'h', 11),
        ('c', 'd', 7), ('c', 'f', 4), ('c', 'i', 2),
        ('d', 'e', 9), ('d', 'f', 14),
        ('e', 'f', 10),
        ('f', 'g', 2),
        ('g', 'h', 1), ('g', 'i', 6),
        ('h', 'i', 7)
    ]
    
    # Add all undirected, weighted edges to the MST graph
    for u, v, w in edges_mst:
        mst_graph.add_edge(u, v, weight=w, directed=False)

    mst_graph.display()
    print("\n[Prim's function will run here later]")
    # Your teammate will write their function and test it like this:
    # mst_result = prims_algorithm(mst_graph.graph, start_node='a')
    # print(f"MST Edges: {mst_result}")