def bfs(graph, start):
    color = [-1] * len(graph) # -1: this node is colored white, 1 this node is colored black

    queue,res = [],[]
    queue.append(start)

    while queue:
        v = queue.pop(0) #number of node (index)
        if color[v] == -1: #we have not visited the node, its white
            color[v] = 1
            res.append(v)
        for node in graph[v]:
            if color[node] == -1: queue.append(node) #add node only if we dont have visited this node before
    return res


if __name__ == '__main__':
    graph = [
             [2,1],
             [],
             [],
             ]
    result = bfs(graph, 0)
    print(result)
