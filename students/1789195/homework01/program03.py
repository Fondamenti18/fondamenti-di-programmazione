
'''Dato un testo da codificare ed una chiave si propone il seguente schema crittografico:

- dalla chiave vengono eliminati  tutti i caratteri C per cui C<'a' o C>'z'. 
- di ciascuno dei caratteri restanti vengono cancellate dalla chiave tutte le occorrenze 
  tranne l'ultima, ottenendo una sequenza DISORDINATA. 
- i caratteri presenti nella stringa cosi' ripulita saranno i soli caratteri del testo 
  ad essere codificati ovvero sostituiti nel testo crittografato (gli altri resteranno invariati). 
- la sequenza ORDINATA dei caratteri rimasti nella chiave viene messa in corrispondenza 
  con la sequenza DISORDINATA dei caratteri ottenuti al passo precedente.

Come esempio di applicazione  consideriamo la chiave
 "sim sala Bim!"
a seguito delle eliminazioni la chiave produce la sequenza DISORDINATA
 "slaim"
 
I soli caratteri del testo  a subire una codifica sarano 's','l', 'a' 'i' ed 'm'. 
Per sapere con cosa verranno codificati questi caratteri si considera la seguente corrispondenza
tra sequenze:
    "ailms" (sequenza ordinata degli stessi caratteri)
    "slaim" (sequenza disordinata ottenuta dalla chiave)
questo determina gli accoppiamenti (a,s), (i,l) (l,a), (m,i) ed (s,m)
la 'a' dunque sara' codificata con 's', la 'i' con 'l' e cosi' via.

Utilizzando la chiave "sim sala Bim!" per codificare il testo  "il mare sa di sale" si 
 otterra' il seguente testo crittografato:
    "il mare sa di sale"   (testo in chiaro)
    "la isre ms dl msae"   (testo crittografato)

La decodifica del testo crittografato opera sulla stessa chive ma sostituisce le lettere
presenti nella sequenza disordinata con quelle della sequenza ordinata.
Quindi nell'esempio precedente le sostituzioni sono invertite:
 (s, a), (l, i) (a, l), (i, m) ed (m, s)

Per altri esempi vedere il file grade03.txt

Implementate le due funzioni
    codifica(chiave, testo_in_chiaro) -> testo_crittografato
    decodifica(chiave, testo_crittografato) -> testo_in_chiaro

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

def codifica(chiave, testo):
	listaDisordinata=eliminaMaiuscole(chiave.replace(' ',''))	#richiama funzione eliminaMaiuscole passandogli come valore la chiave senza spazi vuoti
	listaOrdinata=sorted(listaDisordinata)	#ordina listaDisordinata
	diz={}	#dizionario
	i=0	#incremento
	for j in range(0, len(listaOrdinata)):
		for carattereOrdinata in listaOrdinata[i]:	#scorri listaOrdinata indice i
			for carattereDisordinata in listaDisordinata[i]:	#scorri listaDisordinata indice i
				diz[carattereOrdinata]=carattereDisordinata	#aggiunge al dizionario com chiave il valore carattereOrdinata e come valore il carattereDisordinata	
				i+=1	
		j+=1
	lst=[]	#lista
	for carattere in testo:	#scorre il testo
		if(carattere in diz):	#se trova un carattere che è presente anche nel dizionario
			lst.append(diz[carattere])	#aggiunge alla lista il valore contenuto nella chiave corrispondente al carattere
		else:
			lst.append(carattere)	#aggiunge alla lista il carattere stesso del testo
	testo=''.join(lst)	#converte lista in stringa
	return(testo)
			
def decodifica(chiave, testo):
	listaDisordinata=eliminaMaiuscole(chiave.replace(' ',''))	#richiama funzione eliminaMaiuscole passandogli come valore la chiave senza spazi vuoti
	listaOrdinata=sorted(listaDisordinata)	#ordina listaDisordinata
	diz={}
	i=0
	for j in range(0, len(listaOrdinata)):
		for carattereDisordinata in listaDisordinata[i]:
			for carattereOrdinata in listaOrdinata[i]:
				diz[carattereDisordinata]=carattereOrdinata
				i+=1
		j+=1
	lst=[]
	for carattere in testo:
		if(carattere in diz):
			lst.append(diz[carattere])
		else:
			lst.append(carattere)
	testo=''.join(lst)
	return(testo)
	
def eliminaMaiuscole(stringa):
	for carattere in stringa:	#scorre stringa
		if(carattere == carattere.upper()):	#se il carattere è uguale al carattere stesso maiuscolo
			stringa=stringa.replace(carattere,'')	#elimina carattere
	strChiave=eliminaOccorrenze(stringa)	#richiama funzione eliminaOccorrenze
	return(strChiave)	#ritorna valore alla funzione codifica
	
def eliminaOccorrenze(stringa):
	lst=[]	#lista
	for carattere in stringa:	#scorre stringa
		lst.append(carattere)	#aggiunge carattere stringa nella lista
	for indice in lst[::-1]:	#scorre lista al contrario
		if(lst.count(indice) > 1):	#se il numero di occorrenze del carattere nella stringa è maggiore di 1
			lst.remove(indice)	#rimuovi dalla lista le prime occorrenze		
	return(lst)	#ritorna lista alla funzione eliminaMaiuscole
	
if __name__ == '__main__':	
	print(codifica('abracadabra', 'abracadabra'))