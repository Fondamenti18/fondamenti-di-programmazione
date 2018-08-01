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

La funzoone deve tornare la lista di coppie (area interna, perimetro) nello stesso ordine in cui sono state colorate le aree.
 
Per altri  esempi vedere il file grade03.txt 
'''

from immagini import load,save

def ricolora(fname, lista, fnameout):
    img=load(fname)
    c=0
    listares=[]
    while c<len(lista):
        area=0
        perim=0
        a=lista[c][0]
        b=lista[c][1]
        c1=lista[c][2]
        c2=lista[c][3]
        pixconnessi=[(a,b)]
        perimetro=[]
        for coord in pixconnessi:
            a,b=coord
            if inside(img,a+1,b)==True and img[b][a+1]==img[b][a]:
                if (a+1,b) not in pixconnessi:
                    pixconnessi.append((a+1,b))
            if inside(img,a,b+1)==True and img[b+1][a]==img[b][a]:
                if (a,b+1) not in pixconnessi:
                    pixconnessi.append((a,b+1))
            if inside(img,a-1,b)==True and img[b][a-1]==img[b][a]:
                if (a-1,b) not in pixconnessi:
                    pixconnessi.append((a-1,b))
            if inside(img,a,b-1)==True and img[b-1][a]==img[b][a]:
                if (a,b-1) not in pixconnessi:
                    pixconnessi.append((a,b-1))
            img[b][a]=c1
            area+=1
            if vicini(img,a,b,pixconnessi)<4:
                perimetro.append((a,b))

        for pixel in perimetro:
            a,b=pixel
            img[b][a]=c2
            perim+=1
        
        area=area-perim
        listares.append((area,perim))
        c+=1
        
    save(img,fnameout)
    return listares
            
def vicini(img,x,y,pixconnessi):
    pixvicini=0
    
    nearpix=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    for k in nearpix:
        a,b=k
        if inside(img,a,b)==False or (a,b) not in pixconnessi:
            break
        else:
            pixvicini+=1
    return pixvicini
            

def inside(img, x, y):
    colonne=len(img[0])
    righe=len(img)
    return 0 <= y < righe and 0 <= x < colonne
    
    
    
    '''if __name__=='__main__':
    from PIL import Image
    lista=[(100,100,(255-x,255,255),(0,0,255-x)) for x in range(100)]
    img=ricolora('I4.png',lista,'test9.png')
    save(img,'prova.png')
    imm=Image.open('prova.png')
    imm.show()'''
    

