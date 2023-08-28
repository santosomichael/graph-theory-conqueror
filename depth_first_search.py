from main import get_node_list

node_list = get_node_list()
visited_list = []
start_node = 1

def dfs(node):
    if node.number in visited_list: return    
    visited_list.append(node.number)

    for next_node in node.next_node_list:
        dfs(next_node)

dfs(node_list[start_node - 1])
print(visited_list)