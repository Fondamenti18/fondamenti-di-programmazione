'''

Definiamo adiacenti di un pixel p di un immagine i pixel 
    adiacenti a p in  orizzontale o in  verticale.
Se un pixel e' sul bordo dell'immagine il suo vicinato non comprende 
    i pixel non contenuti nell'immagine.
Il pixel dell'immagine con coordinate(x,y) ha dunque come adiacenti i pixel   
con coordinate (x-1,y),(x+1,y),(x,y-1),(x,y+1) appartenenti all'immagine. 
 
Definiamo connessi due pixel se e' possibile dall'uno raggiungere 
    l'altro spostandosi solo su pixel adiacenti e dello stesso colore 
    (ovviamente perche' cio' sia possobile e' necessario 
     che i due pixel abbiano lo stesso colore).

Per caricare e salvare immagini PNG usate le funzioni load e save che 
    abbiamo preparato nel modulo immagini.py .

Scrivere una funzione ricolora(fname, lista,  fnameout) che presi:
- il percorso di un file che contiene un'immagine in formato PNG
- una lista di quadruple del tipo (x,y,c1,c2) dove  x e y sono coordinate di 
    un pixel dell'immagine e c1 e c2 due triple colore RGB
- il percorso di un file (fnameout) da creare
    legge l'immagine in fname, esegue un'operazione di ricolorazione di alcuni 
    pixel dell'immagine e registra l'immagine ricolorata nel file fnameout.

L'operazione di ricolorazione e' la seguente. Per ciascuna delle quadruple 
    (x,y,c1,c2) della lista (nell'ordine), 
- tutti i pixel connessi al pixel  di coordinate (x,y) nell'immagine vanno 
    ricolorati col colore c1, 
- tutti i pixel del perimetro (che si trovano sul 'bordo') della zona che si 
    e' appena colorata devono essere ricolorati col colore c2.
Il perimetro della zona colorata è l'insieme dei pixel che non hanno tutti e 
    4 i vicini che fanno parte della zona ricolorata 
(ovvero almeno uno è di un colore diverso da quello che si sta ricolorando 
     oppure almeno uno non esiste perchè sarebbe fuori dall'immagine)

Si consideri ad esempio l'immagine 'I1.png', l'invocazione di ricolora
    ('I1.png',[(10,10,(255,0,0), (0,0,255))],’OUT1.png')
produrra' l'immagine 'OUT1.png' identica all'immagine di partenza se non 
    per il fatto che,
 tutti i pixel adiacenti al pixel di coordinate (10,10) (e di colore verde), 
     verranno ricolorati 
 di rosso ((255,0,0)), mentre i pixel sul bordo della zona inizialmente verde 
     vengono ricolorati di blu.

Per ciascuna area ricolorata bisogna inoltre calcolare area interna e 
    perimetro, che sono definite come segue:
- l'area interna e' il numero di pixel ricolorati con il colore c1
- il perimetro è il numero di pixel ricolorati con il colore c2

La funzone deve tornare la lista di coppie (area interna, perimetro) nello 
    stesso ordine in cui sono state colorate le aree.
 
Per altri  esempi vedere il file grade03.txt 
'''

from immagini import *
    
def ricolora(fname, lista, fnameout):
    ''' Funzione principale 
        lista[0][0]=x lista[0][1]=y lista[0][2]=c1 lista[0][3]=c2
    '''
    # leggo immagine
    vet = load(fname)           # vettore
    ris = []                    # lista contenente i ris di area e perimetro
    
    # per ogni tupla nella lista:
    for t in lista:
        vet, ris = modifica(vet, t, ris)
    
    # salvo nuova immagine
    save(vet, fnameout)
    # numero pixel colorati x area e perimetro
    return ris    


