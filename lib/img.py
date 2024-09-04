from PIL import ImageFont, ImageDraw, Image
import time
import datetime

WIDTH = 250
HEIGHT = 122

def create_clock_img(filename:str = "clock.bmp"):
    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 30)
    draw.text((WIDTH/2, HEIGHT/2), time.strftime("%T"),anchor="mm", fill="black", font=font)
    img.save(f"./img/{filename}")

def create_modern_clock(wlan:str, filename:str = "clock.bmp"):
    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 14)
    draw.line((0, 100, WIDTH, 100), fill="black", width=1)
    draw.rectangle([(75, 10), (175, 30)], fill="white", outline="black", width=2)
    draw.text((WIDTH/2, 20), time.strftime("%T"), font=font, fill="black", anchor="mm")
    draw.text((WIDTH/2, 110), f"WLAN: {wlan}", fill="black", font=font, anchor="mm")
    img.save(f"./img/{filename}")

def create_vyse(filename:str = "vyse.bmp"):
    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)
    font1 = ImageFont.truetype("vyse.ttf", 60)
    font2 = ImageFont.truetype("vyse.ttf", 12)
    font3 = ImageFont.truetype("vyse.ttf", 10)

    draw.text((WIDTH/2, HEIGHT/2-10), "Vyse", font=font1, fill="black", anchor="mm")
    draw.text((WIDTH/2, HEIGHT/2+30), "made by harimtim", font=font2, fill="black", anchor="mm")
    draw.text((5, 5), time.strftime("%T")+" Uhr", font=font3, fill="black")
    draw.text((245, 117), "BETA", font=font3, fill="black", anchor="rb")

    img.save(f"./img/{filename}")

create_vyse()