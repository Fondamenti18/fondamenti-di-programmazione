path = list()
goal = []
start_range = []

class Spot():

    def __init__(self, j, i, dy=0, dx=0):
        self.j = j
        self.i = i
        self.dy = dy
        self.dx = dx
        self.acc_y = abs(self.dy)//(self.dy or 1) or 1
        self.acc_x = abs(self.dx)//(self.dx or 1) or 1
        self.prev = []
        self.previous = []
        self.neighbors = []
        self.ls_childs = []

    def add_neighbors(self, grid):
        points_ls = [(self.j-1, self.i), (self.j+1,self.i), (self.j,self.i-1), (self.j,self.i+1),
                     (self.j-1,self.i-1), (self.j-1,self.i+1), (self.j+1,self.i-1), (self.j+1,self.i+1)]
        for point in points_ls:
            if point in grid: self.neighbors.append(Spot(point[0], point[1], point[0]-self.j, point[1]-self.i))

    def add_childs(self, r_path, diz_path, clean_grid):
        ind_p, ind_d = self.set_indices(r_path, diz_path)
        for jj in [-1, 0, 1]:
            for ii in [-1, 0, 1]:
                child = (self.j + jj*self.acc_y + self.dy, self.i + ii*self.acc_x + self.dx)
                if child in clean_grid:
                    if child in r_path: self.add_p_child(child, r_path, ind_p)
                    elif child in diz_path: self.add_d_child(child, diz_path, ind_d)

    def set_indices(self, r_path, diz_path):
        ind_p = 0
        ind_d = 0
        if (self.j, self.i) in r_path: ind_p = r_path.index((self.j, self.i))
        if diz_path: ind_d = diz_path[(self.j, self.i)]
        return ind_p, ind_d

    def add_p_child(self, child, r_path, ind_p):
        ind_p_child = r_path.index(child)
        if ind_p_child > ind_p:
            self.ls_childs.append(Spot(child[0], child[1], child[0] - self.j, child[1] - self.i))

    def add_d_child(self, child, diz_path, ind_d):
        ind_d_child = diz_path[child]
        if ind_d_child > ind_d:
            self.ls_childs.append(Spot(child[0], child[1], child[0] - self.j, child[1] - self.i))

class Speed():
    
    def __init__(self, y, x, spd, dir_y, dir_x, clean_grid):
        self.y = y
        self.x = x
        self.grid = clean_grid  # Grid without holes
        self.spd = spd
        self.dir_y = dir_y
        self.dir_x = dir_x
        self.neighbors = self.add_neighbors(self.y, self.x)
        self.l_p = ''   # Landing point: actual (y, x) + spd in the right direction
        self.l_neighbors = []   # Landing point's neighbors

    def add_neighbors(self, j, i):
        points_ls = [(j, i), (j-1, i), (j+1, i), (j, i-1), (j, i+1), (j-1, i-1), (j-1, i+1), (j+1, i-1), (j+1, i+1)]
        return [point for point in points_ls if point in self.grid]
    
    def add_l_points(self):
        # These two lines add the landing point
        if (self.y + self.spd*self.dir_y, self.x + self.spd*self.dir_x) in self.grid:
            self.l_p = (Speed(self.y + self.spd*self.dir_y, self.x + self.spd*self.dir_x, self.spd-1, self.dir_y, self.dir_x, self.grid))
        # Down lines add landing point's neighbors
        for i in [-1, 1]:
            ls_apg = []
            spid = self.spd + i
            ls_apg = self.add_neighbors(self.y + spid*self.dir_y, self.x + spid*self.dir_x)
            ls_apg = [Speed(u, v, spid, self.dir_y, self.dir_x, self.grid) for u, v in ls_apg]
            self.l_neighbors += ls_apg

    def braking_pnt(self):
        # The braking point is used to stop the car when reconstructing the path
        t_spd = self.spd - 1  # Temp SPD
        pnt = (Speed(self.y + t_spd*self.dir_y, self.x + t_spd*self.dir_x, t_spd, self.dir_y, self.dir_x, self.grid))
        if pnt: return pnt
        else:  # If there is direct braking point, go for one of his neighbors
            return self.add_l_neighbors(self.y + t_spd*self.dir_y, self.x + t_spd*self.dir_x, t_spd)
        
    def add_l_neighbors(self, j, i, vel):
        # This method is used exclusively by the method braking_pnt()
        points_ls = [(j, i), (j-1, i), (j+1, i), (j, i-1), (j, i+1), (j-1, i-1), (j-1, i+1), (j+1, i-1), (j+1, i+1)]
        for pj, pi in points_ls:
            if (pj, pi) in self.grid:
                return Speed(pj, pi, vel, self.dir_y, self.dir_x, self.grid)


