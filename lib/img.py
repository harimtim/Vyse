from PIL import ImageFont, ImageDraw, Image
import time

WIDTH = 250
HEIGHT = 122

def create_vyseV2(wifi:bool, ssh:bool, filename:str = "vyse.bmp"):
    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)
    font1 = ImageFont.truetype("vyse.ttf", 60)
    font2 = ImageFont.truetype("vyse.ttf", 12)
    font3 = ImageFont.truetype("vyse.ttf", 10)

    draw.text((WIDTH/2, HEIGHT/2-10), "Vyse", font=font1, fill="black", anchor="mm")
    draw.text((WIDTH/2, HEIGHT/2+30), "made by harimtim", font=font2, fill="black", anchor="mm")
    draw.text((5, 5), time.strftime("%T")+" Uhr", font=font3, fill="black")
    draw.text((5, 117), "BETA", font=font3, fill="black", anchor="lb")

    if wifi == True:
        bmp = "check.bmp"
    else:
        bmp = "warning.bmp"

    wifi = Image.open(f"./img/{bmp}").resize(size=(16, 16)).convert("RGBA")
    img.paste(wifi, (228, 3), wifi)

    if ssh:
        ssh = Image.open(f"./img/ssh.bmp").resize(size=(16, 16)).convert("RGBA")
        img.paste(ssh, (228, 20), ssh)

    img.save(f"./img/{filename}")