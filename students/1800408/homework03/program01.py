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

def quadrato(filename,c):
    '''Implementare qui la funzione'''
    
    immaginefiltrata=creaimmagine(filename,c)
    lista,listalunghezze=analisi(immaginefiltrata,c)
    risultato1,risultato2=analisi2(lista,listalunghezze) 

    return risultato1,risultato2
    
def creaimmagine(filename,colore): 
    immagineoriginale=load(filename)
    altezza=len(immagineoriginale)
    larghezza=len(immagineoriginale[0])
    immaginenuova=[]
    for h in range(altezza):
        riga=[]
        for l in range(larghezza):
            if immagineoriginale[h][l]==colore:
                riga.append(colore)
            else:
                riga.append('k')        
        immaginenuova.append(riga)   
    #print(immaginenuova)    
    return immaginenuova


def analisi(immaginenuova,colore):  #si distinguono tutti i rettangoli    
    larghezza=len(immaginenuova[0])-1  
    altezza=len(immaginenuova)-1  
    lista=[]
    listalunghezze=set()
    i=0
    while i<=altezza:
        indice=0
        while  indice<=larghezza:  #i è la  riga, indice è la colonna
            
            if indice!=larghezza:
                
                if immaginenuova[i][indice]=='k' and immaginenuova[i][indice+1]==colore:  #caso inizio rettangolo
                    tupla=indice+1,i
                    indice+=1
                    
                elif immaginenuova[i][indice]==colore and immaginenuova[i][indice+1]=='k':  #caso fine rettangolo
                 tuplafinale=indice+1,i
                 indice+=1
                
                    
                elif immaginenuova[i][indice]==colore and immaginenuova[i][indice+1]==colore:
                    tupla=tupla
                    tuplafinale='c'
                    indice+=1
                elif immaginenuova[i][indice]=='k'  and immaginenuova[i][indice+1]=='k':
                    tupla='c'
                    tuplafinale='c'
                    indice+=1       
            elif indice==larghezza:  #non entra in questo caso
                
                if  immaginenuova[i][indice]==colore:
                    tuplafinale=indice+1,i
                    
                else:
                    tupla='c'
                    tuplafinale='c'
                    break
            
            
                
            if tupla!='c' and tuplafinale!='c':
                dimensione=tuplafinale[0]-tupla[0]
                controllo=analisialt(immaginenuova,tupla,colore,dimensione)
                if controllo: 
                    listalunghezze.add(dimensione)
                    lista.append((tupla,dimensione)) 
        i+=1
    return lista,listalunghezze               
                

def analisialt(immaginenuova,tupla,colore,dimensione):  #inserire in analisi affinchè non si calcolino su rettangoli uguali
    c,r=tupla
    risultato=False
    i=0    
    while i<=dimensione-1:
    
        if immaginenuova[r+i][c]==colore:
            risultato=True
            i+=1
        else:
            risultato=False
            break
    if r+dimensione+1<=len(immaginenuova)-1:
        if immaginenuova[r+dimensione+1][c]=='c':
            risultato=False  
    return risultato

def analisi2(lista,listalunghezze):  
  #  print(listalunghezze)
   # print(lista)
    valoremassimo=max(listalunghezze)
    x=0
    while x<=len(lista)-1:
        if lista[x][1]==valoremassimo:
            posizione=lista[x][0]
            break
            
        x+=1
    return valoremassimo,posizione


    
#print(quadrato('Ist0.png',(255,255,255)))
#print(quadrato('Ist4.png',(0,0,255)))  #risultato(60, (100, 50))   a me da (60,(120,30))
#print(quadrato('Ist3.png',(255,0,0)))