
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

def codifica(chiave, testo_in_chiaro):
    chiavpul = ""
    for i in reversed(chiave):
        if i in chiavpul:
            continue
        else:
            chiavpul += i
    copykey = list(reversed(chiavpul))
    for i in copykey[:]:
        if not "a" <= i <= "z":
            copykey.remove(i)
    copycat = sorted(copykey)
    diz = {}
    for x in range(len(copykey)):
        diz[copycat[x]] = copykey[x]
    testo_crittografato = ""
    for x in testo_in_chiaro:
        if x in diz:
            testo_crittografato = testo_crittografato + diz[x]
        else:
            testo_crittografato = testo_crittografato + x
    return testo_crittografato

def decodifica(chiave, testo_crittografato):
    chiavpul = ""
    for i in reversed(chiave):
        if i in chiavpul:
            continue
        else:
            chiavpul += i
    copykey = list(reversed(chiavpul))
    for i in copykey[:]:
        if not "a" <= i <= "z":
            copykey.remove(i)
    copycat = sorted(copykey)
    diz = {}
    for x in range(len(copykey)):
        diz[copykey[x]] = copycat[x]
    testo_in_chiaro = ""
    for x in testo_crittografato:
        if x in diz:
            testo_in_chiaro= testo_in_chiaro + diz[x]
        else:
            testo_in_chiaro = testo_in_chiaro + x
    return testo_in_chiaro