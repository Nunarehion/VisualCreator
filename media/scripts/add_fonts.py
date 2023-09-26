from _import import *
from os import listdir as MyDir
import os

from ctypes import windll, byref, create_unicode_buffer, create_string_buffer
FR_PRIVATE  = 0x10
FR_NOT_ENUM = 0x20

def loadfonts():
    def loadfont(fontpath, private=True, enumerable=False):
        if isinstance(fontpath, str):
            pathbuf = create_unicode_buffer(fontpath)
            AddFontResourceEx = windll.gdi32.AddFontResourceExA
        flags = (FR_PRIVATE if private else 0) | (FR_NOT_ENUM if not enumerable else 0)
        numFontsAdded = AddFontResourceEx(byref(pathbuf), flags, 0)
        return bool(numFontsAdded)

    path = r'media/font'
    dir = MyDir(path)
    for x in dir:
        fontPath = f'{path}/{x}'
        print(loadfont(fontPath))
        print(dir)
        #pyglet.font.add_file(f'{path}\\{x}')




