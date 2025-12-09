from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def weighted_blend(pic1, pic2, wgt1):
    if 0.0 < wgt1 < 1.0:
        pass
    else:
        wgt1 = input("PUT IN A GOOD NUMBER")
        
    width = [pic1.width, pic2.width]
    height = [pic1.height, pic2.height]
    new_width = min(width)
    new_height = min(height)
    new_pic = Picture(new_width, new_height)

    for (x,y) in new_pic:
        r1, g1, b1 = pic1.getColor(x,y)
        r2, g2, b2 = pic2.getColor(x,y)

        new_r = int(r1 + r2)/2
        new_g = int(g1 + g2)/2
        new_b = int(b1 + b2)/2

        new_color = (new_r, new_g, new_b)

        new_pic.setColor(x,y,new_color)

    return new_pic
