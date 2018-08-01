'''

Definiamo adiacenti di un pixel p di un immagine i pixel adiacenti a p in orizzontale o in verticale.
Se un pixel e' sul bordo dell'immagine il suo vicinato non comprende i pixel non contenuti nell'immagine.
Il pixel dell'immagine con coordinate(x,y) ha dunque come adiacenti i pixel   
con coordinate (x-1,y),(x+1,y),(x,y-1),(x,y+1) appartenenti all'immagine. 
 
Definiamo connessi due pixel se e' possibile dall'uno raggiungere l'altro spostandosi solo su   
pixel adiacenti e dello stesso colore (ovviamente perche' cio' sia possibile e' necessario 
che i due pixel abbiano lo stesso colore).

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una funzione ricolora(fname, lista,  fnameout) che presi:
- il percorso di un file che contiene un'immagine in formato PNG
- una lista di quadruple del tipo (x,y,c1,c2) dove x e y sono coordinate di un pixel dell'immagine e c1 e c2 due triple colore RGB
- il percorso di un file (fnameout) da creare
legge l'immagine in fname, esegue un'operazione di ricolorazione di alcuni pixel dell'immagine e 
registra l'immagine ricolorata nel file fnameout.

L'operazione di ricolorazione e' la seguente. Per ciascuna delle quadruple (x,y,c1,c2) della lista (nell'ordine), 
- tutti i pixel connessi al pixel di coordinate (x,y) nell'immagine vanno ricolorati col colore c1, 
- tutti i pixel del perimetro (che si trovano sul 'bordo') della zona che si e' appena colorata devono essere ricolorati col colore c2.
Il perimetro della zona colorata e' l'insieme dei pixel che non hanno tutti e 4 i vicini che fanno parte della zona ricolorata 
(ovvero almeno uno e' di un colore diverso da quello che si sta ricolorando oppure almeno uno non esiste perche' sarebbe fuori dall'immagine)

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
    global lista_immagine
    lista_immagine = load(fname)
    global copia_fnameout
    copia_fnameout = fnameout
    l = []
    
    for t in range(len(lista)):
        x = lista[t][0]
        y = lista[t][1]
        c1 = lista[t][2]
        c2 = lista[t][3]
        colore = lista_immagine[y][x]
    
        #qui trovo il pixel tutto a sinistra dove inizia la figura del colore che cerco
        pixel = 1
        while lista_immagine[y][x-pixel] == colore and x-pixel >= 0:
            pixel += 1
        else:
            pixel = x-pixel+1

        #qui trovo la riga tutto in alto dove inizia la figura del colore che cerco
        riga = 1
        while lista_immagine[y-riga][x] == colore and y-riga >= 0:
            riga += 1
        else:
            riga = y-riga+1
    
        #qui conto i pixel della figura del colore che cerco
        conta = 1
        try:
            while lista_immagine[riga][pixel+conta] == colore:
                conta += 1
        except IndexError:
            pass

        #qui conto le righe della figura del colore che cerco
        conta2 = 1
        try:
            while lista_immagine[riga+conta2][pixel] == colore:
                conta2 += 1
        except IndexError:
            pass
        
        disegna_quad(riga , pixel , conta , conta2 , c2)
        disegna_quad(riga + 1 , pixel + 1 , conta - 2 , conta2 - 2 , c1)
        risultato = calcola(riga , pixel , c1 , c2 , conta , conta2)
        l.append(risultato)
    
    return l
    
def disegna_quad(riga , pixel , conta , conta2 , colore):
    for i in range(conta2):
        for j in range(conta):
            lista_immagine[riga+j][pixel+i] = colore
    save(lista_immagine , copia_fnameout)

def calcola(riga , pixel , c1 , c2 , conta , conta2):
    conta_c1 , conta_c2 = 0 , 0
    for i in range(conta2):
        for j in range(conta):
            if lista_immagine[riga+j][pixel+i] == c1:
                conta_c1 += 1
            elif lista_immagine[riga+j][pixel+i] == c2:
                conta_c2 += 1
    risultato = (conta_c1 , conta_c2)
    return risultato

if __name__ == '__main__':
    print( ricolora( 'I1.png',[(0,0,(0,0,0),(0,5*i,5*i)) for i in range(1,25)],'test6.png' ) )

