#! /usr/bin/env python3

from environment import Environment
from queue import PriorityQueue
from checkIntersect import do_intersect
import math
import numpy as np


def heuristic(a, b):
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


def greedySearch(env):
    #
    # TODO: return a path from start to goal using greedy search
    #
    return []


def uniformCostSearch(env):
    #
    # TODO
    #
    # visited = []
    # queue = PriorityQueue()
    # queue.put((0, [env.goal]))
    # # visited.append(home)
    #
    # while not queue.empty():
    #
    #     node = queue.get()
    #     # print ("Node:",node)
    #     visited = node[1]
    #     current = node[1][len(node[1]) - 1]
    #     # current = node[1][0]
    #     # print ("Current:",current)
    #     if env.start in node[1]:
    #         print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
    #         break
    #
    #     cost = node[0]
    #
    #     neighbors = findsuccessor(current, env)
    #     for neighbor in neighbors:
    #         if neighbor in visited:
    #             continue
    #         temp = node[1][:]
    #         # print ("Temp:",temp)
    #         temp.append(neighbor)
    #         # print ("Temp append neighbor:",temp)
    #         queue.put((cost + env[current][neighbor], temp))
    return []


def astarSearch(env):
    frontier = PriorityQueue()
    frontier.put(env.start, 0)

    print("start", str((env.start.x, env.start.y)))
    # initial the dicts
    came_from = {env.start: None}
    cost_so_far = {env.start: 0}
    while not frontier.empty():
        current = frontier.get()
        print("type of current1")
        print(current)
        print(type(current))

        if current == env.goal:
            break

        neighbors = findsuccessor(current, env)

        for next in neighbors:
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(env.goal, next)
                frontier.put((next.x, next.y), priority)  # todo  这里把vector2D改成了tuple
                came_from[next] = current

    print(came_from, cost_so_far)
    return []


def findsuccessor(current_node, env):
    neighbors_ls = []

    # check each lines and see if they are intersect with the current node,if not ,add the vertex to the neighbors list
    for polygon in env.obstacles:
        for vertex in polygon.vertices:
            for line in env.obstacles_lines:
                if not do_intersect((current_node.x, current_node.y), (vertex.x, vertex.y), (line[0].x, line[0].y),
                                    (line[1].x, line[1].y)):
                    neighbors_ls.append(vertex)

    print("neighbors")
    print(len(neighbors_ls))
    return neighbors_ls


# def heuristic(a: GridLocation, b: GridLocation) -> float:
#     (x1, y1) = a
#     (x2, y2) = b
#     return abs(x1 - x2) + abs(y1 - y2)


if __name__ == '__main__':
    env = Environment('output/environment.txt')
    print("Loaded an environment with {} obstacles.".format(len(env.obstacles)))
    print(env.obstacles.pop().vertices.pop().x)
    print((env.start.x, env.start.y))
    print("lens of lines are {} .".format(len(env.obstacles_lines)))
    # for o in env.obstacles:
    #     for v in o.vertices:
    #         print((v.x, v.y))

    # VG.findEdges(env.obstacles, (env.start.x,env.start.y), (env.goal.x,env.goal.y))
    searches = {
        'greedy': greedySearch,
        'uniformcost': uniformCostSearch,
        'astar': astarSearch
    }

    for name, fun in searches.items():
        print("Attempting a search with " + name)
        Environment.printPath(name, fun(env))
