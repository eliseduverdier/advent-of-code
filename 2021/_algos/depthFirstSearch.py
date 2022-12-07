def depthFirstSearch(visitedGraph, graph, node, paths):
    if visitedGraph[node] > 0 and node == 'end':
        return node
    else:
        visitedGraph[node] += 1
        #print('>',node)
        for neighbour in graph[node]:
            paths.append([node, depthFirstSearch(visitedGraph, graph, neighbour, paths) ])
        return paths
