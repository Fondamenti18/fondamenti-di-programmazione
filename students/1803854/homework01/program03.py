
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
	'''
	Questa funzione di codifica prende in parametro una chiave e un testo. Tramite
	funzioni ausiliarie modifica la chiave e poi genera una corrispondenza biunivoca
	tra i caratteri della chiave modificata ordinata ed i caratteri della chiave modificata
	disordinata. Modifica quindi il testo tramite questa corrispondenza, e restituisce il testo cifrato.
	'''
	chiave = sviluppo_chiave(chiave)
	chiave_ord = ''.join(sorted(chiave))
	testo_new = ''
	diz = {chiave_ord[i]: chiave[i] for i in range(len(chiave))}
	for i in testo:
		if i in diz:
			i = diz[i]
			testo_new += i
		else:
			testo_new += i
			next
	return testo_new

def decodifica(chiave, testo):
	'''
	Questa funzione di decodifica prende in parametro una chiave e un testo cifrato. Tramite
	funzioni ausiliarie modifica la chiave e poi genera una corrispondenza biunivoca
	tra i caratteri della chiave modificata disordinata ed i caratteri della chiave modificataordinata.
	Modifica quindi il testo cifrato tramite questa corrispondenza, e restituisce il testo.
	'''
	chiave = sviluppo_chiave(chiave)
	chiave_ord = ''.join(sorted(chiave))
	testo_new = ''
	diz = {chiave[i]: chiave_ord[i] for i in range(len(chiave))}
	for i in testo:
		if i in diz:
			i = diz[i]
			testo_new += i
		else:
			testo_new += i
			next
	return testo_new
	
def sviluppo_chiave(chiave):
	'''
	Questa funzione impone la condizione che le lettere della chiave appartengano
	all'intervallo ASCII corrispondente alle lettere dell'alfabeto minuscole, dalla a alla z.
	Chiama poi la funzione cancella_occorrenze e restituisce la stringa modificata.
	'''
	chiave = ''.join([C for C in chiave if not (C < 'a' or C > 'z')])
	chiave = cancella_occorrenze(chiave)
	return chiave

def cancella_occorrenze(chiave):
	'''
	E' la funzione piu' interna al programma. Dispone di un algoritmo speciale che le permette
	di eliminare le occorrenze che si ripetono, come fanno le strutture dati conosciute come "insiemi".
	Tuttavia, a differenza degli insiemi, questa funzione restituisce una stringa che ha un disordine
	ben ordinato: ogni lettera che ricorre piu' di una volta viene cancellata, eccetto se la lettera
	in questione e' l'ultima delle occorrenze.
	'''
	chiave_nuova = ''
	for i in range(0, len(chiave)):
		if chiave[i] in chiave[i+1:]:
			next
		else:
			chiave_nuova += chiave[i]
	return chiave_nuova

if __name__ == '__main__':
	print(codifica('sim sala bim','sas'))