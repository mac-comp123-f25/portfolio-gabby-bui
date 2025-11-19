from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *
import random

def copy_pic_into(small_pic,big_pic):
    start_x = random.randint(0, big_pic.width - small_pic.width)
    start_y = random.randint(0, big_pic.height - small_pic.height)
    for (x, y) in small_pic:
        color = small_pic.getColor(x,y)
        big_pic.setColor(start_x+x, start_y+y, color)

green_turtle = Picture("../SampleImages/greenTurtle.jpg")
scene = Picture("../SampleImages/bearLake.jpg")
copy_pic_into(green_turtle, scene)
copy_pic_into(green_turtle, scene)
copy_pic_into(green_turtle, scene)
scene.show()

keep_windows_open()


