
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
    global ordinata
    global disordinata
    ordinata2=[]
    for C in chiave:
        if C in 'abcdefghijklmnopqrstuvwxyz':
            if C not in ordinata2:
                ordinata2.append(C)
                ordinata3=''.join(sorted(ordinata2))
                ordinata=list(ordinata3)
        
    result=[]
    lista=[]
    for C in chiave[::-1]:
        if C in 'abcdefghijklmnopqrstuvwxyz':
            result.append(C)
    for c in result:
        lista.append(c)
        temporanea=''.join([j for i,j in enumerate(lista) if j not in lista[:i]])
        disordinata2=temporanea[::-1]
        disordinata=list(disordinata2)

    testo1=list(testo)
    codificato=[]
    for lettera in testo1:
        if lettera not in ordinata:
            new=testo1[testo1.index(lettera)]
        if lettera in ordinata:
            new=disordinata[ordinata.index(lettera)]
        
        codificato.append(new)
    
        
    return ''.join(codificato)  


def decodifica(chiave, testo):
    global ordinata
    global disordinata
    ordinata2=[]
    for C in chiave:
        if C in 'abcdefghijklmnopqrstuvwxyz':
            if C not in ordinata2:
                ordinata2.append(C)
                ordinata3=''.join(sorted(ordinata2))
                ordinata=list(ordinata3)
        
    result=[]
    lista=[]
    for C in chiave[::-1]:
        if C in 'abcdefghijklmnopqrstuvwxyz':
            result.append(C)
    for c in result:
        lista.append(c)
        temporanea=''.join([j for i,j in enumerate(lista) if j not in lista[:i]])
        disordinata2=temporanea[::-1]
        disordinata=list(disordinata2)

    testo1=list(testo)
    decodificato=[]
    for lettera in testo1:
    
        if lettera not in disordinata:
            new=testo1[testo1.index(lettera)]
        if lettera in disordinata:
            new=ordinata[disordinata.index(lettera)]
        
        decodificato.append(new)
    
        
    return ''.join(decodificato)

