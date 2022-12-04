import time
from rgbtree import  RGBXmasTree, BRGBLed

def xmas_tree_pastel(num):
    tree = RGBXmasTree()
    
    LED_list = [
            BRGBLed(0.04, colour='honeydew'),
            BRGBLed(0.04, colour='lime'),
            BRGBLed(0.04, colour='orchid'),
            BRGBLed(0.04, colour='skyblue'),
            BRGBLed(0.04, colour='lavenderblush'),
            BRGBLed(0.04, colour='turquoise'),
        ]

    for loop in range(num):

        for led_idx in range(tree.length):
            idx = ((led_idx ) % len(LED_list) + loop) % len(LED_list)
            tree.set_pixel(led_idx, LED_list[idx], False)
        tree.refresh()

        time.sleep(0.25)
    tree.off()


if __name__ == '__main__':
    xmas_tree_pastel(10000)
