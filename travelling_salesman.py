from math import *
from random import randrange
from tkinter import *
import pygame


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


def main():
    root = Tk()
    resolution = [root.winfo_screenwidth(), root.winfo_screenheight()]
    screen = pygame.display.set_mode(resolution)
    nodes = generateNodes(10, 5, 0, resolution)

    running = True
    while running:
        screen.fill((0, 0, 0))
        drawScreen(nodes, screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
main()
