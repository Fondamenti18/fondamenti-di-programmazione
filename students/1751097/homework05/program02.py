'''
Obiettivo dell'esercizio e' sviluppare la strategia di gioco di una macchinetta che gira su una pista di formula 1.

Il gioco consiste in un percorso di gara, rappresentato da una griglia di caratteri
(' '=vuoto, '#' = ostacolo, 'A....Z' = auto, '|' = traguardo 'O' = buca tutti gli altri caratteri sono ostacoli)
nella quale si trova la macchina del giocatore (un carattere 'A..Z'), che deve:
    correre attorno alla pista per un intero giro senza sbattere contro ostacoli o altre macchine
    raggiungere il traguardo
    fermarsi senza sbattere (vx=vy=0)

Il punteggio di gioco e' il numero di step che sono stati necessari a percorrere la gara e fermarsi senza sbattere.

Ad ogni istante il simulatore della macchinetta conosce:
    x, y:   la posizione della macchina sulla griglia di gioco
    vx, vy: la velocita' corrente della macchina
Ad ogni step della simulazione il giocatore puo' solo:
    incrementare di 1, decrementare di 1 o lasciare come sono i valodi vx, vy della velocita' (-1,0,+1)
corrispondentemente il simulatore:
    somma gli incrementi/decrementi alle due variabili vx,vy
    somma le velocita' vx,vy alla posizione x,y ottenendo la prossima posizione della macchina
    controlla se la nuova posizione e' vuota
        se la nuova posizione e' occupata (da un ostacolo o da un'altra macchina) il gioco termina senza completare la corsa
        se la posizione contiene una buca si slitta di un carattere a caso fino a restare sulla strada o su un ostacolo
        altrimenti si sposta la macchina sulla nuova posizione
    se il traguardo e' stato raggiunto nella direzione giusta e la macchina e' ferma (vx=vy=0) la gara termina
    altrimenti si riesegue un nuovo step (chiedendo alla funzione 'ai' del giocatore cosa fare)

Il programma che dovete realizzare e' l'AI che guida la macchina, che riceve come input:
    la griglia di gioco del passo precedente (comprese le altre macchine)
    la griglia di gioco del passo corrente (comprese le altre macchine)
    la posizione x,y della propria macchina
    la velocita' vx,vy della propria macchina
    il carattere che individua la vostra macchina
    il verso di rotazione (-1= si parte verso sinistra rispetto al traguardo, +1= si parte verso destra rispetto al traguardo)
    la posizione startx,starty di partenza della macchina
e deve produrre in output la coppia:
    ax, ay  variazione della velocita (coppia di valori -1,0,+1)
La simulazione di tutti i 3 percorsi di gara per la qualificazione (senza visualizzazione) deve impiegare al piu' 1 minuto.

In questo esercizio la valutazione avverra' in tre fasi:
    giro di qualificazione:
        la macchina gira sulla pista di gara da sola, senza altri concorrenti su 3 piste in cui non sono presenti barriere di buche
        superare questa prova da' il punteggio minimo di qualificazione (18)
    giro di premio:
        la macchina gira su una pista di gara simile (ma diversa) da quella "Roma" che contiene barriere di buche
        superare questa prova da' il punteggio di qualificazione 24

    La classifica ottenuta nella qualificazione viene usata per determinare i gironi e poi il torneo di gara della fase successiva
    chi non completa il giro di qualificazione non partecipa al successivo torneo e non e' sufficiente

    Gironi e torneo ad eliminazione:
        (per ogni scontro vengono eseguite due gare, con A a sinistra e B a destra e viceversa)
        viene organizzato un torneo in cui prima si eseguono dei gironi di 4-5 auto
            Le due auto che ottengono il miglior punteggio sul girone partecipano alle eliminatorie successive
            Per ogni gara del girone vengono assegnati:
                3 punti a chi vince la gara
                1 punto per pareggio o scontro
                0 punti a chi perde
                a parita' di punteggio vince la macchina che ha fatto meno incidenti
                a parita' di incidenti viene simulata un'altra gara con una pista con barriere di buche (tipo "roma" per intenderci)

        Le due auto qualificate di ciascun girone partecipano ad una fase eliminatoria a scontro diretto
            l'auto vincente passa il turno (in caso di patta su esegue una gara aggiuntiva con barriere di buche casuali)

    La classifica finale della fase a scontro diretto determina i voti:
        I livelli del torneo ad eliminazione individuano i voti ottenuti, a seconda del numero di partecipanti (per esempio 6 livelli -> 2.1 voti per livello circa)
        Per avere la sufficienza bisogna aver completato almeno il giro di qualificazione sulle diverse piste
        Se una macchina ha ottenuto il voto 24 nella fase di qualificazione, il voto finale dell'esercizio e' almeno 24

COMPORTAMENTO: le auto che usano comportamenti scorrette non superano la qualificazione. Es.
    - precalcolare offline la strategia e inserirla nel programma
    - andare apposta contro l'auto dell'avversario
    - ...

ATTENZIONE: NON usate lettere accentate ne' nel codice ne' nei commenti

'''

