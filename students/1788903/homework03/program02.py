from immagini import *

nero = (0, 0, 0)
bianco = (255, 255, 255)
rosso = (255, 0, 0)
verde = (0, 255, 0)
blu = (0, 0, 255)

def cammino(fname, fname1):
    direzione = 0
    contatore = 0
    x = 0
    y = 0
    board = load(fname)
    codifica = ''

    while contatore < 4:
        if direzione == 0:
            if not dentro(board, x+40, y):
                direzione += 1
                if direzione == 4:
                    direzione = 0
                contatore += 1
            else:
                if board[y][x+40] == bianco or board[y][x+40] == nero:
                    codifica += str(direzione)
                    colora(board, x, y, verde)
                    contatore = 0
                    x, y = muovi(x, y, direzione)
                else:
                    direzione += 1
                    if direzione == 4:
                        direzione = 0
                    contatore += 1
        
        if direzione == 1:
            if not dentro(board, x, y+40):
                direzione += 1
                if direzione == 4:
                    direzione = 0
                contatore += 1
            else:
                if board[y+40][x] == bianco or board[y+40][x] == nero:
                    codifica += str(direzione)
                    colora(board, x, y, verde)
                    contatore = 0
                    x, y = muovi(x, y, direzione)
                else:
                    direzione += 1
                    if direzione == 4:
                        direzione = 0
                    contatore += 1
        
        if direzione == 2:
            if not dentro(board, x - 40, y):
                direzione += 1
                if direzione == 4:
                    direzione = 0
                contatore += 1
            else:
                if board[y][x-40] == bianco or board[y][x-40] == nero:
                    codifica += str(direzione)
                    colora(board, x, y, verde)
                    contatore = 0
                    x, y = muovi(x, y, direzione)
                else:
                    direzione += 1
                    if direzione == 4:
                        direzione = 0
                    contatore += 1
        
        if direzione == 3:
            if not dentro(board, x, y-40):
                direzione += 1
                if direzione == 4:
                    direzione = 0
                contatore += 1
            else:
                if board[y-40][x] == bianco or board[y-40][x] == nero:
                    codifica += str(direzione)
                    colora(board, x, y, verde)
                    contatore = 0
                    x, y = muovi(x, y, direzione)
                else:
                    direzione += 1
                    if direzione == 4:
                        direzione = 0
                    contatore += 1

    colora(board, x, y, blu)
    save(board, fname1)
    return codifica

def colora(img, x, y, colore):
    for px in range(x, x+40):
        for py in range(y, y+40):
            img[py][px] = colore

def muovi(x, y, direzione):
    if direzione == 0:
        return x + 40, y 
    if direzione == 1:
        return x, y + 40
    if direzione == 2:
        return x - 40, y
    if direzione == 3:
        return x, y - 40

def dentro(img, x, y):
    return 0 <= x < len(img) and 0 <= y < len(img[0])
