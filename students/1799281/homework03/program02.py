'''
Un robottino deve muoversi su di una scacchiera di 15 x 15 celle  con celle bianche e nere  ciascuna di lato 40. 
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli (queste celle sono  colorate di rosso).

Un  esempio di scacchiera con ostacoli e' dato  dall'immagine 'I1.png'

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Al'inizio il robottino e' posizionato sulla prima cella in altro a sinistra della scacchiera ed e' rivolto verso destra (x crescente). 
Ad ogni step tenta di ragiungere una delle celle adiacenti in orizzontale o verticale. 
Le regole di movimento del robottino sono le seguenti: 
- al generico step, si sposta sulla cella che ha di fronte se questa e' libera da ostacoli e non ci e' gia transitato in passato. 
- se invece la cella risulta occupata o e' una cella su cui ha gia transitato, ruota di 90 gradi in senso orario ed aspetta lo step successivo. 
- dopo aver ruotato  di 360 gradi senza essere riuscito a spostarsi si ferma. 

Progettare la funzione  percorso(fname, fname1) che presi in input:
- il percorso di un file (fname) contenente l'immagine in formato .png di una scacchiera con ostacoli
- il percorso di un file di tipo .png (fname1) da creare
legge l'immagine della scacchiera in fname, colora di verde le celle della scacchiera percorse dal robottino prima di fermarsi, 
colora di blu la cella in cui il robottino si ferma e registra l'immagine ricolorata nel file fname1. 
Inoltre restituisce una stringa dove in sequanza sono codificati i passi effettuati dal robottino prima di fermarsi. 
La codifica e' a seguente: 
    '0' per un passo verso destra (x crescenti)
    '1' per un passo verso il basso (y crescenti)
    '2' per un passo verso sinistra (x decrescenti)
    '3' per un passo verso l'alto (y decrescenti)

Si puo' assumere che la cella in alto a sinistra sia priva di ostacoli. 

Per esempi di scacchiere con ostacoli e relativi cammini  vedere il file grade02.txt 

NOTA: il timeout per la esecuzione del grader e' fissato a 10*N secondi (per N test eseguiti dal grader)
cammino("C:/Users/john/Desktop/homework3/es2/I1.png","C:/Users/john/Desktop/homework3/es2/prova1.png")
'''

from immagini import *
im=0
im1=0
ostacolo=(255,0,0)
cammino=(0,255,0)
posizione=(0,0,255)
j=0
i=0
holy=0
lista=""
last=0
last1=0
fm=0
def cammino(fname,  fname1):
    ori= 0 #orientamento: 0 destra, 1 basso, 2 sinistra, 3 alto
    global im
    global holy
    global lista
    holy=0
    im=load(fname)
    j=0
    i=0
    c=0   #primo ciclo. i primi pixel sono 0-39 e non 40 <------ molto inutile
    t=0   #idem ma con le righe
    controllo=0
    lista=""
    #print(im[j][i])
    while holy !=4:
        #print(holy)
        if controllo==0:
            controllo,j,i=orizzontale(j,i)
        elif controllo==1:
            #print(type(j),type(i),type(controllo))
            controllo,j,i=verticale(j,i)
        elif controllo==2:
            controllo,j,i=x(j,i)
        elif controllo==3:
            controllo,j,i=y(j,i)
    im=coloreb(last,last1)
    #print(im[last][last1],last,last1)
    #if ori==1:
    #if lista[-1]==lista[-2]:
     #lista=lista[:-1]
    save(im,fname1)
                
    return(lista)         
def coloreb(j,i):
    global last
    global last1
    global im
    last=j
    last1=i
    if i!=599:
        k=j+40
        o=i+40
        t=j
        while t!=k:
            y=i
            while y!=o:
                im[t][y]=(0,0,255)
                y=y+1
            t=t+1
    else:
        k=j+40
        o=i-40
        t=j
        while t!=k:
            y=i
            while y!=o:
                im[t][y]=(0,0,255)
                y=y-1
            t=t+1        
    #print(i,j,im[j][i])
    return(im)                 


                    
                    


    
                

