
'''Dato un testo da codificare ed una chiave si propone il seguente schema crittografico:

- dalla chiave vengono eliminati  tutti i caratteri C per cui C<'a' o C>'z'. 
- di ciascuno dei caratteri restanti vengono cancellate dalla chiave tutte le occorrenze 
  tranne l'ultima, ottenendo una sequenza disordinati. 
- i caratteri presenti nella stringa cosi' ripulita saranno i soli caratteri del testo 
  ad essere codificati ovvero sostituiti nel testo crittografato (gli altri resteranno invariati). 
- la sequenza ORDINATA dei caratteri rimasti nella chiave viene messa in corrispondenza 
  con la sequenza disordinati dei caratteri ottenuti al passo precedente.

Come esempio di applicazione  consideriamo la chiave
 "sim sala Bim!"
a seguito delle eliminazioni la chiave produce la sequenza disordinati
 "slaim"
 
I soli caratteri del testo  a subire una codifica sarano 's','l', 'a' 'i' ed 'm'. 
Per sapere con cosa verranno codificati questi caratteri si considera la seguente corrispondenza
tra sequenze:
    "ailms" (sequenza ordinata degli stessi caratteri)
    "slaim" (sequenza disordinati ottenuta dalla chiave)
questo determina gli accoppiamenti (a,s), (i,l) (l,a), (m,i) ed (s,m)
la 'a' dunque sara' codificata con 's', la 'i' con 'l' e cosi' via.

Utilizzando la chiave "sim sala Bim!" per codificare il testo  "il mare sa di sale" si 
 otterra' il seguente testo crittografato:
    "il mare sa di sale"   (testo in chiaro)
    "la isre ms dl msae"   (testo crittografato)

La decodifica del testo crittografato opera sulla stessa chive ma sostituisce le lettere
presenti nella sequenza disordinati con quelle della sequenza ordinata.
Quindi nell'esempio precedente le sostituzioni sono invertite:
 (s, a), (l, i) (a, l), (i, m) ed (m, s)

Per altri esempi vedere il file grade03.txt

Implementate le due funzioni
    codifica(chiave, testo_in_chiaro) -> testo_crittografato
    decodifica(chiave, testo_crittografato) -> testo_in_chiaro

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

import string

def isBetween_az(letter):
    return letter in string.ascii_lowercase

def creaAccoppiamenti(chiave):
    disordinati = list(chiave)

    C = []
    i = 0
    while i < len(disordinati):
        elemento = disordinati[i]
        if isBetween_az(elemento):
            if elemento not in C:
                C.append(elemento)
        else:
            del disordinati[i]
            i -= 1
        i += 1

    for c in C:
        cInChiave = chiave.count(c)
        for i in range(cInChiave - 1):
            disordinati.remove(c)
    ordinati = sorted(disordinati)
    return dict(zip(ordinati, disordinati))

def codifica(chiave, testo):
    accoppiamenti = creaAccoppiamenti(chiave)

    print(dict(accoppiamenti))

    testoLista = list(testo)
    for i in range(len(testoLista)):
        elemento = testoLista[i]
        if elemento in accoppiamenti:
            testoLista[i] = accoppiamenti[elemento]

    return "".join(testoLista)


def decodifica(chiave, testo):
    accoppiamenti = {y: x for x, y in creaAccoppiamenti(chiave).items()}

    testoLista = list(testo)
    for i in range(len(testoLista)):
        elemento = testoLista[i]
        if elemento in accoppiamenti:
            testoLista[i] = accoppiamenti[elemento]

    return "".join(testoLista)
