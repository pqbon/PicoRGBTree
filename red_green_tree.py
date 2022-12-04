import time
from rgbtree import  RGBXmasTree, BRGBLed


if __name__ == '__main__':
    tree = RGBXmasTree()

    for loop in range(400):
        led_red = BRGBLed(0.5, colour='red')
        led_green = BRGBLed(0.5, colour='green')

        for led_idx in range(tree.length):
            red = (loop % 2 + led_idx) % 2
            if red :
                tree.set_pixel(led_idx, led_red, False)
            else:
                tree.set_pixel(led_idx, led_green, False)
        tree.refresh()

        time.sleep(1.0)
    tree.off()
