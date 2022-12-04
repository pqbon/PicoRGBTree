import time

from machine import Pin, SoftSPI

NAMED_COLORS = {
    'aliceblue':             '#f0f8ff',
    'antiquewhite':          '#faebd7',
    'aqua':                  '#00ffff',
    'aquamarine':            '#7fffd4',
    'azure':                 '#f0ffff',
    'beige':                 '#f5f5dc',
    'bisque':                '#ffe4c4',
    'black':                 '#000000',
    'blanchedalmond':        '#ffebcd',
    'blue':                  '#0000ff',
    'blueviolet':            '#8a2be2',
    'brown':                 '#a52a2a',
    'burlywood':             '#deb887',
    'cadetblue':             '#5f9ea0',
    'chartreuse':            '#7fff00',
    'chocolate':             '#d2691e',
    'coral':                 '#ff7f50',
    'cornflowerblue':        '#6495ed',
    'cornsilk':              '#fff8dc',
    'crimson':               '#dc143c',
    'cyan':                  '#00ffff',
    'darkblue':              '#00008b',
    'darkcyan':              '#008b8b',
    'darkgoldenrod':         '#b8860b',
    'darkgray':              '#a9a9a9',
    'darkgreen':             '#006400',
    'darkgrey':              '#a9a9a9',
    'darkkhaki':             '#bdb76b',
    'darkmagenta':           '#8b008b',
    'darkolivegreen':        '#556b2f',
    'darkorange':            '#ff8c00',
    'darkorchid':            '#9932cc',
    'darkred':               '#8b0000',
    'darksalmon':            '#e9967a',
    'darkseagreen':          '#8fbc8f',
    'darkslateblue':         '#483d8b',
    'darkslategray':         '#2f4f4f',
    'darkslategrey':         '#2f4f4f',
    'darkturquoise':         '#00ced1',
    'darkviolet':            '#9400d3',
    'deeppink':              '#ff1493',
    'deepskyblue':           '#00bfff',
    'dimgray':               '#696969',
    'dimgrey':               '#696969',
    'dodgerblue':            '#1e90ff',
    'firebrick':             '#b22222',
    'floralwhite':           '#fffaf0',
    'forestgreen':           '#228b22',
    'fuchsia':               '#ff00ff',
    'gainsboro':             '#dcdcdc',
    'ghostwhite':            '#f8f8ff',
    'gold':                  '#ffd700',
    'goldenrod':             '#daa520',
    'gray':                  '#808080',
    'green':                 '#008000',
    'greenyellow':           '#adff2f',
    'grey':                  '#808080',
    'honeydew':              '#f0fff0',
    'hotpink':               '#ff69b4',
    'indianred':             '#cd5c5c',
    'indigo':                '#4b0082',
    'ivory':                 '#fffff0',
    'khaki':                 '#f0e68c',
    'lavender':              '#e6e6fa',
    'lavenderblush':         '#fff0f5',
    'lawngreen':             '#7cfc00',
    'lemonchiffon':          '#fffacd',
    'lightblue':             '#add8e6',
    'lightcoral':            '#f08080',
    'lightcyan':             '#e0ffff',
    'lightgoldenrodyellow':  '#fafad2',
    'lightgray':             '#d3d3d3',
    'lightgreen':            '#90ee90',
    'lightgrey':             '#d3d3d3',
    'lightpink':             '#ffb6c1',
    'lightsalmon':           '#ffa07a',
    'lightseagreen':         '#20b2aa',
    'lightskyblue':          '#87cefa',
    'lightslategray':        '#778899',
    'lightslategrey':        '#778899',
    'lightsteelblue':        '#b0c4de',
    'lightyellow':           '#ffffe0',
    'lime':                  '#00ff00',
    'limegreen':             '#32cd32',
    'linen':                 '#faf0e6',
    'magenta':               '#ff00ff',
    'maroon':                '#800000',
    'mediumaquamarine':      '#66cdaa',
    'mediumblue':            '#0000cd',
    'mediumorchid':          '#ba55d3',
    'mediumpurple':          '#9370db',
    'mediumseagreen':        '#3cb371',
    'mediumslateblue':       '#7b68ee',
    'mediumspringgreen':     '#00fa9a',
    'mediumturquoise':       '#48d1cc',
    'mediumvioletred':       '#c71585',
    'midnightblue':          '#191970',
    'mintcream':             '#f5fffa',
    'mistyrose':             '#ffe4e1',
    'moccasin':              '#ffe4b5',
    'navajowhite':           '#ffdead',
    'navy':                  '#000080',
    'oldlace':               '#fdf5e6',
    'olive':                 '#808000',
    'olivedrab':             '#6b8e23',
    'orange':                '#ffa500',
    'orangered':             '#ff4500',
    'orchid':                '#da70d6',
    'palegoldenrod':         '#eee8aa',
    'palegreen':             '#98fb98',
    'paleturquoise':         '#afeeee',
    'palevioletred':         '#db7093',
    'papayawhip':            '#ffefd5',
    'peachpuff':             '#ffdab9',
    'peru':                  '#cd853f',
    'pink':                  '#ffc0cb',
    'plum':                  '#dda0dd',
    'powderblue':            '#b0e0e6',
    'purple':                '#800080',
    'red':                   '#ff0000',
    'rosybrown':             '#bc8f8f',
    'royalblue':             '#4169e1',
    'saddlebrown':           '#8b4513',
    'salmon':                '#fa8072',
    'sandybrown':            '#f4a460',
    'seagreen':              '#2e8b57',
    'seashell':              '#fff5ee',
    'sienna':                '#a0522d',
    'silver':                '#c0c0c0',
    'skyblue':               '#87ceeb',
    'slateblue':             '#6a5acd',
    'slategray':             '#708090',
    'slategrey':             '#708090',
    'snow':                  '#fffafa',
    'springgreen':           '#00ff7f',
    'steelblue':             '#4682b4',
    'tan':                   '#d2b48c',
    'teal':                  '#008080',
    'thistle':               '#d8bfd8',
    'tomato':                '#ff6347',
    'turquoise':             '#40e0d0',
    'violet':                '#ee82ee',
    'wheat':                 '#f5deb3',
    'white':                 '#ffffff',
    'whitesmoke':            '#f5f5f5',
    'yellow':                '#ffff00',
    'yellowgreen':           '#9acd32',
}

