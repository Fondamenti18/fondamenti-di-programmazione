def type_on_cell_change(new, cell, free, must_be):
    checks = [new[cell[0]][0] + new[cell[0]][1] + new[cell[0]][2],
              new[0][cell[1]] + new[1][cell[1]] + new[2][cell[1]],
              new[0][0] + new[1][1] + new[2][2],
              new[0][2] + new[1][1] + new[2][0]]
    if must_be in checks:
        return must_be[0]
    if len(free) is 0:
        return "-"
    return "?"


def type_pause(leng):
    if leng is 0:
        return "-"
    return "?"


def win(check, row, col):
    return check in row or check in col


class NodoTris:
    def __init__(self, griglia, free_cells=None, fast_type=None, father=None, next_player=None, current_player=None):
        self.nome = griglia
        if father is None:
            self.type, self.free_cells, self.next_player, self.current_player = self.analyze_new()
        else:
            self.type = fast_type
            self.free_cells = free_cells
            self.next_player = next_player
            self.current_player = current_player
        self.father = father
        self.sons = self.generate_tree()

    def tipo(self):
        return self.type

    def royalty(self, eit):
        eit[self.type] += 1
        for node in self.sons:
            node.royalty(eit)
        return eit

    def esiti(self):
        num = {'x': 0, 'o': 0, '-': 0, '?': 0}
        self.royalty(num)
        return num['-'], num['o'], num['x']

    def remember_the_name(self, player, level, height, incomplete):
        if level < height:
            for node in self.sons:
                node.remember_the_name(player, level + 1, height, incomplete)
        else:
            if self.type is player:
                incomplete[0] += 1
        return incomplete[0]

    def vittorie_livello(self, giocatore, h):
        return self.remember_the_name(giocatore, 0, h, [0])

    def bomb(self, giocatore):
        if self.type is not '?':
            return self.type is giocatore
        for node in self.sons:
            if node.bomb(giocatore) == (self.next_player is giocatore):
                return self.next_player is giocatore
        return self.next_player is not giocatore

    def strategia_vincente(self, giocatore):
        return self.bomb(giocatore)

    def generate_tree(self):
        if self.type is not "?":
            return []
        to_ret = []
        for cell in self.free_cells:
            to_ret.append(self.on_cell_move(cell))
        return to_ret

    def analyze_players(self, counter):
        if counter['x'] == counter['o']:
            return "o", "x"
        else:
            return "x", "o"

    def analyze_new(self):
        free_cells, col, row, counter = self.analyze_cells([], ['', '', ''], ['', '', ''], {'x': 0, 'o': 0})
        next_player, current_player = self.analyze_players(counter)
        col.append(self.nome[0][0] + self.nome[1][1] + self.nome[2][2])
        col.append(self.nome[0][2] + self.nome[1][1] + self.nome[2][0])
        return self.analyze_type(row, col, free_cells), free_cells, next_player, current_player

    def analyze_cells(self, free_cells, col, row, counter):
        for y in range(3):
            for x in range(3):
                if self.nome[y][x] is '':
                    free_cells.append((y, x))
                else:
                    row[y] += self.nome[y][x]
                    col[x] += self.nome[y][x]
                    counter[self.nome[y][x]] += 1
        return free_cells, col, row, counter

    def analyze_type(self, row, col, free_cells):
        if win("xxx", row, col):
            return "x"
        if win("ooo", row, col):
            return "o"
        return type_pause(len(free_cells))

    def on_cell_move(self, cell):

        new, free_cells = [self.nome[x][:] for x in range(3)], self.free_cells[:]

        new[cell[0]][cell[1]] = self.next_player
        free_cells.remove(cell)

        return NodoTris(new, fast_type=type_on_cell_change(new, cell, free_cells, self.next_player * 3),
                        free_cells=free_cells,
                        next_player=self.current_player,
                        current_player=self.next_player,
                        father=self)


def gen_tree(griglia):
    return NodoTris(griglia)
