# convert2png.py
#!/usr/bin/python
from PIL import Image
import sys

my_img_fldr = r".\my_imgs\\"
my_img_pic = r"tatras"
# my_img_pic = r"mr_mrs"
my_img_format = r".jpg"
my_img_file = my_img_fldr+my_img_pic+my_img_format

try:
    my_img = Image.open(my_img_file)
except IOError:
    print("Unable to load image")    
    sys.exit(1)

my_out_format = r".png"
my_out_file = my_img_fldr+my_img_pic+my_out_format
try:
    my_img.save(my_out_file, "png")
except IOError:
    print("Unable to save image")    
    sys.exit(1)    