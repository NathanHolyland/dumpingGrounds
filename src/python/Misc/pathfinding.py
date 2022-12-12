from math import *


class Node:
    def __init__(self, coord, parent, end):
        self.coord = coord
        self.parent = parent
        dx = abs(end[0] - coord[0])
        dy = abs(end[1] - coord[1])
        self.h = ((sqrt((dx ** 2) + (dy ** 2))) // 1)*10
        if parent:
            self.f = ((parent.f - parent.h) + 1) + self.h
        else:
            self.f = self.h


def aStar(start, end, maze):
    closedList = []
    openList = []
    startNode = Node(start, None, end)
    current = startNode
    while current.coord != end:
        # generates new valid nodes
        for node in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            stepCoord = [current.coord[0] + node[0], current.coord[1] + node[1]]
            if (stepCoord[0] < 0) or (stepCoord[0] > 21):
                continue
            if (stepCoord[1] < 0) or (stepCoord[1] > 21):
                continue
            if maze[stepCoord[1]][stepCoord[0]] == "1": 
                continue
            if current.parent:
                if current.parent.coord == stepCoord:
                    continue

            newNode = Node(stepCoord, current, end)
            openList.append(newNode)

        # selects the next best node
        current = openList[0]

        for x in openList:
            if x.f < current.f:
                current = x
            if x.f == current.f:
                if x.h < current.h:
                    current = x
        openList.remove(current)
        closedList.append(current)

    # finds the path routing from the parents of the end node
    path = [current.coord]
    step = current
    while step.coord != startNode.coord:
        step = step.parent
        path.append(step.coord)
    path.reverse()
    return path
