N, M = map(int, input().split())
Graph = [[] for _ in range(N)]
 
for i in range(M):
    # 0 index
    a, b, direction = map(int, input().split())
    a -= 1
    b -= 1
    Graph[a].append((b, direction))
    Graph[b].append((a, direction))

def node_int_to_string(node):
    node = str(node)
    temp = len(node)
    fill = 5 - temp
    fill_text = "0" * fill
    node = fill_text + node
    return node
 
def node_string_to_int(node):
    index = 0
    for i in node:
        if i == 0:
            pass
        else:
            index = i
            break
    node = int(node[index:])
    return node
 

def return_image_and_moveable_node(image, action):
    """
    Graph
    input image(node), action(direction)
    return image and moveable_direction

    """
    currecnt_node = node_string_to_int(image[:5])
    moveable_nodes = Graph[currecnt_node]
    next_node = float('inf')
    for i in moveable_nodes:
        if i[1] == action:
            next_node = i[0]
    next_image = node_int_to_string(next_node) + str(action)
    next_moveable_nodes = Graph[next_node]
    return next_image, next_moveable_nodes