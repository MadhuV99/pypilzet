# show_image.py
#!/usr/bin/python

from PIL import Image
import sys

my_img_fldr = r".\my_imgs\\"
my_img_file = r"tatras.jpg"

try:
    my_img = Image.open(my_img_fldr+my_img_file)

except IOError:
    print("Unable to load image")
    sys.exit(1)
    
my_img.show()