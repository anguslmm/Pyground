import heapq
from collections import deque
from typing import List, Generator, Set, Tuple

import math

from DataAndAlgorithms.heap import Heap


class GraphNode:
    def __init__(self, name: str, neighbors=None, coords:Tuple[int]=(0, 0)):
        if neighbors is None:
            neighbors = dict()
        self.neighbors = neighbors
        self.name = name
        self.coords:Set[GraphNode] = coords
        for node in self.neighbors.keys():
            if self not in node.neighbors.keys():
                node.neighbors[self] = self.neighbors[node]

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name

class Graph:
    def __init__(self, nodes: Set[GraphNode]=set()):
        self.nodes = nodes

    def dijkstra(self, start: GraphNode, goal: GraphNode, debug=False):
        visited: Set[GraphNode] = set()
        came_from = dict([(x, None) for x in self.nodes])
        h = Heap([(x, math.inf) for x in self.nodes])
        h.change_cost(start, 0)
        while len(h):
            current = h.pop()
            if debug: print('Visiting: ' + str(current.val))
            visited.add(current)
            for neighbor in current.val.neighbors.keys():
                new_cost = h[current.val].cost + current.val.neighbors[neighbor]
                if h[neighbor].cost > new_cost:
                    h.change_cost(neighbor, new_cost)
                    came_from[neighbor] = current.val
        current = goal
        path = []
        while current is not None:
            path.append(current)
            current = came_from[current]
        path = list(reversed(path))
        if debug:
            print([x.name for x in path])
            print([' (' + key.name + '<-' + came_from[key].name + ') ' for key in came_from.keys() if came_from[key]])
        return path


    def bfs_shortest(self, start: GraphNode, goal: GraphNode) -> List[GraphNode]:
        q = deque([(start, [start])])
        steps = 0
        while q:
            steps += 1
            (vertex, path) = q.popleft()
            for next in vertex.neighbors.keys() - set(path):
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
            for next in vertex.neighbors.keys() - set(path): # nexts = [b, c]
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
    b = GraphNode('b',{a: 1})
    c = GraphNode('c')
    d = GraphNode('d', {a: 10, c: 1})
    e = GraphNode('e', {b: 10})
    f = GraphNode('f', {b: 1, d: 5})
    g = GraphNode('g', {d: 10})
    h = GraphNode('h', {e: 10, f: 1})
    i = GraphNode('i', {f: 10, g: 1, h: 1})
    j = GraphNode('j', {g: 20})
    graph = Graph({a, b, c, d, e, f, g, h, i, j})
    for x in graph.bfs_shortest(a, j):
        print(str(x) + '|',end='')
    print('\n***')
    for x in graph.dfs_shortest(a, j):
        for y in x:
            print(str(y) + '|',end='')
        print()

    print("Dijkstra time:")
    print([x.name for x in graph.dijkstra(a, j)])