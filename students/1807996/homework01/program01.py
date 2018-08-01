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


from math import sqrt
def modi(ls,k):
    primi=[]
    #creo una copia della lista di input
    ld=ls[:]
    i=0
    g=0
    #ciclo i numeri della copia e modifico, a seconda dei controlli, la lista di input 
    for numero in (ld):
        #ciclo i numeri contenuti nell'intervallo che va da 2 alla radice quadrata del numero da studiare
        for x in range (2,int(sqrt(numero))+1):
            """se il modulo del n. sudiato per il n. ciclato è uguale a zero 
            e il ris della loro div. è diverso dal n. ciclato allora aggiungo 2 al contatore dei divisori,
            se il ris della loro div.è ugule al numero ciclato allora aggiungo 1 al contatore dei divisori"""
            if numero%x==0:
                if numero//x!=x:
                    g=g+2
                if numero//x==x: 
                    g=g+1
                if g>k:
                    break
        #se il contatore dei divisori è uguale a 0 concateno il numero studiato alla lista dei n. primi
        if g==0:
            if numero>1:
                primi+=[numero]
        #se il cont. dei div. è diverso dal n. richiesto, il numero studiato viene cancellato dalla lista
        if g!=k:
            ls[i:i+1]=[]
        else :
            i=i+1
        g=0
    return primi