class BRGBLed:
    def __init__(self, p_brightness=0.5, p_red=0.0, p_green=0.0, p_blue=0.0, colour=''):
        self.brightness = p_brightness
        if colour == '':
            self.red = p_red
            self.green = p_green
            self.blue = p_blue
        else:
            self.colour = colour
        self._pixel = (self.brightness_bits, self.red, self.green, self.blue)

    @property
    def colour(self):
        #print ("Brightness: ", self.brightness, " Brightness bits: ", self.brightness_bits, " Red: ", self.red, " Green: ", self.green, " Blue: ", self.blue)
        return self._pixel

    @colour.setter
    def colour(self, val):
        if isinstance(val, str):
            if val in NAMED_COLORS:
                val = NAMED_COLORS[val]
            if val[0] == "#":
                val = val.lstrip('#')
            num = int(val, 16)
            _red = (num >> 16) & 0xff
            _green = (num >> 8) & 0xff
            _blue = (num >> 0) & 0xff
            self.red = float(_red) / float(0xff)
            self.green = float(_green) / float(0xff)
            self.blue = float(_blue) / float(0xff)
            self._pixel = (self.brightness_bits, self.red, self.green, self.blue)
        elif isinstance(val, tuple):
            if len(val) == 3:
                self.red = val[0]
                self.green = val[1]
                self.blue = val[2]
                self._pixel = (self.brightness_bits, self.red, self.green, self.blue)
            elif len(val) == 4:
                self.red = val[0]
                self.green = val[1]
                self.blue = val[2]
                self.brightness = val[3]
                self._pixel = val
            else:
                self.red = 0.0
                self.green = 0.0
                self.blue = 0.0
                self.brightness = 0.0
                self._pixel = (self.brightness_bits, self.red, self.green, self.blue)
        else:
            self.red = 0.0
            self.green = 0.0
            self.blue = 0.0
            self.brightness = 0.0
            self._pixel = (0,0,0,0)
        #print ("LED Brightness: ", self.brightness, " Brightness bits: ", self.brightness_bits, " Red: ", self.red, " Green: ", self.green, " Blue: ", self.blue, " Pixel: ", self._pixel)

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, brightness):
        max_brightness = 31
        self._brightness_bits = int(brightness * max_brightness)
        self._brightness = brightness
        # SSSBBBBB (start, brightness)
        self._brightness_ = 0b11100000 | self._brightness_bits

    @property
    def brightness_bits(self):
        return self._brightness_

    def __iter__(self):
        return iter(self._pixel)

    def on(self):
        self.brightness = 0.08
        self.red = 1.0
        self.green = 1.0
        self.blue = 1.0
        self.colour = (1.0, 1.0, 1.0)

    def off(self):
        self.brightness = 0.0
        self.red = 0.0
        self.green = 0.0
        self.blue = 0.0
        self.colour = (0.0, 0.0, 0.0)

class RGBXmasTree:
    def __init__(self, pixels=25, brightness=0.5, mosi_pin=9, clock_pin=28, *args, **kwargs):
        self._spi = SoftSPI(10_000_000, sck=Pin(clock_pin), mosi=Pin(mosi_pin), miso=Pin(12))  # type: ignore
        self.length = pixels
        self._pixels = [BRGBLed() for _ in range(pixels)]
        self.off()

    def __len__(self):
        return len(self._pixels)

    def __getitem__(self, index):
        return self._pixels[index]

    def __iter__(self):
        return iter(self._pixels)

    @property
    def pixels(self):
        return self._pixels

    @pixels.setter
    def pixels(self, pixels):
        self._pixels = pixels
        self.refresh()

    @property
    def colour(self):
        return (self._pixels[0].colour)

    @colour.setter
    def colour(self, value):
        for led in range(self.length):
            self._pixels[led].colour = value
        self.refresh()

    def refresh(self):
        start_of_frame = [0]*4
        end_of_frame = [0]*5
        pixels = []
        assert(len(self._pixels) == self.length)
        for led in self._pixels:
            pixels.append(led.brightness_bits)
            pixels.append(int(led.blue * 255))
            pixels.append(int(led.green * 255))
            pixels.append(int(led.red * 255))
        data = bytearray(start_of_frame + pixels + end_of_frame)
        self._spi.write(data)

    def on(self):
        for p in self._pixels:
            p.on()
        self.refresh()

    def off(self):
        for p in self._pixels:
            p.off()
        self.refresh()

    def close(self):
        self._spi.deinit()
    
    def set_pixel(self, idx, pixel, refresh=True):
        if(idx < 0):
            if refresh == True:
                self.refresh()
            return
        if(idx >= self.length):
            if refresh == True:
                self.refresh()
            return
        self._pixels[idx] = pixel
        if refresh == True:
            self.refresh()

    def get_pixel(self, idx):
        if(idx < 0):
            return 0
        if(idx >= self.length):
            return 0
        return self._pixels[idx]

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