def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, laps):
    ''' Main function called by the Simulator '''
    global goal, path
    if laps:
        path = []
        return activate_brakes(vx, vy, verso)
    if not path:
        ls_grid, ls_grid_o = build_grid(griglia_corrente, starty, startx)
        clean_grid = set(ls_grid) - set(ls_grid_o)
        goal = range_point(ls_grid, starty, startx-verso)
        find_best_path(ls_grid, ls_grid_o, Spot(starty, startx+verso), goal, verso)
        while True:
            n_start = check_path(ls_grid, ls_grid_o)
            if not n_start:
                diz_path = build_diz_path(read_path(path), clean_grid)
                break
            find_best_path(ls_grid, ls_grid_o, Spot(n_start[0], n_start[1]), goal, verso)
        path.insert(0, Spot(starty, startx+verso))
        diz_path = check_holes(diz_path, ls_grid_o)
        path = smart_path(Spot(starty, startx+verso), diz_path, read_path(path), goal, clean_grid)
        speedy_start(starty, startx, verso)
    el = path.pop()
    xx, yy = checked_acc(el.i - x - vx, el.j - y - vy)
    return xx, yy

def find_best_path(ls_grid, ls_grid_o, start, goal, verso):
    ' It founds the shortest path ahead '
    global path
    queue = list()
    visited = set()
    queue.append(start)
    while queue:
        current = queue.pop()
        current.neighbors = []
        if (current.j, current.i) in goal:
            path += current.prev  # Progressive Path
            return
        if (current.j, current.i) in visited: continue
        visited.add((current.j, current.i))
        current.add_neighbors(ls_grid)
        for neighbor in current.neighbors:
            # These line avoids non-sustainable curves
            if drifting_point(current, neighbor): continue
            queue.insert(0, neighbor)
            neighbor.prev = []
            neighbor.prev += current.prev + [neighbor]
    return # ERROR - PATH NOT FOUND

def check_path(grid, grid_o):
    ''' Function that checks every point of the path looking for a not reachable point, and if it founds one,
    it tries to rebuild the corrent path by adding those steps. '''
    global path
    r_path = read_path(path)
    max_i = len(r_path) - 1
    new_path = []
    clean_grid = set(grid) - set(grid_o)  # Grid with no holes
    holes_found = set()
    for coord in r_path:
        if coord not in grid_o: new_path = add_step(new_path, coord[0], coord[1])
        else:
            holes_found.add(coord)
            if r_path[r_path.index(coord)-1] in holes_found: continue # Avoids taking multiple times the same hole
            i_coord = r_path.index(coord) - 1  # Coordinates of the step before a hole
            new_coord = r_path[i_coord]
            dir_y, dir_x, spd = calc_tool(r_path, i_coord, new_coord, max_i, grid_o)
            obj = Speed(new_coord[0], new_coord[1], spd, dir_y, dir_x, clean_grid)
            obj.add_l_points()
            r_l_neighbors = read_l_neighbors(obj.l_neighbors)
            n = spd - 1  # Width of the hole
            y = 0
            new_path = add_step(new_path, obj.y, obj.x)
            for y in range(n):
                intersection = set(r_l_neighbors) & set(r_path)
                if intersection: # No problem at first step
                    element = intersection.pop()
                    obj, r_l_neighbors = choose_l_neighbor(obj, element, intersection)
                    new_path = add_step(new_path, obj.y, obj.x)
                else:
                    new_path, obj = fix_path(obj, new_path)
                    path = new_path
                    return (obj.y, obj.x)  # Coordinates from which search for a new path
    path = new_path
    return  # PATH IS OKAY

def fix_path(obj, new_path):
    ' This function repairs the unsatisfable path by adding those speed-obliged points '
    obj.spd -= 1  # Braking point's purpose is to reduce the speed to allow to find a new shortest path
    while obj.spd:
        if (obj.y, obj.x) not in read_path(new_path): 
            new_path.append(Spot(obj.y, obj.x))
        obj = obj.braking_pnt()
    return new_path, obj

def smart_path(start, diz_path, r_path, goal_pnts, clean_grid):
    ' A smart function, it looks for the best speed to use '
    ls = list()
    ls.append(start)
    while ls:
        current = ls.pop()
        if (current.j, current.i) in goal_pnts:
            print('trovato')
            return current.previous[::-1]
        current.add_childs(r_path, diz_path, clean_grid)
        ls += current.ls_childs
        for child in current.ls_childs:
            child.previous += current.previous + [child]
    return # ERROR - NO BEST PATH FOUND

def speedy_start(starty, startx, verso):
    ' If at the beginning the speed is not too high, it increases it '
    vel_y = vel_x = acc_y = acc_x = counter = 0
    yyy, xxx = starty, startx
    r_path = read_path(path)[::-1]
    for ely, elx in r_path:
        acc_y = ely - yyy - vel_y
        acc_x = elx - xxx - vel_x
        if acc_y not in [-1, 0, 1] or acc_x not in [-1, 0, 1]: counter += 1
        acc_x, acc_y =checked_acc(acc_x, acc_y)
        vel_y += acc_y
        vel_x += acc_x
        yyy += vel_y
        xxx += vel_x
    if counter > 5: 
        path.append(Spot(starty, startx+verso))
        return  # Speed is too high
    return

