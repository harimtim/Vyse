from lib import module, img
from PIL import Image
import time
import os

epd = module.EPD()
epd.init_fast()

for i in range(10+1):
    img.create_clock_img()
    epd.display_fast(epd.getbuffer(Image.open("./img/clock.bmp")))
    time.sleep(1)

epd.Clear()