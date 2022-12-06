import time
import math
from rgbtree import  RGBXmasTree, BRGBLed

def xmas_tree_redgreen_bright(num):
    tree = RGBXmasTree()

    step_size = 360 / tree.length
    led_red = BRGBLed(0.25, colour='red')
    led_green = BRGBLed(0.25, colour='green')

    for loop in range(num):
        for led_idx in range(tree.length):
            red = (loop % 2 + led_idx) % 2
            idx = ((led_idx + loop) % tree.length)
            bright = step_size * idx
            if red :
                led_red.brightness = ((math.sin(bright) + 1.0) * 0.5) * 0.666
                tree.set_pixel(led_idx, led_red, False)
            else:
                led_green.brightness = ((math.cos(bright) + 1.0) * 0.5)  * 0.666
                tree.set_pixel(led_idx, led_green, False)
        tree.refresh()

        time.sleep(1.0)
    tree.off()

if __name__ == '__main__':
    xmas_tree_redgreen_bright(100)
