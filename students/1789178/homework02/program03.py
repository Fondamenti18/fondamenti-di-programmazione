'''
Abbiamo una stringa i cui elementi sono cifre tra '0' e '9' (comprese) che rappresenta la struttura di una parola.
La parola contiene al piu' 10 lettere diverse (ma puo' essere piu' lunga di 10 lettere se alcune sono ripetute), 
e la struttura si ottiene dalla parola sostituendo ciascuna lettera con una cifra, secondo le regole:
- a lettera uguale corrisponde cifra uguale
- a lettere diverse corrispondono cifre diverse

Esempio: 'cappello' -> '93447228'
Esempio: 'cappello' -> '12334556'

Sia data una "struttura" ed un insieme di parole. 
Vogliamo ottenere il sottoinsieme delle parole date compatibili con la struttura data.

Esempio: se la struttura e' '1234' e le parole sono { 'cane', 'gatto', 'nasa', 'oca', 'pino'}
le parole dell'insieme che sono compatibili con la struttura sono {'pino', 'cane'}

Scrivere una funzione decod( pfile, struttura) che prende in input:
- il percorso di un file (pfile), contenente testo organizzato in righe ciascuna composta da una sola parola
- una stringa di almeno 1 carattere, composta solo da cifre (la struttura delle parole da cercare)

La funzione  deve restituire l'insieme delle parole di pfile che sono compatibili con la struttura data.

Per gli esempi vedere il file grade03.txt

AVVERTENZE: 
	non usare caratteri non ASCII, come le lettere accentate;
	non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
    for x,val in enumerate (ls):
        
        #ls=set(x)
        azazel=list(set(ls[x]))
        for y,val in enumerate (azazel):
            if len(azazel) == len(ln):
            #if(len(azazel[y])== len(ln[y])):
                s[azazel[y]]=ln[y]
        for z,val in enumerate(ls[x]):
            if(ls[x][z] in s):
                ss+=s[ls[x][z]]
                #print()
                
        MAGAZZINO DEI VECCHI CICLI DI PROVA         

    for x in ls:
        azazel=''.join(list(set(x)))
        if len(azazel) == len(ln):
            #print(azazel)
            #print(x)
            for z in range(len(azazel)):
                #print('iao')
                ss=x.replace(azazel[z],ln[z])
            #for y in range(len(azazel)):
'''
#def conv(s,n):

      
 #   return s
#from string import maketrans
def eliminaDop(ln):
    z=''
    for x in ln:
        if x not in z:
            z+=x
    #print(z)
    return z
def cosss(testo1,ln,codice,ls):
    lss=[]
    for x in range(len(ls)):
        if(len(ls[x])==len(codice)):
            if(len(set(ls[x])) == len(ln)):
                #print(ls[x])
                azazel=eliminaDop(ls[x])
                #print(azazel)
                for y in range(len(azazel)):
                    ls[x]=ls[x].replace(azazel[y],ln[y])
                #print(ls[x])
                if(ls[x]==codice):
                    lss.append(testo1[x])
                #trantab= maketrans(azazel,ln)
                #print(ls[x].translate(trantab))
    
    return lss
def decod(pfile, codice):
    '''inserire qui il codice'''
    f=open(pfile,'r')
    l=f.read()
    azazel=[]
    lss=[]
    ls=l.split('\n')
    ln=eliminaDop(codice)
    prova=''
    testo1=[]
    testo1[:]=ls[:]
    lss[:]=cosss(testo1,ln,codice,ls)
    
    return set(lss)



#print(decod('file03.txt','3533939339'))