from random     import randint
from collections import deque
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

pathv = []

def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, laps):

    if (x, y) == (startx, starty) or check_deviation(griglia_corrente, griglia_precedente, car, (x,y), (vx,vy)):
        global pathv
        #print('NEW PATH! ')
        start = (x, y)

        end = find_end(griglia_corrente, (startx, starty))
        fake_end = find_fake_end(griglia_corrente, (startx, starty), end)

        game_map = build_map_dijkstra(griglia_corrente, start, fake_end)
        game_map[end] = fake_end

        path = find_path(game_map, start, end)
        pathv = convert_velocity(path, vx, vy)
        #print(pathv)
        #print("verso", verso)
    try:
        return pathv.pop()
    except IndexError:
        return (0, 0) #(-verso,0)
'''
def check_deviation(grid, coords, vel):
    prev = (coords[0] + vel[0], coords[1] + vel[1])
    print("e",element(grid, prev))
    if element(grid, prev) == 'O':
        return True
    return False
'''
'''
def check_deviation(pgrid, cgrid, car):
    for y in range(len(pgrid)):
        for x in range(len(pgrid[0])):
            coords = (x,y)
            if element(pgrid, coords) == car:
                print("TROVATO!!!!!", element(cgrid, coords) == 'O' )
                return element(cgrid, coords) == 'O'

    return False
'''
'''
def check_deviation(cgrid, pgrid, car, coords, vel):
    car_coords = get_car(pgrid, car)
    slit_coords = (car_coords[0] + vel[0], car_coords[1] + vel[1])
    return coords != slit_coords
'''

# se funziona usare questa versione (performance)
def check_deviation(cgrid, pgrid, car, coords, vel):
    prev_coords = (coords[0] - vel[0], coords[1] - vel[1])

    return element(pgrid, prev_coords) != car

def get_car(grid, car):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            coords = (x,y)
            car_elem = element(grid, coords)
            if car_elem == car:
                return coords

    raise Exception('Car [' + car + '] not found')
'''
def convert_velocity(path, vx, vy):
    current = path.pop(0)
    current_vx = vx
    current_vy = vy

    result = []
    for nxt in path:
        dx = nxt[0] - current[0]
        dy = nxt[1] - current[1]
        if dx != 0:
            if current_vx == 0:
                result.append((dx, -current_vy))
                current_vx = dx
            else:
                result.append((0, -current_vy))

            current_vy -= current_vy
        elif dy != 0:
            if current_vy == 0:
                result.append((-current_vx, dy))
                current_vy = dy
            else:
                result.append((-current_vx, 0))

            current_vx -= current_vx

        current = nxt

    return result
'''
def convert_velocity(path, vx, vy):
    result = []
    lines = split_straight_lines(path)

    vel = (vx, vy) # velocita' iniziale
    vel_sum = abs_(vel) # somma accumulata degli incrementi di velocita'
    i = 0
    m = 0
    while i < len(lines): # per ogni linea retta
        start,end = lines[i]
        dist = diff(end, start)
        incr = get_vel_increment(dist)
        #print('start: ', start, 'end:', end, 'dist: ', dist, 'incr: ', incr)
        #start:  (11, 3) end: (20, 3) dist:  (9, 0) incr:  (1, 0)
        while start != end:
            new_vel = add(vel, incr)
            dist = add(abs_(diff(end, start)), abs_(incr)) # calcola la nuova distanza rimanente

            #print('vel_sum: ', vel_sum, 'dist_2: ', dist, 'vel: ', vel, 'start: ', start)
            if compare(add(vel_sum, abs_(new_vel)), dist) < 0: # se l'incremento della velocita' e' minore della distanza rimanente
                #print('new_vel: ', new_vel)
                vel_sum = add(vel_sum, abs_(new_vel))
                vel = new_vel
                result.append(incr)
            elif compare(vel_sum, dist) >= 0: # se bisogna cominciare a decelerare
                #print('entro')
                vel_sum = diff(vel_sum, abs_(vel))
                vel = diff(vel, incr)
                result.append(neg(incr))
            else:
                result.append((0,0)) # lascia la velocita' invariata
            
            #print('velocità: ', vel, 'inizio: ', start)
            start = add(start, vel) # avanza fino alla tile successiva
            
            m += 1
            
        vel = (0, 0) # velocita' iniziale
        vel_sum = vel
        result.append(neg(incr))
        i += 1
        

    result.reverse()
    return result

