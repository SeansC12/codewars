class Node():
    def __init__(self):
        self.next = None

node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

# def loop_size(node):
#     nodes = list()
#     return calculate_loop_size(node, nodes)

# def calculate_loop_size(node, node_list):
#     if node in node_list:
#         return len(node_list) - node_list.index(node)
#     else:
#         node_list.append(node)
#         return calculate_loop_size(node.next, node_list)

def loop_size(node):
    nodes = set()
    current = node
    another_current = node
    i = 0
    while True:
        if current in nodes:
            duplicate = current
            break
        nodes.add(current)
        current = current.next
    print(duplicate)
    
    while True:
        i += 1
        if another_current == duplicate:
            break
        another_current = another_current.next
    print(len(nodes), i)
    return len(nodes) - i + 1

print(loop_size(node1))