def modifica(vet, tupla, ris):
    ''' calcola le modifiche de fare al vettore secondo gli elementi 
        della tupla
    '''
    c1,c2 = tupla[2], tupla[3]              # colArea, colPerimetro
    smist = set()                           # pixel gia' smistati
    coda = [tupla[1], tupla[0]]             # pixel da smistare [y,x]
    area,perim = [],[]                      # pixel da colorare
    
 #   # se sto ricolorando
 #   if vet[tupla[1]tupla[0]] == c1:
 #       perim = perimetro(vet, tupla[1],tupla[0])
    
    # finche' ho pixel da analizzare
    while coda != []:
        y,x = coda[0],coda[1]   # coordinate pixel
        cont = 0                # contatore per pixel adicenti
        coda, cont, smist = destra(vet, y,x, coda, cont, smist)
        coda, cont, smist = giu(vet, y,x, coda, cont, smist)
        coda, cont, smist = sinistra(vet, y,x, coda, cont, smist)
        coda, cont, smist = su(vet, y,x, coda, cont, smist)
        # se tutti e quattro i pixel adiacenti sono dello stesso colore
        if cont == 4:
            area.append(y)      # aggiungo coordinate
            area.append(x)      # ...
        # altrimenti e perimetro
        else:
            perim.append(y)     # aggiungo coordinate
            perim.append(x)     # ...
        
        smist.add((y,x))        # segno che pixel e' gia' stato analizzato
        coda.remove(coda[0])    # elimino pixel da coda
        coda.remove(coda[0])    # ...

    # valori che dovro' ritornare
    ris.append((len(area)//2,len(perim)//2)) 
    # coloro vettore
    vet = colora(vet, area,perim, c1,c2)
      
    
    return(vet, ris)

#def perimetro(vet, y,x):
    

def destra(vet, y,x, coda, cont, smist):
    ''' controlla se pixel adiacente a destra e' fuori da vettore o di colore 
        errato(in caso non incrementa contatore) e se e' stato gia' analizzato
    '''
    # se pixel a destra non e' fuori da vettore o di colore differente
    if x+1 < len(vet[0]) and vet[y][x] == vet[y][x+1]:
        # se pixel non e' stato gia' visionato
        if (y,x+1) not in smist:
            coda.append(y)          # aggiungo coordinate da controllare
            coda.append(x+1)        # ...
            smist.add((y,x+1))
        return coda, cont+1, smist  # incremento
    # pixel accanto e' di colore diverso
    return coda, cont, smist
    
def giu(vet, y,x, coda, cont, smist):
    if y+1 < len(vet) and vet[y][x] == vet[y+1][x]:
        if (y+1,x) not in smist:
            coda.append(y+1)
            coda.append(x)
            smist.add((y+1,x))
        return coda, cont+1, smist
    return coda, cont, smist

def sinistra(vet, y,x, coda, cont, smist):
    if x-1 >= 0 and vet[y][x] == vet[y][x-1]:
        if (y,x-1) not in smist:
            coda.append(y)
            coda.append(x-1)
            smist.add((y,x-1))
        return coda, cont+1, smist
    return coda, cont, smist

def su(vet, y,x, coda, cont, smist):
    if y-1 >= 0 and vet[y][x] == vet[y-1][x]:
        if (y-1,x) not in smist:
            coda.append(y-1)
            coda.append(x)
            smist.add((y-1,x))
        return coda, cont+1, smist
    return coda, cont, smist



def colora(vet, area,perim, c1,c2):
    # colora area e perimetro del vettore, rispettivamente del colore c1 e c2
    
    while perim != []:
        vet[perim[0]][perim[1]] = c2
        perim.remove(perim[0])
        perim.remove(perim[0])
        
    # controllo per non ricolorare
    if area != []:
        if vet[area[2]][area[3]] == c1:
            return vet
        
        # finche' ci sono pixel da colorare
        while area != []:
            vet[area[0]][area[1]] = c1      # colore pixel nel vettore
            area.remove(area[0])            # elimino pixel
            area.remove(area[0])            # ...
    
    return vet

