# show_tkinter.py
#!/usr/bin/python

from PIL import Image, ImageTk
from tkinter import Tk
from tkinter.ttk import Frame, Label
import sys

class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.loadImage() 
        self.initUI()
        
        
    def loadImage(self):
        my_img_fldr = r".\my_imgs\\"
        my_img_pic = r"tatras"
        # my_img_pic = r"mr_mrs"
        my_img_format = r".jpg"
        my_img_file = my_img_fldr+my_img_pic+my_img_format
        try:
            self.img = Image.open(my_img_file)

        except IOError:
            print("Unable to load image")
            sys.exit(1)
        
    
    def initUI(self):
      
        my_img_pic = r"tatras"
        # my_img_pic = r"mr_mrs"
        self.master.title(my_img_pic)
        
        my_img = ImageTk.PhotoImage(self.img)
        label = Label(self, image=my_img)
        
        # reference must be stored
        label.image = my_img
        
        label.pack()
        self.pack()
        
        
    def setGeometry(self):
      
        w, h = self.img.size
        self.master.geometry(("%dx%d+300+300") % (w, h))
        

def main():
  
    root = Tk()
    ex = Example()
    ex.setGeometry()
    root.mainloop()  


if __name__ == '__main__':
    main()  