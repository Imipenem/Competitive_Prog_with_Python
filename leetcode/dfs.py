import random

def dfs(graph, start):
    color = [-1] * len(graph)
    res = []
    
    for u in range(len(graph)):
        if color[u] == -1:
            res.append(u)
            color[u] = 1
            dfs_visit(graph,u,res,color)
    return res

def dfs_visit(graph,node,res,color):
    for v in graph[node]:
        if color[v] == -1:
            res.append(v)
            color[v] = 1
            dfs_visit(graph,v,res,color)

def dfsII(graph, start):
    color = [-1] * len(graph)
    res,stack = [],[]
    stack.append(start)
    color[start] = 1
    
    while stack:
        v = stack.pop()
        res.append(v)
        
    
        for node in graph[v][::-1]:
            if color[node] == -1:
                stack.append(node)
                color[node] = 1
    

    return res


if __name__ == '__main__':
    print("Hello")

