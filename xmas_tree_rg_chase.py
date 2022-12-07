import time
import math
from rgbtree import  RGBXmasTree, BRGBLed

def xmas_tree_redgreen_bright(num):
    tree = RGBXmasTree()

    step_size = (360 / tree.length) * 3

    for loop in range(num):
        for led_idx in range(tree.length):
            red = (loop % 2 + led_idx) % 2
            if red :
                colour = 'red'
            else:
                colour = 'green'
            idx = ((led_idx + loop) % tree.length)
            bright = step_size * idx
            brightness = ((math.sin(bright) + 1.0) * 0.5) * 0.75
            tree.set_pixel(led_idx, BRGBLed(brightness, colour=colour), False)
        tree.refresh()

        time.sleep(0.5)
    tree.off()

if __name__ == '__main__':
    xmas_tree_redgreen_bright(100)
