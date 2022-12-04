import time
import math
from rgbtree import  RGBXmasTree, BRGBLed

def xmas_tree_pastel(num):
    tree = RGBXmasTree()

    for loop in range(num):
        for led_idx in range(tree.length):
            idx = (((led_idx ) % tree.length + loop) % tree.length) + 0.5

            bright = ((math.sin(360 * idx * 9) + 1.0) * 0.5) * 0.12
            red = (math.sin(360 * idx * 2) + 1.0) * 0.5
            green = (math.sin(360 * idx * 3) + 1.0) * 0.5
            blue = (math.sin(360 * idx * 4) + 1.0) * 0.5

            tree.set_pixel(led_idx, BRGBLed(bright, red, green, blue))
        tree.refresh()

        time.sleep(0.25)
    tree.off()

if __name__ == '__main__':
    xmas_tree_pastel(10000)
