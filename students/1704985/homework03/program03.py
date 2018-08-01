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

from immagini import load,save

def ricolora(fname, lista, fnameout):
    img=load(fname)
    i=0
    
    lista_finale=[]
    
    while i<len(lista):
        
        ambush=0
        pembush=0
        y=lista[i][1]
        c1=lista[i][2]
        x=lista[i][0]
        c2=lista[i][3]
        ciccio=[(x,y)]
        pem=[]
        
        for eddai in ciccio:
            x,y=eddai
            if inside(img,x+1,y)==True and img[y][x+1]==img[y][x]:
                if(x+1,y) not in ciccio:
                    ciccio+=((x+1,y))
            if inside(img,x-1,y)==True and img[y][x-1]==img[y][x]:
                if(x-1,y) not in ciccio:
                    ciccio+=((x-1,y))
            if inside(img,x,y+1)==True and img[y+1][x]==img[y][x]:
                if(x,y+1) not in ciccio:
                    ciccio+=((x,y+1))
            if inside(img,x,y-1)==True and img[y-1][x]==img[y][x]:
                if(x,y-1) not in ciccio:
                    ciccio+=((x,y-1))
                    
           
        
        for lardo in ciccio:
            x,y=lardo
            img[y][x]=c1
            ambush+=1
            if connessi(img,x,y,ciccio)!=4:
                pem+=((x,y))
                
        for pixel in pembush:
            a,b=pixel
            img[b][a]=c2
            pembush+=1
            
        lista_finale+=(ambush,pembush)
        i+=1
                 
    save(img,fnameout)    
    return lista_finale
    
    
    
def connessi(img,x,y,ciccio):
    ciccio_2=0
    adj= [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    for k in adj:
        a,b=k
        if inside(img,a,b)!=True or (a,b) not in ciccio:
            break
        else:
            ciccio_2+=1
    return ciccio_2                
            
            
            
def righe(img):
    return len(img)

def colonne(img):
    return len(img[0])

def inside(img,x,y):
    return 0 <= y < righe(img) and 0 <= x < colonne(img)