# divide il path in blocchi di linee rette
def split_straight_lines(path):
    result = []

    line_start = path.pop()
    prev = line_start
    dprev = None

    while len(path) > 0:
        nxt = path.pop()
        d = diff(nxt, prev)
        if dprev is None: dprev = d
        if d != dprev:
            result.append((line_start, prev))
            line_start = prev
            dprev = d
        prev = nxt

    result.append((line_start, prev))

    return result

def diff(c1, c2):
    return (c1[0] - c2[0], c1[1] - c2[1])

def diff_abs(c1, c2):
    return (abs(c1[0] - c2[0]), abs(c1[1] - c2[1]))

def add(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])

def neg(c1):
    return (-c1[0], -c1[1])

def abs_(c1):
    return (abs(c1[0]), abs(c1[1]))

def get_vel_increment(diff):
    x,y = 0,0

    if diff[0] < 0:
        x = -1
    elif diff[0] > 0:
        x = 1

    if diff[1] < 0:
        y = -1
    elif diff[1] > 0:
        y = 1

    return (x, y)

def compare(c1, c2):
    if c1[0] < c2[0] or c1[1] < c2[1]:
        return -1
    elif c1[0] > c2[0] or c1[1] > c2[1]:
        return 1

    return 0

def find_end(grid, start):
    for o in neighbors(grid, start, []):
        if grid[o[1]][o[0]] == '|':
            return o
    raise Exception('Traguardo non trovato!')

def find_fake_end(grid, start, end):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    return (end[0] + dx,end[1] + dy)

def build_map_breadth_first(grid, start):
    frontier = deque()
    frontier.append(start)
    came_from = {}
    came_from[start] = None

    while len(frontier) > 0:
        current = frontier.popleft()
        for nxt in neighbors(grid, current):
            if nxt not in came_from:
                frontier.append(nxt)
                came_from[nxt] = current

    return came_from

def build_map_greedy(grid, start, end):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == end:
            break

        for nxt in neighbors(grid, current):
            if nxt not in came_from:
                priority = heuristic(end, nxt)
                frontier.put(nxt, priority)
                came_from[nxt] = current

    return came_from

def build_map_dijkstra(grid, start, end):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == end:
            break

        for nxt in neighbors(grid, current, ['#', '|']):
            new_cost = cost_so_far[current] + cost(grid, current, nxt)
            if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                cost_so_far[nxt] = new_cost
                priority = new_cost
                frontier.put(nxt, priority)
                came_from[nxt] = current

    return came_from

def build_map_a_star(grid, start, end):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == end:
            break

        for nxt in neighbors(grid, current):
            new_cost = cost_so_far[current] + cost(grid, current, nxt)
            if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                cost_so_far[nxt] = new_cost
                priority = new_cost + heuristic(end, nxt)
                frontier.put(nxt, priority)
                came_from[nxt] = current

    return came_from

def cost(grid, current, nxt):
    cost = 1
    elem = element(grid, nxt)
    if elem == 'O':
        ngb_n = neighbors(grid, nxt, [])
        cost = [100, 1000][int(any(element(grid, n) == '#' for n in ngb_n))] # un ostacolo al bordo costa 100, interno 10

    return cost

def heuristic(a, b):
   # Manhattan distance on a square grid
   return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_path(game_map, start, end):
    current = end
    path = []
    while current != start:
        path.append(current)
        current = game_map[current]
    path.append(start)
    #path.reverse()

    return path

def neighbors(grid, point, to_avoid = ["#", "O", "|"]):
    def appendIf(i, acc):
        (x, y) = (point[0] + i[0], point[1] + i[1])
        if inside(grid, x, y) and grid[y][x] not in to_avoid:
            acc.append((x, y))

    ngb = []
    appendIf((0, -1), ngb)
    appendIf((-1, 0), ngb)
    appendIf((0, 1 ), ngb)
    appendIf((1, 0 ), ngb)
    #print('ngb', ngb)
    return ngb

def element(grid, coords):
    x,y = coords
    return grid[y][x]

def inside(grid, x, y):
    '''Verifica se il pixel di coordinate x,y è contenuto nella griglia'''
    return 0 <= x < width(grid) and 0 <= y < height(grid)

def width(grid):
    return len(grid[0]) # è la prima riga mi da le colonne e dunque la larghezza

def height(grid):
    return len(grid) # numero di righe quindi l'altezza della matrice
