
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

def generachiave(chiave):
    
    nonordin = []
    othernonordin = []
    ordin = []
    
    chiave = list(chiave)
    
    for e in range(len(chiave)-1,-1,-1):
        if chiave[e] < 'a' or chiave[e] > 'z':
            del chiave[e]
            
    for e in range(len(chiave)-1,-1,-1):
        c = 0
        for l in range(len(othernonordin)-1,-1,-1):
            if chiave[e] == othernonordin[l]:
                c = 1
        if c == 0:
            othernonordin += list(chiave[e])
            
    for e in range(0, len(othernonordin)):
        nonordin = list(othernonordin[e]) + nonordin
        
    ordin = sorted(nonordin)
    
    return nonordin, ordin
    

def codifica(chiave, testo):
    
    p,d = generachiave(chiave)
    testo = list(testo)
    
    for i , t in enumerate(testo):
        f = 0
        for j , c in enumerate(p):
            if testo[i] == d[j] and f == 0:
                testo[i] = p[j]
                f = 1
                
    testo = ''.join(testo)
    
    return testo

def decodifica(chiave, testo):
    
    p,d = generachiave(chiave)
    testo = list(testo)
    
    for i , t in enumerate(testo):
        f = 0
        for j , c in enumerate(p):
            if testo[i] == p[j] and f == 0:
                testo[i] = d[j]
                f = 1
                
    testo = ''.join(testo)
    
    return testo
    
    
    
