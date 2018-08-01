'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un intero 
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls = [121, 4, 37, 441, 7, 16] 
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine della funzione si avra' che la lista ls=[441,16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''
import math
   
def modi(ls,k):
    N_primi=[]
    Ls_divisori=[]
    divisori_mancanti=[]
    rimozzione=[]
    for i in ls:
        count=0
        Ls_divisori=divisori(i)
        if Ls_divisori[0]==i:
            N_primi=N_primi+[Ls_divisori[0]]
        divisori_mancanti=DivisoriMancanti(Ls_divisori)
        if i in divisori_mancanti:
            divisori_mancanti.remove(i)
        for speciali in divisori_mancanti:
             if i//speciali not in divisori_mancanti:
                  divisori_mancanti=divisori_mancanti+[i//speciali]		 
        for x in divisori_mancanti:
            count=count+1
        if count==k:
            rimozzione=rimozzione+[i]

    ls[:]=rimozzione
    return N_primi

def DivisoriMancanti2(lsDiv):
	ls3=[]
	for op1 in range(len(lsDiv)-1):
		for op2 in range(op1+1,len(lsDiv)):
			if(lsDiv[op2]%lsDiv[op1])!=0:
				ls3=ls3+[lsDiv[op1]*lsDiv[op2]]
	lsDiv=lsDiv+ls3	
	lsDiv.sort()	
	return lsDiv

def DivisoriMancanti(lsDiv):
	ls3=[]
	check=0
	for x in lsDiv:		
		if lsDiv.count(x)>1 and x!=check:
			for b in range(1,lsDiv.count(x)+1):				
				ls3=ls3+[x**b]
			check=x
	lsDiv=lsDiv+ls3
	lsDiv=list(set(lsDiv))
	lsDiv.sort()	
	return DivisoriMancanti2(lsDiv)

def divisori(numero):
	divisore=3
	if(numero%2)==0 and numero//2>1:
		return [2]+divisori(numero//2)
	while(int(math.sqrt(numero))>=divisore):
		if (numero%divisore)==0:
			return [divisore]+divisori(numero//divisore)
		divisore=divisore+2
	return [numero]


        
