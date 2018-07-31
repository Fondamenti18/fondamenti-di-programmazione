
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
def decodifica(chiave, testo):
    strKey=''
    for i in chiave[::-1]:
        if i not in strKey and 'a'<=i<='z':
            strKey+=i
    strKey=strKey[::-1]
    strKeyO=strKey
    for i in range(len(strKeyO)):
        for m in range(len(strKeyO)-1):
            if strKeyO[m]>strKeyO[m+1]:
                if m-1<0:
                    strKeyO=strKeyO[m+1]+strKeyO[m]+strKeyO[m+2:]
                elif m-1==0:
                    strKeyO=strKeyO[m-1]+strKeyO[m+1]+strKeyO[m]+strKeyO[m+2:]
                else:
                    strKeyO=strKeyO[:m]+strKeyO[m+1]+strKeyO[m]+strKeyO[m+2:]
    lstKey=[]
    for i in range(len(strKey)):
        lstKey.append((strKey[i],strKeyO[i]))
    for i in range(len(testo)):
        for m in range(len(lstKey)):
            if testo[i]==lstKey[m][0]:
                testo=testo[:i]+lstKey[m][1]+testo[i+1:]
                break
    return testo

def codifica(chiave, testo):
    strKey=''
    for i in chiave[::-1]:
        if i not in strKey and 'a'<=i<='z':
            strKey+=i
    strKey=strKey[::-1]
    strKeyO=strKey
    for i in range(len(strKeyO)):
        for c in range(len(strKeyO)-1):
            if strKeyO[c]>strKeyO[c+1]:
                if c-1<0:
                    strKeyO=strKeyO[c+1]+strKeyO[c]+strKeyO[c+2:]
                elif c-1==0:
                    strKeyO=strKeyO[c-1]+strKeyO[c+1]+strKeyO[c]+strKeyO[c+2:]
                else:
                    strKeyO=strKeyO[:c]+strKeyO[c+1]+strKeyO[c]+strKeyO[c+2:]
    lstKey=[]
    for i in range(len(strKey)):
        lstKey.append((strKeyO[i],strKey[i]))
    for i in range(len(testo)):
        for c in range(len(lstKey)):
            if testo[i]==lstKey[c][0]:
                testo=testo[:i]+lstKey[c][1]+testo[i+1:]
                break
    return testo

