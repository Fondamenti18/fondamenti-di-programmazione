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

from immagini import *

def controlla(img1,r,c):
    img = img1.copy()
    lista_temp = []
    lista_temp.append((c,r))
    lista_connessi = set()
    lista_connessi.add((c,r))
    colore_nativo = img[c][r]
    mierda = (11,11,11)
    img[lista_temp[0][0]][lista_temp[0][1]] = mierda
    
    
    while len(lista_temp) > 0:
        
        #controlla se non sta sui bordi SU
        if lista_temp[0][0] != 0:
            if img[lista_temp[0][0]-1][lista_temp[0][1]] == colore_nativo:
                lista_temp.append((lista_temp[0][0]-1,lista_temp[0][1]))
                lista_connessi.add((lista_temp[0][0]-1,lista_temp[0][1]))
                img[lista_temp[0][0]-1][lista_temp[0][1]] = mierda
                
        #controlla se non sta sui bordi GIU
        if lista_temp[0][0] != len(img)-1:
            if img[lista_temp[0][0]+1][lista_temp[0][1]] == colore_nativo:
                lista_temp.append((lista_temp[0][0]+1,lista_temp[0][1]))
                lista_connessi.add((lista_temp[0][0]+1,lista_temp[0][1]))
                img[lista_temp[0][0]+1][lista_temp[0][1]] = mierda
                
        #controlla se non sta sul bordo SINISTRA
        if lista_temp[0][1] != 0:
            if img[lista_temp[0][0]][lista_temp[0][1]-1] == colore_nativo:
                lista_temp.append((lista_temp[0][0],lista_temp[0][1]-1))
                lista_connessi.add((lista_temp[0][0],lista_temp[0][1]-1))
                img[lista_temp[0][0]][lista_temp[0][1]-1] = mierda
                
        #controlla se non sta sul bordo DESTRA
        if lista_temp[0][1] != len(img[0])-1:
            if img[lista_temp[0][0]][lista_temp[0][1]+1] == colore_nativo:
                lista_temp.append((lista_temp[0][0],lista_temp[0][1]+1))
                lista_connessi.add((lista_temp[0][0],lista_temp[0][1]+1))
                img[lista_temp[0][0]][lista_temp[0][1]+1] = mierda
        
        lista_temp.pop(0)
        
    return lista_connessi

def colora(img,lista_connessi,c1,c2):
    area = 0
    perimetro = 0
    for i in lista_connessi:
        lato = False
        
        if (i[0],i[1]-1) in lista_connessi:
            if (i[0],i[1]+1) in lista_connessi:
                if (i[0]+1,i[1]) in lista_connessi:
                    if (i[0]-1,i[1]) in lista_connessi:
                        lato = True
        
        if lato == True:
            img[i[0]][i[1]] = c1
            area += 1
        else:
            img[i[0]][i[1]] = c2
            perimetro += 1
        
    return img,area,perimetro

def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    img = load(fname)
    lista_connessi = set()
    Listona = []
    
    for x in lista:
        lista_connessi = controlla(img,x[0],x[1])
        img,A,P = colora(img,lista_connessi,x[2],x[3])
        Listona.append((A,P))
    
    save(img,fnameout)
    return Listona

