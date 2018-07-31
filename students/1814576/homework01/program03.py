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
def calcolochiave(chiave):
	chiave=[C for C in chiave if C>='a' and C<='z']
	#per avere la chiave disordinata ma con tutte le occorrenze

	chiavedis=[]
	chiaveord=[]
	
	c=0
	#for per eliminare le occorrenze nella chiave
	for i in chiave:
		if i not in chiave[c+1:]:
			chiavedis+=[i]
		c+=1

	chiaveord=sorted(chiavedis) 
	#per avere la chiave ordinata
	
	return chiavedis,chiaveord
	
def codifica(chiave, testo):
	'''inserire qui la vostra implementazione'''
	codifica=''

	chiavedis,chiaveord=calcolochiave(chiave)

	rel=list(zip(chiaveord,chiavedis)) 
	#con la funzione zip ottengo una lista di tuple, che mi garantisce un'ottima relazione tra le due chiavi
	#e lavorerò nella lista rel come se fosse una matrice con doppi indici
	
	j=0
	for a in testo:
		cont=False
		j=0
		while j<len(rel):
			if a==rel[j][0]:
					codifica+=rel[j][1] 
					#il secondo indice è solo 0 o 1, essendo per logica una matrice di due colonne
					cont=True
					break 
					#essendo carattere per carattere il controllo viene effettuato uno alla volta. Appena lo trova nella chiave non ha senso
					#continuare il ciclo
			else:
				j+=1 
				#scorre le righe
		if cont==False: 
			#se non sono stati trovati collegamenti tra il carattere del testo originale, si scrive il carattere che non può essere cifrato
			codifica+=a

	return codifica
	

def decodifica(chiave, testo):
	'''inserire qui la vostra implementazione'''
	decodifica=''
	
	chiavedis,chiaveord=calcolochiave(chiave)
	
	rel=list(zip(chiavedis,chiaveord))
	#il calcolo delle chiavi è identico per le due funzioni, mentre la creazione della matrice è invertita per la decodifica
	
	j=0
	for a in testo:
		cont=False
		j=0
		while j<len(rel):
			if a==rel[j][0]:
					decodifica+=rel[j][1]
					cont=True
					break
			else:
				j+=1
		if cont==False:
			decodifica+=a

	return decodifica