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
	listaprimi = []
	nuovalista = []
	'''Ciclo che controlla tutti i numeri presti in ls'''
	for numero in ls:
                '''Definisco una lista che conterrà i vari divisori di numero. Inoltre definisco variabile newnumero che conterrà il valore intero della radice quadrata del numero aumentato di l'''
                listadivisori = []
                newnumero=int(math.sqrt(numero)+1)
                '''
                Ciclo che parte dal 2 e arriva a newnumero. La radice quadrata viene utilizzata perché un numero può essere scomposto come una moltiplicazione tra due numeri se non è primo.
                Se uno dei fattori della moltiplicazione è minore della radice quadrata logicamente l'altro fattore dovrà essere maggiore della radice quadrata. E di conseguenza può essere calcolato dividendo il numero per il fattore
                noto (ecco perché la variabile secondodivisore). Con il primo if vengono calcolati tutti i divisori minori della radice, con il secondo, invece, quelli maggiori. Esempio: num = 10000 ----> sqrt(10000) = 100 ----> div1= 25 ---->
                secondodivisore = 10000/25 = 400 ---> div2 = 400 ----> div1*div2=num (num/div1 = div2 ---> num=div1*div2)
                '''
                for num in range(2,newnumero):
                        if numero%num ==0:
                                listadivisori.append(num)
                                listadivisori.append(numero//num)
                '''Escludo dalla lista dei valori tutti i valori uguali'''
                listadivisori = list(set(listadivisori))
                if len(listadivisori) == k:
                        nuovalista.append(numero)
                elif len(listadivisori) == 0:
                        listaprimi.append(numero)
	ls[:] = list(nuovalista)
	return listaprimi
                                
                           
