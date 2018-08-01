'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore rettangoli 
di vari colori i cui assi sono sempre parallei agli assi dell'immagine.

Vedi ad esempio l'immagine Img1.png

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py.

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

from immagini import load

def quadrato(filename,c):
    img=load(filename) #apro l'immagine nel percorso filename con la funzione fornita
    
    latoMax=0 #assegno 0 alla variabile che dovrà tenere sotto controllo il lato massimo trovato finora
    temp=[]
    
    for y, riga in enumerate(img):
        for x, pixel in enumerate(riga):
            if img[y][x]==c: #se il pixel è dello stesso colore, lo aggiungo alla lista
                temp.append(c)
                if inside(img, x+1, y)==False or img[y][x+1]!=c: #se il pixel successivo non esiste o è di colore diverso, significa che è finito un possibile lato dello stesso colore
                    primaX=x-len(temp) + 1 #ricavo la x del punto in alto a sinistra del possibile quadrato
                    
                    square=checkSquare(img, latoMax, temp, primaX, y, c)
                    if square!=False:
                        latoMax, punto = square
                        
                    temp[:]=[] #svuoto la lista temp per trovare altri possibili lati sulla stessa riga

    return latoMax, punto
                

def checkSquare(img, latoMax, temp, x, y, c):
    '''Ritorna, nell'ordine, la lunghezza del lato più grande che si può costruire a partire da temp in input e le coordinate del suo punto in alto a sinistra'''
    #x sarebbe primaX, ovvero la coordinata del punto in alto a sinistra
    indice=y
    
    if len(temp)==1:
        return 1, (x,y)
    
    while len(temp)>latoMax: #vedi se il seguente controllo è utile: and len(set(temp))==1
        
        indice+=1 #si aumenta l'indice delle righe da controllare
        if 0 <= indice < len(img): #verifico che la riga successiva esiste
            
            if img[indice][x:x+len(temp)]==temp: #significa che alla riga sotto si trovano i punti dello stesso colore in posizione equivalente
                if indice-y+1==len(temp): #significa che ha controllato le n righe necessarie affinché sia un quadrato
                    return len(temp), (x,y) #con y uguale a quella data in input ma x forse cambiata
                    #len(temp) sarà latoMax, il punto (x,y) sarà il punto in alto a sx del quadrato.
            else:
                #significa che alla riga sotto il lato di quel colore è più piccolo di quel colore
                try:
                    prima=img[indice][x:x+len(temp)].index(c) #ricavo la prima occorrenza del colore giusto alla riga sotto
                    ultima=len(img[indice][x:x+len(temp)])-img[indice][x:x+len(temp)][::-1].index(c) #ricavo l'indice dell'ultima occorrenza del colore giusto alla riga sotto
                except:
                    return False
                
                x+=prima #modifico la coordinata sommandoci il numero di pixel che sto per levare a sinistra in modo che alla prossima iterazione l'if controlli la lista giusta
                
                #cancello i pixel di colore sbagliato (a sinistra e a destra) alla lista-controllo temp.
                temp=temp[prima:ultima]
                
                while img[indice][x:x+len(temp)]!=temp: #si riesegue il controllo sulla stessa riga con il temp e la x modificati
                    if (255,0,0) in set(img[indice][x:x+len(temp)]):
                        prova=img[indice][x:x+len(temp)].index((255,0,0))
                        temp=temp[:prova] #mettere -1?
                    elif (0,0,0) in set(img[indice][x:x+len(temp)]):
                        prova=len(img[indice][x:x+len(temp)])-img[indice][x:x+len(temp)][::-1].index((0,0,0))
                        temp=temp[prova:] #mettere +1?
                        x+=prova
                    else:
                        return False

        else: return False #se la riga sotto non esiste, sicuramente non ci può essere un quadrato
        
    #se esce dal ciclo while, significa che lun<=latoMax, perciò è inutile continuare a verificare se è un quadrato perché sarebbe più piccolo di quello cercato finora 
    return False    
        
        
def inside(img, x, y):
    '''verifica per ciascun pixel dato in input se si trova all'interno dell'immagine)'''
    return 0 <= y < len(img) and 0 <= x < len(img[0])

if __name__=='__main__':
    quadrato('Ist4.png',(0,0,255))

