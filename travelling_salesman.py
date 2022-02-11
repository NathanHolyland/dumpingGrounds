from math import *
from random import randrange
from re import A
from tkinter import *
from turtle import Screen
from numpy import Infinity
import random
import time
import pygame

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

class Node:
    def __init__(self, x, y, r, w):
        self.x = x
        self.y = y
        self.r = r
        self.w = w

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.x, self.y), self.r, self.w)

    def distTo(self, node):
        return sqrt((self.x - node.x)**2 + (self.y-node.y)**2)


def generateNodes(number_of_nodes, radius, width, resolution):
    nodeList = []
    for i in range(number_of_nodes):
        coord = [randrange(resolution[0]*0.1, resolution[0]-resolution[0]*0.1),
                 randrange(resolution[1]*0.1, resolution[1]-resolution[1]*0.1)]
        new_node = Node(coord[0], coord[1], radius, width)
        nodeList.append(new_node)
    return nodeList


def drawScreen(nodeList, surface):
    for node in nodeList:
        node.draw(surface)


def drawRoute(route, colour, slow, surface):
    points = []
    for node in route:
        coordinates = [node.x, node.y]
        points.append(coordinates)
    if slow:
        for i in range(len(points)-1):
            pygame.draw.line(surface, colour, points[i], points[i+1], 2)
            time.sleep(0.05)
            pygame.display.flip()
    else:
        pygame.draw.lines(surface, colour, False, points, 2)


def greedySearch(nodeList):
    nodes_to_visit = nodeList.copy()
    route = [nodeList[0]]
    distance = 0
    current_node = nodeList[0]
    nodes_to_visit.remove(current_node)
    while len(nodes_to_visit) != 0:
        shortest_path = nodes_to_visit[0]
        for node in nodes_to_visit:
            if current_node.distTo(node) < current_node.distTo(shortest_path):
                shortest_path = node
        distance += current_node.distTo(shortest_path)
        nodes_to_visit.remove(shortest_path)
        route.append(shortest_path)
        current_node = shortest_path
    return route, distance
    

def antOptimise(nodeList, iterations, dstBias, pheromoneIntensity, pheromoneBias, decay, numAnts, screen):
    pheromoneTrails = {}
    for start in nodeList:
        pheromoneTrails[start] = {}
        for end in nodeList:
            if start == end:
                continue
            pheromoneTrails[start][end] = 1

    bestRoute = [None, Infinity]

    for i in range(iterations):
        for dictionary in pheromoneTrails:
            for element in pheromoneTrails[dictionary]:
                pheromoneTrails[dictionary][element] *= 1-decay
        for i in range(numAnts):
            unvisited = nodeList.copy()
            distance = 0
            current = nodeList[random.randint(0,len(nodeList)-1)]
            route = [current]
            unvisited.remove(current)
            for i in range(len(unvisited)):
                selection = []
                weights = []
                for node in unvisited:
                    dst = current.distTo(node)
                    desirability = 1/(dst**dstBias) * (pheromoneTrails[current][node]**pheromoneBias)
                    selection.append(node)
                    weights.append(desirability)
                choice = random.choices(selection, weights=weights, k=1)[0]
                distance += current.distTo(choice)
                route.append(choice)
                unvisited.remove(choice)
                current = choice
            pheromoneStrength = pheromoneIntensity/distance
            for i in range(len(route)-1):
                pheromoneTrails[route[i]][route[i+1]] += pheromoneStrength
            if distance < bestRoute[1]:
                bestRoute = [route, distance]
                screen.fill((0,0,0))
                drawRoute(bestRoute[0], (0, 0, 255), False, screen)
                distanceText = font.render(("Distance: "+str(bestRoute[1])), True, (255, 255, 255))
                screen.blit(distanceText,(0,0))
                pygame.display.flip()
    return bestRoute[0], bestRoute[1]

def selection(algorithm, nodes, screen):
    name = "Invalid Input"
    if algorithm == "G":
        name = "Greedy Search"
        route, distance = greedySearch(nodes)
        return route, distance, name
    if algorithm == "A":
        name = "Ant Optimisation"
        # (Iterations, dstBias, pheromoneIntensity, pheromoneBias, decay, antsPerGroup)
        route, distance = antOptimise(nodes, 30, 3, 1, 1, 0.7, 100, screen)
        return route, distance, name
            
            
def main():
    print("Which Algorithm Should Be Used \n G | Greedy Search \n A | Ant Optimise")
    algorithm = input()
    print("Should the route draw instantly? Y | N")
    slow = input()
    root = Tk()
    resolution = [root.winfo_screenwidth(), root.winfo_screenheight()]
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Travelling Salesman Problem")



    nodes = generateNodes(200, 10, 2, resolution)
    #antOptimise(nodes, 5)

    start_time = time.time()
    route, distance, name = selection(algorithm, nodes, screen)
    end_time = time.time()
    elapsed = round(end_time - start_time, 3)
    text1 = font.render(("Total Distance: "+str(round(distance))), True, (255, 255, 255))
    text2 = font.render(("Algorithm Used: "+name), True, (255, 255, 255))
    text3 = font.render(("Time Taken: "+str(elapsed)), True, (255, 255, 255))

    running = True

    #first draw
    if slow == "N":
        screen.fill((0, 0, 0))
        drawScreen(nodes, screen)
        drawRoute(route, [200, 50, 50], True, screen)
        pygame.display.flip()
    while running:
        screen.fill((0, 0, 0))
        drawRoute(route, [200, 50, 50], False, screen)
        drawScreen(nodes, screen)
        screen.blit(text1,(0,0))
        screen.blit(text2,(0,resolution[1]*0.03))
        screen.blit(text3,(0,resolution[1]*0.06))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
main()
