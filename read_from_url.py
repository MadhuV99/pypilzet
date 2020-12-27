# read_from_url.py
#!/usr/bin/python
from PIL import Image
import requests
import sys

url = 'https://i.ytimg.com/vi/vEYsdh6uiS4/maxresdefault.jpg'
# url = 'https://1drv.ms/u/s!AnI65yz9QGkGhuZ7-ay71-2xLncV0Q?e=OPzgHr'
try:
    resp = requests.get(url, stream=True).raw

except requests.exceptions.RequestException as e: 
    print("Request Error!", e) 
    sys.exit(1)

try:
    my_img_url = Image.open(resp)
    my_img_url.show()

except IOError:
    print("Unable to open image")
    sys.exit(1)

my_img_fldr = r".\my_imgs\\"
my_img_pic = r"sid"
my_img_format = r".jpg"    
my_out_pic = my_img_pic+"_url"
my_out_file = my_img_fldr+my_out_pic+my_img_format
try:
    # img.save('sid.jpg', 'jpeg') 
    my_img_url.save(my_out_file, 'jpeg')
except IOError:
    print("Unable to save image")    
    sys.exit(1)
