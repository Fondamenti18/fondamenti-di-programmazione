
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
import re
from itertools import count

def gen_sequence_dict(key, mode):
    chars = "".join(re.findall("[a-z]", key))[::-1]
    unique_chars = ""
    sequence_dict = dict()
    for l in chars:
        if l not in unique_chars: unique_chars += l
    sorted_chars = sorted(unique_chars[::-1])
    if mode == "crypt":
        for i, char, sorted_char in zip(count(), unique_chars[::-1], sorted_chars):
            sequence_dict[sorted_char] = (char, "|" + str(i)+ "|")
    elif mode == "decrypt":
        for i, char, sorted_char in zip(count(), unique_chars[::-1], sorted_chars):
            sequence_dict[char] = (sorted_char, "|"+ str(i) + "|")
    return sequence_dict

def codifica(chiave, testo):
    crypt_dict = gen_sequence_dict(chiave, "crypt")
    for key, value in crypt_dict.items():
        if key in testo:
            testo = testo.replace(key, crypt_dict[key][1])
    for key, value in crypt_dict.items():
        if value[1] in testo:
            testo = testo.replace(value[1], value[0])
    return testo

def decodifica(chiave, testo):
    crypt_dict = gen_sequence_dict(chiave, "decrypt")
    for key, value in crypt_dict.items():
        if key in testo:
            testo = testo.replace(key, crypt_dict[key][1])
    for key, value in crypt_dict.items():
        if value[1] in testo:
            testo = testo.replace(value[1], value[0])
    return testo
