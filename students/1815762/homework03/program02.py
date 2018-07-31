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
'''

from immagini import *



def riempi(img,r,c,gr,gc,verde):
    try:
        start=c
        while r<gr:
            c=start
            while c<gc:
                img[r][c]=verde
                c+=1
            r+=1
    except IndexError:
        pass
        
    return img,r,c,gr,gc


def direz(vardestra,vargiu,varsinistra,varsu,blu,passo,img,nero,bianco,r,c):
    if passo[-1]==' ':
        if img[r+39][c+39]==nero or img[r+39][c+39]==bianco:
            vardestra=True
            vargiu=True
            varsinistra=True
            varsu=True
            blu=True
    elif passo[-1]=='0':
        print(r,c)
        if c==len(img[0]):
            try:
                if img[r][c-1]==nero or img[r][c-1]==bianco:
                    vardestra=False
                    vargiu=True
                    varsinistra=False
                    varsu=False
                    blu=False
                elif img[r-1][c-41]==bianco or img[r-1][c-41]==nero:
                    vardestra=False
                    vargiu=False
                    varsinistra=True
                    varsu=False
                    blu=False
                elif img[r-41][c-1]==nero or img[r-41][c-1]==bianco:
                    vardestra=False
                    vargiu=False
                    varsinistra=False
                    varsu=True
                    blu=False
                else:
                    vardestra=False
                    vargiu=False
                    varsinistra=False
                    varsu=False
                    blu=True
            except IndexError:
                pass
        elif r==len(img):
            try:
                if img[r-1][c]==nero or img[r-1][c]==bianco:
                    vardestra=True
                    vargiu=False
                    varsinistra=False
                    varsu=False
                    blu=False
                elif img[r-1][c-41]==bianco or img[r-1][c-41]==nero:
                    vardestra=False
                    vargiu=False
                    varsinistra=True
                    varsu=False
                    blu=False
                elif img[r-41][c-1]==nero or img[r-41][c-1]==bianco:
                    vardestra=False
                    vargiu=False
                    varsinistra=False
                    varsu=True
                    blu=False
                else:
                    vardestra=False
                    vargiu=False
                    varsinistra=False
                    varsu=False
                    blu=True
            except IndexError:
                pass
        elif img[r-1][c]==nero or img[r-1][c]==bianco:
            vardestra=True
            vargiu=False
            varsinistra=False
            varsu=False
            blu=False
        elif img[r][c-1]==nero or img[r][c-1]==bianco:
            vardestra=False
            vargiu=True
            varsinistra=False
            varsu=False
            blu=False
        elif img[r-1][c-41]==bianco or img[r-1][c-41]==nero:
            vardestra=False
            vargiu=False
            varsinistra=True
            varsu=False
            blu=False
        elif img[r-41][c-1]==nero or img[r-41][c-1]==bianco:
            vardestra=False
            vargiu=False
            varsinistra=False
            varsu=True
            blu=False
        else:
            vardestra=False
            vargiu=False
            varsinistra=False
            varsu=False
            blu=True
    elif passo[-1]=='1':
        if r==len(img):
            try:
                if img[r-1][c-41]==bianco or img[r-1][c-41]==nero:
                    vardestra=False
                    vargiu=False
                    varsinistra=True
                    varsu=False
                    blu=False
                elif img[r-41][c-1]==nero or img[r-41][c-1]==bianco:
                    vardestra=False
                    vargiu=False
                    varsinistra=False
                    varsu=True
                    blu=False
                elif img[r-1][c]==nero or img[r-1][c]==bianco:
                    vardestra=True
                    vargiu=False
                    varsinistra=False
                    varsu=False
                    blu=False
                else:
                    vardestra=False
                    vargiu=False
                    varsinistra=False
                    varsu=False
                    blu=True
            except IndexError:
                pass
        elif c==40:
            try:
                if img[r][c-1]==bianco or img[r][c-1]==nero:
                    vardestra=False
                    vargiu=True
                    varsinistra=False
                    varsu=False
                    blu=False
                elif img[r-41][c-1]==bianco or img[r-41][c-1]==nero:
                    vardestra=False
                    vargiu=False
                    varsinistra=False
                    varsu=True
                    blu=False
                elif img[r-1][c]==nero or img[r-1][c]==bianco:
                    vardestra=True
                    vargiu=False
                    varsinistra=False
                    varsu=False
                    blu=False
                else:
                    vardestra=False
                    vargiu=False
                    varsinistra=False
                    varsu=False
                    blu=True
            except IndexError:
                pass
        elif img[r][c-1]==nero or img[r][c-1]==bianco:
            vardestra=False
            vargiu=True
            varsinistra=False
            varsu=False
            blu=False
        elif img[r-1][c-41]==bianco or img[r-1][c-41]==nero:
            vardestra=False
            vargiu=False
            varsinistra=True
            varsu=False
            blu=False
        elif img[r-41][c-1]==nero or img[r-41][c-1]==bianco:
            vardestra=False
            vargiu=False
            varsinistra=False
            varsu=True
            blu=False
        elif img[r-1][c]==nero or img[r-1][c]==bianco:
            vardestra=True
            vargiu=False
            varsinistra=False
            varsu=False
            blu=False
        else:
            vardestra=False
            vargiu=False
            varsinistra=False
            varsu=False
            blu=True
    elif passo[-1]=='2':
        if c==40:
            try:
                if img[r-41][c-1]==nero or img[r-41][c-1]==bianco:
                    vardestra=False
                    vargiu=False
                    varsinistra=False
                    varsu=True
                    blu=False
                elif img[r-1][c]==nero or img[r-1][c]==bianco:
                    vardestra=True
                    vargiu=False
                    varsinistra=False
                    varsu=False
                    blu=False
                elif img[r][c-1]==nero or img[r][c-1]==bianco:
                    vardestra=False
                    vargiu=True
                    varsinistra=False
                    varsu=False
                    blu=False
                else:
                    vardestra=False
                    vargiu=False
                    varsinistra=False
                    varsu=False
                    blu=True
            except IndexError:
                pass
        elif img[r-1][c-41]==bianco or img[r-1][c-41]==nero:
            vardestra=False
            vargiu=False
            varsinistra=True
            varsu=False
            blu=False
        elif img[r-41][c-1]==nero or img[r-41][c-1]==bianco:
            vardestra=False
            vargiu=False
            varsinistra=False
            varsu=True
            blu=False
        elif img[r-1][c]==nero or img[r-1][c]==bianco:
            vardestra=True
            vargiu=False
            varsinistra=False
            varsu=False
            blu=False
        elif img[r][c-1]==nero or img[r][c-1]==bianco:
            vardestra=False
            vargiu=True
            varsinistra=False
            varsu=False
            blu=False
        else:
            vardestra=False
            vargiu=False
            varsinistra=False
            varsu=False
            blu=True
    elif passo[-1]=='3':
        if c==len(img):
            try:
                if img[r-41][c-1]==nero or img[r-41][c-1]==bianco:
                    vardestra=False
                    vargiu=False
                    varsinistra=False
                    varsu=True
                    blu=False
                elif img[r][c-1]==nero or img[r][c-1]==bianco:
                    vardestra=False
                    vargiu=True
                    varsinistra=False
                    varsu=False
                    blu=False
                elif img[r-1][c-41]==bianco or img[r-1][c-41]==nero:
                    vardestra=False
                    vargiu=False
                    varsinistra=True
                    varsu=False
                    blu=False
                else:
                    vardestra=False
                    vargiu=False
                    varsinistra=False
                    varsu=False
                    blu=True
            except IndexError:
                pass
        elif img[r-41][c-1]==nero or img[r-41][c-1]==bianco:
            vardestra=False
            vargiu=False
            varsinistra=False
            varsu=True
            blu=False
        elif c==len(img[0]):
            if img[r-1][c-1]==nero or img[r-1][c-1]==bianco:
                vardestra=True
                vargiu=False
                varsinistra=False
                varsu=False
                blu=False
        elif img[r-1][c]==nero or img[r-1][c]==bianco:
            vardestra=True
            vargiu=False
            varsinistra=False
            varsu=False
            blu=False
        elif img[r][c-1]==nero or img[r][c-1]==bianco:
            vardestra=False
            vargiu=True
            varsinistra=False
            varsu=False
            blu=False
        elif img[r-1][c-41]==bianco or img[r-1][c-41]==nero:
            if c-41<0:
                vardestra=False
                vargiu=False
                varsinistra=False
                varsu=False
                blu=True
            else:
                vardestra=False
                vargiu=False
                varsinistra=True
                varsu=False
                blu=False 
        else:
            vardestra=False
            vargiu=False
            varsinistra=False
            varsu=False
            blu=True
    return vardestra,vargiu,varsinistra,varsu,blu
def controllo(vardestra,vargiu,varsinistra,varsu,blu,passo,r,c,gr,gc):
    if vardestra==True and vargiu==True and varsinistra==True and varsu==True and blu==True:
        gr=r+40
        gc=c+40
        passo.pop()
        passo+='0'
    elif vardestra==False and vargiu==False and varsinistra==False and varsu==True and blu==False:
        gr=r-40
        r=gr-40
        c=c-40
        passo+='3'
    elif vardestra==True and vargiu==False and varsinistra==False and varsu==False and blu==False:
        gr=r
        r=r-40
        gc=c+40
        passo+='0'
    elif vardestra==False and vargiu==True and varsinistra==False and varsu==False and blu==False:
        gr=r+40
        c=c-40
        passo+='1'
    elif vardestra==False and vargiu==False and varsinistra==True and varsu==False and blu==False:
        gc=c-40
        c=(c-40)-40
        r=r-40
        passo+='2'
    elif vardestra==False and vargiu==False and varsinistra==False and varsu==False and blu==True:
        r=r-40
        c=c-40
        passo+='K'
    return r,c,gr,gc,passo


def cammino(fname,fname1):
    '''Implementare qui la funzione'''
    verde=(0,255,0)
    bianco=(255,255,255)
    blue=(0,0,255)
    nero=(0,0,0)
    img=load(fname)
    r=0
    c=0
    gr=0
    gc=0
    breaks=False
    passo=[' ']
    vardestra=False
    vargiu=False
    varsinistra=False
    varsu=False
    blu=False
    lst=''
    while breaks==False:
        vardestra,vargiu,varsinistra,varsu,blu=direz(vardestra,vargiu,varsinistra,varsu,blu,passo,img,nero,bianco,r,c)
        r,c,gr,gc,passo=controllo(vardestra,vargiu,varsinistra,varsu,blu,passo,r,c,gr,gc)
        if passo[-1]=='K':
            img,r,c,gr,gc=riempi(img,r,c,gr,gc,blue)
            breaks=True
        else:
            img,r,c,gr,gc=riempi(img,r,c,gr,gc,verde)
    
    x=0
    passo.pop(0)
    passo.pop(-1)
    for x in range(len(passo)):
        lst+=passo[x]
        
    file=save(img,fname1)
    return lst



        
        
    
            
                                        














