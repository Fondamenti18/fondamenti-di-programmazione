from immagini import load,save
import pprint

 
def disegna(img, x, y, w, h, c):
 
    for colonna in range(y, y+h):
        for riga in range(x, x+w):    
            img[riga][colonna] = c


def aggiusta(direzione,index):
    if index >=4:
        index-=4
    return index

def cond1(colonna,riga,verde,rosso,blu,img,finito):
    
    if riga+40 >= 600 or img[riga+40][colonna] == verde or img[riga+40][colonna] == rosso:
            if colonna+40 >= 600 or img[riga][colonna+40] == verde or img[riga][colonna+40] == rosso:
                if img[riga-40][colonna] == verde or img[riga-40][colonna] == rosso or riga-40 < 0:
                    if img[riga][colonna-40] == verde or img[riga][colonna-40] == rosso or colonna-40 <0:
                        finito = True
                        disegna(img, riga, colonna, 40, 40, blu)
    return finito



def cammino(fname,  fname1):
    
    img = load(fname) 
    direzione = ('destra','sotto','sinistra','sopra')
    index = 0
    lista = []
    riga = 0
    colonna = 0
    scontro = 0
    finito = False
    verde = (0,255,0)
    blu = (0,0,255)
    bianco = (0,0,0)
    nero = (255,255,255)
    rosso = (255,0,0)
    disegna(img, riga, colonna, 40, 40, verde)
    while  True:

        finito = cond1(colonna,riga,verde,rosso,blu,img,finito)
        if finito == True:
            break
     
          
        if direzione[index] == 'destra':
            newcolonna = colonna +40

            if newcolonna < 0 or newcolonna >= 600:
                index += 1
                index = aggiusta(direzione, index)
                continue
            
            if img[riga][newcolonna] == nero or img[riga][newcolonna] == bianco:
                colonna += 40
                disegna(img, riga, colonna, 40, 40, verde)
                lista.append('0')
                
            elif img[riga][newcolonna] == rosso or img[riga][newcolonna] == verde:
                index += 1
                index = aggiusta(direzione, index)
                

        elif direzione[index] == 'sotto':
            newriga = riga + 40

            if newriga < 0 or newriga >= 600:
                index += 1
                index = aggiusta(direzione, index)
                continue
            
            if img[newriga][colonna] == nero or img[newriga][colonna] == bianco:
                riga += 40
                disegna(img, riga, colonna, 40, 40, verde)
                lista.append('1')
                
            elif img[newriga][colonna] == rosso or img[newriga][colonna] == verde:
                index += 1
                index = aggiusta(direzione, index)

                
        elif direzione[index] == 'sinistra':
            newcolonna = colonna - 40
            
            if newcolonna < 0 or newcolonna >= 600:
                index += 1
                index = aggiusta(direzione, index)
                continue
            
            if img[riga][newcolonna] == nero or img[riga][newcolonna] == bianco:
                colonna -= 40
                disegna(img, riga, colonna, 40, 40, verde)
                lista.append('2')
                
            elif img[riga][newcolonna] == rosso or img[riga][newcolonna] == verde:
                index += 1
                index = aggiusta(direzione, index)
                
            
        elif direzione[index] == 'sopra':
            newriga = riga - 40
            
            if newriga < 0 or newriga >= 600:
                index += 1
                index = aggiusta(direzione, index)
                continue

            if img[newriga][colonna] == nero or img[newriga][colonna] == bianco:
                riga -= 40
                disegna(img, riga, colonna, 40, 40, verde)
                lista.append('3')

            elif img[newriga][colonna] == rosso or img[newriga][colonna] == verde:
                index +=1
                index = aggiusta(direzione, index)
                            
        
              
                                 
    save(img, fname1)
    stringa = ''.join(lista)
    return stringa
