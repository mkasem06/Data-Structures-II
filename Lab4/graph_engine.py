import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, u, v, weight=0, directed=False):
        self.add_node(u)
        self.add_node(v)
        self.graph[u].append((v, weight))
        if not directed:
            self.graph[v].append((u, weight))

    def display(self):
        for node, edges in self.graph.items():
            print(f"{node}: {edges}")

def prims(graph, start):
    visited = set()
    mst_edges = []
    total_weight = 0
    pq = [(0, start, None)]
    while pq:
        weight, node, parent = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        if parent is not None:
            mst_edges.append((parent, node, weight))
            total_weight += weight
            print(f"  Added edge: {parent} --> {node}  (weight {weight})")
        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, neighbor, node))
    return mst_edges, total_weight

def topological_sort(graph):
    from collections import deque
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor, _ in graph[node]:
            in_degree[neighbor] += 1
    queue = deque()
    for node in in_degree:
        if in_degree[node] == 0:
            queue.append(node)
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor, _ in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return result

if __name__ == "__main__":
    print("--- Testing Topological Sort Graph ---")
    topo_graph = Graph()
    edges_topo = [
        (7, 5), (7, 6),
        (5, 2), (5, 4),
        (6, 4), (6, 3),
        (2, 1), (3, 1),
        (1, 0)
    ]
    for u, v in edges_topo:
        topo_graph.add_edge(u, v, directed=True)
    topo_graph.display()
    result = topological_sort(topo_graph.graph)
    print(f"Topological Sort: {result}")
    print(f"Expected:         [7, 6, 5, 4, 3, 2, 1, 0]")
    print("--- Testing Prim's MST Graph ---")
    mst_graph = Graph()
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
    for u, v, w in edges_mst:
        mst_graph.add_edge(u, v, weight=w, directed=False)
    mst_graph.display()
    print("\n[Running your Prim's function]")
    mst_result, final_weight = prims(mst_graph.graph, 'a')
    print(f"Final MST Edges: {mst_result}")
    print(f"Final Weight: {final_weight}")
