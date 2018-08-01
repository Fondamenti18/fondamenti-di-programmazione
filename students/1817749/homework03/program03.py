import png


def join_pixels(pixel_one, pixel_two):
    pixel_one["Near Pixels"].append(pixel_two)
    pixel_two["Near Pixels"].append(pixel_one)


def take_pixel_info(img, y_counter, x_counter, color):
    pixel = {"Color": color, "Coord": (y_counter, x_counter), "Near Pixels": []}
    if x_counter is not 0:
        join_pixels(pixel, img[y_counter][x_counter - 1])
    if y_counter is not 0:
        join_pixels(pixel, img[y_counter - 1][x_counter])
    return pixel


def load(fname):
    img, y_counter = [], 0
    for li in png.Reader(open(fname, mode='rb')).asRGB8()[2]:
        img.append([])
        for i in range(0, len(li), 3):
            img[y_counter].append(take_pixel_info(img, y_counter, i//3, (li[i], li[i + 1], li[i + 2])))
        y_counter += 1
    return img


def save(img, filename):
    png.from_array([[pixel["Color"] for pixel in line] for line in img], 'RGB').save(filename)


def closed_same_counter(pixel, color):
    cont = 0
    for pixel in pixel["Near Pixels"]:
        if pixel["Color"] == color:
            cont += 1
    return cont


def add_closer(buffer, pixel, area_set, border_set, color):
    for pixel in pixel["Near Pixels"]:
        if pixel["Color"] == color and pixel["Coord"] not in area_set and pixel["Coord"] not in border_set:
            buffer.add(pixel["Coord"])


def set_color(img, fill_color, area_color, area_set, border_set):
    for coord in area_set:
        img[coord[0]][coord[1]]["Color"] = fill_color
    for coord in border_set:
        img[coord[0]][coord[1]]["Color"] = area_color


def get_lists(buffer, img, color):
    area_set, border_set = set(), set()
    while buffer:
        coord = buffer.pop()
        pixel = img[coord[0]][coord[1]]
        if closed_same_counter(pixel, color) == 4:
            area_set.add(coord)
        else:
            border_set.add(coord)
        add_closer(buffer, pixel, area_set, border_set, color)
    return area_set, border_set


def edit(pixel, fill, border, img):
    area_list, border_list = get_lists({pixel["Coord"]}, img, pixel["Color"])
    set_color(img, fill, border, area_list, border_list)
    return len(area_list), len(border_list)


def ricolora(fname, lista, fnameout):
    img = load(fname)
    to_return = [edit(img[action[1]][action[0]], action[2], action[3], img) for action in lista]
    save(img, fnameout)
    return to_return
