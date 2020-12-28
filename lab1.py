"""
@File: hw2.py
@author: Jonathan Baxley
Lab main
"""

import sys
from PIL import Image

from AIlab1.seasons import *

"""
Reads the elevation file
@:param: name - str - name of the file
@:return: returns a 2d array of elevation
"""
def read_terrain(name):
    terrain = []
    with open(name) as f:
        line = f.readline()
        while line:
            i = 0
            values = line.split("   ")
            lst = []
            for x in values:
                if i > 394:
                    break
                if x == '':
                    continue
                elevation = float(x)
                lst.append(elevation)
                i += 1
            line = f.readline()
            terrain.append(lst)

    return terrain

"""
reads the target points
@:param: name - str - name of the file
@:return: returns a 2d array of points
"""
def read_destination(name):
    points = []
    with open(name) as f:
        line = f.readline()
        while line:
            value = line.rstrip("\n")
            values = value.split(" ")
            xy = []
            x = int(values[0])
            y = int(values[1])
            xy.append(x)
            xy.append(y)
            points.append(xy)

            line = f.readline()
    return points


"""
creates a 2d array to represent an image
@:param: name of the image - image - str
@:return: a 2d array containing the image
"""
def get_image(image):
    image_array = [[list() for i in range(395)] for j in range(500)]

    image_list = image.load()

    for x in range(500):
        for y in range(395):
            image_array[x][y] = image_list[y, x]

    return image_array


"""
Main function
expects arguments for image file, elevation file, destination file, season, and destination for new picture
"""
def main():
    if len(sys.argv) < 6:
        print('wrong')
    seasons = ["spring", "summer", "fall", "winter"]

    if sys.argv[4] not in seasons:
        print("Incorrect season argument")
        return

    elevation = read_terrain(str(sys.argv[2]))
    dest = read_destination(str(sys.argv[3]))
    im = Image.open(str(sys.argv[1]))

    image = get_image(im)
    if sys.argv[4] == "winter":
        win = winter(dest, image, elevation)
        print(win)
        for x in win:
            print(x)
            im.putpixel((x[0], x[1]), (139, 197, 230))
    if sys.argv[4] == "fall":
        fa = fall(image)
        for x in fa:
            im.putpixel((x[0], x[1]), (143, 68, 0))
    elif sys.argv[4] == "spring":
        spr = spring(dest, image, elevation)
        for x in spr:
            im.putpixel((x[0], x[1]), (155, 84, 10))


    list = search(dest, image, elevation)

    for x in list:
        for y in x:
            im.putpixel((y[0], y[1]), (255, 0, 255))

    for x in dest:
        im.putpixel((x[0], x[1]), (255, 0, 0))

    im.save(sys.argv[5])


if __name__ == '__main__':
    main()