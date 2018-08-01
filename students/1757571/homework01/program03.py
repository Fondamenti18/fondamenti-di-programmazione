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

def cleanChar(string):
    #Elimina i caratteri non compresi nell'intervallo di codifica
    NoCharString=""
    for character in string:
        if 'a'<=character<='z':
            NoCharString= NoCharString+character
    return NoCharString

def cleanOccurrence(string):
    #Mantiene solamente l'ultima occorrenza dei caratteri della stringa
    NoOccurString=""
    CorrectString=""
    for char in reversed(string):
        if char not in NoOccurString:
            NoOccurString=NoOccurString+char
    for char in reversed(NoOccurString):
        CorrectString=CorrectString+char
    return CorrectString
        
        
def cleanString(string):
    #Utilizza i metodi cleanChar e cleanOccurrence per ottenere una stringa
    #pulita adatta alla codificazione
    noChar=cleanChar(string)
    myString=cleanOccurrence(noChar)
    return myString

def createKeyCode(noOrder, Order):
    #Associa la sequenza ordinata a quella disordinata creando il dizionario
    #utilizzato per la codifica
    myDict={}
    const=0
    var=len(noOrder)
    while const<var:
        myDict[Order[const]]=noOrder[const]
        const=const+1
    return myDict

def createKeyDecode(noOrder, Order):
    #Associa la sequenza disordinata a quella ordinata creando il dizionario
    #utilizzato per la codifica
    myDict={}
    const=0
    var=len(noOrder)
    while const<var:
        myDict[noOrder[const]]=Order[const]
        const=const+1
    return myDict

def keyTranslate(keytionary, string):
    #Lavora il testo applicando la traduzione attraverso la codifica del dizionario
    UsedKeys=keytionary.keys()
    CryptText=""
    for char in string:
        if char in UsedKeys:
            CryptText=CryptText+char.replace(char,keytionary.get(char))
        else:
            CryptText=CryptText+char
    return CryptText

def codifica(chiave, testo):
    UnorderKey=cleanString(chiave)
    OrderKey=''.join(sorted(UnorderKey))
    dictKey=createKeyCode(UnorderKey, OrderKey)
    return keyTranslate(dictKey, testo)

def decodifica(chiave, testo):
    UnorderKey=cleanString(chiave)
    OrderKey=''.join(sorted(UnorderKey))
    dictKey=createKeyDecode(UnorderKey, OrderKey)
    return keyTranslate(dictKey, testo)