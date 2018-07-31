

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

def codifica(chiave,testo):
    testo0=[]
    testo_in_lista=[]
    l1=[]
    off=0
    m=0
    for i in chiave:
        l1.append(i)
    for i in l1:
        if ord(i)==32:
            l1.remove(i)
    off1=0
    for i in range(len(l1)):
        if ord(l1[i-off1])<ord('a') or ord(l1[i-off1])>ord('z'):
            l1.pop(i-off1)
            off1+=1
    for i in range(len(l1)):
            if l1.count(l1[i-off])>1:
                l1.remove(l1[i-off])
                off+=1
    l2=sorted(l1)
    for i in testo:
        testo0.append(m)
    for i in testo:
        testo_in_lista.append(i)
    for i in range(len(l1)):
        for n in range(len(testo_in_lista)):
            if testo_in_lista[n]==l2[i] and testo0[n]==0:
                testo_in_lista[n]=l1[i]
                testo0[n]=1
    testo=''
    for i in testo_in_lista:
        testo+=i
    return (testo)
        
        

def decodifica(chiave, testo):
    testo0=[]
    testo_in_lista=[]
    l1=[]
    off=0
    m=0
    for i in chiave:
        l1.append(i)
    for i in l1:
        if ord(i)==32:
            l1.remove(i)
    off1=0
    for i in range(len(l1)):
        if ord(l1[i-off1])<ord('a') or ord(l1[i-off1])>ord('z'):
            l1.pop(i-off1)
            off1+=1
    for i in range(len(l1)):
            if l1.count(l1[i-off])>1:
                l1.remove(l1[i-off])
                off+=1
    l2=sorted(l1)
    for i in testo:
        testo0.append(m)
    for i in testo:
        testo_in_lista.append(i)
    for i in range(len(l1)):
        for n in range(len(testo_in_lista)):
            if testo_in_lista[n]==l1[i] and testo0[n]==0:
                testo_in_lista[n]=l2[i]
                testo0[n]=1
    testo=''
    for i in testo_in_lista:
        testo+=i
    return (testo)
