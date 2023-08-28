from main import get_node_list

node_list = get_node_list()
visited_list = []
start_node = 1

def bfs(index):
   for next_node in node_list[visited_list[index] - 1].next_node_list:
      if next_node.number not in visited_list:
         visited_list.append(next_node.number)

   if len(node_list) - 1 != index:
      bfs(index + 1)

visited_list.append(node_list[start_node - 1].number)
bfs(0)
print(visited_list)