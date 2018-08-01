
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
    '''inserire qui la vostra implementazione'''
    for i in range(255):
        if i < 97 or i > 122:
            chiave = chiave.replace(chr(i), '')
    sl = list(chiave)
    for i in range(len(chiave)):
        n = chiave.rfind(chiave[i])
        if n > i:
            sl[i] = " "
    sdis = ""
    for i in sl:
        if i != " ":
            sdis += i
    srlista = list(sdis)
    srolista = sorted(sdis)
    sro = ""
    for i in srolista:
        sro += i
    testolista = list(testo)
    for i in range(len(testolista)):
        if sro.find(testolista[i]) >= 0:
            testolista[i] = srlista[sro.find(testolista[i])]
    rtestoo = ""
    for i in testolista:
        rtestoo += i
    return rtestoo

def decodifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    for i in range(255):
        if i < 97 or i > 122:
            chiave = chiave.replace(chr(i), '')
    lettchiave = list(chiave)
    for i in range(len(chiave)):
        n = chiave.rfind(chiave[i])
        if n > i:
            lettchiave[i] = " "
    sdis = ""
    for i in lettchiave:
        if i != " ":
            sdis += i
    srolista = sorted(sdis)
    sro = ""
    for i in srolista:
        sro += i
    testolista = list(testo)
    for i in range(len(testolista)):
        if sdis.find(testolista[i]) >= 0:
            testolista[i] = srolista[sdis.find(testolista[i])]
    rtesto = ""
    for i in testolista:
        rtesto += i
    return rtesto