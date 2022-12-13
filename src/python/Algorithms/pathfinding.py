def indexOf(node, routes):
    for i in range(len(routes)):
        if routes[i][0] == node:
            return i

def distanceOf(node, routes):
    for route in routes:
        if route[0] == node:
            return route[1]
    return None

def pathOf(node, routes):
    for route in routes:
        if route[0] == node:
            return route[2]
    return None

def replace(node, routes, new_route):
    i = indexOf(node, routes)
    routes[i] = new_route

def findSmallest(routes, unvisited):
    smallest = None
    for route in routes:
        if not (route[0] in unvisited):
            continue
        if route[1] == -1:
            continue
        if smallest == None:
            smallest = route
        elif route[1] < smallest[1]:
            smallest = route
    if smallest is None:
        return None
    return smallest[0]

def djikstras(startNode, endNode, adjList, pathReturn=True, distanceReturn=False, routesReturn=False, countUnreachable=False):
    # adjList = {Node: (Edge, Edge, Edge...)} 
    # Edge = (Node, dist)
    unvisited = list(adjList.keys()) #these keys could literally be anything
    routes = [] #(node, distance, path)
    for node in unvisited:
        routes.append((node, -1, [])) #-1 indicates unknown or infinity
    
    replace(startNode, routes, (startNode, 0, []))
    currentNode = startNode
    while len(unvisited) != 0:
        dist = distanceOf(currentNode, routes)
        path = pathOf(currentNode, routes)
        neighbours = adjList[currentNode]
        for edge in neighbours:
            if distanceOf(edge[0], routes) == -1 or edge[1]+dist < distanceOf(edge[0], routes):
                replace(edge[0], routes, (edge[0], edge[1]+dist, path+[currentNode]))
        unvisited.remove(currentNode)
        currentNode = findSmallest(routes, unvisited)
        if currentNode is None:
            break
    returnStatement = []
    if pathReturn:
        returnStatement.append(pathOf(endNode, routes))
    if distanceReturn:
        returnStatement.append(distanceOf(endNode, routes))
    if routesReturn:
        returnStatement.append(routes)
    if countUnreachable:
        returnStatement.append(len(unvisited))
    if len(returnStatement) == 1:
        return returnStatement[0]
    if len(returnStatement) == 0:
        return None
    return returnStatement

if __name__ == "__main__":
    adjList = {
        "a": [("b", 1), ("d", 1), ("c", 1)],
        "b": [("a", 1), ("d", 1)],
        "c": [("a", 1)],
        "d": [("e", 1), ("b", 1), ("a", 1)],
        "e": [("d", 1)]
        }
    path = djikstras("e", "b", adjList)
    print(path)