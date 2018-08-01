'''

Definiamo adiacenti di un pixel p di un immagine i pixel adiacenti a p in  orizzontale o in  verticale.
Se un pixel e' sul bordo dell'immagine il suo vicinato non comprende i pixel non contenuti nell'immagine.
Il pixel dell'immagine con coordinate(x,y) ha dunque come adiacenti i pixel   
con coordinate (x-1,y),(x+1,y),(x,y-1),(x,y+1) appartenenti all'immagine. 
 
Definiamo connessi due pixel se e' possibile dall'uno raggiungere l'altro spostandosi solo su   
pixel adiacenti e dello stesso colore (ovviamente perche' cio' sia possobile e' necessario 
che i due pixel abbiano lo stesso colore).

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una funzione ricolora(fname, lista,  fnameout) che presi:
- il percorso di un file che contiene un'immagine in formato PNG
- una lista di quadruple del tipo (x,y,c1,c2) dove  x e y sono coordinate di un pixel dell'immagine e c1 e c2 due triple colore RGB
- il percorso di un file (fnameout) da creare
legge l'immagine in fname, esegue un'operazione di ricolorazione di alcuni pixel dell'immagine e 
registra l'immagine ricolorata nel file fnameout.

L'operazione di ricolorazione e' la seguente. Per ciascuna delle quadruple (x,y,c1,c2) della lista (nell'ordine), 
- tutti i pixel connessi al pixel  di coordinate (x,y) nell'immagine vanno ricolorati col colore c1, 
- tutti i pixel del perimetro (che si trovano sul 'bordo') della zona che si e' appena colorata devono essere ricolorati col colore c2.
Il perimetro della zona colorata è l'insieme dei pixel che non hanno tutti e 4 i vicini che fanno parte della zona ricolorata 
(ovvero almeno uno è di un colore diverso da quello che si sta ricolorando oppure almeno uno non esiste perchè sarebbe fuori dall'immagine)

Si consideri ad esempio l'immagine 'I1.png', l'invocazione di ricolora('I1.png',[(10,10,(255,0,0), (0,0,255))],’OUT1.png')
produrra' l'immagine 'OUT1.png' identica all'immagine di partenza se non per il fatto che,
 tutti i pixel adiacenti al pixel di coordinate (10,10) (e di colore verde), verranno ricolorati 
 di rosso ((255,0,0)), mentre i pixel sul bordo della zona inizialmente verde vengono ricolorati di blu.

Per ciascuna area ricolorata bisogna inoltre calcolare area interna e perimetro, che sono definite come segue:
- l'area interna e' il numero di pixel ricolorati con il colore c1
- il perimetro è il numero di pixel ricolorati con il colore c2

La funzone deve tornare la lista di coppie (area interna, perimetro) nello stesso ordine in cui sono state colorate le aree.
 
Per altri  esempi vedere il file grade03.txt 
'''

from immagini import *

def ricolora(fname, lista, fnameout):
    '''ricolorare i pixel adiacenti al pixel di partenza col colore c1 e il suo bordo col colore c2.'''
    
    img = load(fname)
    
    risultato = []
    
    indice = 0
    for y in lista:
        indice += 1
        colore_ini = (img[y[1]][y[0]])
        tupla_check = [(y[0], y[1])]
        
        bordo = []
        
        area = 0
        #index = 1
        for x in tupla_check:
            w, h = x
            if w+1 < len(img[0]) and (w+1, h) not in tupla_check and img[h][w+1] == colore_ini:
                tupla_check.append((w+1, h))
            if w-1 >= 0 and (w-1, h) not in tupla_check and img[h][w-1] == colore_ini:
                tupla_check.append((w-1, h))
            if h+1 < len(img) and (w, h+1) not in tupla_check and img[h+1][w] == colore_ini:
                tupla_check.append((w, h+1))
            if h-1 >= 0 and (w, h-1) not in tupla_check and img[h-1][w] == colore_ini:
                tupla_check.append((w, h-1))
        
        for coord in tupla_check:
            if coord[0]+1 < len(img[0]):
                if img[coord[1]][coord[0]+1] != colore_ini:
                    bordo.append((coord[0], coord[1]))
            else:
                bordo.append((coord[0], coord[1]))
            
            if coord[0]-1 >= 0:
                if img[coord[1]][coord[0]-1] != colore_ini:
                    bordo.append((coord[0], coord[1]))
            else:
                bordo.append((coord[0], coord[1]))
            
            if coord[1]+1 < len(img):
                if img[coord[1]+1][coord[0]] != colore_ini:
                    bordo.append((coord[0], coord[1]))
            else:
                bordo.append((coord[0], coord[1]))
            
            if coord[1]-1 >= 0:
                if img[coord[1]-1][coord[0]] != colore_ini:
                    bordo.append((coord[0], coord[1]))
            else:
                bordo.append((coord[0], coord[1]))
        
        for x in tupla_check:
            img[x[1]][x[0]] = y[2]
            area += 1
        
        perimetro = 0
        for coord_bordo in bordo:
            if img[coord_bordo[1]][coord_bordo[0]] != y[3]:
                img[coord_bordo[1]][coord_bordo[0]] = y[3]
                perimetro += 1
                area -= 1
        
