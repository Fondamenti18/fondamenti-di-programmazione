
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

def codifica(chiave, clearphrase):
    cryptphrase = ''
    newC = ''
    c = 0                                   #
    c1 = 0                                  #
    c2 = 0                                  #
    chars = 0                               # Posizione del carattare di clearphrase
    k = key(chiave)
    # Per ogni lettera della frase in chiaro
    for elem in range(len(clearphrase)):

        # Se la lettera della frase in chiaro non è una lettera presente nella chiave
        if clearphrase[elem] not in k.values():
            # Concatenala alla stringa della Frase Criptata senza eseguire la criptazione
            cryptphrase = str(cryptphrase + clearphrase[elem])

        # Altrimenti esegui la criptazione
        else:
            cryptphrase = str(cryptphrase + k[clearphrase[elem]])
            
    return cryptphrase
        

def key(chiave):
    lKey = []
    lKeyc = []
    k = {}
    for lettera in chiave:            
        if ord(lettera)>=ord('a') and ord(lettera)<=ord('z'):
            lKey.append(lettera)
    for lettera in lKey:
        if lKey.count(lettera)>1 and lettera not in lKeyc:
            for i in range(lKey.count(lettera)-1):
                lKeyc.append(lettera)
    for lettera in lKeyc:
        lKey.remove(lettera)
    lKeyc = lKey.copy()
    lKey.sort()
    for i in range(0,len(lKey)):
        k[lKey[i]] = lKeyc[i]
    return k

#le chiavi diventano i valori e i valori diventano le chiavi
def reverse(dictionary):
    reverseDiz = {}
    for key in dictionary:
        reverseDiz[dictionary[key]] = key
    return reverseDiz


def decodifica(chiave, clearphrase):
    cryptphrase = ''
    newC = ''
    c = 0                                   #
    c1 = 0                                  #
    c2 = 0                                  #
    chars = 0                               # Posizione del carattare di clearphrase
    k = reverse(key(chiave))
    # Per ogni lettera della frase in chiaro
    for elem in range(len(clearphrase)):

        # Se la lettera della frase in chiaro non è una lettera presente nella chiave
        if clearphrase[elem] not in k.values():
            # Concatenala alla stringa della Frase Criptata senza eseguire la criptazione
            cryptphrase = str(cryptphrase + clearphrase[elem])

        # Altrimenti esegui la criptazione
        else:
            cryptphrase = str(cryptphrase + k[clearphrase[elem]])
            
    return cryptphrase




