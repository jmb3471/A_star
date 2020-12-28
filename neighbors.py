"""
@File: neighbors.py
@author: Jonathan Baxley
Class for handling getting neighbors of a node
"""

"""
function that retrieves all neighbor nodes 
@:param: current_node, node that neighbors should be retrieved from
@:param: elevation, 2d array representing elevation
@:param: image, 2d array representing the image
"""
def get_neighbors(current_node, elevation, image):
    children = []
    x = current_node[0]
    y = current_node[1]
    i = 0
    if x > 0:

        neighbor_val = image[current_node[1] - 1][current_node[0]]
        neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
        neighbor_height = elevation[current_node[0] - 1][current_node[1]]
        neighbor = []
        neighbor.append(current_node[0] - 1)
        neighbor.append(current_node[1])
        neighbor.append(neighbor_height)
        neighbor.append(neighbor_color)
        neighbor.append(0)
        neighbor.append(0)
        neighbor.append(0)
        neighbor.append(0)
        neighbor.append(current_node)
        children.append(neighbor)

        if y > 0:
            neighbor_height = elevation[current_node[0] - 1][current_node[1] - 1]
            neighbor_val = image[current_node[1] - 1][current_node[1] - 1]
            neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
            neighbor = []
            neighbor.append(current_node[0] - 1)
            neighbor.append(current_node[1] - 1)
            neighbor.append(neighbor_height)
            neighbor.append(neighbor_color)
            neighbor.append(0)
            neighbor.append(0)
            neighbor.append(0)
            neighbor.append(0)
            neighbor.append(current_node)
            children.append(neighbor)

        if y < 499:
            neighbor_height = elevation[current_node[0] - 1][current_node[1] + 1]
            neighbor_val = image[current_node[1] - 1][current_node[0] + 1]
            neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
            neighbor = []
            neighbor.append(current_node[0] - 1)
            neighbor.append(current_node[1] + 1)
            neighbor.append(neighbor_height)
            neighbor.append(neighbor_color)
            neighbor.append(0)
            neighbor.append(0)
            neighbor.append(0)
            neighbor.append(0)
            neighbor.append(current_node)
            children.append(neighbor)

    if y > 0:
        neighbor_height = elevation[current_node[0]][current_node[0] - 1]
        neighbor_val = image[current_node[1]][current_node[0] - 1]
        neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
        neighbor = []
        neighbor.append(current_node[0])
        neighbor.append(current_node[1] - 1)
        neighbor.append(neighbor_height)
        neighbor.append(neighbor_color)
        neighbor.append(0)
        neighbor.append(0)
        neighbor.append(0)
        neighbor.append(0)
        neighbor.append(current_node)
        children.append(neighbor)

        if x < 499:
            neighbor_height = elevation[current_node[0] + 1][current_node[1] - 1]
            neighbor_val = image[current_node[1] + 1][current_node[0] - 1]
            neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
            neighbor = []
            neighbor.append(current_node[0] + 1)
            neighbor.append(current_node[1] - 1)
            neighbor.append(neighbor_height)
            neighbor.append(neighbor_color)
            neighbor.append(0)
            neighbor.append(0)
            neighbor.append(0)
            neighbor.append(0)
            neighbor.append(current_node)
            children.append(neighbor)

    if x < 499:
        neighbor_height = elevation[current_node[0] + 1][current_node[1]]
        neighbor_val = image[current_node[1] + 1][current_node[0]]
        neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
        neighbor = []
        neighbor.append(current_node[0] + 1)
        neighbor.append(current_node[1])
        neighbor.append(neighbor_height)
        neighbor.append(neighbor_color)
        neighbor.append(0)
        neighbor.append(0)
        neighbor.append(0)
        neighbor.append(0)
        neighbor.append(current_node)
        children.append(neighbor)

        if y < 499:
            neighbor_height = elevation[current_node[0] + 1][current_node[1] + 1]
            neighbor_val = image[current_node[1] + 1][current_node[0] + 1]
            neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
            neighbor = []
            neighbor.append(current_node[0] + 1)
            neighbor.append(current_node[1] + 1)
            neighbor.append(neighbor_height)
            neighbor.append(neighbor_color)
            neighbor.append(0)
            neighbor.append(0)
            neighbor.append(0)
            neighbor.append(0)
            neighbor.append(current_node)
            children.append(neighbor)

    if y < 499:
        neighbor_height = elevation[current_node[0]][current_node[1] + 1]
        neighbor_val = image[current_node[1]][current_node[0] + 1]
        neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
        neighbor = []
        neighbor.append(current_node[0])
        neighbor.append(current_node[1] + 1)
        neighbor.append(neighbor_height)
        neighbor.append(neighbor_color)
        neighbor.append(0)
        neighbor.append(0)
        neighbor.append(0)
        neighbor.append(0)
        neighbor.append(current_node)
        children.append(neighbor)
    return children

"""
gets the neighbors for any pixel for a particular season
"""
def neighbors_season(image, x, y,):
    children = []
    if x > 0:
        neighbor_val = image[y + 1][x]
        neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
        children.append(neighbor_color)
        if y > 0:
            neighbor_val = image[y][x + 1]
            neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
            children.append(neighbor_color)
        if y < 499:
            neighbor_val = image[y - 1][x + 1]
            neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
            children.append(neighbor_color)
    if y > 0:
        neighbor_val = image[y][x - 1]
        neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
        children.append(neighbor_color)
        if x < 499:
            neighbor_val = image[y + 1][x - 1]
            neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
            children.append(neighbor_color)
    if x < 499:
        neighbor_val = image[y + 1][x]
        neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
        children.append(neighbor_color)
        if y < 499:
            neighbor_val = image[y + 1][x + 1]
            neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
            children.append(neighbor_color)
    if y < 499:
        neighbor_val = image[y][x + 1]
        neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
        children.append(neighbor_color)
    return children

"""
function that returns which color a point is on based on rgb values
@:return: returns an int that will be used as a scalar
"""
def identify_color(r, g, b):
    if r == 205 and g == 0 and b == 101:
        #return "OUT"
        return 1000
    elif r == 0 and g == 0 and b == 0:
        #return "FOOTPATH"
        return .1
    elif r == 75 and g == 51 and b == 3:
        #return "PAVED"
        return .05
    elif r == 0 and g == 0 and b == 255:
        #return "LAKE"
        return 1001
    elif r == 5 and g == 73 and b == 24:
        #return "IMPASSIBLE"
        return 1000
    elif r == 2 and g == 136 and b == 40:
        #return "WALK"
        return .75
    elif r == 2 and g == 208 and b == 60:
        #return "SLOW"
        return .6
    elif r == 255 and g == 255 and b == 255:
        #return "EASY"
        return .5
    elif r == 255 and g == 192 and b == 0:
        #return "ROUGH"
        return .55
    elif r == 248 and g == 148 and b == 18:
        #return "OPEN"
        return .25
    elif r == 143 and g == 68 and b == 0:
        #return "FALL"
        return .2
    elif r == 139 and g == 197 and b == 230:
        #return "ICE"
        return 1
    elif r == 155 and g == 84 and b == 10:
        #return "MUD"
        return 1.5
    else:
        return 10000