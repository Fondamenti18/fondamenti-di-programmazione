
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
i=len(chiav(chiave))-len(chiav(chiave))
while i<len(chiav(chiave)):
        lst+=(chiav(chiave)[i])+(chiave_ord[i])
        i+=1
        
        def cose(c,co,t):
    i=0
    while i<len(t):
       for x in co:
           if t[i]==x:
               t.replace(t[i],)
'slaim','ailms','il mare sa di sale' la isre ms dl msae


finale +=c[int(c.index(co[int(a)-1])-1)]
    return finale
    
    +=c[int(co.index(g))]
'''   

def cod(c,co,t):
    finale=''
    for g in t:
        if not g in co:
            finale+=g
        else:
            finale +=c[int(co.index(g))]
    return finale
def string(s):
   g=[]
   a=0
   while a<len(s):
       g.append(s[a])
       a+=1
   return g
def lis(g):
    for i in g:
       while g.count(i)>1:
           g.remove(i)
    return g#esco dal for
def chiav(chiave):
    chiave1=chiave.replace(' ','')
    chiave2=''
    for i in chiave1:
        if i.isalpha() and i.islower():
            chiave2+=i
    return ''.join(lis(string(chiave2)))
def codifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    chiave_ord=''.join(sorted(chiav(chiave)))
    return cod(chiav(chiave),chiave_ord,testo)
    
    
def decodifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    chiave_ord=''.join(sorted(chiav(chiave)))
    chiave1=chiav(chiave)
    finale=''
    for g in testo:
        if not g in chiave1:
            finale+=g
        else:
            finale +=chiave_ord[int(chiave1.index(g))]
    return finale
