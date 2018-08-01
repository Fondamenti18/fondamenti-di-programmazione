game_set = None


def get_possible(position, speed):
    boost = -1 + (speed[0] > 0) * 2, -1 + (speed[1] > 0) * 2
    return [
        ((position[0] + speed[0] + boost[0], position[1] + speed[1] + boost[1]), (boost[0], boost[1])),
        ((position[0] + speed[0] + boost[0], position[1] + speed[1]), (boost[0], 0)),
        ((position[0] + speed[0] + boost[0], position[1] + speed[1] - boost[1]), (boost[0], -boost[1])),
        ((position[0] + speed[0], position[1] + speed[1] + boost[1]), (0, boost[1])),
        ((position[0] + speed[0], position[1] + speed[1]), (0, 0)),
        ((position[0] + speed[0], position[1] + speed[1] - boost[1]), (0, -boost[1])),
        ((position[0] + speed[0] - boost[0], position[1] + speed[1] + boost[1]), (-boost[0], boost[1])),
        ((position[0] + speed[0] - boost[0], position[1] + speed[1]), (-boost[0], 0)),
        ((position[0] + speed[0] - boost[0], position[1] + speed[1] - boost[1]), (-boost[0], -boost[1]))
    ]


def get_order(first, second):
    return [first, int(first == 0), -(first + int(first == 0))], [second, int(second == 0), -(second + int(second == 0))]


def get_possible_slowdown(position, speed):
    order = get_order((speed[0] is not 0)*(1 - (speed[0] > 0) * 2), (speed[1] is not 0)*(1 - (speed[1] > 0) * 2))
    return [
        ((position[0] + speed[0] + order[0][0], position[1] + speed[1] + order[1][0]), (order[0][0], order[1][0])),
        ((position[0] + speed[0] + order[0][0], position[1] + speed[1] + order[1][1]), (order[0][0], order[1][1])),
        ((position[0] + speed[0] + order[0][0], position[1] + speed[1] + order[1][2]), (order[0][0], order[1][2])),
        ((position[0] + speed[0] + order[0][1], position[1] + speed[1] + order[1][0]), (order[0][1], order[1][0])),
        ((position[0] + speed[0] + order[0][1], position[1] + speed[1] + order[1][1]), (order[0][1], order[1][1])),
        ((position[0] + speed[0] + order[0][1], position[1] + speed[1] + order[1][2]), (order[0][1], order[1][2])),
        ((position[0] + speed[0] + order[0][2], position[1] + speed[1] + order[1][0]), (order[0][2], order[1][0])),
        ((position[0] + speed[0] + order[0][2], position[1] + speed[1] + order[1][1]), (order[0][2], order[1][1])),
        ((position[0] + speed[0] + order[0][2], position[1] + speed[1] + order[1][2]), (order[0][2], order[1][2]))
    ]


