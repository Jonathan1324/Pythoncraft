from ursina import *

from scripts.python.colors import *

grassbox = []
woodbox = []
glassbox = []
randomcolorbox = []

def add_box(position):
    grassbox.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.5,
            color=green(),
            position=position,
            texture='Textures/Blocks/grass.png'
        )
    )

def add_random_box(position):
    woodbox.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.5,
            color=brown(),
            position=position,
            texture='Textures/Blocks/wood.png'
        )
    )

def add_glass_box(position):
    glassbox.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.5,
            color=white(),
            position=position,
            texture='Textures/Blocks/glass.png'
        )
    )

def add_random_color_box(position):
    randomcolorbox.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.5,
            color=random_color(),
            position=position,
            texture='Textures/Blocks/randomcolorbox.png'
        )
    )