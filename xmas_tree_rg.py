import time
from rgbtree import  RGBXmasTree, BRGBLed

def xmas_tree_redgreen(num):
    tree = RGBXmasTree()

    for loop in range(num):
        led_red = BRGBLed(0.25, colour='red')
        led_green = BRGBLed(0.25, colour='green')

        for led_idx in range(tree.length):
            red = (loop % 2 + led_idx) % 2
            if red :
                tree.set_pixel(led_idx, led_red, False)
            else:
                tree.set_pixel(led_idx, led_green, False)
        tree.refresh()

        time.sleep(1.0)
    tree.off()

if __name__ == '__main__':
    xmas_tree_redgreen(100)
