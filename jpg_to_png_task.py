from PIL import Image
import os
from sys import argv

first_loc = os.getcwd()
jpg_loc = (os.getcwd() + '\\' + argv[1])
if argv[2] not in os.listdir():
    os.mkdir(argv[2])
png_loc = os.getcwd() + '\\' + argv[2]

for img in os.listdir(jpg_loc):
	if img.endswith('.jpg'):
	    os.chdir(jpg_loc)
	    current_img = Image.open(img)
	    png_img_name = os.path.splitext(img)[0]
	    os.chdir(png_loc)
	    current_img.save(f'{png_img_name}.png', 'png')
