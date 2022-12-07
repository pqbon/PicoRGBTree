import time
import math
from rgbtree import  RGBXmasTree, BRGBLed

def xmas_tree_waves(num):
    tree = RGBXmasTree()

    step_size = 360 / tree.length

    for loop in range(num):
        for led_idx in range(tree.length):
            idx = ((led_idx + loop) % tree.length)

            bright = ((math.cos(step_size * idx * 5) + 1.0) * 0.5) * 0.125
            red = (math.sin(step_size * idx * 2) + 1.0) * 0.5
            green = (math.sin(step_size * idx * 3) + 1.0) * 0.5
            blue = (math.sin(step_size * idx * 4) + 1.0) * 0.5

            tree.set_pixel(led_idx, BRGBLed(bright, red, green, blue))
        tree.refresh()

        time.sleep(0.25)
    tree.off()

if __name__ == '__main__':
    xmas_tree_waves(10000)
