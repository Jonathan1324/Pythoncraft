from ursina import *

def random_color():
    red = random.Random().random() * 255
    green = random.Random().random() * 255
    blue = random.Random().random() * 255
    return color.rgb(red, green, blue)

def brown():
    return color.rgb(63, 32, 23)

def white():
    return color.rgb(255, 255, 255)

def green():
    return color.rgb(0, 200, 0)