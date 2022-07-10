# 1 Dijkstra's Algorithm transport network connecting eight cities
# and the distances between them is shown.
# Find the shortest routes between the following cities (16 points):
# •	Between cities A and H.
# •	Between cities A and F.
# •	Between cities D and H.
# •	Between cities B and F.


from queue import PriorityQueue


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight


def dijkstra(graph, start_vertex):
    D = {v: float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


def as_index(input_char):
    return ord(input_char) - ord("A")


adj_list = {
    'A': {'B': 1, 'C': 2},
    'B': {'C': 1, 'E': 2, 'D': 5},
    'C': {'D': 2, 'E': 1, 'F': 4},
    'D': {'E': 3, 'F': 6, 'G': 8},
    'E': {'F': 3, 'G': 7},
    'F': {'G': 5, 'H': 2},
    'G': {'H': 6},
}
routes = [
    ["A", "H"],
    ["A", "F"],
    ["D", "H"],
    ["B", "F"]
]

for start_V, end_V in routes:
    g = Graph(8)
    for fromV, toVs in adj_list.items():
        for toV, cost in toVs.items():
            g.add_edge(as_index(fromV), as_index(toV), cost)

    D = dijkstra(g, as_index(start_V))
    print(f"Route from city {start_V} to city {end_V} is {D[as_index(end_V)]}")