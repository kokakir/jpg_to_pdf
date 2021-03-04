# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 12:50:31 2021

@author: koka5
"""

from PIL import Image
import os

dir_path = input("path to folder: ").split("\\")
str_ = ''
for j in range(len(dir_path)):
    str_ = str_ + dir_path[j] + "/"
path, dirs, files = next(os.walk(str_))
file_count = len(files)
im = []
for i in range(file_count):
    im.append(Image.open(str_ + files[i]))
    im[i] = im[i].convert('RGB')

im[0].save(str_ + 'K21_Kyrychek.pdf', save_all = True, append_images = im[1:])
print('ready')