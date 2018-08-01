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
import png

def quadrato(fname,c):
    '''Implementare qui la funzione'''
    a =load(fname,c)
    controllo = 0
    lunghezza_lato_riga=0
    lunghezza_lato_colonna =0
    controllo_colonna_1=0
    controllo_colonna_2=0
    lista_coordinate=[]
    l_diff=[]
    cont_rig_1=0
    cont_rig_2=0
    differenza_colonne=0
    differenza_righe=0
    diz={}
    lista_righe=[]
    diz2={}
    diz3={}
    h = 1
    for rig in range(len(a[0])):
        for col in range(len(a)):
            
            if a[col][rig] == c :
                
                if controllo == 0:
                    
                    controllo_colonna_1=col
                    
                    controllo +=1
                    #if col in diz:
                        
                     
                if a[col+1][rig] != c and controllo == 1: #and col+1 < len(a) and rig < len(a[0]) and controllo == 1 and :
                    #print(lista_coordinate)
                    lista_coordinate.append((cont_rig_1,rig))
                    controllo_colonna_2=col                     
                    differenza_colonne=controllo_colonna_2-controllo_colonna_1
                    
                    
                    if not controllo_colonna_1 in diz :
                        
                        h = 1
                        
                        diz[controllo_colonna_1] = differenza_colonne+1
                    else:
                        h+=1
                    
                         
                        
                    controllo = 0
                    
    for col in range(len(a)):
        for rig in range(len(a[0])):
            
            if a[col][rig] == c :
                
                if controllo == 0:
                    cont_rig_1 = rig
                    controllo +=1
                    #if col in diz:
                        
                     
                if a[col][rig+1] != c and  controllo == 1:#col < len(a) and rig+1 < len(a[0]) and :
                    
                    
                    cont_rig_2=rig                    
                    differenza_righe=cont_rig_2-cont_rig_1
                    
                    if not cont_rig_1 in diz2 :
                        diz2[cont_rig_1] = differenza_righe+1
                    
                    controllo = 0
                    
    
    indice_massimo1 = max(diz,key=diz.get)
    indice_massimo2 = max(diz2,key=diz2.get)
    
    return(diz[indice_massimo1],(indice_massimo2,indice_massimo1))
    
    
    
    
    
    
    
        
        
    
    

       

def load(fname,c):
    """ Carica la immagine PNG dal file fname.
        Torna una lista di liste di pixel.
        Ogni pixel è una tupla (R, G, B) dei 3 colori.
        Ciascun colore è un intero tra 0 e 255 compresi.
    """
   
    
    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                l+=[(line[i], line[i+1], line[i+2])]
    
            img+=[l]
    return img
    
        
        
        
        
        
        
    
    
    
    
    
    
    
    