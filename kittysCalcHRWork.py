# https://www.hackerrank.com/challenges/kittys-calculations-on-a-tree/problem


class Queue:

    def __init__(self):
        self.items = []
        
    def __repr__(self):
        rep = 'Queue: '
        for value in self.items:
            rep = rep + str(value) + ' '
        return rep

    def add(self, value: int):
        self.items.append(value)
        
    def remove(self):
        if len(self.items) == 0:
            return None
        else:
            value = self.items[0]
            self.items = self.items[1:]
            return value


def print_graph(graph):
    length = len(graph)
    for i in range(length):
        for j in range(length):
            print(graph[i][j], end=" ")
        print("")


def run():
    graph = []
    n = int(input('Enter the no of nodes in the tree: '))
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(False)
        graph.append(row)

    while True:
        a = int(input('Enter 1st node of edge: '))
        b = int(input('Enter 2nd node of edge: '))
        if a == b:
            print('Cannot have edge from one node to the same node')
        elif a >= n or b >= n:
            print('Index out of range')
        else:
            if is_cycle_formed(graph, (a, b)) == True:
                print('Given edge cannot be added, it forms a cycle')
            else:
                graph[a][b] = True
                graph[b][a] = True
        choice = input('Enter another edge? (y/n/g) ')
        if choice == 'n':
            break
        elif choice == 'g':
            print_graph(graph)
    
    while True:
        choice = input('Find distance between nodes: ')
        if choice == 'n':
            break
        else:
            nodeA = int(input('Enter 1st node: '))
            nodeB = int(input('Enter 2nd node: '))
            print(f'Distance between nodes {nodeA} and {nodeB} is {count_distance(graph, (nodeA, nodeB))}')

def is_cycle_formed(graph: list, nodes: tuple):
    nodeA = nodes[0]
    nodeB = nodes[1]
    
    checked = set()
    to_check = Queue()
    to_check.add(nodeA)

    length = len(graph)
    value = to_check.remove()
    
    while value is not None and value not in checked:
        # print(f'checking {value} in row')
        checked.add(value)
        for i in range(length):
            if graph[value][i] == True:
                if i == nodeB:
                    return True
                else:
                    if i not in checked:
                        to_check.add(i)
        value = to_check.remove()
    return False


def count_distance(graph: list, nodes: tuple) -> int:
    nodeA = nodes[0]
    nodeB = nodes[1]

    if nodeA == nodeB:
        return 0

    checked = set()
    to_check = Queue()
    to_check.add((nodeA, 1))

    length = len(graph)
    value = to_check.remove()

    while value is not None and value[0] not in checked:
        print(f'checking {value[0]} in row')
        checked.add(value[0])
        for i in range(length):
            if graph[value[0]][i] == True:
                if i == nodeB:
                    return value[1] # distance
                else:
                    if i not in checked:
                        to_check.add((i, value[1] + 1))
        value = to_check.remove()
    
    return -1


def get_pairs(nodes: set):
    nodes = list(nodes)
    length = len(nodes)

    pairs = []

    for i in range(length - 1):
        for j in range(i+1, length):
            pairs.append((nodes[i], nodes[j]))
    
    return pairs

# run()
print(get_pairs({4,5,6,7}))