 #-*- coding: utf-8 -*-

import os
filename = input('filename:')
search_dir = os.path.abspath('.')

def search_file(name, path):
    for x in os.listdir(path):    
        if os.path.isdir(x):
              search_file(name, x)
        elif name in x:
            print('find', os.path.abspath(x))

search_file(filename, search_dir)




