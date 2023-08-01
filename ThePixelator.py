import base64
from pathlib import Path
from random import choices
from PIL import Image
import math
import pickle

def makeRGBArray():
    obfArray = []
    for i in range(0,65):
        colour = choices(range(0,255)), choices(range(0,255)), choices(range(0,255))
        my_ints = tuple(int(l[0]) for l in colour)
        obfArray.append(my_ints)
    return obfArray

def create_image(rgb_values, width, height):
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
    base64_txt += '+'

obfArray = makeRGBArray()
obf_dict = {index: value for index, value in enumerate(obfArray)}
colourArray = []
for char in base64_txt:
    if char == 'a':
        colourArray.append(tuple(obfArray[0]))
    if char == 'b':
        colourArray.append(tuple(obfArray[1]))
    if char == 'c':
        colourArray.append(tuple(obfArray[2]))
    if char == 'd':
        colourArray.append(tuple(obfArray[3]))
    if char == 'e':
        colourArray.append(tuple(obfArray[4]))
    if char == 'f':
        colourArray.append(tuple(obfArray[5]))
    if char == 'g':
        colourArray.append(tuple(obfArray[6]))
    if char == 'h':
        colourArray.append(tuple(obfArray[7]))
    if char == 'i':
        colourArray.append(tuple(obfArray[8]))
    if char == 'j':
        colourArray.append(tuple(obfArray[9]))
    if char == 'k':
        colourArray.append(tuple(obfArray[10]))
    if char == 'l':
        colourArray.append(tuple(obfArray[11]))
    if char == 'm':
        colourArray.append(tuple(obfArray[12]))
    if char == 'n':
        colourArray.append(tuple(obfArray[13]))
    if char == 'o':
        colourArray.append(tuple(obfArray[14]))
    if char == 'p':
        colourArray.append(tuple(obfArray[15]))
    if char == 'q':
        colourArray.append(tuple(obfArray[16]))
    if char == 'r':
        colourArray.append(tuple(obfArray[17]))
    if char == 's':
        colourArray.append(tuple(obfArray[18]))
    if char == 't':
        colourArray.append(tuple(obfArray[19]))
    if char == 'u':
        colourArray.append(tuple(obfArray[20]))
    if char == 'v':
        colourArray.append(tuple(obfArray[21]))
    if char == 'w':
        colourArray.append(tuple(obfArray[22]))
    if char == 'x':
        colourArray.append(tuple(obfArray[23]))
    if char == 'y':
        colourArray.append(tuple(obfArray[24]))
    if char == 'z':
        colourArray.append(tuple(obfArray[25]))
    if char == 'A':
        colourArray.append(tuple(obfArray[26]))
    if char == 'B':
        colourArray.append(tuple(obfArray[27]))
    if char == 'C':
        colourArray.append(tuple(obfArray[28]))
    if char == 'D':
        colourArray.append(tuple(obfArray[29]))
    if char == 'E':
        colourArray.append(tuple(obfArray[30]))
    if char == 'F':
        colourArray.append(tuple(obfArray[31]))
    if char == 'G':
        colourArray.append(tuple(obfArray[32]))
    if char == 'H':
        colourArray.append(tuple(obfArray[33]))
    if char == 'I':
        colourArray.append(tuple(obfArray[34]))
    if char == 'J':
        colourArray.append(tuple(obfArray[35]))
    if char == 'K':
        colourArray.append(tuple(obfArray[36]))
    if char == 'L':
        colourArray.append(tuple(obfArray[37]))
    if char == 'M':
        colourArray.append(tuple(obfArray[38]))
    if char == 'N':
        colourArray.append(tuple(obfArray[39]))
    if char == 'O':
        colourArray.append(tuple(obfArray[40]))
    if char == 'P':
        colourArray.append(tuple(obfArray[41]))
    if char == 'Q':
        colourArray.append(tuple(obfArray[42]))
    if char == 'R':
        colourArray.append(tuple(obfArray[43]))
    if char == 'S':
        colourArray.append(tuple(obfArray[44]))
    if char == 'T':
        colourArray.append(tuple(obfArray[45]))
    if char == 'U':
        colourArray.append(tuple(obfArray[46]))
    if char == 'V':
        colourArray.append(tuple(obfArray[47]))
    if char == 'W':
        colourArray.append(tuple(obfArray[48]))
    if char == 'X':
        colourArray.append(tuple(obfArray[49]))
    if char == 'Y':
        colourArray.append(tuple(obfArray[50]))
    if char == 'Z':
        colourArray.append(tuple(obfArray[51]))
    if char == '0':
        colourArray.append(tuple(obfArray[52]))
    if char == '1':
        colourArray.append(tuple(obfArray[53]))
    if char == '2':
        colourArray.append(tuple(obfArray[54]))
    if char == '3':
        colourArray.append(tuple(obfArray[55]))
    if char == '4':
        colourArray.append(tuple(obfArray[56]))
    if char == '5':
        colourArray.append(tuple(obfArray[57]))
    if char == '6':
        colourArray.append(tuple(obfArray[58]))
    if char == '7':
        colourArray.append(tuple(obfArray[59]))
    if char == '8':
        colourArray.append(tuple(obfArray[60]))
    if char == '9':
        colourArray.append(tuple(obfArray[61]))
    if char == '/':
        colourArray.append(tuple(obfArray[62]))
    if char == '=':
        colourArray.append(tuple(obfArray[63]))
    if char == '+':
        colourArray.append(tuple(obfArray[64]))

with open("colourSeed.csv", 'wb') as g:
    pickle.dump(obfArray, g)
    g.close()


result_image = create_image(colourArray, math.ceil(math.sqrt(len(colourArray))), math.ceil(math.sqrt(len(colourArray))))
