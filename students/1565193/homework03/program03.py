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

rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)
#fname=r"C:\Scuola\Università\Informatica\Materie\Fondamenti di Programmazione\Programmi\homework03\es3\I2.png"
#lista=[(i*30+1,j*30+1,nero, verde) for i in range(10) for j in range (10)if not (i+j)%2]+[(i*30+1,j*30+1,rosso,bianco) for i in range(10) for j in range (10)if  (i+j)%2]
#fnameout=r"C:\Scuola\Università\Informatica\Materie\Fondamenti di Programmazione\Programmi\homework03\es3\test6.png"

from immagini import *
    
def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    
    x,y,x2,y2,per,area=0,0,0,0,0,0
    inter,bordo,perimetro,aree,per_ar=[],[],[],[],[]
    imag=load(fname)
    
    for k in lista:
        y,y2=k[1]-1,k[1]-1
        pix1=imag[k[1]-1][k[0]-1]
        bordo,inter,inter2=[],[],[]
    
        for i in range(len(imag)+1):    
            x,x2,x3,x4=k[0]-1,k[0]-1,k[0]-1,k[0]-1
            
            for j in range(len(imag[0])+1): 
                
              if x>-1 and y>-1:
                if imag[y][x]==pix1:
                    try:
                        
                        #print(y,x,'ciao')
                        #print(imag[y][x-1])
                        if imag[y][x-1]==pix1 or imag[y-1][x]==pix1:
                            #print(y,x)
                            inter.append((y,x))
                            area+=1
                            x-=1
                        else: bordo.append((y,x))
                    except IndexError: #pass
                        if x==-1 or y==-1:bordo.append((y,x))
                        #print('ciao')
                        #inter.append((y,x))
                        #print(inter)
              if x2<len(imag[0]) and y>-1:

                
                if imag[y][x2]==pix1:
                    #if x2>98:print(x2)
                    try:
                        #if x2>98 and y==9:print(x2)
                        #if x2>98 and y==9:print(x2,y,x2>98 and y==9)
                        #if k[0]==90:print(y,x)
                        #print(x2,len(imag[0]),x2==len(imag[0])-1)
                        #if x2>98 and y==9:print(imag[y][x2+1]==pix1)
                        if imag[y][x2+1]==pix1 or imag[y-1][x2]==pix1:
                            #print(x2)
                            inter.append((y,x2))
                            area+=1
                            x2+=1
                        else:
                            #print(y,x2)
                            bordo.append((y,x2))
                            #if x2==99 and y==9: print(inter)
                    except IndexError: #pass
                        if x2==len(imag[0])-1 or y==-1: bordo.append((y,x2))

              if x3>-1 and y2<len(imag):
                #print(y2,x3)
                if imag[y2][x3]==pix1:
                    try:
                        #print(y,x)
                        if imag[y2][x3-1]==pix1 or imag[y2-1][x3]==pix1:
                            inter.append((y2,x3))
                            area+=1
                            x3-=1
                        else: bordo.append((y2,x3))
                    except IndexError: #pass 
                        if x3==-1 or y2==len(imag)-1:bordo.append((y2,x3))
                        #bordo.append((y,x))
              if x4<len(imag[0]) and y2<len(imag):
                if imag[y2][x4]==pix1:
                    try:
                        #print(y,x)
                        if imag[y2][x4+1]==pix1 or imag[y2-1][x4]==pix1:
                            inter.append((y2,x4))
                            area+=1
                            x4+=1
                        else: bordo.append((y2,x4))
                    except IndexError: #pass
                        if x4==len(imag[0])-1 or y2==len(imag)-1:bordo.append((y2,x4))
              #if x2>98:print(x2)
                #if k[0]==90:print(x,x2)
              if x==-1 and x2==len(imag[0]): break
            y-=1
            y2+=1
            #if k[0]==90:print(y,y2)
            if y<=-1 and y2>=len(imag): break
        inter=list(set(inter))
        inter2=inter.copy()
        #print(sorted(inter))
        
        #print((0,1) in inter)
        
        for t in inter2:
            try:
                if imag[t[0]-1][t[1]]!=pix1 or imag[t[0]][t[1]-1]!=pix1 or imag[t[0]+1][t[1]]!=pix1 or imag[t[0]][t[1]+1]!=pix1: 
                    bordo.append((t[0],t[1]))
                    inter.remove((t[0],t[1]))
                    per+=1
                    area-=1
            except IndexError:
                bordo.append((t[0],t[1]))
                inter.remove((t[0],t[1]))
                per+=1
                area-=1
                #print(pix1)
            #print(t[0],t[1],len(list(set(bordo))))
        #print(sorted(bordo))        
          
        #print(sorted(inter))
        #perimetro.append(len(bordo))
        #aree.append(len(inter))
        per_ar.append((len(inter),len(list(set(bordo)))))
        
        for t in inter: imag[t[0]][t[1]]=k[2]
        for t in bordo: imag[t[0]][t[1]]=k[3]
        
    
    #print(inter)
        save(imag,fnameout)
            
    return per_ar
            