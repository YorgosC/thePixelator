import base64
from pathlib import Path
from PIL import Image
import pickle

def readPxls(img):
    pixels = img.load()

    width, height = img.size
    rgb_values = []

    for i in range(width):
        for j in range(height):
            rgb_values.append(pixels[j,i])
    return rgb_values
    img.close()

myimg = Image.open("/ThePixelator/Colours.png")
rgbArray = readPxls(myimg)

with open ("/ThePixelator/colourSeed.csv", 'rb') as f:
    colourSeed = pickle.load(f)
    f.close()

b64_charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/=+'

def decodeKey(rgb_values, seed, charset):
    b64_string = ''
    seed_dict = {index: value for index, value in enumerate(seed)}
    for rgb in rgb_values:
        for key, value in seed_dict.items():
            if rgb == value:
                b64_string += charset[key]
    return b64_string

b64_string = decodeKey(rgbArray, colourSeed, b64_charset)
b64_string = b64_string.replace("+", "")

decoded_bytes = base64.b64decode(b64_string)
decoded_string = decoded_bytes.decode('ascii')

with open("SexyAgain.txt", "w") as f:
    f.write(decoded_string)
    f.close()
