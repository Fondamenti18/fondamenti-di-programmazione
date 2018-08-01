'''

Definiamo adiacenti di un pixel p di un immagine i pixel adiacenti a p in  orizzontale o in  verticale.
Se un pixel e' sul bordo dell'immagine il suo vicinato non comprende i pixel non contenuti nell'immagine.
Il pixel dell'immagine con coordinate(x,y) ha dunque come adiacenti i pixel   
con coordinate (x-1,y),(x+1,y),(x,y-1),(x,y+1) appartenenti all'immagine. 
 
Definiamo connessi due pixel se e' possibile dall'uno raggiungere l'altro spostandosi solo su   
pixel adiacenti e dello stesso colore (ovviamente perche' cio' sia possobile e' necessario 
che i due pixel abbiano lo stesso colore).

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una funzione ricolora(fname, lista,  fnameout) che presi:
- il percorso di un file che contiene un'immagine in formato PNG
- una lista di quadruple del tipo (x,y,c1,c2) dove  x e y sono coordinate di un pixel dell'immagine e c1 e c2 due triple colore RGB
- il percorso di un file (fnameout) da creare
legge l'immagine in fname, esegue un'operazione di ricolorazione di alcuni pixel dell'immagine e 
registra l'immagine ricolorata nel file fnameout.

L'operazione di ricolorazione e' la seguente. Per ciascuna delle quadruple (x,y,c1,c2) della lista (nell'ordine), 
- tutti i pixel connessi al pixel  di coordinate (x,y) nell'immagine vanno ricolorati col colore c1, 
- tutti i pixel del perimetro (che si trovano sul 'bordo') della zona che si e' appena colorata devono essere ricolorati col colore c2.
Il perimetro della zona colorata è l'insieme dei pixel che non hanno tutti e 4 i vicini che fanno parte della zona ricolorata 
(ovvero almeno uno è di un colore diverso da quello che si sta ricolorando oppure almeno uno non esiste perchè sarebbe fuori dall'immagine)

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
def righe(img): return len(img)
def colonne(img): return len(img[0])
def contenuto(img,i,j):
    #ritorna true se il pixel(i,j) è dentro l'immagine img, false altrimenti
    iw, ih = righe(img), colonne(img)
    return 0 <= i < iw and 0 <= j < ih


from immagini import *
def adiacenti(immagine,x,y):
    lista = []
    lista1 = []
    sinistra = (y,x-1)
    destra = (y,x+1)
    su = (y-1,x)
    giu = (y+1,x)
    lista = [sinistra,destra,su,giu]
    listaPosizioni=[]
    for pixel in lista:
        if contenuto(immagine,pixel[1],pixel[0]) == True and immagine[pixel[0]][pixel[1]] == immagine[y][x]:
            #lista1.append(immagine[pixel[0]][pixel[1]])
            listaPosizioni.append((pixel[0],pixel[1]))
    return listaPosizioni

                
    



def ricolora(fname,lista,fnameout):
    '''Implementare qui la funzione'''
    immagine=load(fname)
    pieni=tuple()
    margini=tuple()
    listaRisultati=[]
    for quadrupla in lista:
        connesso = connessi(immagine,quadrupla[0],quadrupla[1])
        pieni = connesso[1]
        margini = connesso[0]
        for pixel in pieni:
            immagine[pixel[1]][pixel[0]] = quadrupla[2]
        for pixel in margini:
            immagine[pixel[1]][pixel[0]] = quadrupla[3]
        listaRisultati.append((len(pieni),len(margini)))
    #print(immagine)
    save(immagine,fnameout)
    return listaRisultati

def connessi(immagine,x,y):
    insieme=set()
    insiemeParziale = {(x,y)}
    insiemeMargine= set()
    while len(insiemeParziale) != 0:
        #print(insieme)
        #prendo una tupla a caso dalla lista
        #print(insiemeParziale)
        coordinate = insiemeParziale.pop()
        #print(coordinate)
        if immagine[y][x]==immagine[coordinate[1]][coordinate[0]] :
            insieme.add(coordinate)
        #print(coordinate)
        #ne vedo gli adiacenti
        listaAdiacenti = adiacenti(immagine,coordinate[1],coordinate[0])
        #print(listaAdiacenti)
        #scorro gli adiacenti
        #se gli adiacenti sono meno di 4 aggiungo la tupla all'insieme dei margini
        if len(listaAdiacenti) < 4:
            #print(coordinate)
            insiemeMargine.add((coordinate[0],coordinate[1]))
            insiemeMargine.add(coordinate)
        #scorro gli adiacenti
        for tupla in listaAdiacenti:
            #se il pixel con le coordinate della tupla ha lo stesso colore del pixel iniziale e la tupla non fa già parte dell'insieme la aggiungo
            if immagine[tupla[1]][tupla[0]] == immagine[y][x] and tupla not in insieme:
                insieme.add(tupla)
                insiemeParziale.add(tupla)
    for tupla in insiemeMargine:
        if tupla in insieme:
            insieme.remove(tupla)
    return (insiemeMargine,insieme)