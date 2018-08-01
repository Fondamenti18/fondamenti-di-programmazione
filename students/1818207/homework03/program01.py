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
from immagini import *

def quadrato(filename,c):
    picture =load(filename)
    color = c
    altezza = len(picture)   #INDICIZZO RIGHE
    larghezza = len(picture[0]) #INDICIZZO COLONNE
    lato1 = 0
    lato2 = 0
    v = 0
    listariga = []
    prerisultato = [1,[]]
    prerisultato2 = []
    
    for x in range(altezza): #ITERO LE RIGHE
        #print (x)
        if color in picture[x]: #DENTRO LA RIGA IN ANALISI OSSERVO SE C'E' IL COLORE
            #print (x)
            for y in range(larghezza): #ITERO I PIXEL DI UNA RIGA 
                
                if picture[x][y] == color: #SE IL PIXEL CORRISPONDE AUMENTO DI UNO LA MISURA DEL LATO
                    lato1 += 1
                    #print (y)
                if picture[x][y] != color:
                    if lato1 != 0: #ATTENTISSIMO PU0' NON SERVIRTI
                        #print(lato1)
                        checkquad = x + lato1
                        latorif = y - lato1
                        iterott = latorif + lato1
                        listariga.append(lato1)
                        lato1 = 0
                        
                        #print(x,color)
                        #print(listariga)
                        if listariga[0] != '' :
                            
                            #print(listariga,checkquad,x)
                            listariga.clear()
                            #print(listariga)
                        
                            for i in range(x,altezza):
                                cercaquadrato =checkquad - 1
                                #print(i)
                                
                                for y in range(latorif,iterott):
                                    #print(y)
                                    
                                    if picture[i][y] == color: #SE IL PIXEL CORRISPONDE AUMENTO DI UNO LA MISURA DEL LATO
                                        lato2 += 1
                                        #print(lato2)
                                    if y == iterott -1  :
                                        #print (iterott)
                                        #print(larghezza)
                                        if lato2 == checkquad - x:
                                            #print (lato2)
                                            var = cercaquadrato + 1 - x
                                            v += 1
                                            oldlat2 = lato2
                                            #print (checkquad  - x,'rif lato',v,'checkquadv',lato2,'lat', var,i,'i',checkquad,x,cercaquadrato,'cercaquad')
                                            lato2 = 0
                                          
                                            for z in range(1,oldlat2+1):
                                                if z / v == 1:
                                                    #print('quadratino',v,z,prerisultato)
                                                    if z >= prerisultato[0] and v >= prerisultato[0]:
                                                        
                                                        prerisultato.clear()
                                                        prerisultato.append(z)
                                                        tup = (latorif,x)
                                                        print('dio',prerisultato,latorif,checkquad - x,x,v)
                                                        break
                                                        
                                                        
                                                        
                                            
                                            #print (lato2,v,'lato2v')
                                        if i == checkquad-1 :
                                                #print ('diooooooooooo',var, checkquad)
                                                if v == var:
                                                    #print('è un quadrato',latorif,checkquad - v )
                                                    v = 0
                                                    
                                                    #print(v,'èv')
                                                    latorif = 0
                                                    #checkquad = 0
                                                    #if color in larghezza
                                                else:
                                                    v = 0
                                                    lato2 = 0
                                #print (x,i)
                                #if color in picture[i]:
                                    
                            
                                            #if i == checkquad-1 and v =!: 
                                #else:  
                                     #print ('non è un quadrato')
                                     #v = 0
                                     #lato2 = 0
                                     




    return prerisultato[0],tup

#quadrato("diocan.png",(239,160,0))
#quadrato("diocan1.png",(239,160,0))
#quadrato("Ist0.png",(255,255,255))
u =quadrato('Ist1.png',(255,0,0))
#quadrato('Ist2.png',(255,0,0))
#quadrato("Ist4.png",(0,0,255))
#quadrato('Ist3.png',(255,0,0))
print (u)