
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
def crea_chiave(s1):
    "Funzione che, presa una stringa, la usa per ritornare una lista di tuple che fungono da chiave di codifica e decodifica di un testo"
    ls=[]
    ls1=[]
    for x1 in s1:
        if ord(x1)>=97 and ord(x1)<=122:
            ls+=[x1]
    ls.reverse()
    for x1 in ls:
        if not x1 in ls1:
            ls1+=[x1]
    ls1.reverse()
    ls2=sorted(ls1)
    ls3=[]
    c=0
    while c<len(ls1):
        ls3+=[(ls1[c],ls2[c])]
        c+=1
    return ls3

def codifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    ls=crea_chiave(chiave)
    ls1=list(testo)
    c=0
    for x in ls1:
        for y in ls:
            if x==y[1]:
                ls1[c]=y[0]
        c+=1
    return ''.join(ls1)
                
                

def decodifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    ls=crea_chiave(chiave)
    ls1=list(testo)
    c=0
    for x in ls1:
        for y in ls:
            if x==y[0]:
                ls1[c]=y[1]
        c+=1
    return ''.join(ls1)