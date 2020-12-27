# grayscale.py
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

my_img_bnw = my_img.convert('L')
my_img_bnw.show()

my_out_pic = my_img_pic+"_bnw"
my_out_file = my_img_fldr+my_out_pic+my_img_format
try:
    my_img_bnw.save(my_out_file)
except IOError:
    print("Unable to save image")    
    sys.exit(1)    