# 3 Develop an algorithm to check whether the given graph is bipartite
# (a graph whose set of vertices can be divided into two parts such that each edge
# of the graph connects each vertex from one part to some vertex of the other part,
# i.e. there are no edges between vertices of the same part of the graph).

def isBipartite(vertex, adj):
    color = [-1] * vertex
    my_queue = []

    for i in range(vertex):
        if color[i] == -1:
            my_queue.append([i, 0])
            color[i] = 0

            while len(my_queue) != 0:
                p = my_queue[0]
                my_queue.pop(0)

                current_vertex = p[0]
                color_current_vertex = p[1]

                for vert in adj[current_vertex]:
                    if color[vert] == color_current_vertex:
                        return False

                    if color[vert] == -1:
                        if color_current_vertex == 1:
                            color[vert] = 0
                        else:
                            color[vert] = 1
    return True


V, E = 4, 8
adj_list = [
    [0, 3],
    [0, 8],

    [1, 2],

    [2, 1],
    [2, 5],

    [3, 0],

    [4, 5],

    [5, 2],
    [5, 4],

    [6, 9],

    [7, 4],

    [8, 9],
    [8, 0],

    [9, 6],
    [9, 8],
]
print("Yes" if isBipartite(V, adj_list) else "No")
