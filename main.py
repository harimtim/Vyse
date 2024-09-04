from lib import module, img
from PIL import Image
import socket
import time
import os

def get_ssid():
    try:
        ssid = os.popen("iwgetid -r").read().strip()
        return ssid
    except:
        return None

def check_ssh():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect(("localhist", 22))
    except (socket.timeout, socket.error):
        return False
    return True


epd = module.EPD()
epd.init()
epd.Clear(0xFF)
epd.Clear(0xFF)
epd.Clear(0xFF)

for i in range(10+1):
    img.create_modern_clock(wlan=get_ssid())
    epd.harimtim(epd.getbuffer(Image.open("./img/clock.bmp")))
    epd.harimtim(epd.getbuffer(Image.open("./img/clock.bmp")))
    epd.harimtim(epd.getbuffer(Image.open("./img/clock.bmp")))

epd.Clear(0xFF)
epd.Clear(0xFF)
epd.Clear(0xFF)