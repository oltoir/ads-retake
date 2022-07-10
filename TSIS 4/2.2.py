def search(fromV, toV, graph, costs, parents):
    next_node = fromV

    while next_node != toV:
        for neighbor in graph[next_node]:
            if graph[next_node][neighbor] + costs[next_node] > costs[neighbor]:
            # if graph[next_node][neighbor] + costs[next_node] < costs[neighbor]:
                costs[neighbor] = graph[next_node][neighbor] + costs[next_node]
                parents[neighbor] = next_node
            del graph[neighbor][next_node]
        del costs[next_node]

        next_node = max(costs, key=costs.get)
        # next_node = min(costs, key=costs.get)

    return parents


def backpedal(fromV, toV, search_result):
    current_node = toV
    path = [toV]
    reverse_path = []

    while current_node != fromV:
        path.append(search_result[current_node])
        current_node = search_result[current_node]

    for i in range(len(path)):
        reverse_path.append(path[-i - 1])

    return reverse_path


adj_list = {
    'A': {'C': 5, 'D': 1, 'E': 2},
    'B': {'H': 1, 'G': 3},
    'C': {'A': 5, 'D': 3, 'I': 2,},
    'D': {'A': 1, 'C': 3, 'H': 2},
    'E': {'A': 2, 'F': 3},
    'F': {'E': 3, 'G': 1},
    'G': {'B': 3, 'F': 1, 'H': 2},
    'H': {'B': 1, 'D': 2, 'G': 2, 'I': 2},
    'I': {'C': 2, 'H': 2}
}

inf = float('inf')
# costs = {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf, 'G': inf, 'H': inf, 'I': inf}
costs = {'A': 0, 'B': -inf, 'C': -inf, 'D': -inf, 'E': -inf, 'F': -inf, 'G': -inf, 'H': -inf, 'I': -inf}

parents = {}
result = search('A', 'B', adj_list, costs, parents)
# print(f"shortest path={backpedal('A', 'B', result)}")
print(f"longest path={backpedal('A', 'B', result)}")
