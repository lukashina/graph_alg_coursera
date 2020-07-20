# python3

def get_cc_number(edge_list: list, nodes: set):
    visited = []
    cc = 0
    for v in nodes:
        if v not in visited:
            cc = cc + 1
            visited = explore(v, edge_list, visited)
    return cc


def explore(v: int, edge_list: list, visited: list):
    visited.append(v)
    for (u, w) in edge_list:
        if u == v:
            if w not in visited:
                explore(w, edge_list, visited)
        elif w == v:
            if u not in visited:
                explore(u, edge_list, visited)
    return visited


def read_input():
    line = input().split(" ")
    num_of_nodes, num_of_edges = int(line[0]), int(line[1])
    nodes = set([i for i in range(1, num_of_nodes + 1)])
    edge_list = []
    for i in range(num_of_edges):
        line = input().split(" ")
        node1, node2 = int(line[0]), int(line[1])
        edge_list.append((node1, node2))

    return edge_list, nodes


if __name__ == '__main__':
    graph, nodes_set = read_input()
    print(get_cc_number(graph, nodes_set))
