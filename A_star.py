"""
@File: A_star.py
@author: Jonathan Baxley
Main A_star function
"""
import math

from AIlab1.neighbors import *


"""
main A_star function that finds an optimal path
searches between two points
"""
def A_star(start, goal, image, elevation):
    visited = []
    yet_to = []

    # node is represented by array of length 8
    start_node = []
    start_node.append(start[0])
    start_node.append(start[1])
    start_node.append(elevation[start[0]][start[1]])
    start_val = image[start[0]][start[1]]
    start_color = identify_color(start_val[0], start_val[1], start_val[2])
    start_node.append(start_color)
    start_node.append(0)
    start_node.append(0)
    start_node.append(0)
    start_node.append(0)
    start_node.append(None)
    track = dict()
    goal_node = []
    goal_node.append(goal[0])
    goal_node.append(goal[1])
    goal_node.append(elevation[start[0]][start[1]])
    goal_val = image[goal[0]][goal[1]]
    goal_color = identify_color(goal_val[0], goal_val[1], goal_val[2])
    goal_node.append(goal_color)
    goal_node.append(0)
    goal_node.append(0)
    goal_node.append(0)
    goal_node.append(0)

    yet_to.append(start_node)

    k = 0
    while len(yet_to) > 0:
        current_node = yet_to[0]
        i = 0

        for j, node in enumerate(yet_to):
            if node[6] < current_node[6]:
                i = j
                current_node = node
        yet_to.pop(i)
        visited.append(current_node)

        if current_node[0] == goal_node[0] and current_node[1] == goal_node[1]:

            path = []
            current = current_node
            dist = current[7]
            while current is not None:
                lst = []
                lst.append(current[0])
                lst.append(current[1])
                path.append(lst)
                current = current[8]
            return (path[::-1], dist)

        children = get_neighbors(current_node, elevation, image)

        for child in children:
            for k in visited:
                if child[0] == k[0] and child[1] == k[1]:
                    continue
            child[5] = current_node[5] + get_g(current_node, child)
            child[4] = get_h(child, goal_node)
            child[6] = child[4] + child[5]
            child[7] = get_h(current_node, child) + current_node[7]

            visited.append(child)
            for j in yet_to:
                if child[0] == j[0] and child[1] == child[1] and child[5] >= j[5]:
                    continue

            yet_to.append(child)

    return []


"""
h_function used to calculate h
uses 3d distance function to calculate
@:param: current node - node you are on now
@:param: goal - node you want to be at
"""
def get_h(current, goal):
    x = (current[0] - goal[0]) * 10.55
    y = (current[1] - goal[1]) * 7.5
    h = math.sqrt(math.pow(x, 2) + math.pow(y, 2) + math.pow(current[2] - goal[2], 2))
    return h


"""
g_function used to calculate g
uses distance * color scalar to calculate g
@:param: current - current node on
@:param: goal - node being moved to
"""
def get_g(current, goal):
    distance = get_h(current, goal)
    g = distance * goal[3]

    return g


"""
Overall search function to accumulate all nodes travelled
@:param: path - path is the overall path to be taken
@:param: image - 2d array representing an image
@:param: elevation - 2d array representing elevation

"""
def search(path, image, elevation):
    final = []
    dist = 0
    for i in range(len(path)-1):
        lst = A_star(path[i], path[i+1], image, elevation)
        final.append(lst[0])
        dist += lst[1]

    i = 0
    for x in final:
        for j in range(len(x)):
            if j < len(x) - 1:
                print(str(x[j]) + " travelled to " + str(x[j+1]))

        i += 1

    print("Total distance travelled " + str(dist))
    return final