#        print("tupla c1\n", tupla_check)
#        print("\n\n\ntupla c2\n", bordo)
            
#        print("area")
#        perimetro = 0
#        for x in bordo:
#            if img[x[1]][x[0]] != y[3]:
#                img[x[1]][x[0]] = y[3]
#                perimetro += 1
#                area -= 1
#        print("perimetro")
        risultato.append((area, perimetro))
    save(img, fnameout)
    return risultato
#
#rosso = (255,   0,   0)
#blu   = (  0,   0, 255)
#verde = (  0, 255,   0)
#nero  = (  0,   0,   0)
#bianco= (255, 255, 255)
#giallo= (255, 255,   0)
#cyan  = (  0, 255, 255)
#magenta= (255,  0, 255)
#ricolora('I1.png',[(10,10,bianco,blu),(90,10,verde,rosso)],'test3.png')

'''
            if 0 <= h < len(img) and 0 <= w < len(img[0]):
                img[h][w] = y[2]
                area += 1
                
                if w+1 >= len(img[0]):
                    bordo.append((w, h))
                else:
                    if img[h][w+1] != colore_ini and img[h][w+1] != y[2]:
                        bordo.append((w, h))
                    else:
                        if img[h][w+1] == y[2] and (w+1, h) not in tupla_check and img[h][w+1] != colore_ini:
                            bordo.append((w, h))
                        elif img[h][w+1] == colore_ini:
                            if (w+1, h) not in tupla_check:
                                tupla_check.append((w+1, h))
                
                if h+1 >= len(img):
                    bordo.append((w, h))
                else:
                    if img[h+1][w] != colore_ini and img[h+1][w] != y[2]:
                        bordo.append((w, h))
                    else:
                        if img[h+1][w] == y[2] and (w, h+1) not in tupla_check and img[h+1][w] != colore_ini:
                            bordo.append((w, h))
                        elif img[h+1][w] == colore_ini:
                            if (w, h+1) not in tupla_check:
                                tupla_check.append((w, h+1))
                
                if w-1 < 0:
                    bordo.append((w, h))
                else:
                    if img[h][w-1] != colore_ini and img[h][w-1] != y[2]:
                        bordo.append((w, h))
                    else:
                        if img[h][w-1] == y[2] and (w-1, h) not in tupla_check and img[h][w-1] != colore_ini:
                            bordo.append((w, h))
                        elif img[h][w-1] == colore_ini:
                            if (w-1, h) not in tupla_check:
                                tupla_check.append((w-1, h))
                
                if h-1 < 0:
                    bordo.append((w, h))
                else:
                    if img[h-1][w] != colore_ini and img[h-1][w] != y[2]:
                        bordo.append((w, h))
                    else:
                        if img[h-1][w] == y[2] and (w, h-1) not in tupla_check and img[h-1][w] != colore_ini:
                            bordo.append((w, h))
                        elif img[h-1][w] == colore_ini:
                            if (w, h-1) not in tupla_check:
                                tupla_check.append((w, h-1))
'''
               
               
               
               
               
               
               
                    
'''
                    for pos_w in range(w, len(img[0])):
                        if img[h][pos_w] != colore_ini and img[h][pos_w] != y[2] and (pos_w, h) not in tupla_check:
                            bordo.append((pos_w-1, h))
                            tupla_check.append((pos_w-1, h))
                            break
                        else:
                            if img[h][pos_w] == y[2] and img[h][pos_w] != colore_ini and (pos_w, h) not in tupla_check:
                                bordo.append((pos_w-1, h))
                                tupla_check.append((pos_w-1, h))
                                break
                            elif img[h][pos_w] == colore_ini and (pos_w, h) not in tupla_check:
                                img[h][pos_w] = y[2]
                                tupla_check.append((pos_w, h))
                                area += 1
                    if pos_w == len(img[0])-1:
                        bordo.append((pos_w, h))
                        tupla_check.append((pos_w, h))
                    
                    for pos_h in range(h, len(img)):
                        if img[pos_h][w] != colore_ini and img[pos_h][w] != y[2] and (w, pos_h) not in tupla_check:
                            bordo.append((w, pos_h-1))
                            tupla_check.append((w, pos_h-1))
                            break
                        else:
                            if img[pos_h][w] == y[2] and img[pos_h][w] != colore_ini and (w, pos_h) not in tupla_check:
                                bordo.append((w, pos_h-1))
                                tupla_check.append((w, pos_h-1))
                                break
                            elif img[pos_h][w] == colore_ini and (w, pos_h) not in tupla_check:
                                img[pos_h][w] = y[2]
                                tupla_check.append((w, pos_h))
                                area += 1
                    if pos_h == len(img)-1:
                        bordo.append((w, pos_h))
                        tupla_check.append((w, pos_h))
                    
                    for pos_w in range(w, -1, -1):
                        if img[h][pos_w] != colore_ini and img[h][pos_w] != y[2] and (pos_w, h) not in tupla_check:
                            bordo.append((pos_w+1, h))
                            tupla_check.append((pos_w+1, h))
                            break
                        else:
                            if img[h][pos_w] == y[2] and img[h][pos_w] != colore_ini and (pos_w, h) not in tupla_check:
                                bordo.append((pos_w+1, h))
                                tupla_check.append((pos_w+1, h))
                                break
                            elif img[h][pos_w] == colore_ini and (pos_w, h) not in tupla_check:
                                img[h][pos_w] = y[2]
                                tupla_check.append((pos_w, h))
                                area += 1
                    if pos_w == 0:
                        bordo.append((pos_w, h))
                        tupla_check.append((pos_w, h))
                    
                    for pos_h in range(h, -1, -1):
                        if img[pos_h][w] != colore_ini and img[pos_h][w] != y[2] and (w, pos_h) not in tupla_check:
                            bordo.append((w, pos_h+1))
                            tupla_check.append((w, pos_h+1))
                            break
                        else:
                            if img[pos_h][w] == y[2] and img[pos_h][w] != colore_ini and (w, pos_h) not in tupla_check:
                                bordo.append((w, pos_h+1))
                                tupla_check.append((w, pos_h+1))
                                break
                            elif img[pos_h][w] == colore_ini and (w, pos_h) not in tupla_check:
                                img[pos_h][w] = y[2]
                                tupla_check.append((w, pos_h))
                                area += 1
                    if pos_h == 0:
                        bordo.append((w, pos_h))
                        tupla_check.append((w, pos_h))
                    
                    tupla_check.append((w+1, h))
                    tupla_check.append((w-1, h))
                    tupla_check.append((w, h+1))
                    tupla_check.append((w, h-1))
                    
#                    if h_ini-index >= 0 and w_ini+index < len(img[0]):
#                        if img[h_ini-index][w_ini+index] == colore_ini:
#                            tupla_check.append((w_ini+index, h_ini-index))
#                    if h_ini+index < len(img) and w_ini-index >= 0:
#                        if img[h_ini+index][w_ini-index] == colore_ini:
#                            tupla_check.append((w_ini-index, h_ini+index))
                    index += 1
'''
                
                
                
                
                
                
'''
                for pos_w in range(w, len(img[0])):
                    if img[h][pos_w] != colore_ini and img[h][pos_w] != y[2] and (pos_w, h) not in tupla_usati:
                        bordo.append((pos_w-1, h))
                        tupla_usati.append((pos_w-1, h))
                        break
                    else:
                        if img[h][pos_w] == y[2] and img[h][pos_w] != colore_ini and (pos_w, h) not in tupla_usati:
                            bordo.append((pos_w-1, h))
                            tupla_usati.append((pos_w-1, h))
                            break
                        elif img[h][pos_w] == colore_ini and (pos_w, h) not in tupla_usati:
                            img[h][pos_w] = y[2]
                            tupla_usati.append((pos_w, h))
                            area += 1
                if pos_w == len(img[0])-1:
                    bordo.append((pos_w, h))
                    tupla_usati.append((pos_w, h))
                
                for pos_h in range(h, len(img)):
                    if img[pos_h][w] != colore_ini and img[pos_h][w] != y[2] and (w, pos_h) not in tupla_usati:
                        bordo.append((w, pos_h-1))
                        tupla_usati.append((w, pos_h-1))
                        break
                    else:
                        if img[pos_h][w] == y[2] and img[pos_h][w] != colore_ini and (w, pos_h) not in tupla_usati:
                            bordo.append((w, pos_h-1))
                            tupla_usati.append((w, pos_h-1))
                            break
                        elif img[pos_h][w] == colore_ini and (w, pos_h) not in tupla_usati:
                            img[pos_h][w] = y[2]
                            tupla_usati.append((w, pos_h))
                            area += 1
                if pos_h == len(img)-1:
                    bordo.append((w, pos_h))
                    tupla_usati.append((w, pos_h))
                
                for pos_w in range(w, -1, -1):
                    if img[h][pos_w] != colore_ini and img[h][pos_w] != y[2] and (pos_w, h) not in tupla_usati:
                        bordo.append((pos_w+1, h))
                        tupla_usati.append((pos_w+1, h))
                        break
                    else:
                        if img[h][pos_w] == y[2] and img[h][pos_w] != colore_ini and (pos_w, h) not in tupla_usati:
                            bordo.append((pos_w+1, h))
                            tupla_usati.append((pos_w+1, h))
                            break
                        elif img[h][pos_w] == colore_ini and (pos_w, h) not in tupla_usati:
                            img[h][pos_w] = y[2]
                            tupla_usati.append((pos_w, h))
                            area += 1
                if pos_w == 0:
                    bordo.append((pos_w, h))
                    tupla_usati.append((pos_w, h))
                
                for pos_h in range(h, -1, -1):
                    if img[pos_h][w] != colore_ini and img[pos_h][w] != y[2] and (w, pos_h) not in tupla_usati:
                        bordo.append((w, pos_h+1))
                        tupla_usati.append((w, pos_h+1))
                        break
                    else:
                        if img[pos_h][w] == y[2] and img[pos_h][w] != colore_ini and (w, pos_h) not in tupla_usati:
                            bordo.append((w, pos_h+1))
                            tupla_usati.append((w, pos_h+1))
                            break
                        elif img[pos_h][w] == colore_ini and (w, pos_h) not in tupla_usati:
                            img[pos_h][w] = y[2]
                            tupla_usati.append((w, pos_h))
                            area += 1
                if pos_h == 0:
                    bordo.append((w, pos_h))
                    tupla_usati.append((w, pos_h))
                
                if h_ini-index >= 0 and w_ini+index < len(img[0]):
                    if img[h_ini-index][w_ini+index] == colore_ini:
                        tupla_check.append((w_ini+index, h_ini-index))
                if h_ini+index < len(img) and w_ini-index >= 0:
                    if img[h_ini+index][w_ini-index] == colore_ini:
                        tupla_check.append((w_ini-index, h_ini+index))
                index += 1
'''
                
                    
                