# =============================================================================
#  UTILITY FUNCTIONS
# =============================================================================

def calc_tool(r_path, i_coord, coord, max_i, grid_o):
    ''' Pure mathematical function, used to outline some helpfull infos, such as: the directions in which
    the hole extends to, the minimum speed necessary to cross the hole. '''
    dir_y = coord[0] - r_path[i_coord-1][0]
    dir_x = coord[1] - r_path[i_coord-1][1]    
    if dir_y and dir_y == dir_x:
        dir_y = r_path[i_coord+1][0] - coord[0]
        dir_x = r_path[i_coord+1][1] - coord[1]
    speed = 0
    i_coord += 1
    while 0 <= i_coord + speed < max_i and r_path[i_coord + speed] in grid_o:  speed += 1
    # Speed has been incresead by one because 'speed' indicates the width of the hole.
    return dir_y, dir_x, speed+1

def range_point(grid, y, x):
    ' Function used to determine the actual lenght of the start / finish '
    a, b = -1, 1
    while (y+a, x) in grid: a -= 1
    while (y+b, x) in grid: b += 1
    goal = [(i+y, x) for i in range(a+1,b)]
    return goal

def build_grid(grid, starty, startx):
    ''' This function forms 2 grids: ls_grid_o which holds only the non-dangerous holes, while
    ls_gird has both the holes and the passable points '''
    global start_range
    ls_grid = []
    ls_grid_o = []
    h = len(grid)
    w = len(grid[0])
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[j][i] in ' |AXB': ls_grid.append((j,i))
            elif grid[j][i] == 'O' and borderless(grid, h, w, j, i): 
                ls_grid.append((j,i))
                ls_grid_o.append((j,i))
    start_range = range_point(ls_grid, starty, startx)
    return clean_from_start(ls_grid, start_range), ls_grid_o

def build_diz_path(path, clean_grid):
    ' Forms a dictionary for extending the path '
    diz = dict()
    points_ls = [(-1, 0), (+1, 0), (0, -1), (0, +1), (-1, -1), (-1, +1), (+1, -1), (+1, +1)]
    for j, i in path:
        diz[(j, i)] = path.index((j, i))
        for a,b in points_ls:
            coord = (j+a, i+b)
            if coord not in path and coord in clean_grid and coord not in diz:
                diz[coord] = path.index((j, i))
    return diz

def check_holes(diz_path, ls_grid_o):
    ' Calculates the amount of holes in the path '
    if len(ls_grid_o) > 15: # Lots of holes found in path, really high speed needed
        return diz_path
    return {}

def clean_from_start(ls_grid, start_range):
    ' Forms a grid with no starting points '
    return [point for point in ls_grid if point not in start_range]

def borderless(grid, h, w, j, i):
    ' Looks for holes nearby ostacles '
    ls_pnts = [(j-1, i), (j, i+1), (j-1, i), (j, i-1)]
    for point in ls_pnts: 
        if not(0 <= point[0] < h and 0 <= point[1] < w and grid[point[0]][point[1]]  in ' OAXB|'): return False
    return True

def drifting_point(current, neighbor):
    ' Checks if if there is a die-hard point '
    if current.dy != neighbor.dy and current.dy+neighbor.dy == 0: return True
    if current.dx != neighbor.dx and current.dx+neighbor.dx == 0: return True
    return False

def read_path(path):
    ' Path with objects --> Path with coordinates '
    return [(el.j, el.i) for el in path]

def read_l_neighbors(neighbors):
    ' Same behaviour as read_path() '
    return [(el.y, el.x) for el in neighbors]

def choose_l_neighbor(obj, element, intersection):
    " Choses a new target among all landing point's neighbors "
    if obj.l_p and (obj.l_p.y, obj.l_p.x) in intersection:
        obj = obj.l_p
        obj.add_l_points()
        r_l_neighbors = read_l_neighbors(obj.l_neighbors)
        return obj, r_l_neighbors
    # There is no landing point, choses one from l_neighbors
    for el in obj.l_neighbors:
        if (el.y, el.x) == element:
            obj = el
            obj.add_l_points()
            r_l_neighbors = read_l_neighbors(obj.l_neighbors)
    return obj, r_l_neighbors

def add_step(new_path, y, x):
    ' It inserts a step that was not present in the path, but that should '
    if (y, x) not in read_path(new_path):
        new_path.append(Spot(y, x))
    return new_path

def activate_brakes(vx, vy, verso):
    " Function explains itself "
    if vx: xx = -verso
    else: xx = 0
    if vy: yy = -(abs(vy)//vy)
    else: yy = 0
    return xx, yy

def checked_acc(xx, yy):
    ' If the cars exceeds with the speed, it must be stopped. '
    if xx < -1: xx = -1
    elif xx > 1: xx = 1
    if yy < -1: yy = -1
    elif yy > 1: yy = 1
    return xx, yy