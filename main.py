from lib import module, img
from PIL import Image
import subprocess
import socket
import pywifi
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

def get_interfaces():
    wifi = pywifi.PyWiFi()
    interfaces = []
    
    for interface in wifi.interfaces():
        if interface.name().startswith("wlan"):
            interfaces.append(interface.name())
    
    return interfaces

def check_adapter():
    if "wlan1" in get_interfaces():
        return True
    else:
        return False

def check_ssh():
    result = subprocess.run(["ss", "-t"], capture_output=True, text=True)
    output = result.stdout.rstrip("Peer Address:Port Process")
    if "ssh" in output:
       return True
    else:
        return False   

epd = module.EPD()
epd.init()

while True:
    img.create_vyseV2(check_adapter(), check_ssh())
    epd.display(epd.getbuffer(Image.open("./img/vyse.bmp")))
    time.sleep(10)