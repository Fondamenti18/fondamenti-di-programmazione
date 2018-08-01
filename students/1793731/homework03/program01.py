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
import immagini 

def quadrato(filename,c):
    listPixels = immagini.load(filename)
    lunghezzaLatoQuadrato=0
    posizioneX=0
    posizioneY=0
    numeroRighe=len(listPixels)
    numeroColonne=len(listPixels[0])
    for riga in range(numeroRighe):
        for colonna in range(numeroColonne):
            pixelLetto=getPixel(riga,colonna,listPixels)
            if c == pixelLetto:
                lato=calcolaLatoOrizzontale(colonna,c,listPixels[riga])
                if lato > lunghezzaLatoQuadrato: 
                    if riga+lato < numeroRighe and getPixel(riga,colonna+lato-1,listPixels)==c: 
                        if verificaQuadrato(riga,colonna,c,lato,listPixels):
                            if lunghezzaLatoQuadrato < lato or lunghezzaLatoQuadrato == 0:
                                lunghezzaLatoQuadrato=lato
                                posizioneX=colonna
                                posizioneY=riga                
    return(lunghezzaLatoQuadrato,(posizioneX,posizioneY))
    
def calcolaLatoOrizzontale(y,colorePixel,pixelsRiga):
    lunghezzaLato=1
    for posPixel in range(y+1, len(pixelsRiga)):
        if colorePixel==pixelsRiga[posPixel]:
            lunghezzaLato+=1
        else:
            break
    return lunghezzaLato

def verificaQuadrato(x,y,colorePixel,lunghezzaLato,listPixels):
    giro=0
    for riga in range(x,lunghezzaLato+x):
        for colonna in range(y,lunghezzaLato+y):
            if colorePixel!=getPixel(riga,colonna,listPixels): 
                return False
        giro+=1
    return True
                
def getPixel(x,y,listPixels):
    tuplaPx=tuple()
    try:
        tuplaPx=listPixels[x][y]
    except:
        print ("x: "+ str(x)+" y: " + str(y))
    return tuplaPx


