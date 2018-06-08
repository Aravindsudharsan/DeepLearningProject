from PIL import Image
import os, sys
import glob

count=0
for i in (os.listdir(os.getcwd())):
    if i.endswith(".png"):
        count=count+1
        im = Image.open(i)
        bg = Image.new("RGB", im.size, (255,255,255))
        bg.paste(im,im)
        bg.save("image_%d.jpg"%count)
        


im = Image.open("100900_0.png")
bg = Image.new("RGB", im.size, (255,255,255))
bg.paste(im,im)
bg.save("colors.jpg")

