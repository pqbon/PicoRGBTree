import time
import random
from rgbtree import  RGBXmasTree, BRGBLed

def random_color():
    b = (random.choice(range(100)) / 100) * 0.5
    r = random.random()
    g = random.random()
    b = random.random()
    return (b, r, g, b)

def xmas_tree_random(num):
    tree = RGBXmasTree()
    for loop in range(num):
        pixel = random.choice(range(tree.length))
        tree.set_pixel(pixel, BRGBLed(colour=random_color()))
        time.sleep(0.05)
    tree.off()

if __name__ == '__main__':
    xmas_tree_random(100)
