from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

pic1 = Picture("../SampleImages/mightyMidway.jpg")
n_pixels = pic1.getWidth()*pic1.getHeight()
print(n_pixels)

pic2 = pic1.copy()
width = pic2.getWidth()
height = pic2.getHeight()
corner_x = width - 1
corner_y = height - 1
pic2.setColor(corner_x, corner_y, "red")

pic2.save("../SampleImages/mightyMidway-redCorners.jpg")
pic2.explore()

keep_windows_open()

