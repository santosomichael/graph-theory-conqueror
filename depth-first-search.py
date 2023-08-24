class Node:
  def __init__(self, number, next_list):
    self.number = number
    self.next_list = next_list

edge_list = [
    (1, 2),
    (2, 4), (2, 5),
    (3, 7), (3, 10), (3, 4),
    (4, 2), (4, 3), (4, 5), (4, 8), (4, 9),
    (5, 2), (5, 4), (5, 6), (5, 9),
    (6, 5), (6, 9),
    (7, 3), (7, 10),
    (8, 4), (8, 9), (8, 11),
    (9, 4), (9, 6), (9, 8), (9, 11), (9, 12),
    (10, 3), (10, 7),
    (11, 8), (11, 9),
    (12, 9),
    (13, 7)
]

all_edge_set = set(edge[0] for edge in edge_list)

def print_node_list(node_list):
    for node in node_list:
        print(f"Number : {node.number}")
        print(f"Next   : {node.next_list}\n")

# fill the node_list with the tree node
node_list = []
now_index = 0
for edge in all_edge_set:
    temp_next_list = []
    # looping to all edge list to take the connection node
    while(now_index != len(edge_list)):
        now_edge = edge_list[now_index]
        if now_edge[0] == edge:
            temp_next_list.append(now_edge[1])
            now_index += 1
        else:
            break
    
    node = Node(edge, temp_next_list)
    node_list.append(node)

print_node_list(node_list)

# replace the number with actual node
for node in node_list:
    temp_next_list = []
    for num in node.next_list:
        temp_next_list.append(node_list[num])
    
    node.next_list = temp_next_list

print_node_list(node_list)

















