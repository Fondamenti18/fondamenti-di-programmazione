'''Dato un testo da codificare ed una chiave si propone il seguente schema crittografico:

DONE dalla chiave vengono eliminati  tutti i caratteri C per cui C<'a' o C>'z'. DONE
DONE di ciascuno dei caratteri restanti vengono cancellate dalla chiave tutte le occorrenze
  tranne l'ultima, ottenendo una sequenza DISORDINATA. DONE
DONE i caratteri presenti nella stringa cosi' ripulita saranno i soli caratteri del testo
  ad essere codificati ovvero sostituiti nel testo crittografato (gli altri resteranno invariati).DONE
DONE la sequenza ORDINATA dei caratteri rimasti nella chiave viene messa in corrispondenza
  con la sequenza DISORDINATA dei caratteri ottenuti al passo precedente. DONE

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

'''codifica un testo data una determinata chiave'''
def codifica(chiave, testo):
    return substitute(chiave,testo,0);

'''decodifica un testo data una determinata chiave'''
def decodifica(chiave, testo):
    return substitute(chiave,testo,1);

''' rimuove caratteri speciali dalla stringa'''
''' per ogni char, rimuove tutte le occorrenze esclusa l'ultima'''
def clear_string(s):
    temp = ""

    for c in s:
        if (c >= 'a' and c <= 'z'): temp += c

    for c in set(temp):
        last = temp.rindex(c)
        temp = temp[:last].replace(c, "") + temp[last:]
    return(temp)

'''sostituisce i caratteri per codifica/decodifica'''
def substitute(chiave,testo,k):
    index_list = []
    for i in range(len(testo)):
        if (testo[i].isupper()): index_list.append(i)

    unsorted_key = clear_string(chiave)
    sorted_key = "".join(sorted(clear_string(chiave)))
    for i in range(len(unsorted_key)):
        if(k == 0):
            testo = testo.replace(sorted_key[i],unsorted_key[i].upper())
        elif(k == 1):
            testo = testo.replace(unsorted_key[i],sorted_key[i].upper())
    testo = testo.lower()

    for i in index_list:
        testo = testo[:i] + testo[i].upper() + testo[i+1:]
    return testo
