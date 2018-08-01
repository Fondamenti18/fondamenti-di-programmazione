
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
	seD=crypto(chiave)[0]		#sequenza Disordinata#
	seO=crypto(chiave)[-1]		#sequenza Ordinata#
	
	
	return critt(testo,seO,seD)	# ritorno con chiamata della funzione che permette la codifica del testo #
	
    


def decodifica(chiave, testo):
	seD=crypto(chiave)[0]		#sequenza Disordinata#
	seO=crypto(chiave)[-1]		#sequenza Ordinata#
	return unicript(testo,seO,seD)	# ritorno con chiama della funzione che permette di decifrare il testo #

	
def crypto(chiave):
	seO=''		#stringa sequenza ordinata#
	seD=''		#stringa sequenza disordinata#
	sein=''		#stringa intermedia tra l'ordinata e disordinata#
	lst=[]		#lista vuota per riordinamento alfabetico sequenza disordinata con comando sorted#
	nseoc=''	#stringa sequenza disordinata ordinata alfabeticamente#
	
	#ciclo for per verificare condizione in cui vengono eliminate le lettere C <'a' or C >'z' #
	
	for i in range(0,len(chiave)):
		if not(chiave[i] < 'a' or chiave[i] > 'z'):	#if not variavile logica, se non vero allora esegui istruzione #
			seO=seO+chiave[i]
	
	# controllo se la chiave è una codifica debole #	
	
	if seO == '':
		return seO,seD
			
			
	#ciclo for per l'eliminazione delle occorrenze (parte dall'ultima lettere)#
	
	for i in range(len(seO),-1,-1):
		if seO[i-1] not in sein:	#if not in varivale logica, se la lettera Ordinata non è nella variavile intermedia inseriscila#
			sein=sein+seO[i-1]
	
	#ciclo for per la 'ordinare' la sequenza disordinata che verra usata come indice di cambio delle lettere(anche questo ciclo parte dall'ultima lettera)#
	
	for i in range(len(sein),0,-1):
		seD=seD+sein[i-1]
	
	#uso comando sorted per ordinare alfabeticamente la sequenza disordinata#
	lst=sorted(seD)
	
	#ciclo for per assegnare a variabile nseoc la sequenza disordinata ordinata alfabeticamente per la corrispondeza delle lettere da cambiare#
	
	for i in range(0,len(lst)):
		nseoc=nseoc+str(lst[i])
		
	return seD, nseoc
	
# funzione che permette di codificare il testo #	
def critt(testo,seO,seD):
	parola=''	# variabile che verra' usata per il risultato #
	for i in range(0,len(testo)):	# ciclo for per lavorare singolarmente su ogni lettera del testo #
		if testo[i] in seO:			# controllo se la lettera da lavorare si trova nella sequenza ordinata #
			for j in range(0,len(seO)): # ciclo for che verra' utulizzato per trovare la lettera da cambiare #
				if testo[i] == seO[j]:	# controllo e ricerca della lettera da cambiare, l'indice 'j' indichera' la lettera nella sequenza Disordinata#
					parola=parola+seD[j]	# sostituizione della lettera del testo con la lettera codificata #
		else:	# se la lettera non è nella sequenza Ordinata non verra' modificata #
			parola=parola+testo[i]
	return parola

# funzione che permette la decodificazione del testo, stesso funzionamento con l'unica modifica il cambio del controllo con la sequenza Ordinata/Disordinata#	
def unicript(testo,seO,seD):
	parola=''
	for i in range(0,len(testo)):
		if testo[i] in seO:
			for j in range(0,len(seD)):
				if testo[i] == seD[j]:
					parola=parola+seO[j]
		else:
			parola=parola+testo[i]
	return parola
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	