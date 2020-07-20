# python3
def has_path(graph: list, visited_nodes: list, start_node: int, end_node: int) -> int:
    visited_nodes.append(start_node)
    for (u, v) in graph:
        if u == start_node:
            if v not in visited_nodes:
                has_path(graph, visited_nodes, v, end_node)
        elif v == start_node:
            if u not in visited_nodes:
                has_path(graph, visited_nodes, u, end_node)
    return int(end_node in visited_nodes)


def read_input():
    line = input().split(" ")
    num_of_nodes, num_of_edges = int(line[0]), int(line[1])
    graph = []
    for i in range(num_of_edges):
        line = input().split(" ")
        edge = (int(line[0]), int(line[1]))
        graph.append(edge)
    line = input().split(" ")
    start_node, end_node = int(line[0]), int(line[1])

    return graph, start_node, end_node


if __name__ == '__main__':
    edges_list, start, end = read_input()
    print(has_path(edges_list, [], start, end))
