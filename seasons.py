"""
@File: seasons.py
@author: Jonathan Baxley
Function to handle the different seasons
"""

from AIlab1.A_star import *

"""
function to return a list with all of the points to be changed to fall
@:param: 2d array representing the image
@:return: 2d array representing points to be changed
"""
def fall(image):
    fall = []
    for x in range(390):
        for y in range(495):
            lst = []
            lst.append(x)
            lst.append(y)

            val = image[y][x]
            color = identify_color(val[0], val[1], val[2])
            if color == .1:
                children = neighbors_season(image, x, y)

                for i in children:
                    if i == .5:
                        fall.append(lst)
                        break
    return fall

"""
function to change winter
"""
def winter(dest, image, elevation):
    winter = []
    ice = []
    for x in range(390):
        for y in range(495):
            lst = []
            lst.append(x)
            lst.append(y)

            val = image[y][x]
            color = identify_color(val[0], val[1], val[2])
            if color == 1001:
                children = neighbors_season(image, x, y)

                for i in children:
                    if i != 1001:
                        winter.append(lst)
                        break

    while len(winter) != 0:
        current = winter.pop()
        d = 0
        visit = []
        visit.append(current)
        x = current[0]
        y = current[1]
        children = []
        if x > 0:
            lst = []
            lst.append(x)
            lst.append(y+1)
            neighbor_val = image[y + 1][x]
            neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
            lst.append(neighbor_color)
            children.append(lst)
            if y > 0:
                lst = []
                lst.append(x+1)
                lst.append(y)
                neighbor_val = image[y][x + 1]
                neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
                lst.append(neighbor_color)
                children.append(lst)
            if y < 499:
                lst = []
                lst.append(x + 1)
                lst.append(y - 1)
                neighbor_val = image[y - 1][x + 1]
                neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
                lst.append(neighbor_color)
                children.append(lst)
        if y > 0:
            lst = []
            lst.append(x - 1)
            lst.append(y)
            neighbor_val = image[y][x - 1]
            neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
            lst.append(neighbor_color)
            children.append(lst)
            if x < 499:
                lst = []
                lst.append(x - 1)
                lst.append(y + 1)
                neighbor_val = image[y + 1][x - 1]
                neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
                lst.append(neighbor_color)
                children.append(lst)
        if x < 499:
            lst = []
            lst.append(x + 1)
            lst.append(y)
            neighbor_val = image[y][x + 1]
            neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
            lst.append(neighbor_color)
            children.append(lst)
            if y < 499:
                lst = []
                lst.append(x + 1)
                lst.append(y + 1)
                neighbor_val = image[y + 1][x + 1]
                neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
                lst.append(neighbor_color)
                children.append(lst)
        if y < 499:
            lst = []
            lst.append(x + 1)
            lst.append(y)
            neighbor_val = image[y][x + 1]
            neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
            lst.append(neighbor_color)
            children.append(lst)

            for j in children:
                if j[2] == 1001:
                    ice.append(j)
                if d < 7:
                    visit.append(j)
        d += 1

    return ice


"""
function to change spring
"""
def spring(dest, image, elevation):
    water = []
    spring = []

    for x in range(390):
        for y in range(495):
            lst = []
            lst.append(x)
            lst.append(y)

            val = image[y][x]
            color = identify_color(val[0], val[1], val[2])
            if color == 1001:
                children = neighbors_season(image, x, y)

                for i in children:
                    if i != 1001:
                        water.append(lst)
                        break

    while len(water) != 0:
        current = water.pop()
        d = 0
        visit = []
        visit.append(current)
        x = current[0]
        y = current[1]
        children = []

        if x > 0:
            lst = []
            lst.append(x)
            lst.append(y+1)
            neighbor_val = image[y + 1][x]
            neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
            lst.append(neighbor_color)
            children.append(lst)
            if y > 0:
                lst = []
                lst.append(x+1)
                lst.append(y)
                neighbor_val = image[y][x + 1]
                neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
                lst.append(neighbor_color)
                children.append(lst)
            if y < 499:
                lst = []
                lst.append(x + 1)
                lst.append(y - 1)
                neighbor_val = image[y - 1][x + 1]
                neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
                lst.append(neighbor_color)
                children.append(lst)
        if y > 0:
            lst = []
            lst.append(x - 1)
            lst.append(y)
            neighbor_val = image[y][x - 1]
            neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
            lst.append(neighbor_color)
            children.append(lst)
            if x < 499:
                lst = []
                lst.append(x - 1)
                lst.append(y + 1)
                neighbor_val = image[y + 1][x - 1]
                neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
                lst.append(neighbor_color)
                children.append(lst)
        if x < 499:
            lst = []
            lst.append(x + 1)
            lst.append(y)
            neighbor_val = image[y][x + 1]
            neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
            lst.append(neighbor_color)
            children.append(lst)
            if y < 499:
                lst = []
                lst.append(x + 1)
                lst.append(y + 1)
                neighbor_val = image[y + 1][x + 1]
                neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
                lst.append(neighbor_color)
                children.append(lst)
        if y < 499:
            lst = []
            lst.append(x + 1)
            lst.append(y)
            neighbor_val = image[y][x + 1]
            neighbor_color = identify_color(neighbor_val[0], neighbor_val[1], neighbor_val[2])
            lst.append(neighbor_color)
            children.append(lst)

        for j in children:
            if j[2] != 1001:
                spring.append(j)
            if d < 15:
                visit.append(j)
        d += 1

    return spring

    return image

