import png


def save(img, filename):
    pngimg = png.from_array(img, 'RGB')
    pngimg.save(filename)


def run_x(y):
    png_line, path_line = [], []
    for x in range(0, len(y), 3):
        current_pixel = (y[x], y[x + 1], y[x + 2])
        png_line.append(current_pixel)
        if x % 120 == 0:
            if current_pixel == (255, 0, 0):
                path_line += ['o']
            else:
                path_line += [' ']
    return png_line, path_line


def read(img_png):
    img_array, path, y_counter = [], [], 0
    for y in img_png:
        png_line, path_line = run_x(y)
        if y_counter % 40 == 0:
            path.append(path_line)
        img_array.append(png_line)
        y_counter += 1
    return [img_array, path]


def edit(coord, color, img):
    for i in range(40):
        img[(coord[0] * 40) + i][(coord[1] * 40):(coord[1] * 40) + 40] = [color] * 40
    return img


def get_next_position(position, direction):
    if direction == 0:
        return [position[0], position[1] + 1]
    if direction == 1:
        return [position[0] + 1, position[1]]
    if direction == 2:
        return [position[0], position[1] - 1]
    if direction == 3:
        return [position[0] - 1, position[1]]


def can_go_next_direcion(path, position, direction):
    next_position = get_next_position(position, direction)
    return 0 <= next_position[0] <= 14 and 0 <= next_position[1] <= 14 and path[next_position[0]][
        next_position[1]] == ' ', next_position


def run(path, position, direction, img, fname1, count):
    if count == 4:
        save(edit(position, (0, 0, 255), img), fname1)
        return ""
    can_move, new_position = can_go_next_direcion(path, position, direction)
    if can_move:
        path[position[0]][position[1]] = 'o'
        return str(direction) + run(path, new_position, direction, edit(position, (0, 255, 0), img), fname1, 0)
    return run(path, position, (direction + 1) % 4, img, fname1, count + 1)


def cammino(fname, fname1):
    img_array, path = read(png.Reader(open(fname, mode='rb')).asRGB8()[2])
    return run(path, [0, 0], 0, img_array, fname1, 0)
