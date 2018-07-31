
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

La decodifica del testo crittografato opera sulla stessa chiave ma sostituisce le lettere
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
    a=pulita(chiave)
    b=ordinata(chiave)
    c=''
    
    for x in testo:
        if x in b:
            h=hello(x, b)
            j=a[h[0]]
            c+=j
            
        else:
            c+=x
            
    return c

def hello(x, o):
    return [pos for pos, char in enumerate(o) if char==x]


def chiavedis(chiave):
    ret=''
    for c in chiave:
        if 'a'<=c<='z':
            ret+=c
    return ret


def pulita(chiave):
    chiave1=chiavedis(chiave)
    chiave3=''
    chiave4=chiave1[::-1]
    for w in chiave4:
        if w not in chiave3:
            chiave3+=w
    q=chiave3[::-1]
    return q

def ordinata(chiave):
    chiave2=pulita(chiave)
    return ''.join(sorted(chiave2))

def posizione(chiave):
    for x in chiave:
        if x in ordinata(chiave):
            return [pos for pos, char in enumerate(x) if char==x]

def decodifica(chiave, testo):
    a=pulita(chiave)
    b=ordinata(chiave)
    c=''
    
    for x in testo:
        if x in a:
            h=hello(x, a)
            j=b[h[0]]
            c+=j
            
        else:
            c+=x
            
    return c


