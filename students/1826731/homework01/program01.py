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

def modi(ls,k):
    def propri(n):
        """Calcola quanti divisori propri ha un numero"""
        FattoriPrimi = []
        c1 = 2
        while n != 1:
            c2 = c1
            while n % c2 == 0:
                n = n // c2
                FattoriPrimi.append(c2)
            c1 = c2 + 1
        NDivisori = 1
        while len(FattoriPrimi)!= 0:
            for x in FattoriPrimi:
                NVolte = 0
                while x in FattoriPrimi:
                    NVolte = NVolte + 1
                    FattoriPrimi.remove(x)
                NDivisori = NDivisori * (NVolte + 1)
        return NDivisori - 2
    
    ListaCopia = ls.copy()
    NumPrimi = []
    for x in ListaCopia:
        NPropri = propri(x)
        if NPropri > 0 and NPropri != k:
            ls.remove(x)
        elif NPropri == 0:
            ls.remove(x)
            NumPrimi.append(x)            
    return NumPrimi
