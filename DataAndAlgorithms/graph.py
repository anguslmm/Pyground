import heapq
from collections import deque
from typing import List, Generator, Set, Tuple


class GraphNode:
    def __init__(self, name: str, neighbors=set(), coords:Tuple[int]=(0,0)):
        self.neighbors = neighbors
        self.name = name
        self.coords:Set[GraphNode] = coords
        for node in self.neighbors:
            if self not in node.neighbors:
                node.neighbors.add(self)

    def __str__(self):
        return self.name

class Graph:
    def __init__(self, nodes: Set[GraphNode]=set()):
        self.nodes = nodes


    def bfs_shortest(self, start: GraphNode, goal: GraphNode) -> List[GraphNode]:
        q = deque([(start, [start])])
        steps = 0
        while q:
            steps += 1
            (vertex, path) = q.popleft()
            for next in vertex.neighbors - set(path):
                if next == goal:
                    print(steps)
                    return path + [next]
                else:
                    q.append((next, path + [next]))

    def dfs_paths(self, start: GraphNode, goal: GraphNode) -> Generator[List[GraphNode], None, None]:
        stack = [(start, [start])] # [(a, [a])]
        steps = 0
        while stack:
            steps += 1
            (vertex, path) = stack.pop() # a, [a]
            for next in vertex.neighbors - set(path): # nexts = [b, c]
                if next == goal:
                    print(steps)
                    steps = 0
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))

    def dfs_shortest(self, start: GraphNode, goal: GraphNode) -> List[List[GraphNode]]:
        paths = list(self.dfs_paths(start, goal))
        if len(paths) == 0:
            return []
        result = [paths[0]]
        minlen = len(paths[0])
        for a in paths[1:]:
            if len(a) < minlen:
                minlen = len(a)
                result = [a]
            if len(a) == minlen:
                result.append(a)
        return result

if __name__ == "__main__":
    a = GraphNode('a')
    b = GraphNode('b',{a})
    c = GraphNode('c')
    d = GraphNode('d', {a, c})
    e = GraphNode('e', {b})
    f = GraphNode('f', {b, d})
    g = GraphNode('g', {d})
    h = GraphNode('h', {e, f})
    i = GraphNode('i', {f, g, h})
    j = GraphNode('j', {g})
    graph = Graph({a, b, c, d, e, f, g, h, i})
    for x in graph.bfs_shortest(a, j):
        print(str(x) + '|',end='')
    print('\n***')
    for x in graph.dfs_shortest(a, j):
        for y in x:
            print(str(y) + '|',end='')
        print()