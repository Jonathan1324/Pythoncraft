from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import pathlib

import subprocess, sys

from scripts.python.colors import *
from scripts.python.addblocks import *

app = Ursina()
player = FirstPersonController()
Sky()

app_path = str(pathlib.Path(__file__).parent.resolve())[:-3]

hotbar1texture = "HotbarLeft"
hotbar2texture = "HotbarPart2"
hotbar3texture = "HotbarPart3"
hotbar4texture = "HotbarPart"
hotbar5texture = "HotbarPart"
hotbar6texture = "HotbarPart"
hotbar7texture = "HotbarPart"
hotbar8texture = "HotbarPart"
hotbar9texture = "HotbarPart9"

window.fullscreen = True
window.borderless = True
window.title = "Minecraft"

mouse.position = 1, 0, 0

for x in range(25):
    for z in range(25):
        add_box( (x, 0, z) )

hotbarPart1 = Entity(model='quad',parent=camera.ui)
hotbarPart1.scale_y=0.07
hotbarPart1.scale_x=0.07
hotbarPart1.x=-0.2425
hotbarPart1.y=-0.45 + (hotbarPart1.scale_y*0.5)
hotbarPart1.texture = hotbar1texture + "On.png"

hotbarPart2 = Entity(model='quad',parent=camera.ui)
hotbarPart2.scale_y=0.07
hotbarPart2.scale_x=0.06
hotbarPart2.x=-0.1775
hotbarPart2.y=-0.45 + (hotbarPart2.scale_y*0.5)
hotbarPart2.texture = hotbar2texture + ".png"

hotbarPart3 = Entity(model='quad',parent=camera.ui)
hotbarPart3.scale_y=0.07
hotbarPart3.scale_x=0.06
hotbarPart3.x=-0.1175
hotbarPart3.y=-0.45 + (hotbarPart3.scale_y*0.5)
hotbarPart3.texture = hotbar3texture + ".png"

hotbarPart4 = Entity(model='quad',parent=camera.ui)
hotbarPart4.scale_y=0.07
hotbarPart4.scale_x=0.06
hotbarPart4.x=-0.0575
hotbarPart4.y=-0.45 + (hotbarPart4.scale_y*0.5)
hotbarPart4.texture = hotbar4texture + ".png"

hotbarPart5 = Entity(model='quad',parent=camera.ui)
hotbarPart5.scale_y=0.07
hotbarPart5.scale_x=0.06
hotbarPart5.x=0.0025
hotbarPart5.y=-0.45 + (hotbarPart5.scale_y*0.5)
hotbarPart5.texture = hotbar5texture + ".png"

hotbarPart6 = Entity(model='quad',parent=camera.ui)
hotbarPart6.scale_y=0.07
hotbarPart6.scale_x=0.06
hotbarPart6.x=0.0625
hotbarPart6.y=-0.45 + (hotbarPart6.scale_y*0.5)
hotbarPart6.texture = hotbar6texture + ".png"

hotbarPart7 = Entity(model='quad',parent=camera.ui)
hotbarPart7.scale_y=0.07
hotbarPart7.scale_x=0.06
hotbarPart7.x=0.1225
hotbarPart7.y=-0.45 + (hotbarPart7.scale_y*0.5)
hotbarPart7.texture = hotbar7texture + ".png"

hotbarPart8 = Entity(model='quad',parent=camera.ui)
hotbarPart8.scale_y=0.07
hotbarPart8.scale_x=0.06
hotbarPart8.x=0.1825
hotbarPart8.y=-0.45 + (hotbarPart8.scale_y*0.5)
hotbarPart8.texture = hotbar8texture + ".png"

hotbarPart9 = Entity(model='quad',parent=camera.ui)
hotbarPart9.scale_y=0.07
hotbarPart9.scale_x=0.06
hotbarPart9.x=0.2425
hotbarPart9.y=-0.45 + (hotbarPart9.scale_y*0.5)
hotbarPart9.texture = hotbar9texture + ".png"

hotbar1 = "On"
hotbar2 = "Off"
hotbar3 = "Off"
hotbar4 = "Off"
hotbar5 = "Off"
hotbar6 = "Off"
hotbar7 = "Off"
hotbar8 = "Off"
hotbar9 = "Off"

def close_game():
    app.quit()

