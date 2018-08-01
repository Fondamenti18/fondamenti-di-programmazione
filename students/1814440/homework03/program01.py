'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore rettangoli 
di vari colori i cui assi sono sempre parallei agli assi dell'immagine.

Vedi ad esempio l'immagine Img1.png

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una  funzione quadrato(filename, C) che prende in input:
- il percorso di un file (filename) che contine un immagine in formato png della  tipologia appena descritta.
- una tupla C che rappresenta un colore in formato RGB (3 valori interi tra 0 e 255 compresi)

La funzione deve restituire nell'ordine:
- la lunghezza del lato del quadrato pieno di dimensione massima e colore C interamente visibile nell'immagine. 
- le coordinate  (x,y)  del pixel dell'immagine che corrisponde alla posizione 
all'interno dell'immagine del punto in alto a sinistra del quadrato. 

In caso ci siano più quadrati di dimensione massima, va considerato quello il cui punto 
in alto a sinistra occupa la riga minima  (e a parita' di riga la colonna minima) all'interno dell' immagine. 

Si può assumere che nell'immagine e' sempre  presente almeno un pixel del colore cercato.

Per gli esempi vedere il file grade01.txt

ATTENZIONE: Il timeout è impostato a 10*N secondi (con N numero di test del grader).
'''

from immagini import *

def calcola(imm,x,y,minX,minY,c,lato,flag):
    mioLato=0
    if flag: mioLato=subitoSeguente(imm,x,y,c,lato)
    else: mioLato=ricorsiva(imm,x,y,c,lato+1)
    if mioLato-1>lato:
        minX,minY,lato=x,y,mioLato
        return minX,minY,lato-1,True
    return minX,minY,lato,False

def inside(imm,x,y):
    return 0<=x<len(imm[0]) and 0<=y<len(imm)

def ricorsiva(imm,x,y,c,lato):
    if lato==0: lato=1
    for a in range(lato):
        for b in range(lato):
            if not inside(imm,a+x,b+y) or imm[b+y][a+x]!=c:
                return lato
    return ricorsiva(imm,x,y,c,lato+1)

def subitoSeguente(imm,x,y,c,lato):
    ''' se entro qui dentro vuold ire che sto scansionando un quadrato probabilmente più grande di quello scansionato
    prima che era diventato il nuovo miglior uadrato. Mi risparmio così innumerevoli controlli e cicli '''
    while True:
        for k in range(lato+1):
            if not inside(imm,x+lato,y+k) or imm[y+k][x+lato]!=c:
                return lato
        for k in range(lato+1):
            if not inside(imm,x+lato,y+lato) or imm[y+lato][x+k]!=c:
                return lato
        lato+=1

def quadrato(filename,c):
    imm=load(filename).copy()
    minX,minY=-1,-1
    lato=-1
    flag=False
    for y in range(len(imm)):
        for x in range(len(imm[0])):
            if imm[y][x]==c:
                if not flag: minX,minY,lato,flag=calcola(imm,x,y,minX,minY,c,lato,False)
                else: minX,minY,lato,flag=calcola(imm,x,y,minX,minY,c,lato,True)
    return lato,(minX,minY)

if __name__=='__main__':
    quadrato('Ist1.png',(255,0,0))
