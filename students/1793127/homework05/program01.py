'''
Obiettivo dell'esercizio e' sviluppare la strategia di gioco per il gioco del Mastermind. 

Nel gioco del Mastermind un  giocatore (il "decodificatore"), deve indovinare un  codice segreto.
Il codice segreto e' di N cifre decimali distinte (NO RIPETIZIONI, solo 10 possibili simboli per ciascuna posizione).
Il decodificatore cerca di indovinare il codice per tentativi. Strategicamente  nel tentativo 
possono essere presenti anche cifre ripetute pur  sapendo che nel codice non sono presenti ripetizioni. 
In risposta ad  ogni tentativo viene fornito un aiuto producendo una coppia di interi (a,b) dove:

- a e' il numero di cifre giuste al posto giusto,
cioe' le cifre del codice da indovinare che sono effettivamente presenti nel tentativo al posto giusto.
- b e' il numero di cifre  giuste ma al posto sbagliato,
cioe' le cifre del codice da indovinare che sono effettivamente presenti nel tentativo solo al posto sbagliato.

Ad esempio per il codice
    34670915 e il tentativo
    93375948
la risposta deve essere la coppia (2,3).
Il 2 viene fuori dal contributo delle cifre 7 e 9 del codice da indovinare in quarta e sesta posizione,
il numero 2 e' dovuto alle cifre 3,4,5 che compaiono tra le cifre del tentativo ma mai al posto giusto.

Nella nostra versione di Mastermind il valore di N (lunghezza del codice) puo' essere 6, 7 o 8 e nella coppia data
in  risposta ai tentativi non si vuole rivelare quale delle due due cifre rappresenta il numero di  cifre giuste al posto giusto 
di conseguenza nella coppia di risposta  i valori di a e b possono risultare invertiti.
Ad esempio per il codice 34670915 e il tentativo 93375948 le risposte (2,3) e (3,2) sono entrambe possibili.


Una configurazione del  gioco viene rappresentata come lista di liste (L). 
Il primo elemento di L e' un intero N rappresentante la lunghezza del codice.
Ciascuno degli eventuali altri elementi di L rappresenta un tentativo fin qui
effettuato dal decodificatore e la relativa risposta.
Piu' precisamente  L[i] con i>0, se presente, conterra' una tupla composta da due elementi:
- la lista di N cifre  con il tentativo effettuato dal decodificatore in un qualche passo precedente
- la tupla di interi (a,b) ricevuta in risposta.


Il programma che dovete realizzare contiene la seguente funzione:
 
    decodificatore(configurazione)

che e' l'AI che guida il gioco. La funzione  riceve come input la configurazione attuale del gioco e produce un tentativo (lista di caratteri in '0-9').

Per questo esercizio la valutazione avverra' nel seguente modo: 
avete 150 tentativi e 30 secondi di tempo per indovinare quanti piu' codici possibile.
Il punteggio ottenuto e' dato dal numero di codici che riuscite ad indovinare.

Tutti i vostri elaborati al termine verranno valutati su di uno stesso set di codici,
questa operazione  determinera' una classifica dei vostri elaborati.
Per entrare in classifica bisogna indovinare almeno cinque codici.
La classifica viene suddivisa in 14 fasce che corrispondono ai voti da 18 a 31 ed a 
ciascun programma viene assegnato il voto corrispondente.
Se il numero di valori diversi e' minore di 14 il voto sara' proporzionale alla posizione
nella graduatoria (con il primo che prende 31 e l'ultimo 18)

In allegato vi viene fornito un  simulatore di gioco (simulatore1.py) che vi permettera' di 
autovalutare la vostra strategia. Il simulatore genera  codici casuali e invoca il vostro 
programma per ottenere i vari tentativi. Appena un codice  viene indovinato ne viene 
proposto uno nuovo. Il processo termina quando avete esaurito i vostri 150 tentativi
o sono passati  i 30 secondi.

ATTENZIONE: NON usate lettere accentate ne' nel codice ne' nei commenti
'''
from copy import deepcopy
terz1=[]
terz2=[]
quart1=[]
quart2=[]
M=0
N=0
T=0
A=0
p1=[]
p2=[]
def decodificatore(configurazione):
	global terz1
	global terz2
	global quart1
	global quart2
	global M
	global N
	global T
	global A
	global p1
	global p2
	lst=[]
	cont=len(configurazione)
	if cont==1:
		terz1=[]
		terz2=[]
		quart1=[]
		quart2=[]
		M=0
		N=0
		T=1
		A=0
		p1=[]
		p2=[]
	l=configurazione[0]
	if cont<11 and(cont==1 or configurazione[cont-1][1]==(0,0)):
		for i in range(l):
			lst.append(cont-1)
	elif cont<11:
		lst=deepcopy(configurazione[cont-1][0])
		for i in range(l):
			if i>=(l//2):
				lst[i]=cont-1
	elif cont==11:
		i=0
		quart0=[]
		quart1=[]
		quart2=[]
		for x in configurazione:
			if i!=0:
				if configurazione[i][1]==(0,0):
					quart0.append(i-1)
				elif (configurazione[i][1]==(0,1) or configurazione[i][1]==(1,0)) and quart1==[]:
					quart1.append(i-1)
				elif configurazione[i][1]==(1,1):
					quart1.append(i-1)
				elif (configurazione[i][1]==(0,2) or configurazione[i][1]==(2,0)):
					quart2.append(i-1)
				elif (configurazione[i][1]==(0,1) or configurazione[i][1]==(1,0)) and quart1!=[]:
					quart0.append(i-1)
			i+=1
		configurazione.append(quart0)
		configurazione.append(quart1)
		configurazione.append(quart2)
		lst=configurazione[12]+configurazione[13]
		p1=configurazione[12]
		p2=configurazione[13]
	elif (cont==15 and (configurazione[14][1]==(0,l) or configurazione[14][1]==(l,0))) or (cont==15 and l==7 and (configurazione[14][1]==(1,6) or configurazione[14][1]==(6,1))):
		lst=configurazione[13]+configurazione[12]
		p1=configurazione[13]
		p2=configurazione[12]
	elif (cont==16 and (configurazione[15][1]==(0,l) or configurazione[15][1]==(l,0))) or (cont==16 and l==7 and (configurazione[15][1]==(1,6) or configurazione[15][1]==(6,1))):
		l1=trasl_list(configurazione[13])
		l2=trasl_list(configurazione[12])
		p1=l1
		p2=l2
		lst=l1+l2
	elif (cont==17 and (configurazione[16][1]==(0,l) or configurazione[16][1]==(l,0))) or (cont==17 and l==7 and (configurazione[16][1]==(1,6) or configurazione[16][1]==(6,1))):
		l1=trasl_list(configurazione[12])
		l2=trasl_list(configurazione[13])
		p1=l1
		p2=l2
		lst=l1+l2
	elif (cont==18 and (configurazione[17][1]==(0,l) or configurazione[17][1]==(l,0))) or (cont==18 and l==7 and (configurazione[17][1]==(1,6) or configurazione[17][1]==(6,1))):
		l1=trasl_list(configurazione[13])
		l2=trasl_list(configurazione[12])
		l3=trasl_list(l1)
		l4=trasl_list(l2)
		p1=l3
		p2=l4
		lst=l3+l4
	elif (cont==19 and (configurazione[18][1]==(0,l) or configurazione[18][1]==(l,0))) or (cont==19 and l==7 and (configurazione[18][1]==(1,6) or configurazione[18][1]==(6,1))):
		l1=trasl_list(configurazione[12])
		l2=trasl_list(configurazione[13])
		l3=trasl_list(l1)
		l4=trasl_list(l2)
		p1=l3
		p2=l4
		lst=l3+l4
	elif (cont==20 and (configurazione[19][1]==(0,l) or configurazione[19][1]==(l,0))) or (cont==20 and l==7 and (configurazione[19][1]==(1,6) or configurazione[19][1]==(6,1))):
		l1=trasl_list(configurazione[13])
		l2=trasl_list(configurazione[12])
		l3=trasl_list(l1)
		l4=trasl_list(l2)
		l5=trasl_list(l3)
		l6=trasl_list(l4)
		p1=l5
		p2=l6
		lst=l5+l6
	elif (cont==21 and (configurazione[20][1]==(0,l) or configurazione[20][1]==(l,0))) or (cont==21 and l==7 and (configurazione[20][1]==(1,6) or configurazione[20][1]==(6,1))):
		l1=trasl_list(configurazione[12])
		l2=trasl_list(configurazione[13])
		l3=trasl_list(l1)
		l4=trasl_list(l2)
		l5=trasl_list(l3)
		l6=trasl_list(l4)
		p1=l5
		p2=l6
		lst=l5+l6
	elif (configurazione[cont-1][1]!=(0,l) or configurazione[cont-1][1]!=(l,0)) and cont<23:
		while len(configurazione)!=23:
			configurazione.append((configurazione[cont-1][0],configurazione[cont-1][1]))
		lst=deepcopy(configurazione[cont-1][0])
		for x in range(l):
			lst[x]=configurazione[11][0]
		i=0
		j=0
		for x in lst:
			if x==configurazione[11][0] and j==l-1:
				lst[j]=configurazione[cont-1][0][1]
				i+=1
			if x==configurazione[11][0] and i==0:
				lst[j]=configurazione[cont-1][0][0]
				i+=1
			j+=1
		N=2
		T=1
		M=1
		A=0
	elif (configurazione[cont-1][1]==(0,N) or configurazione[cont-1][1]==(N,0)) and M<len(p1)-T and A==0:
		lst=spost_cifr_list(configurazione[cont-1][0],p1[0],configurazione[11][0])
		M+=1
	elif (configurazione[cont-1][1]==(1,N-1) or configurazione[cont-1][1]==(N-1,1)) and A==0:
		M=1
		T+=1
		A+=1
		lst=deepcopy(configurazione[cont-1][0])
		i=0
		j=0
		for x in lst:
			if x==configurazione[11][0] and i==0:
				lst[j]=p1[1]
				i+=1
			if j==l-1:
				lst[j]=configurazione[11][0]
			j+=1
	elif (M==len(p1)-T) and A==0:
		lst=spost_cifr_list(configurazione[cont-1][0],p1[0],configurazione[11][0])
		M=1
		T+=1
		A+=1
		i=0
		j=0
		for x in lst:
			if x==configurazione[11][0] and i==0:
				lst[j]=p1[1]
				i+=1
			if j==l-1:
				lst[j]=configurazione[11][0]
			j+=1
	elif (configurazione[cont-1][1]==(1,N-1) or configurazione[cont-1][1]==(N-1,1)) and M<len(p1)-T and A==1:
		lst=spost_cifr_list(configurazione[cont-1][0],p1[1],configurazione[11][0])
		M+=1
	elif (configurazione[cont-1][1]==(0,N) or configurazione[cont-1][1]==(N,0)) and A==1:
		N+=1
		M=1
		T+=1
		A+=1
		lst=deepcopy(configurazione[cont-1][0])
		i=0
		j=0
		for x in lst:
			if x==configurazione[11][0] and i==0:
				lst[j]=p1[2]
				i+=1
			j+=1
		if len(p1)==3:
			T=1
			N+=1
			A=3
			i=0
			j=0
			for x in lst:
				if x==configurazione[11][0] and i==0:
					lst[j]=p2[0]
					i+=1		
				j+=1
	elif (M==len(p1)-T) and A==1:
		lst=spost_cifr_list(configurazione[cont-1][0],p1[1],configurazione[11][0])
		N+=1
		M=1
		T+=1
		A+=1
		i=0
		j=0
		for x in lst:
			if x==configurazione[11][0] and i==0:
				lst[j]=p1[2]
				i+=1
			j+=1
		if len(p1)==3:
			T=1
			N+=1
			A=3
			i=0
			j=0
			for x in lst:
				if x==configurazione[11][0] and i==0:
					lst[j]=p2[0]
					i+=1		
				j+=1
	elif (configurazione[cont-1][1]==(1,N-1) or configurazione[cont-1][1]==(N-1,1)) and M<len(p1)-T and A==2:
		lst=spost_cifr_list(configurazione[cont-1][0],p1[2],configurazione[11][0])
		M+=1
	elif (configurazione[cont-1][1]==(0,N) or configurazione[cont-1][1]==(N,0)) and A==2:
		N+=2
		M=1
		T=1
		A+=1
		lst=deepcopy(configurazione[cont-1][0])
		i=0
		j=0
		for x in lst:
			if x==configurazione[11][0] and i==0:
				lst[j]=p1[3]
				i+=1
			j+=1
		i=0
		j=0
		for x in lst:
			if x==configurazione[11][0] and i==0:
				lst[j]=p2[0]
				i+=1		
			j+=1
	elif (M==len(p1)-T) and A==2:
		lst=spost_cifr_list(configurazione[cont-1][0],p1[2],configurazione[11][0])
		N+=2
		M=1
		T=1
		A+=1
		i=0
		j=0
		for x in lst:
			if x==configurazione[11][0] and i==0:
				lst[j]=p1[3]
				i+=1
			j+=1
		i=0
		j=0
		for x in lst:
			if x==configurazione[11][0] and i==0:
				lst[j]=p2[0]
				i+=1		
			j+=1
	elif (configurazione[cont-1][1]==(1,N-1) or configurazione[cont-1][1]==(N-1,1)) and M<len(p2)-T and A==3:
		lst=spost_cifr_list(configurazione[cont-1][0],p2[0],configurazione[11][0])
		M+=1
	elif (configurazione[cont-1][1]==(0,N) or configurazione[cont-1][1]==(N,0)) and A==3:
		M=1
		N+=1
		T+=1
		A+=1
		lst=deepcopy(configurazione[cont-1][0])
		i=0
		j=0
		for x in lst:
			if x==configurazione[11][0] and i==0:
				lst[j]=p2[1]
				i+=1
			j+=1
	elif (M==len(p2)-T) and A==3:
		lst=spost_cifr_list(configurazione[cont-1][0],p2[0],configurazione[11][0])
		M=1
		N+=1
		T+=1
		A+=1
		i=0
		j=0
		for x in lst:
			if x==configurazione[11][0] and i==0:
				lst[j]=p2[1]
				i+=1
			j+=1
	elif (configurazione[cont-1][1]==(1,N-1) or configurazione[cont-1][1]==(N-1,1)) and M<len(p2)-T and A==4:
		lst=spost_cifr_list(configurazione[cont-1][0],p2[1],configurazione[11][0])
		M+=1
	elif (configurazione[cont-1][1]==(0,N) or configurazione[cont-1][1]==(N,0)) and A==4:
		N+=1
		M=1
		T+=1
		A+=1
		lst=deepcopy(configurazione[cont-1][0])
		i=0
		j=0
		for x in lst:
			if x==configurazione[11][0] and i==0:
				lst[j]=p2[2]
				i+=1
			j+=1
	elif (M==len(p2)-T) and A==4:
		lst=spost_cifr_list(configurazione[cont-1][0],p2[1],configurazione[11][0])
		N+=1
		M=1
		T+=1
		A+=1
		i=0
		j=0
		for x in lst:
			if x==configurazione[11][0] and i==0:
				lst[j]=p2[2]
				i+=1
			j+=1
	elif (configurazione[cont-1][1]==(1,N-1) or configurazione[cont-1][1]==(N-1,1)) and M<len(p2)-T and A==5:
		lst=spost_cifr_list(configurazione[cont-1][0],p2[2],configurazione[11][0])
		M+=1
	elif (configurazione[cont-1][1]==(0,N) or configurazione[cont-1][1]==(N,0)) and A==5:
		N+=1
		M=1
		T=1
		A+=1
		lst=deepcopy(configurazione[cont-1][0])
		i=0
		j=0
		for x in lst:
			if x==configurazione[11][0] and i==0:
				lst[j]=p2[3]
				i+=1
			j+=1
	elif (M==len(p2)-T) and A==5:
		lst=spost_cifr_list(configurazione[cont-1][0],p2[2],configurazione[11][0])
		N+=1
		M=1
		T=1
		A+=1
		i=0
		j=0
		for x in lst:
			if x==configurazione[11][0] and i==0:
				lst[j]=p2[3]
				i+=1
			j+=1
	return lst

def trasl_list(l):
	lout=deepcopy(l)
	i=0
	for x in l:
		if i==(len(l)-1):
			lout[0]=x
		else:
			lout[i+1]=x
		i+=1
	return lout
	
def spost_cifr_list(l,n,p):
	lout=deepcopy(l)
	i=0
	j=0
	bol=False
	for x in l:
		if x==n:
			while lout[i+j]!=p and i+j<(len(lout)-1) and bol==False:
				if lout[i+j+1]==p:
					lout[i+j+1]=n
					lout[i]=p
					bol=True
				j+=1
		i+=1
	return lout