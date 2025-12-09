from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def scale_up(pic):
    new_pic_width = pic.width*2
    new_pic_height = pic.height*2
    new_pic = Picture(new_pic_width, new_pic_height)

    for (x,y) in pic:
        color = pic.getColor(x,y)
        new_pic.setColor(2*x,2*y,color)
        new_pic.setColor(2*x+1,2*y,color)
        new_pic.setColor(2*x,2*y+1,color)
        new_pic.setColor(2*x+1,2*y+1,color)

    return new_pic

green_turtle = Picture("../SampleImages/greenTurtle.jpg")
green_turtle_scale = scale_up(green_turtle)
green_turtle.show()
green_turtle_scale.show()

keep_windows_open()