def input(key):

    global hotbar1
    global hotbar2
    global hotbar3
    global hotbar4
    global hotbar5
    global hotbar6
    global hotbar7
    global hotbar8
    global hotbar9

    for box in woodbox:
        if box.hovered:
            if key == "right mouse down":
                if hotbar1 == "On":
                    add_box(box.position + mouse.normal)
                elif hotbar2 == "On":
                    add_random_box(box.position + mouse.normal)
                elif hotbar3 == "On":
                    add_glass_box(box.position + mouse.normal)
                elif hotbar9 == "On":
                    add_random_color_box(box.position + mouse.normal)
            if key == "left mouse down":
                woodbox.remove(box)
                destroy(box)

    for box in grassbox:
        if box.hovered:
            if key == "right mouse down":
                if hotbar1 == "On":
                    add_box(box.position + mouse.normal)
                elif hotbar2 == "On":
                    add_random_box(box.position + mouse.normal)
                elif hotbar3 == "On":
                    add_glass_box(box.position + mouse.normal)
                elif hotbar9 == "On":
                    add_random_color_box(box.position + mouse.normal)
            if key == "left mouse down":
                grassbox.remove(box)
                destroy(box)

    for box in glassbox:
        if box.hovered:
            if key == "right mouse down":
                if hotbar1 == "On":
                    add_box(box.position + mouse.normal)
                elif hotbar2 == "On":
                    add_random_box(box.position + mouse.normal)
                elif hotbar3 == "On":
                    add_glass_box(box.position + mouse.normal)
                elif hotbar9 == "On":
                    add_random_color_box(box.position + mouse.normal)
            if key == "left mouse down":
                glassbox.remove(box)
                destroy(box)

    for box in randomcolorbox:
        if box.hovered:
            if key == "right mouse down":
                if hotbar1 == "On":
                    add_box(box.position + mouse.normal)
                elif hotbar2 == "On":
                    add_random_box(box.position + mouse.normal)
                elif hotbar3 == "On":
                    add_glass_box(box.position + mouse.normal)
                elif hotbar9 == "On":
                    add_random_color_box(box.position + mouse.normal)
            if key == "left mouse down":
                randomcolorbox.remove(box)
                destroy(box)

    if key == 'scroll up':
        if hotbar1 == "On":
            hotbarPart1.texture = hotbar1texture + ".png"
            hotbarPart9.texture = hotbar9texture + "On.png"
            hotbar1 = "Off"
            hotbar9 = "On"
        elif hotbar2 == "On":
            hotbarPart1.texture = hotbar1texture + "On.png"
            hotbarPart2.texture = hotbar2texture + ".png"
            hotbar1 = "On"
            hotbar2 = "Off"
        elif hotbar3 == "On":
            hotbarPart2.texture = hotbar2texture + "On.png"
            hotbarPart3.texture = hotbar3texture + ".png"
            hotbar2 = "On"
            hotbar3 = "Off"
        elif hotbar4 == "On":
            hotbarPart3.texture = hotbar3texture + "On.png"
            hotbarPart4.texture = hotbar4texture + ".png"
            hotbar3 = "On"
            hotbar4 = "Off"
        elif hotbar5 == "On":
            hotbarPart4.texture = hotbar4texture + "On.png"
            hotbarPart5.texture = hotbar5texture + ".png"
            hotbar4 = "On"
            hotbar5 = "Off"
        elif hotbar6 == "On":
            hotbarPart5.texture = hotbar5texture + "On.png"
            hotbarPart6.texture = hotbar6texture + ".png"
            hotbar5 = "On"
            hotbar6 = "Off"
        elif hotbar7 == "On":
            hotbarPart6.texture = hotbar6texture + "On.png"
            hotbarPart7.texture = hotbar7texture + ".png"
            hotbar6 = "On"
            hotbar7 = "Off"
        elif hotbar8 == "On":
            hotbarPart7.texture = hotbar7texture + "On.png"
            hotbarPart8.texture = hotbar8texture + ".png"
            hotbar7 = "On"
            hotbar8 = "Off"
        elif hotbar9 == "On":
            hotbarPart8.texture = hotbar8texture + "On.png"
            hotbarPart9.texture = hotbar9texture + ".png"
            hotbar8 = "On"
            hotbar9 = "Off"
    
    if key == 'scroll down':
        if hotbar1 == "On":
            hotbarPart1.texture = hotbar1texture + ".png"
            hotbarPart2.texture = hotbar2texture + "On.png"
            hotbar1 = "Off"
            hotbar2 = "On"
        elif hotbar2 == "On":
            hotbarPart2.texture = hotbar2texture + ".png"
            hotbarPart3.texture = hotbar3texture + "On.png"
            hotbar2 = "Off"
            hotbar3 = "On"
        elif hotbar3 == "On":
            hotbarPart3.texture = hotbar3texture + ".png"
            hotbarPart4.texture = hotbar4texture + "On.png"
            hotbar3 = "Off"
            hotbar4 = "On"
        elif hotbar4 == "On":
            hotbarPart4.texture = hotbar4texture + ".png"
            hotbarPart5.texture = hotbar5texture + "On.png"
            hotbar4 = "Off"
            hotbar5 = "On"
        elif hotbar5 == "On":
            hotbarPart5.texture = hotbar5texture + ".png"
            hotbarPart6.texture = hotbar6texture + "On.png"
            hotbar5 = "Off"
            hotbar6 = "On"
        elif hotbar6 == "On":
            hotbarPart6.texture = hotbar6texture + ".png"
            hotbarPart7.texture = hotbar7texture + "On.png"
            hotbar6 = "Off"
            hotbar7 = "On"
        elif hotbar7 == "On":
            hotbarPart7.texture = hotbar7texture + ".png"
            hotbarPart8.texture = hotbar8texture + "On.png"
            hotbar7 = "Off"
            hotbar8 = "On"
        elif hotbar8 == "On":
            hotbarPart8.texture = hotbar8texture + ".png"
            hotbarPart9.texture = hotbar9texture + "On.png"
            hotbar8 = "Off"
            hotbar9 = "On"
        elif hotbar9 == "On":
            hotbarPart9.texture = hotbar9texture + ".png"
            hotbarPart1.texture = hotbar1texture + "On.png"
            hotbar9 = "Off"
            hotbar1 = "On"

    if key == '1':
        hotbarPart1.texture = hotbar1texture + "On.png"
        hotbarPart2.texture = hotbar2texture + ".png"
        hotbarPart3.texture = hotbar3texture + ".png"
        hotbarPart4.texture = hotbar4texture + ".png"
        hotbarPart5.texture = hotbar5texture + ".png"
        hotbarPart6.texture = hotbar6texture + ".png"
        hotbarPart7.texture = hotbar7texture + ".png"
        hotbarPart8.texture = hotbar8texture + ".png"
        hotbarPart9.texture = hotbar9texture + ".png"
        hotbar1 = "On"
        hotbar2 = "Off"
        hotbar3 = "Off"
        hotbar4 = "Off"
        hotbar5 = "Off"
        hotbar6 = "Off"
        hotbar7 = "Off"
        hotbar8 = "Off"
        hotbar9 = "Off"
        

    if key == '2':
        hotbarPart1.texture = hotbar1texture + ".png"
        hotbarPart2.texture = hotbar2texture + "On.png"
        hotbarPart3.texture = hotbar3texture + ".png"
        hotbarPart4.texture = hotbar4texture + ".png"
        hotbarPart5.texture = hotbar5texture + ".png"
        hotbarPart6.texture = hotbar6texture + ".png"
        hotbarPart7.texture = hotbar7texture + ".png"
        hotbarPart8.texture = hotbar8texture + ".png"
        hotbarPart9.texture = hotbar9texture + ".png"
        hotbar1 = "Off"
        hotbar2 = "On"
        hotbar3 = "Off"
        hotbar4 = "Off"
        hotbar5 = "Off"
        hotbar6 = "Off"
        hotbar7 = "Off"
        hotbar8 = "Off"
        hotbar9 = "Off"

    if key == '3':
        hotbarPart1.texture = hotbar1texture + ".png"
        hotbarPart2.texture = hotbar2texture + ".png"
        hotbarPart3.texture = hotbar3texture + "On.png"
        hotbarPart4.texture = hotbar4texture + ".png"
        hotbarPart5.texture = hotbar5texture + ".png"
        hotbarPart6.texture = hotbar6texture + ".png"
        hotbarPart7.texture = hotbar7texture + ".png"
        hotbarPart8.texture = hotbar8texture + ".png"
        hotbarPart9.texture = hotbar9texture + ".png"
        hotbar1 = "Off"
        hotbar2 = "Off"
        hotbar3 = "On"
        hotbar4 = "Off"
        hotbar5 = "Off"
        hotbar6 = "Off"
        hotbar7 = "Off"
        hotbar8 = "Off"
        hotbar9 = "Off"
    
    if key == '4':
        hotbarPart1.texture = hotbar1texture + ".png"
        hotbarPart2.texture = hotbar2texture + ".png"
        hotbarPart3.texture = hotbar3texture + ".png"
        hotbarPart4.texture = hotbar4texture + "On.png"
        hotbarPart5.texture = hotbar5texture + ".png"
        hotbarPart6.texture = hotbar6texture + ".png"
        hotbarPart7.texture = hotbar7texture + ".png"
        hotbarPart8.texture = hotbar8texture + ".png"
        hotbarPart9.texture = hotbar9texture + ".png"
        hotbar1 = "Off"
        hotbar2 = "Off"
        hotbar3 = "Off"
        hotbar4 = "On"
        hotbar5 = "Off"
        hotbar6 = "Off"
        hotbar7 = "Off"
        hotbar8 = "Off"
        hotbar9 = "Off"

    if key == '5':
        hotbarPart1.texture = hotbar1texture + ".png"
        hotbarPart2.texture = hotbar2texture + ".png"
        hotbarPart3.texture = hotbar3texture + ".png"
        hotbarPart4.texture = hotbar4texture + ".png"
        hotbarPart5.texture = hotbar5texture + "On.png"
        hotbarPart6.texture = hotbar6texture + ".png"
        hotbarPart7.texture = hotbar7texture + ".png"
        hotbarPart8.texture = hotbar8texture + ".png"
        hotbarPart9.texture = hotbar9texture + ".png"
        hotbar1 = "Off"
        hotbar2 = "Off"
        hotbar3 = "Off"
        hotbar4 = "Off"
        hotbar5 = "On"
        hotbar6 = "Off"
        hotbar7 = "Off"
        hotbar8 = "Off"
        hotbar9 = "Off"

    if key == '6':
        hotbarPart1.texture = hotbar1texture + ".png"
        hotbarPart2.texture = hotbar2texture + ".png"
        hotbarPart3.texture = hotbar3texture + ".png"
        hotbarPart4.texture = hotbar4texture + ".png"
        hotbarPart5.texture = hotbar5texture + ".png"
        hotbarPart6.texture = hotbar6texture + "On.png"
        hotbarPart7.texture = hotbar7texture + ".png"
        hotbarPart8.texture = hotbar8texture + ".png"
        hotbarPart9.texture = hotbar9texture + ".png"
        hotbar1 = "Off"
        hotbar2 = "Off"
        hotbar3 = "Off"
        hotbar4 = "Off"
        hotbar5 = "Off"
        hotbar6 = "On"
        hotbar7 = "Off"
        hotbar8 = "Off"
        hotbar9 = "Off"

    if key == '7':
        hotbarPart1.texture = hotbar1texture + ".png"
        hotbarPart2.texture = hotbar2texture + ".png"
        hotbarPart3.texture = hotbar3texture + ".png"
        hotbarPart4.texture = hotbar4texture + ".png"
        hotbarPart5.texture = hotbar5texture + ".png"
        hotbarPart6.texture = hotbar6texture + ".png"
        hotbarPart7.texture = hotbar7texture + "On.png"
        hotbarPart8.texture = hotbar8texture + ".png"
        hotbarPart9.texture = hotbar9texture + ".png"
        hotbar1 = "Off"
        hotbar2 = "Off"
        hotbar3 = "Off"
        hotbar4 = "Off"
        hotbar5 = "Off"
        hotbar6 = "Off"
        hotbar7 = "On"
        hotbar8 = "Off"
        hotbar9 = "Off"

    if key == '8':
        hotbarPart1.texture = hotbar1texture + ".png"
        hotbarPart2.texture = hotbar2texture + ".png"
        hotbarPart3.texture = hotbar3texture + ".png"
        hotbarPart4.texture = hotbar4texture + ".png"
        hotbarPart5.texture = hotbar5texture + ".png"
        hotbarPart6.texture = hotbar6texture + ".png"
        hotbarPart7.texture = hotbar7texture + ".png"
        hotbarPart8.texture = hotbar8texture + "On.png"
        hotbarPart9.texture = hotbar9texture + ".png"
        hotbar1 = "Off"
        hotbar2 = "Off"
        hotbar3 = "Off"
        hotbar4 = "Off"
        hotbar5 = "Off"
        hotbar6 = "Off"
        hotbar7 = "Off"
        hotbar8 = "On"
        hotbar9 = "Off"

    if key == '9':
        hotbarPart1.texture = hotbar1texture + ".png"
        hotbarPart2.texture = hotbar2texture + ".png"
        hotbarPart3.texture = hotbar3texture + ".png"
        hotbarPart4.texture = hotbar4texture + ".png"
        hotbarPart5.texture = hotbar5texture + ".png"
        hotbarPart6.texture = hotbar6texture + ".png"
        hotbarPart7.texture = hotbar7texture + ".png"
        hotbarPart8.texture = hotbar8texture + ".png"
        hotbarPart9.texture = hotbar9texture + "On.png"
        hotbar1 = "Off"
        hotbar2 = "Off"
        hotbar3 = "Off"
        hotbar4 = "Off"
        hotbar5 = "Off"
        hotbar6 = "Off"
        hotbar7 = "Off"
        hotbar8 = "Off"
        hotbar9 = "On"
    
    if key == 'escape': 
        close_game()
app.run()