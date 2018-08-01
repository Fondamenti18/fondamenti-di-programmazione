
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

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def findElemArr (arr, elem):
    
    trovato = False
    j = 0
    while j<len(arr) and (not trovato):
        if elem == arr[j]:
            trovato = True
        j+=1
    return trovato

def getKeys (mainStr, check):
    
    letters = ''
    i = len(mainStr) - 1
    
    while i >= 0:
        currentChar = mainStr[i]
        if findElemArr(alphabet, currentChar) == True:
            if  findElemArr(letters, currentChar) == False: #verifico che non ho salvato la lettera
                letters += currentChar #salvo la lettera associato all'indice corrispondente
        i-=1
        
    letters = letters[::-1] 
    ordered = ''.join(sorted(letters))
    
    keys = {}
    
    for ik in range(0, len(ordered)):
        if(check == True):
            keys[ordered[ik]] = letters[ik]
        else:
            keys[letters[ik]] = ordered[ik]
            
    return keys
    
def codStr (mainStr, keys):
    
    finalStr = ''
    
    for i in range(0, len(mainStr)):
        key = keys.get(mainStr[i], False)
        if key != False:
            finalStr += key
        else:
            finalStr += mainStr[i]
        i+=1
    return finalStr

def codifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    keys = getKeys(chiave, True)
    return codStr(testo, keys)

def decodifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    keys = getKeys(chiave, False)
    return codStr(testo, keys)
