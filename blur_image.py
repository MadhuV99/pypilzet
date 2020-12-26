# blur_image.py
#!/usr/bin/python

from PIL import Image, ImageFilter
import sys

my_img_fldr = r".\my_imgs\\"
my_img_file = r"tatras"
try:
    my_img = Image.open(my_img_fldr+my_img_file)
except IOError:
    print("Unable to load image")    
    sys.exit(1)

blur_img = my_img.filter(ImageFilter.BLUR)
my_out_file = r"mr_mrs_blur.png"
blur_img.save(my_img_fldr+my_out_file)