from random import shuffle
from typing import Generic, TypeVar, List, Tuple

T = TypeVar('T')

class HeapNode(Generic[T]):
    def __init__(self, val: T, cost: int=0):
        self.val = val
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __le__(self, other):
        return self.cost <= other.cost

    def __eq__(self, other):
        return self.cost == other.cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __ge__(self, other):
        return self.cost >= other.cost


class Heap(Generic[T]):
    def __init__(self, heap: List[Tuple[T, int]]):
        self.__heap = [HeapNode(x, i) for x, i in set(heap)]
        self.__dict = dict([(x.val, x) for x in self.__heap])
        self.heapify()

    def __len__(self):
        return len(self.__heap)

    def __getitem__(self, key: int):
        return self.__heap[key]

    def __iter__(self):
        return self.__heap.__iter__()

    def __str__(self):
        result = ''
        l = 0
        for i, x in enumerate(self.__heap):
            if i == l + 1:
                l = (l + 1)*2
                result += '| '
            result += str(x.val) + ' '
        return result

    def pop(self):
        h = self.__heap
        ll = len(h) - 1
        h[ll], h[0] = h[0], h[ll]
        res = h.pop()
        self.sift_down(0)
        return res

    def push(self, node: HeapNode[T]):
        if node not in self.__heap:
            self.__heap.append(node)
        self.__dict[node.val] = node
        self.heapify()

    def change_cost(self, val: T, new_cost: int):
        self.__dict[val].cost = new_cost
        self.heapify()

    def heapify(self):
        h = self.__heap
        current_parent = self.get_parent(len(h) - 1)  # start with last parent (parent of last leaf)
        while current_parent >= 0:
            self.sift_down(current_parent)
            current_parent -= 1

    def sift_down(self, i: int):
        h = self.__heap
        ll = len(h) - 1 # last leaf
        i1, i2 = self.get_children(i) # indexes of children
        while i1 <= ll:
            least = i1 # least is the first child by default
            if i2 <= ll and h[i2] < h[i1]: # if the second child exists and is the least, set it so
                least = i2
            if h[least] < h[i]:  # if the least of those is less than the parent, swap them
                h[i], h[least] = h[least], h[i]
                i = least # move or index to the newly swapped child so we keep checking down the line
                i1, i2 = self.get_children(i) # assign our new children now so that we break if there are none
            else: # if we didn't swap, we're done
                break


    def get_parent(self, i: int) -> int:
        return (i-1)//2

    def get_children(self, i: int) -> Tuple[int, int]:
        return (i*2 +1, i*2 +2)

if __name__ == "__main__":
    print('TESTING THE HEAP:')
    a = [(str(x), x) for x in range(1, 40)]
    shuffle(a)
    print('Random array of numbers:')
    print(' '.join([s for s, v in a]))
    heap = Heap(a)
    print('That array in a heap:')
    print(heap)
    print('Pushing 0 into that heap:')
    heap.push(HeapNode('0', 0))
    print(heap)
    print('Changing 10 to cost -1')
    heap.change_cost('10', -1)
    print(heap)
    print('That array heap sorted:')
    for x in range(len(heap)):
        print(heap.pop().val + ' ', end='')