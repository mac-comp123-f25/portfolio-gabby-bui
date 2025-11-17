from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def simple_blend(pic1, pic2):
    new_pic = Picture(pic1.width, pic1.height)

    for (x,y) in new_pic:
        r1, g1, b1 = pic1.getColor(x,y)
        r2, g2, b2 = pic2.getColor(x,y)

        new_r = int(r1 + r2)/2
        new_g = int(g1 + g2)/2
        new_b = int(b1 + b2)/2

        new_color = (new_r, new_g, new_b)

        new_pic.setColor(x,y,new_color)

    return new_pic

p1 = Picture("../SampleImages/daylilies.jpg")
p2 = Picture("../SampleImages/wildColumbine.jpg")
p3 = simple_blend(p1, p2)

p3.show()

keep_windows_open()