def colore(j,i):
    global last
    global last1
    global im
    last=j
    last1=i
    if i!=599 :
        k=j+40
        o=i+40
        t=j
        while t!=k:
            y=i
            while y!=o:
                im[t][y]=(0,255,0)
                y=y+1
            t=t+1
    elif i==599 and j==599:
        k=j-40
        o=i-40
        t=j
        while t!=k:
            y=i
            while y!=o:
                im[t][y]=(0,255,0)
                y=y-1
            t=t-1                
    else:
        k=j+40
        o=i-40
        t=j
        while t!=k:
            y=i
            while y!=o:
                im[t][y]=(0,255,0)
                y=y-1
            t=t+1        
    #print(i,j,im[j][i])
    return(im)
def orizzontale(j,i):      #ori 0
    print("ORIZZONTALE")
    global lista
    global holy
    global im
    c=0
    while j != 600:


        
            while i != 600:




                #if ori==0: 

                if i+40<600:
                
                    if im[j][i]==(255,0,0) or im[j][i]==(0,255,0) and (im[j][i+40]==(255,0,0) or im[j][i+40]==(0,255,0)):     #se sono posizionato in un ostacolo
                        #print("1")
                        
                        holy=holy+1
                        ori=1
                        return(ori,j,i)
                    elif im[j][i+40]!=(255,0,0) and  im[j][i+40]!=(0,255,0):  #ok
                            im=colore(j,i)
                            i=i+40
                            holy=0
                            lista=lista+"0"
                            print("2, aggiungo")
                    elif im[j][i+40]==(255,0,0) or im[j][i+40]==(0,255,0):
                        #print("meh")          #cambiare orientamento
                        im=colore(j,i)
                        ori=1
                        holy=holy+1
                        print("3")
                        #lista=lista+"0"
                        return(ori,j,i)
                        #i=i+80
                    #elif im[j][i+40]==posizione:
                        #return(10,j,i)
                if i+40>=600:
                    #print(j)
                    if i+40==600 and (im[j][i] != (0,255,0) and im[j][i] != (255,0,0)):
                        #lista=lista[:-1]
                        im=colore(j,i)
                        i=599
                        ori=1
                        print("4",j,i)
                        return(ori,j,i)
                    else:
                        #lista=lista+"0"
                        holy=holy+1
                        ori=1
                        print("5")
                        return(ori,j,i)     #finita la scacchiera a destra
                    #print(i)
                    j=j+40
                    i=0
                    break
def verticale(j,i):       #ori 1
     #print(len(im),len(im[56]))
        print("verticale")
        global lista
        global holy
        global im
        while i <= 600:
            
            while j <= 600:
                
             #print(j+40)
             if j+40<600:
                #print(j,i)
                if im[j][i]==(255,0,0) or im[j][i]==(0,255,0) and (im[j+40][i]==(255,0,0) or im[j+40][i]==(0,255,0)) :      #se sono posizionato in un ostacolo
                    holy=holy+1
                    print("1")
                    ori=2
                    return(ori,j,i)
                elif im[j+40][i]!=(255,0,0) and  im[j+40][i]!=(0,255,0):  
                        im=colore(j,i)
                        j=j+40
                        holy=0
                        lista=lista+"1"
                        print("2, aggiungo")
                elif im[j+40][i]==(255,0,0) or im[j+40][i]==(0,255,0):
                    print("3")
                    holy=holy+1
                    im=colore(j,i)
                    ori=2       #<----------------------qui
                    return(ori,j,i)
                    #j=j+80
                elif im[j+40][i]==posizione:
                    return(10,j,i)
             if j+40>=600:
                #print(j,i,"qui")
                if j+40==600 and (im[j][i] != (0,255,0)  and im[j][i] != (255,0,0)):
                    im=colore(j,i)
                    #lista=lista+"1"
                    j=599
                    ori=2
                    print("4, aggiungo")
                    return(ori,j,i)
                elif j+40!=0 and (im[j][i] != (0,255,0)  and im[j][i] != (255,0,0)):
                    ori=2      #finita la scacchiera verso l'alto
                    holy=holy+1
                    lista=lista+"1"
                    #print("cambio qui",j,i)
                    return(ori,j,i)
                else:
                    ori=2      #finita la scacchiera verso l'alto
                    holy=holy+1
                    #lista=lista+"3"
                    print("cambio qui weaw",j,i)
                    return(ori,j,i)
                i=i+40
                j=0
                #print(j,i,"qui")
                break                  #<----------------- molto importante
