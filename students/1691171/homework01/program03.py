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


def rimuovi_duplicati(orig):
    ris = orig[:]
    k = 0
    while k < len(ris):
        pos = 0
        i = 0
        while i < len(ris):
            if ris[i] == ris[k]:
                c = ris[i]
                pos = i
            i += 1
        # ho trovato la posizione dell'ultimo, quindi tolgo tutti quelli uguali a c in altre posizioni
        j = 0
        copia = ris[:]
        ris = ''
        while j < len(copia):
            if pos == j or copia[j] != copia[k]:
                ris += copia[j]
            j += 1
        k += 1
    return ris


def ripulisci_chiave(chiave):
    pulita = ''
    for c in chiave:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            pulita += c
        pulita = rimuovi_duplicati(pulita)
    return pulita


def codifica(chiave, testo):
    disordinata = ripulisci_chiave(chiave)
    ordinata = ''.join(sorted(disordinata))
    corrispondenze = {}
    i = 0
    while i < len(ordinata):
        corrispondenze[ordinata[i]] = disordinata[i]
        i += 1

    ris = ''
    i = 0
    while i < len(testo):
        if testo[i] in corrispondenze.keys():
            ris += corrispondenze[testo[i]]
        else:
            ris += testo[i]
        i += 1

    return ris


def decodifica(chiave, testo):
    disordinata = ripulisci_chiave(chiave)
    ordinata = ''.join(sorted(disordinata))
    corrispondenze = {}
    i = 0
    while i < len(ordinata):
        corrispondenze[disordinata[i]] = ordinata[i]
        i += 1

    ris = ''
    i = 0
    while i < len(testo):
        if testo[i] in corrispondenze.keys():
            ris += corrispondenze[testo[i]]
        else:
            ris += testo[i]
        i += 1

    return ris
