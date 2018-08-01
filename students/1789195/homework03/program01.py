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
    img=load(filename)  #carica immagine
    lst_max=()      #lista coordinate x,y rettangolo maggiore
    lun_max=0       #lunghezza del rettangolo maggiore
    lst=()         
    
    count_y=0       #contatore righe
    count_x=0       #contatore colonne
    try:
        for y in img:   #scorre righe immagine
            for x in y:     #scorre colonne righe
                if(x==c):   #se la tupla in x è uguale al colore c
                    lst=cercaRet(img, count_y, count_x, c)  #richiama funzione cercaRet               
                    if(lst[0]>lun_max):      #se la lunghezza è maggiore di lun_max
                        lun_max=lst[0]       #lun_max è uguale a lunghezza
                        lst_max=(lst[2], lst[1])  #lista_max aggiunge coordinate x,y del rettangolo
                count_x+=1      #incremente count_x di 1
            count_x=0   #reset count_x
            count_y+=1   #incrementa count_y di 1 
    except:
        pass
    return(lun_max,lst_max)
        
        
def cercaRet(img, y, x, c):
    lst=()   #aggiunge alla lista lst il numero di y e x, cioè il primo pixel del rettangolo
    i=0    
    j=0
    count_lar=0     #contatore larghezza rettangolo
    count_lun=0     #contatore lunghezza rettangolo
    try:
        while(img[y+i][x+j]==c and i+1<len(img)):     #se l'immagine in coordinare y+i, x è uguale al colore c
            while(img[y+i][x+j]==c and j+1<len(img[0])):    #se l'immagine in coordinare y+i, x+j è uguale al colore c                 
                j+=1    #aumenta j di 1, colonna
            count_lar=j     #count larghezza rettangolo
            j=0     #reset j, colonna 
            count_lun+=1    #aumenta contatore lunghezza di 1
            if(i+1>=count_lar):
                break
            else:
                i+=1    #aumenta i di 1, riga    
        lst+=(count_lun, y, x)   #aggiunge alla lista lst la lunghezza del rettangolo
    except:
        pass
    
    return(lst)
   
    
    
if __name__== '__main__':
    print(quadrato('Ist3.png',(255,0,0)))
