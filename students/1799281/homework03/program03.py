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
"C:/Users/john/Desktop/homework3/es3/prova.png"
"C:/Users/john/Desktop/homework3/es3/l1.png"
"C:/Users/john/Desktop/homework3/es3/prova.png"
 while j<len(im):           #ricoloro tutto

            i=w
            while i<len(im[j]):
                if i+1<len(im[j]):
                    if im[j][i]==colore:
                        im[j][i]=c1
                        area=area+1
                    if im[j][i+1]==colore:
                        im[j][i+1]=c1
                        area=area+1
                        i=i+1
                    elif im[j][i+1]!=colore:
                        j=j+1
                        break
                else:
                    break"
                    
                            while j<len(im):
            i=w
            while i<len(im):
                if j==q or (flag==True and j==cont-1):
                    if im[j][i]==colore:
                        im[j][i]=c2
                        if flag!=True:
                            cont=cont+1
                        i=i+1
                        #print(cont)
                    else:
                        print(cont)
                        flag=True
                elif j!=q :     #and (flag==True and j!=cont-1)
                    if im[j][i]==colore:
                        im[j][i]=c2
                        print(j)
                if flag==True and i==cont-1:
                    temp=j
               # i=i+1
            j=j+1
            f (i-1>=0 and im[j][i-1]!=colore and im[j-1][i]!=c2) or (i+1<len(im) and im[j][i+1]!=colore and im[j][i+1]!=c2)


                        if im[j][i]!=colore:
                save(im,"C:/Users/john/Desktop/homework3/es3/prova.png")
                print("1",j,i)
                return(perimetro)
            if (i+1<len(im) and im[j][i+1]==colore) or (i+1==len):     #orizzontale +1
                print("2",i)
                if im[j][i]==colore:
                    perimetro=perimetro+1
                    im[j][i]=c2
                #break
            if (i==0 and im[j][i]==colore) :            #o;o
                im[j][i]=c2
                perimetro=perimetro+1
            if j-1<q or j==0 or j==len(im) or(j-1>=0 and im[j-1][i]!=colore and im[j-1][i]!=c2) or (j+1<=len(im) and im[j+1][i]!=colore and im[j+i][i]!=c2) : #più in alto nulla oppure in alto altro colore oppure in basso altro colore 
                if im[j][i]==colore:
                    perimetro=perimetro+1
                    im[j][i]=c2
            if  (j==len(im) and im[j][i]==colore) or (i==len(im[j]) and im[j][i]==colore) or (j==0 and im[j][i]==colore):
                if im[j][i]==colore:
                    perimetro=perimetro+1
                    im[j][i]=c2
'''

from immagini import *
im=0
def ricolora(fname, lista, fnameout):
    global im
    im=load(fname)
    j=0
    i=0
    area=0
    per=0
    cont=0
    flag=False
    lst=[]

    #print(len(lista))
    for y, x, c1, c2 in lista:
        tupla=()
        j=0
        i=0
        area=0
        per=0
        cont=0
        colore=im[y][x]
        j=y
        i=x

        
        while i < len(im[j]):        #-------------------per trovare l'inizio
            if i-1>=0:
                if im[j][i-1]==colore:
                    i=i-1
                   # print("daj")
                else:
                    break
            else:
                break
        while j<len(im):
            if j-1>=0:
                if im[j-1][i]==colore:
                    j=j-1
                else:
                    break
            else:
                break           #------------------------fino a qui  or (i-1<0)


        q,w=j,i
        j,i=w,q
        #print(q,w,j,i)                       #perimetro!
        i=q
        j=w
        per=perimetro(q,w,colore,c2)
                 #area
        while j<len(im):
            i=q
            while i<len(im[j]):
                if im[j][i]==c2 and (i+1<len(im[j]) and im[j][i+1]!=colore):
                   # print("1",im[j][i+1],j)
                    break
               # elif im[j][i]==c2 and (i+1<=len(im[j]) and im[j][i+1]==colore):
                    
                if im[j][i]==colore:
                    #print("3",i)
                    im[j][i]=c1
                    area=area+1
                elif im[j][i]!=colore and im[j][i]!=c2 :
                    #print("2",im[j][i],j,i)
                    break
                    #return(j,i)
                i=i+1
            j=j+1
        tupla=tupla+(area,per)
        lst=lst+[tupla]

            
    








        
       
            #j=j+1
        
    #print(j,i)     
    #im[j][i]=(255,255,255)
    save(im,fnameout)
    return(lst)
    
    





def perimetro(q,w,colore,c2):
    global im
    j,i=w,q
    #print(j,q)
    perimetro=0
    while j<len(im):
        i=q
        while i<len(im[j]):
            if im[j][i]!=colore and im[j][i]!=c2 or (im[j][i]!=colore and im[j][i]==c2): #or (im[j][i]!=colore and im[j][i]==c2)
                return(perimetro)
            if i==q:
                perimetro=perimetro+1
                im[j][i]=c2
                i=i+1
                #print("a",j,i)
                continue
                #break
            if j==w:
                #if im
                perimetro=perimetro+1
                im[j][i]=c2
                #i=i+1
                #print("0",j,i)
                #continue
                #break
            if (i+1<len(im[j]) and im[j][i+1]==colore) and ((j-1>=0 and im[j-1][i]!=colore and im[j-1][i]!=c2)) :     #se dopo c'è colore e sopora no     dovrebbe andare bene or ) or (j+1<len(im) and im[j+1]!=colore and im[j+1][i]!=c2)
                im[j][i]=c2
               # print("1",j,i)
                perimetro=perimetro+1
            elif i+1<len(im[j]) and im[j][i+1]!=colore:       #se dopo non c'è colore
                im[j][i]=c2
               # print("2",j,i)
                if j!=w:
                    perimetro=perimetro+1          #<-------------yay
                break
            elif (i+1<len(im[j]) and im[j][i+1]==colore) and ((j+1<len(im) and im[j+1][i]!=colore )):       #potrebbero esserci conseguenze!
                #print("sadam")
                #print("3",j,i)
                perimetro=perimetro+1
                im[j][i]=c2
            #if j+1<len(im) and im[j+1][i]==colore and (i-1>=0 and im[j][i-1]!=colore and im[j][i-1]!=c2) :        #se nella riga sotto c'è colore ma orizzontalmente no or (i+1<=len(im[j]) and im[j][i+1]!=colore and  im[j][i+1]!=c2)
                #im[j][i]=c2
            #elif j+1<len(im) and im[j+1][i]!=colore:    #se nellar iga sotto non c'è colore
               # im[j][i]=c2
                #print("waw")
                #break
            if j+1==len(im) and im[j][i]==colore:         #se sono al limite in basso
                im[j][i]=c2
                #print("4",j,i)
                perimetro=perimetro+1
            elif j+1==len(im) and im[j][i]!= colore:        #limite in basso ma di colore sbagliato
                #im[j][i]=c2
                break
            if i+1==len(im[j]) and im[j][i]==colore:            #limite a destra
                im[j][i]=c2
                #print("5",j,i)
                if (len(im[j])!=q):
                    perimetro=perimetro+1
            elif i+1==len(im[j]) and im[j][i]!= colore:       #limite a destra colore sbagliato
                #im[j][i]=c2
                break
                #save(im,"C:/Users/john/Desktop/homework3/es3/prova.png")
                #return(area)
            i=i+1
        j=j+1                        #fine perimetro
    #print(j,i)
    return(perimetro)












































                
                
                
        
        

