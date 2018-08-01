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
'''


def decod(pfile, codice):
	lstCod=convCodice(codice)
	lstPar=[]
	lstTesto=[]
	diz={}
	insi=[]
	lstDef=[]
	variabile=''
	with open(pfile, mode='rt', encoding='utf-8') as f:
		for parola in f:
			lstPar=convParola(parola)
			lstTesto=convTesto(parola)
			if(len(lstCod)==len(lstPar)):
				diz=assegnazioneValore(lstCod, lstPar)
				for cifra in codice:
					lstDef+=(diz[cifra])
				if(lstDef==lstTesto):
					insi.append(''.join(lstDef))
			lstDef=[]
			lstTesto=[]
			diz.clear()
	return(set(insi))
	
def convCodice(codice):
	lstCodice=[]
	for cifra in codice:
		lstCodice.append(cifra)
	for cifra in lstCodice[::-1]:
		if(lstCodice.count(cifra)>1):
			lstCodice.remove(cifra)
	return(lstCodice)
	
def convTesto(testo):
	lstTesto=[]
	for carattere in testo:
		if not carattere.isalpha():
			testo=testo.replace(carattere,'')
	for lettera in testo:
		lstTesto.append(lettera.lower())

	return(lstTesto)
	
def convParola(testo):
	lstParola=[]
	for carattere in testo:
		if not carattere.isalpha():
			testo=testo.replace(carattere,'')
	for lettera in testo:
		lstParola.append(lettera.lower())
	for lettera in lstParola[::-1]:
		if(lstParola.count(lettera)>1):
			lstParola.remove(lettera)
	return(lstParola)
	
def assegnazioneValore(codice, parola):
	dizionario={}
	i=0
	while(i<len(parola)):
		for cifra in codice:
			dizionario[cifra]=[parola[i]]
			i+=1
	return(dizionario)

if __name__ == '__main__':  
	print(decod('file03.txt','121'))




