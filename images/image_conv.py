#! /usr/bin/env python3

import os, sys
from PIL import Image
from glob import glob 
size = (128,128)
folder = "C:/Users/teyee/Documents/PYTHON EARL/PythonAPI/images/"
for file in glob('ic_*'): # ignore hidden file (images/.DS_Store) from iteration
    path, filename = os.path.split(file)
    filename = os.path.splitext(filename)[0] # get filename without extension
    image = Image.open(file).convert('RGB')
    image.rotate(270)
    image.resize(size)
    image.save('C:/Users/teyee/Documents/PYTHON EARL/PythonAPI/icons/{}.jpeg'.format(filename))
print('OK')

    