import time
import math
from rgbtree import  RGBXmasTree, BRGBLed

def xmas_tree_solid(num):
    tree = RGBXmasTree()

    for loop in range(num):
        idx = (loop % tree.length) + 0.5
        bright = ((math.sin(360 * idx * 3) + 1.0) * 0.5) * 0.12
        red = (math.sin(360 * idx * 2) + 1.0) * 0.5
        green = (math.sin(360 * idx * 7) + 1.0) * 0.5
        blue = (math.sin(360 * idx * 9) + 1.0) * 0.5

        tree.colour = (bright, red, green, blue)

        time.sleep(0.25)
    tree.off()

if __name__ == '__main__':
    xmas_tree_solid(10000)