#                if img[h][pos_w] == colore_ini and (pos_w, h) not in tupla_usati:
#                    img[h][pos_w] = y[2]
#                    tupla_usati.append((pos_w, h))
#                    area += 1
#                elif img[h][pos_w] != colore_ini and img[h][pos_w] != y[2]:
#                    bordo.append((pos_w-1, h))
#            if pos_w == len(img[0])-1:
#                bordo.append((pos_w-1, h))
#            if (w+1, h) not in tupla_check:
#                tupla_check.append((w+1, h))
#            if (w, h+1) not in tupla_check:
#                tupla_check.append((w, h+1))
#            if (w-1, h) not in tupla_check:
#                tupla_check.append((w-1, h))
#            if (w, h-1) not in tupla_check:
#                tupla_check.append((w, h-1))
    
#rosso = (255,   0,   0)
#blu   = (  0,   0, 255)

#verde = (  0, 255,   0)
#nero  = (  0,   0,   0)
#bianco= (255, 255, 255)
#giallo= (255, 255,   0)
#cyan  = (  0, 255, 255)
#magenta=(255,  0, 255)
#ricolora('I1.png',[(10,10,rosso,blu)],'test1.png')
'''
for y in lista:
    tupla_check = [(y[0], y[1])]
    tupla_colore = load_img[tupla_check[0][1]][tupla_check[0][0]]
    
    last_h = 0
    last_w = 0
    ini_h = 0
    ini_w = 0
    
    area = 1
    for x in tupla_check:
        w, h = x
        if load_img[h][w] == tupla_colore or load_img[h][w] == y[2]:
            load_img[h][w] = y[2]
            if h+1 < len(load_img) and (w, h+1) not in tupla_check:
                if load_img[h+1][w] == tupla_colore:
                    area += 1
                    load_img[h+1][w] = y[2]
                    tupla_check.append((w, h+1))
                    if h >= last_h:
                        last_h = h+1
            if w+1 < len(load_img[0]) and (w+1, h) not in tupla_check:
                if load_img[h][w+1] == tupla_colore:
                    area += 1
                    load_img[h][w+1] = y[2]
                    tupla_check.append((w+1, h))
                    if w >= last_w:
                        last_w = w+1
            if h-1 >= 0 and (w, h-1) not in tupla_check:
                if load_img[h-1][w] == tupla_colore:
                    area += 1
                    load_img[h-1][w] = y[2]
                    tupla_check.append((w, h-1))
                    ini_h = h-1
            if w-1 >= 0 and (w-1, h) not in tupla_check:
                if load_img[h][w-1] == tupla_colore:
                    area += 1
                    load_img[h][w-1] = y[2]
                    tupla_check.append((w-1, h))
                    ini_w = w-1
    
    perimetro = 0
    ini_w_copy = ini_w
    ini_h_copy = ini_h
    
    while ini_w_copy <= last_w:
        if load_img[ini_h][ini_w_copy] != y[3] and load_img[last_h][ini_w_copy] != y[3]:
            perimetro += 2
            area -= 2
        elif load_img[ini_h][ini_w_copy] != y[3] or load_img[last_h][ini_w_copy] != y[3]:
            perimetro += 1
            area -= 1
        load_img[ini_h][ini_w_copy] = y[3]
        load_img[last_h][ini_w_copy] = y[3]
        ini_w_copy += 1
    
    while ini_h_copy <= last_h:
        if load_img[ini_h_copy][ini_w] != y[3] and load_img[ini_h_copy][last_w] != y[3]:
            perimetro += 2
            area -= 2
        elif load_img[ini_h_copy][ini_w] != y[3] or load_img[ini_h_copy][last_w] != y[3]:
            perimetro += 1
            area -= 1
        load_img[ini_h_copy][ini_w] = y[3]
        load_img[ini_h_copy][last_w] = y[3]
        ini_h_copy += 1
'''
            
#        
#        cont_area = 0
#        cont_perimetro = 0
#        ini_w_copy = ini_w
#        ini_h_copy = ini_h
#        while ini_h_copy <= last_h:
#            while ini_w_copy <= last_w:
#                print(load_img[ini_h_copy][ini_w_copy], y[2], y[3])
#                if load_img[ini_h_copy][ini_w_copy] == y[2]:
#                    cont_area += 1
#                else:
#                    cont_perimetro += 1
#                ini_w_copy += 1
#            ini_h_copy += 1
        #risultato.append((area, perimetro))
    #return risultato