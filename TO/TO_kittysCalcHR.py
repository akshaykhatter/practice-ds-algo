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

def get_pairs(nodes: set):
    
    nodes = list(nodes)
    length = len(nodes)

    pairs = []

    if len(nodes) == 0:
        return pairs

    for i in range(length - 1):
        for j in range(i+1, length):
            pairs.append((nodes[i], nodes[j]))
    
    return pairs

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

first_line = str(input()).split(" ")
no_of_nodes = int(first_line[0])
no_of_sets = int(first_line[1])

graph = []
for _ in range(no_of_nodes):
    row = []
    for _ in range(no_of_nodes):
        row.append(False)
    graph.append(row)

for i in range(no_of_nodes - 1):
    edge_line = str(input()).split(" ")
    nodeA = int(edge_line[0]) - 1
    nodeB = int(edge_line[1]) - 1

    graph[nodeA][nodeB] = True
    graph[nodeB][nodeA] = True

for _ in range(no_of_sets):
    no_elements_in_set = int(input())
    elements_line = str(input()).split(" ")
    elements_set = set()

    for i in range(no_elements_in_set):
        elements_set.add(int(elements_line[i]) - 1)
    
    pairs_list = get_pairs(elements_set)

    intermediate_result = 0

    for pair in pairs_list:
        distance = count_distance(graph, pair)
        intermediate_result = intermediate_result + ((pair[0] + 1) * (pair[1] + 1) * distance)
    
    result = intermediate_result % (10**9 + 7)
    print(result)
