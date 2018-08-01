
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

def criptaChiave(chiave):
    ''' TALE FUNZIONE MI ESEGUE LE OPERAZIONI SULLA CHIAVE '''
    chiave=chiave.replace(' ','') # elimino gli spazi
    lista=[]#lista che contiene i caratteri della chiave
    for car in chiave: # lascio solo le lettere minuscole
        if car>='a' and car<='z': lista.append(car)
    for n in range(len(lista)-1,0,-1): #scorro la lista al contrario
        for i,c in enumerate(lista[:n]):
            if c==lista[n]: lista[i]='' #per ora non elimono niente, lo elimino alla riga successiva e insieme mi ricostruisco la stringa
    chiave=''.join(lista)
    return chiave

def criptaDecripta(testo,chiave,chiave2):
    ''' FUNZIONE CHE CRIPTA E DECRIPTAINSIEME '''
    testo2='' #testo criptato
    for car in testo: #scorro il testo
        flag=True
        for i in range(len(chiave2)): #confronto ogni lettera con la chiave
            if car==chiave2[i]:
                testo2+=chiave[i]
                flag=False
        if flag: testo2+=car
    return testo2

def codifica(chiave, testo):
    chiave=criptaChiave(chiave) # mi genero la chiave da usare per criptare
    chiave2=''.join(sorted(chiave))
    return criptaDecripta(testo,chiave,chiave2)


def decodifica(chiave, testo):
    chiave=criptaChiave(chiave) # mi genero la chiave da usare per criptare
    chiave2=''.join(sorted(chiave))
    return criptaDecripta(testo,chiave2,chiave)
