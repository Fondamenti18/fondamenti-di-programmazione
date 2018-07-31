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


def checkKey(chiave):
    key = []
    for i in range(len(chiave)):
        # if is alphabet and not Uppercase and not a space then add into the list
        if chiave[i].isalpha() and not chiave[i].isupper() and not chiave.isspace():
            key.append(chiave[i])
    return key


def dupkey(list):
    '''Find the Duplicate char and insert in another list which needs to compare with the main list to create a Key with unique value'''
    DupKey = []
    for i in list:
        if i not in DupKey:
            DupKey.append(i)
    return DupKey


def removeDupKey(singleKey, keylist):
    '''Remove duplicate character'''
    for i in singleKey:
        while keylist.count(i) != 1:
            keylist.remove(i)
    return keylist


def createKey(chiave):
    '''create the unique key'''
    global key, sortKey

    key = checkKey(chiave)  # check key function
    singleChar = dupkey(key)  # duplicate key find function
    key = removeDupKey(singleChar, key)  # remove duplicate key function
    sortKey = sorted(key)

def chiaveUnica(chiave,chiaveOrd):
    '''create dictionary with keys '''
    keysDict={}
    for i in range(len(chiave)):
        keysDict[chiave[i]] = chiaveOrd[i]

    return keysDict

def exchange (testo,keys):
    '''replace keys'''
    replace=''
    for i in range(len(testo)):
        if testo[i] in keys.keys():
            replace += keys.get(testo[i])
        else:
            replace += testo[i]
    return replace

def codifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    createKey(chiave)

    EncKeys = chiaveUnica(sortKey, key)
    encrypt=exchange(testo,EncKeys)

    return encrypt


def decodifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    decKeys = chiaveUnica(key, sortKey)
    decrypt = exchange(testo,decKeys)

    return decrypt
