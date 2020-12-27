# watermark.py
from PIL import Image, ImageDraw, ImageFont
import sys

my_img_fldr = r".\my_imgs\\"
my_img_pic = r"tatras"
# my_img_pic = r"mr_mrs"
my_img_format = r".jpg"
my_img_file = my_img_fldr+my_img_pic+my_img_format

try:
    my_img_water = Image.open(my_img_file)
except IOError:
    print("Unable to load image")    
    sys.exit(1)

idraw = ImageDraw.Draw(my_img_water)
text = "Maxam Trendz"
font = ImageFont.truetype("arial.ttf", size=18)
idraw.text((10, 10), text, font=font)
my_img_water.show()

# my_img.save('tatras_watermarked.png')  
my_out_pic = my_img_pic+"_water"
my_out_file = my_img_fldr+my_out_pic+my_img_format
try:
    my_img_water.save(my_out_file)
except IOError:
    print("Unable to save image")    
    sys.exit(1)      