# draw2image.py
#!/usr/bin/python
from PIL import Image, ImageDraw
import sys

my_img_rect = Image.new('RGBA', (200, 200), 'white')    
idraw = ImageDraw.Draw(my_img_rect)
idraw.rectangle((10, 10, 100, 100), fill='blue')
my_img_rect.show()

my_img_fldr = r".\my_imgs\\"
my_img_pic = r"rectangle"
my_img_format = r".png"    
my_out_pic = my_img_pic+"_draw"
my_out_file = my_img_fldr+my_out_pic+my_img_format
try:
    # img.save('rectangle.png')
    my_img_rect.save(my_out_file, 'png')
except IOError:
    print("Unable to save image")    
    sys.exit(1)