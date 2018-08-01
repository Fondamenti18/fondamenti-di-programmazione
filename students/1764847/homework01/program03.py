
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
    '''Prende in input una chiave e un testo, restituisce
    il testo codificato'''
    s = ''
    sDisordinata = stringaDisordinata(chiave, testo)
    sOrdinata = ordinaStringa(sDisordinata)
    d = accoppiamenti(sOrdinata, sDisordinata, True)
    s = cod(d, testo)
    return s


def decodifica(chiave, testo):
    '''Prende in input una chiave e un testo cosificato,
    restituisce il testo decodificato'''
    s = ''
    sDisordinata = stringaDisordinata(chiave, testo)
    sOrdinata = ordinaStringa(sDisordinata)
    d = accoppiamenti(sOrdinata, sDisordinata, False)
    s = cod(d, testo)
    return s


def stringaDisordinata(chiave, testo):
    '''Prende in input una chiave ed un testo,
    restituisce una stringa disordinata'''
    s = ''
    sDisordinata = ''
    for i in chiave:
        if i >= 'a' and i <= 'z':
            s += i
    for j in range(len(s)-1, -1, -1):
        if s[j] not in sDisordinata:
            sDisordinata = s[j] + sDisordinata
    return sDisordinata


def ordinaStringa(s):
    '''Riceve in input una stringa disordinata e
    restituisce una altra che contiene gli stessi
    caratteri della stringa in input ma ordinata'''
    sOrdinata = ''
    a = sorted(s)
    for i in a:
        sOrdinata += i
    return sOrdinata


def accoppiamenti(sOrdinata, sDisordinata, valBooleano):
    '''Date in input una stringa ordinata, una stringa
    disordinata e un valore Booleano, se il valore booleano == True
    restituisce un dizionario dove come chiave
    c e un carattere della stringa ordinata e come valore
    un carattere della stringa disordinata, se invece il valore
    booleano == False, restituisce un dizionario dove come chiave
    c'e' un carattere della stringa disordinata e come valore un
    carattere della stringa ordinata'''
    d = {}
    if valBooleano == True:
        for i in range(len(sOrdinata)):
            d[sOrdinata[i]] = sDisordinata[i]
        return d
    for i in range(len(sDisordinata)):
        d[sDisordinata[i]] = sOrdinata[i]
    return d

      

def verificaChiavi(d, chiave):
    '''Prende in input un dizionario e una chiave,
    restituisce True se la chiave è presente nel dizionare
    False altrimenti'''
    booleano = False
    for c in d:
        if c == chiave:
            booleano = True
            break
    return booleano




def cod(d, testo):
    '''Prende in input un dizionario e un testo
    e da in output il testo codificato'''
    s = '' 
    for c in range(len(testo)):
        if verificaChiavi(d, testo[c]) == False:
            s += testo[c]
        else:
            for chiave in d:
                if chiave == testo[c]:
                    s += d[testo[c]]
    return s

