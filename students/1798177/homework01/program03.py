# coding=utf-8
# Dato un testo da codificare ed una chiave si propone il seguente schema
# crittografico:
#
# - dalla chiave vengono eliminati  tutti i caratteri C per cui C<'a' o C>'z'.
# - di ciascuno dei caratteri restanti vengono cancellate dalla chiave tutte le
# occorrenze tranne l'ultima, ottenendo una sequenza DISORDINATA.
# - i caratteri presenti nella stringa cosi' ripulita saranno i soli caratteri
# del testo ad essere codificati ovvero sostituiti nel testo crittografato
# (gli altri resteranno invariati).
# - la sequenza ORDINATA dei caratteri rimasti nella chiave viene messa in
# corrispondenza con la sequenza DISORDINATA dei caratteri ottenuti al passo
# precedente.
#
# Come esempio di applicazione  consideriamo la chiave
#  "sim sala Bim!"
# a seguito delle eliminazioni la chiave produce la sequenza DISORDINATA
#  "slaim"
#
# I soli caratteri del testo  a subire una codifica sarano 's','l', 'a' 'i' ed
# 'm'. Per sapere con cosa verranno codificati questi caratteri si considera la
# seguente corrispondenza tra sequenze:
#    "ailms" (sequenza ordinata degli stessi caratteri)
#    "slaim" (sequenza disordinata ottenuta dalla chiave)
# questo determina gli accoppiamenti (a,s), (i,l) (l,a), (m,i) ed (s,m)
# la 'a' dunque sara' codificata con 's', la 'i' con 'l' e cosi' via.
#
# Utilizzando la chiave "sim sala Bim!" per codificare il testo  "il mare sa di
# sale" si otterra' il seguente testo crittografato:
#    "il mare sa di sale"   (testo in chiaro)
#    "la isre ms dl msae"   (testo crittografato)
#
# La decodifica del testo crittografato opera sulla stessa chive ma sostituisce
# le lettere presenti nella sequenza disordinata con quelle della sequenza
# ordinata. Quindi nell'esempio precedente le sostituzioni sono invertite:
# (s, a), (l, i) (a, l), (i, m) ed (m, s)
#
# Implementate le due funzioni
#    codifica(chiave, testo_in_chiaro) -> testo_crittografato
#    decodifica(chiave, testo_crittografato) -> testo_in_chiaro
#
# ATTENZIONE: NON USATE LETTERE ACCENTATE.
# ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio
# dell'esercizio e' zero.

import re
from collections import OrderedDict

def get_two_keys(raw_key):
    '''Ritorna la chiave disordinata e quella ordinata.'''
    # Questa espressione regolare permette di levare tutti i caratteri non
    # permessi, ritornando una stringa filtrata.
    raw_key = list(re.sub('[^a-z]', "", raw_key))
    raw_key.reverse()

    # OrderedDict è una sottoclasse di Dict che tiene conto dell'ordine di
    # inserimento delle chiavi. Dato che in un dizionario la chiave è univoca,
    # altre chiavi con lo stesso valore vengono "scartate".
    disordered_key = list(OrderedDict.fromkeys(raw_key))

    # Viene convertita la lista da caratteri a numeri.
    # map ritorna una mappa (poi in lista) che applica ad ogni elemento di
    # una lista una funziona (in questo caso anonima).
    disordered_key = list(map(lambda char: ord(char), disordered_key))

    disordered_key.reverse()

    ordered_key = disordered_key.copy()
    ordered_key.sort()

    return disordered_key, ordered_key

def codifica(chiave, testo):
    disordered_key, ordered_key = get_two_keys(chiave)

    # Si può creare un dizionario partendo da due liste di stessa lunghezza,
    # facendo corrispondere la chiave agli elementi della prima ed ai attributi
    # gli elementi della seconda (con zip).
    chiave = dict(zip(ordered_key, disordered_key))

    # Il metodo translate usa un dizionario per convertire determinati caratteri
    # (la chiave) nei loro attributi.
    return testo.translate(chiave)

def decodifica(chiave, testo):
    disordered_key, ordered_key = get_two_keys(chiave)

    # Nella decodifica il dizionario è invertito rispetto alla codifica.
    chiave = dict(zip(disordered_key, ordered_key))

    return testo.translate(chiave)
