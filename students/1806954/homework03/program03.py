from immagini import *

def control(pixel,cont,color,pixels):
    while pixel != []:
        x,y=pixel.pop()
        pixels[x][y]=color
        cont+=1
    return cont, x, y, pixels[x][y]

def inside(pixels, x, y):
    return 0 <= y < len(pixels) and 0 <= x < len(pixels[0])

def color (pixels, x, y, c1, c2, colore, toControl=[], toColor=[], border=[]):
    dx=False
    top=False
    sx=False
    bot=False
    if inside(pixels,x+1,y) and pixels[x+1][y]==colore:
        if [x+1,y] not in toControl and [x+1,y] not in toColor and [x+1,y] not in border:               
            toControl+=[[x+1,y]]
        dx=True
    if inside(pixels,x,y+1) and pixels[x][y+1]==colore:
        if [x,y+1] not in toControl and [x,y+1] not in toColor and [x,y+1] not in border:
            toControl+=[[x,y+1]]
        top=True
    if inside (pixels,x-1,y) and pixels[x-1][y]==colore:
        if [x-1,y] not in toControl and [x-1,y] not in toColor and [x-1,y] not in border:
            toControl+=[[x-1,y]]
        sx=True
    if inside(pixels,x,y-1) and pixels[x][y-1]==colore:
        if [x,y-1] not in toControl and [x,y-1] not in toColor and [x,y-1] not in border:
            toControl+=[[x,y-1]]
        bot=True
    if dx and top and sx and bot:
        toColor+=[[x,y]]
    elif dx or top or sx or bot:
        border+=[[x,y]]
    return toControl, toColor, border

def pix(inp,pixels):
    control1=0
    control2=0
    y,x,color1,color2=inp
    toColor=[pixels[x][y]]
    toControl, toColor, border=color(pixels, x, y, color1, color2, pixels[x][y], [] , toColor)
    while toControl != []:
        x,y=toControl.pop()
        toControl, toColor, border=color(pixels, x, y, color1, color2, pixels[x][y], toControl, toColor, border)
    del toColor[0]
    control1,x,y,pixels[x][y]=control(toColor,control1,color1,pixels)
    control2,x,y,pixels[x][y]=control(border,control2,color2,pixels)
    
    return [(control1,control2)]

    
def ricolora(fname, lista, fnameout):
    pixels = load(fname)
    lP=[]
    for x in lista:
        lP+=pix (x,pixels)
    save(pixels,fnameout)
    return lP
