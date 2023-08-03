import base64
from pathlib import Path
from random import choices
from PIL import Image
import math
import pickle

def makeRGBArray():
    obf_array = []
    for i in range(0,65):
        colour = choices(range(0,255)), choices(range(0,255)), choices(range(0,255))
        my_ints = tuple(int(l[0]) for l in colour)
        obf_array.append(my_ints)
    return obf_array

def createImage(rgb_values, width, height):
    img = Image.new('RGB', (width, height), color = 'white')
    pixels = img.load()
    for i in range(width):
        for j in range(height):
            pixels[j,i] = rgb_values[j+(i*width)]
    img.save("/ThePixelator/Colours.png")
    img.close()

txt = open("/ThePixelator/ShakespeareSample.txt", "r", encoding="utf-8").read()
txt_bytes = txt.encode('ascii')
base64_bytes = base64.b64encode(txt_bytes)
base64_txt = base64_bytes.decode('ascii')

size_dif = (math.ceil(math.sqrt(len(base64_txt)))*math.ceil(math.sqrt(len(base64_txt))))-len(base64_txt)
for i in range(0, size_dif):
    base64_txt += '$'
    
b64_charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/=+$'
charset_dict = {index: value for index, value in enumerate(b64_charset)}

obf_array = makeRGBArray()
colour_array = []
for char in base64_txt:
    for key, value in charset_dict.items():
        if char == value:
            colour_array.append(tuple(obf_array[key]))
      
with open("colourSeed.csv", 'wb') as g:
    pickle.dump(obf_array, g)
    g.close()

result_image = createImage(colour_array, math.ceil(math.sqrt(len(colour_array))), math.ceil(math.sqrt(len(colour_array))))
