import time
from rgbtree import  RGBXmasTree, BRGBLed

def xmas_tree_colours(num):
    tree = RGBXmasTree()
    
    LED_list = [
            BRGBLed(0.06125, colour='blue'),
            BRGBLed(0.06125, colour='yellow'),
            BRGBLed(0.06125, colour='red'),
            BRGBLed(0.06125, colour='purple'),
            BRGBLed(0.06125, colour='green'),
        ]

    for loop in range(num):

        for led_idx in range(tree.length):
            idx = ((led_idx ) % len(LED_list) + loop) % len(LED_list)
            tree.set_pixel(led_idx, LED_list[idx], False)
        tree.refresh()

        time.sleep(0.333)
    tree.off()


if __name__ == '__main__':
    xmas_tree_colours(10000)
