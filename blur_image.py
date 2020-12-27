# blur_image.py
#!/usr/bin/python

from PIL import Image, ImageFilter
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

my_img_blur = my_img.filter(ImageFilter.BLUR)
my_img_blur.show()

my_out_pic = my_img_pic+"_blur"
my_out_file = my_img_fldr+my_out_pic+my_img_format
try:
    my_img_blur.save(my_out_file)
except IOError:
    print("Unable to save image")    
    sys.exit(1)    