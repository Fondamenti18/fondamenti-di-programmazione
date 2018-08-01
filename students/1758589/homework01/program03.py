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

La decodifica del testo crittografato opera sulla stessa chiave ma sostituisce le lettere
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
def elimina_occ(string):
    l_no_occ = []
    for i in range(len(string)-1,-1,-1):
        if string[i] not in l_no_occ:
            l_no_occ.insert(0,string[i])
    return l_no_occ

def costruzione_chiave(stringa):
    strminuscolo = ''
    for c in stringa:
        if ('a' <= c <= 'z') and c.isalpha():
            strminuscolo += c
    listaD = list(strminuscolo)
    listaDISORDINATA = elimina_occ(listaD)
    return listaDISORDINATA

def codifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    disordinata = costruzione_chiave(chiave)
    ordinata = sorted(disordinata)
    testo_in_chiaro = list(testo)

    testo_crittografato = []
    for e in testo_in_chiaro:
        if e in ordinata:
            indice = ordinata.index(e)
            e = disordinata[indice]
            testo_crittografato += [e]
        else:
            testo_crittografato += [e]
    testo_crittografato = ''.join(testo_crittografato)
    return testo_crittografato


def decodifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    disordinata = costruzione_chiave(chiave)
    ordinata = sorted(disordinata)
    testo_crittografato = list(testo)

    testo_in_chiaro = []
    for e in testo_crittografato:
        if e in disordinata:
            indice = disordinata.index(e)
            e = ordinata[indice]
            testo_in_chiaro += [e]
        else:
            testo_in_chiaro += [e]
    testo_in_chiaro = ''.join(testo_in_chiaro)
    return testo_in_chiaro
