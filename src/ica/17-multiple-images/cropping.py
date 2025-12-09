from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def crop_picture(pic, start_x, start_y, width, height):
    cropped_pic = Picture(width, height)

    for (x) in range(start_x, start_x + width):
        for y in range(start_y, start_y + height):
            color = pic.getColor(x,y)
            cropped_pic.setColor(x-start_x,y-start_y,color)

    return cropped_pic

dam = Picture("../SampleImages/hooverDam.jpg")
dam_crop1 = crop_picture(dam, 260, 90, 240, 210)
dam_crop2 = crop_picture(dam, 100, 150, 100, 150)
dam_crop1.show()
dam_crop2.show()

keep_windows_open()