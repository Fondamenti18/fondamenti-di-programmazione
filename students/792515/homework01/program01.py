'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un intero 
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls = [121, 4, 37, 441, 7, 16] 
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine della funzione si avra' che la lista ls=[16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

import math

def modi(ls,k):
    "inserite qui il vostro codice"
    lsPrimi=[]
    lsRimuovi=[]
#faccio un ciclo su tutti gli elementi della lista in input...
    for i in range(len(ls)):
        GeneraDivPropri=False
        Dividendo=abs(ls[i])
        Divisore=2
        DivisoreMax=math.sqrt(abs(ls[i]))
        Passo=1
#...se il dividendo è pari divido per due e mi muovo di uno, altrimenti divido per tre e mi muovo di due...
        if Dividendo%2==0:
            Divisore=2
            Passo=1
        else:
            Divisore=3
            Passo=2
        Resto=0
        Quoziente=1
        lsDivPropri=[]
        lsDivPropri2=[]
#individuo i divisori propri con un primo ciclo di divisioni
        while Divisore<=DivisoreMax:
            Resto=Dividendo%Divisore
            Quoziente=Dividendo//Divisore
            if Resto==0 and Divisore<=DivisoreMax:
                if not Divisore in lsDivPropri and Divisore>1:
                    lsDivPropri=lsDivPropri+[Divisore]
                if not Quoziente in lsDivPropri and Quoziente>1:
                    lsDivPropri=lsDivPropri+[Quoziente]
                if not abs(ls[i])//Divisore in lsDivPropri and abs(ls[i])//Divisore>1 and abs(ls[i])//Divisore<abs(ls[i]):
                    lsDivPropri=lsDivPropri+[abs(ls[i])//Divisore]
                if not abs(ls[i])//Quoziente in lsDivPropri and abs(ls[i])//Quoziente>1 and abs(ls[i])//Quoziente<abs(ls[i]):
                    lsDivPropri=lsDivPropri+[abs(ls[i])//Quoziente]
                Dividendo=Quoziente
                if Dividendo==1:
                    Divisore=DivisoreMax+1
                if Dividendo%2==0:
                    Divisore=2
                    Passo=1
                else:
                    Divisore=3
                    Passo=2
            else:
                Divisore=Divisore+Passo
        lsDivPropri.sort()
#se la lista dei divisori propri è vuota vuol dire che ho trovato un numero primo, non ho bisogno di generare i divisori con i cicli di moltiplicazioni
        if len(lsDivPropri)==0:
            lsPrimi=lsPrimi+[ls[i]]
        else:
            GeneraDivPropri=True
#ricavo gli ulteriori divisori propri con un secondo ciclo di moltiplicazioni a partire dai divisori propri ricavati precedentemente
        Dividendo=abs(ls[i])
        while GeneraDivPropri==True:
            for j in range(len(lsDivPropri)):
                for z in range(len(lsDivPropri)):
                    Divisore=lsDivPropri[j]*lsDivPropri[z]
                    if Divisore>abs(ls[i])/2:
                        break
                    Resto=Dividendo%Divisore
                    Quoziente=Dividendo//Divisore
                    if Resto==0 and not Divisore in lsDivPropri and not Divisore in lsDivPropri2:
                        lsDivPropri2=lsDivPropri2+[Divisore]
# se alla fine dei cibli di moltiplicazioni non ho trovato ulteriori divisori, mi fermo
            if len(lsDivPropri2)==0:
                GeneraDivPropri=False
            else:
                lsDivPropri=lsDivPropri+lsDivPropri2
                lsDivPropri.sort()
                lsDivPropri2=[]
#Controllo che iln umero di divisori primi sia uguale a k, in caso contrario aggiorno la lista dei numeri da rimuovere
        if len(lsDivPropri)!=k:
            lsRimuovi=lsRimuovi+[ls[i]]
#rimuovo gli elementi che non hanno k divisori propri
    for i in range(len(lsRimuovi)):
        ls.remove(lsRimuovi[i])
    return lsPrimi