class GameSet:
    def __init__(self, game_map, position, speed, me, direction):
        self.map_length = len(game_map[0])
        self.map_height = len(game_map)
        self.start_position = position
        self.direction = direction
        self.position = position
        self.fastest_way = None
        self.map = game_map
        self.speed = speed
        self.holder = {}
        self.my_name = me
        self.reach_value = 0
        self.finish, self.holes, self.after_finishes = [], [], []
        self.look_at_map()
        self.holed_graph, self.graph_map = self.create_maps(position)
        self.faster_path = []
        self.find_faster()
        self.road_map = self.create_road_map()
        self.find_path((position[0], position[1] + direction), (speed[0], speed[1] + direction))

    def look_at_char(self, char, pos):
        if char == 'O':
            self.holes.append(pos)
        if char == '|':
            self.finish.append(pos)
            self.after_finishes.append((pos[0], pos[1] - self.direction))

    def look_at_map(self):
        for y in range(self.map_height):
            for x in range(self.map_length):
                self.look_at_char(self.map[y][x], (y, x))

    def get_connected_end(self):
        for end in self.finish:
            if self.get_near(self.holed_graph, end, self.reach_value - 1):
                return end

    def find_faster(self):
        next_node = self.get_connected_end()
        for x in reversed(range(1, self.reach_value)):
            self.faster_path.append(next_node)
            next_node = self.get_near(self.holed_graph, next_node, x)[0]

    def circled(self, node, rad):
        to_ret = []
        for cell in self.get_circle(node, rad):
            to_ret.extend(cell)
        return to_ret

    def create_road_map(self):
        to_ret = [[False for _ in y] for y in self.map]
        for node in self.faster_path:
            for coord in self.circled(node, 5):
                to_ret[coord[0]][coord[1]] = True
        return to_ret

    def holed(self, ret):
        return [[-1 if x == 0 else x for x in y] for y in ret]

    def de_holed(self, ret):
        return [[-1 if (y, x) in self.holes else ret[y][x] for x in range(len(ret[y]))] for y in range(len(ret))]

    def start_graph_map(self, pos):
        to_ret = [[0 if x == ' ' or x == 'O' else -1 for x in y] for y in self.map]
        to_ret[pos[0]][pos[1]] = 1
        return to_ret

    def create_maps(self, pos):
        ret = self.calculate_graph(self.start_graph_map(pos), 1, [pos])
        for finish in self.finish:
            ret[finish[0]][finish[1]] = self.reach_value
        return self.holed(ret), self.de_holed(ret)

    def calculate_graph(self, to_ret, value, final_list):
        while True:
            new_list, value = [], value + 1
            for position in final_list:
                for next_position in self.get_near(to_ret, position):
                    to_ret[next_position[0]][next_position[1]] = value
                    if next_position in self.after_finishes:
                        to_ret[next_position[0]][next_position[1] + self.direction] = value + 1
                        self.reach_value = value + 1
                        return to_ret
                    new_list.append(next_position)
            final_list = new_list

    def in_map(self, node):
        return 0 <= node[0] < self.map_height and 0 <= node[1] < self.map_length

    def get_circle(self, node, rad):
        return [[(y, x) for x in range(node[1] - rad, node[1] + rad)
                 if ((y - node[0]) ** 2) + ((x - node[1]) ** 2) > 2 * rad and self.in_map((y, x))]
                for y in range(node[0] - rad, node[0] + rad)]

    def get_near(self, scheme, pos, is_this=0):
        return [new_pos
                for new_pos in [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]
                if self.in_map(new_pos) and scheme[new_pos[0]][new_pos[1]] == is_this]

    def can_reach(self, position, speed):
        return [could for could in get_possible(position, speed)
                if self.in_map(could[0]) and self.road_map[could[0][0]][could[0][1]]
                and self.graph_map[could[0][0]][could[0][1]] > self.graph_map[position[0]][position[1]]]

    def can_slow(self, position, speed):
        return [could for could in get_possible_slowdown(position, speed)
                if self.in_map(could[0]) and self.map[could[0][0]][could[0][1]] == ' ']

    def find_path(self, position, speed):
        to_ret = [[-1 if x is -1 else 0 for x in y] for y in self.graph_map]
        to_ret[position[0]][position[1]] = 1
        self.find_path_ric(to_ret, position, speed, 2)

    def handle_node(self, node, to_ret, step):
        to_ret[node[0]][node[1]] = step
        if node in self.finish:
            self.fastest_way = [[x for x in y] for y in to_ret]

    def find_path_ric(self, to_ret, position, speed, step):
        for could in self.can_reach(position, speed):
            self.handle_node(could[0], to_ret, step)
            if self.fastest_way is None:
                self.find_path_ric(to_ret, could[0], (speed[0] + could[1][0], speed[1] + could[1][1]), step + 1)
        to_ret[position[0]][position[1]] = 0

    def next_faster_cell(self, position, speed):
        for cell in self.can_reach(position, speed):
            if self.fastest_way[cell[0][0]][cell[0][1]] == self.fastest_way[position[0]][position[1]] + 1:
                return cell[1][1], cell[1][0]

    def next_slower_cell(self, position, speed):
        for cell in self.can_slow(position, speed):
            if self.map[cell[0][0]][cell[0][0]] is ' ':
                return cell[1][1], cell[1][0]

    def get_next_move(self, position, speed, laps):
        if laps == 0:
            return self.next_faster_cell(position, speed)
        return self.next_slower_cell(position, speed)


def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, laps):
    global game_set
    if griglia_precedente == griglia_corrente:
        game_set = GameSet(griglia_corrente, (y, x), (vy, vx), car, verso)
    return game_set.get_next_move((y, x), (vy, vx), laps)
