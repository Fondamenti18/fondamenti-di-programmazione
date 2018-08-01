import png


def decod(png_img, c):
    img = []
    for line in png_img:
        new_line = []
        count = 0
        for i in reversed(range(0, len(line), 3)):
            pixel = (line[i], line[i + 1], line[i + 2])
            if pixel == c:
                count += 1
            else:
                count = 0
            new_line.insert(0, count)
        img += [new_line]
    return img


def check(img, coord, radius):
    if (coord[0] + radius) >= len(img):
        return False
    for i in range(coord[0], coord[0] + radius):
        if img[i][coord[1]] < radius:
            return False
    return True


def quadrato(filename, c):
    Res = decod(png.Reader(open(filename, mode='rb')).asRGB8()[2], c)
    size = 1
    last_coord = (0, 0)
    for y in range(len(Res)):
        for x in range(len(Res[y])):
            while check(Res, (y, x), size):
                size += 1
                last_coord = (x, y)
    return (size-1), last_coord