def x(j,i):      #ori 2
    print("sinisstra")
    global holy
    global lista
    global im
    while j != 600:


        
            while i != 600:




                #if ori==0: 

                if i-40>0:
                
                    if im[j][i]==(255,0,0) or im[j][i]==(0,255,0) and (im[j][i-40]==(255,0,0) or im[j][i-40]==(0,255,0)):     #se sono posizionato in un ostacolo 
                        holy=holy+1
                        print("ei",holy)
                        ori=3
                        return(ori,j,i)
                    elif im[j][i-40]!=(255,0,0) and  im[j][i-40]!=(0,255,0):  #ok
                            print("1",j,i)
                            im=colore(j,i)
                            print("2, aggiungo")
                            lista=lista+"2"
                            if i==599:
                                i=600
                                lista=lista[:-1]
                                #print("tolgo")
                            if  j==599:
                                j=560
                            i=i-40
                            holy=0
                    elif im[j][i-40]==(255,0,0) or im[j][i-40]==(0,255,0):
                        print("meh")          #cambiare orientamento
                        holy=holy+1
                        im=colore(j,i)
                        ori=3
                        return(ori,j,i)
                        #i=i+80
                elif im[j][i-40]==posizione:
                    return(10,j,i)
                if i-40<=0:
                    if im[j][i-40]==(255,0,0) or im[j][i-40]==(0,255,0):
                        holy=holy+1
                        ori=3
                        return(ori,j,i)
                    #print(j)
                    if i-40==0 and (im[j][i] != (0,255,0)  and im[j][i] != (255,0,0)):
                        print("3, aggiungo")
                        im=colore(j,i)
                        lista=lista+"2"
                        i=0
                        ori=3
                        #print("onion")
                        return(ori,j,i)
                    #print(i)
                    else:      #finita la scacchiera a sinistra
                        ori=3
                        holy=holy+1
                        #print("cambio qui",j,i)
                        return(ori,j,i)
                    j=j-40
                    i=0
                    break 
def y(j,i):
        global lista
        global holy
        global im
        global fm
        print("su")
        while i != 600:              #ori = 3
            
            while j != 600:
                
             #print(j+40)
             if j-40>0:
                #print(j,i)
                if im[j][i]==(255,0,0) or im[j][i]==(0,255,0) and (im[j-40][i]==(255,0,0) or im[j-40][i]==(0,255,0)) :      #se sono posizionato in un ostacolo
                    holy=holy+1
                    ori=0
                    return(ori,j,i)
                elif im[j-40][i]!=(255,0,0) and  im[j-40][i]!=(0,255,0):  
                        im=colore(j,i)
                        j=j-40
                        holy=0
                        lista=lista+"3"
                        print("scrivo 1")
                elif im[j-40][i]==(255,0,0) or im[j-40][i]==(0,255,0):
                   # print("meh")
                    holy=holy+1
                    im=colore(j,i)
                    ori=0       #<----------------------qui
                    #print(j,i)
                    return(ori,j,i)
                    #j=j+80
                elif im[j-40][i]==posizione:
                    return(10,j,i)
             if j-40<=0:
                #print(j,i,"qui")
                if j-40==0 and (im[j][i] != (0,255,0)  and im[j][i] != (255,0,0) and im[j-40][i]!=(0,255,0)):
                    im=colore(j,i)
                    lista=lista+"3"
                    print(" 2 scrivo")
                    #j=1
                    ori=0
                    #print(j,i)
                    return(ori,j,i)
                elif j-40!=0 and (im[j][i] != (0,255,0)  and im[j][i] != (255,0,0)):
                    ori=0      #finita la scacchiera verso l'alto
                    holy=holy+1
                    #lista=lista+"3"
                    #print("gh",j,i)
                    return(ori,j,i)
                else:
                    ori=0      #finita la scacchiera verso l'alto
                    holy=holy+1
                    #lista=lista+"3"
                    fm=1
                    print("cambio qui",j,i)
                    return(ori,j,i)
                    
                i=i-40
                j=0
                #print(j,i,"qui")
                break             
