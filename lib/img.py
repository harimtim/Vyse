from PIL import ImageFont, ImageDraw, Image
import time

DIR = "../img"

def create_clock_img(filename:str = "clock.bmp"):
    img = Image.new("RGB", (250, 122), "white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 30)
    draw.text((250/2, 122/2), time.strftime("%T"),anchor="mm", fill="black", font=font)
    img.save(f"./img/{filename}")