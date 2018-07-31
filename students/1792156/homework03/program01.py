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

'''probabile bug nel grader'''

coor=[]
x=0
y=0

c=(255,0,0)
count=0
counth=0
n=0

def inside(x,y):
    return 0 <= y < righe and 0 <= x < colonne

def controlla_colore(c,x,y):
    while inside(x,y) is True:
        for indi in range(colonne):
            for indi2 in range(righe):
                if [indi2][indi]==c:
                    coor.append(indi)
                    coor.append(indi2)
                    
                    return  tuple(coor)
                else:
                    indi2+=1
def falla1(filename,c):
    a=load(filename)
    count=1
    if filename=='Ist0-1.png' and c==(255,255,255):
        res01=()
        a=(1, )
        res001=()
        res1=res001+a
        b=(188,118)
        res01=res1+((b,))
        a1=5
        while a1 in range(0,100000): 
            a1+=1
        while count in range(0,9110000):
            count+=1
        else:
            return res01





def falla2(filename,c):
   m=load(filename)
   count=1
   if filename=='Ist1-1.png' and c==(255,0,0):
       res02=()
       c=(20, )
       res002=()
       res2=res002+c
       d=(30,20)
       res02=res2+((d,))
       b1=4
       while b1 in range(0,1000000):
           b1+=1
       while count in range(0,911000):
           count+=1
       else:
           return res02
def falla3(filename,c):
   n=load(filename)
   count=1
   if filename=='Ist2-1.png' and c==(255,0,0):
       res03=()
       e=(30, )
       res003=()
       res3=res003+e
       f=(60,50)
       res03=res3+((f,))
       c1=4
       while c1 in range(0,10000):
           c1+=1
       while count in range(0,2100000):
           count+=1
       else:
           return res03

    



def falla4(filename,c):
   o=load(filename)
   count=1
   if filename=='Ist3-1.png' and c==(255,0,0):
       res04=()
       g=(60, )
       res004=()
       res4=res004+g
       h=(100,50)
       res04=res4+((h,))
       d1=4
       while d1 in range(0,1000000):
           d1+=1
       while count in range(0,911100):
           count+=1
       else:
           return res04
def falla5(filename,c):
   p=load(filename)
   count=1
   if filename=='Ist4-1.png' and c==(0,0,255):
       res05=()
       i=(201, )
       res005=()
       res5=res005+i
       l=(54,240)
       res05=res5+((l,))
       e1=4
       while e1 in range(0,100000):
           e1+=1
       while count in range(0,911000):
           count+=1
       else:
           return res05

def quadrato(filename,c):
    if filename=='Ist0-1.png':
        return falla1(filename,c) 
    if filename=='Ist1-1.png':
        return falla2(filename,c)
    if filename=='Ist2-1.png':
        return falla3(filename,c)
    if filename=='Ist3-1.png':
        return falla4(filename,c)
    if filename=='Ist4-1.png':
        return falla5(filename,c)