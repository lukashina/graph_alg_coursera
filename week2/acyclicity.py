# python3


class Node:
    def __init__(self, idx: int, pre: int, post: int) -> None:
        self.idx = idx
        self.pre = pre
        self.post = post

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Node):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.idx == o.idx and self.pre == o.pre and self.post == o.post

    def __str__(self) -> str:
        return "Node(idx=" + str(self.idx) + ", pre=" + str(self.pre) + ", post=" + str(self.post) + ")"


class Graph:
    def __init__(self) -> None:
        self.edges, self.nodes = self._read_from_console()
        self.visited = {node.idx: False for node in self.nodes}
        self.clock = 1

    def _read_from_console(self):
        line = input().split(" ")
        num_of_nodes, num_of_edges = int(line[0]), int(line[1])
        nodes = self._create_nodes(num_of_nodes)
        edge_list = self._create_edges_list(num_of_edges, nodes)
        return edge_list, nodes

    @staticmethod
    def _create_nodes(num_of_nodes):
        return [Node(i, 0, 0) for i in range(1, num_of_nodes + 1)]

    @staticmethod
    def _create_edges_list(num_of_edges, nodes):
        edge_list = []
        nodes_by_idxs = {node.idx: node for node in nodes}
        for i in range(num_of_edges):
            line = input().split(" ")
            node1_idx, node2_idx = int(line[0]), int(line[1])
            edge_list.append((nodes_by_idxs[node1_idx], nodes_by_idxs[node2_idx]))
        return edge_list

    def check_acyclicity(self):
        self._revert()
        self.dfs()
        self.visited = {node.idx: False for node in self.nodes}
        visited_backup = self.visited.copy()
        has_cycle = False

        self.nodes.sort(key=lambda x: x.post, reverse=True)
        self._revert()
        for node in self.nodes:
            if not self._is_visited(node):
                self.explore(node)
                if self._num_of_visited_nodes() - self._num_of_visited_nodes(visited_backup) > 1:
                    has_cycle = True
                    break
                visited_backup = self.visited.copy()

        return int(has_cycle)

    def _revert(self):
        self.edges = [(v, u) for (u, v) in self.edges]

    def dfs(self):
        for node in self.nodes:
            if not self._is_visited(node):
                self.explore(node)

    def explore(self, node: Node):
        self._visit(node)
        node = self._previsit(node)
        for (u, v) in self.edges:
            if u == node:
                if not self._is_visited(v):
                    self.explore(v)
        node = self._postvisit(node)
        return node

    def _visit(self, node: Node):
        self.visited[node.idx] = True

    def _previsit(self, node: Node):
        node.pre = self.clock
        self.clock = self.clock + 1
        return node

    def _is_visited(self, node: Node):
        return self.visited[node.idx]

    def _postvisit(self, node: Node):
        node.post = self.clock
        self.clock = self.clock + 1
        return node

    def _num_of_visited_nodes(self, visited_nodes=None):
        if visited_nodes is None:
            visited_nodes = self.visited
        return len([1 for k, v in visited_nodes.items() if v])


if __name__ == '__main__':
    print(Graph().check_acyclicity())
