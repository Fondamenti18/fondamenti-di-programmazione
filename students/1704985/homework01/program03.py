
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


def prima(testo):
    prima=''
    for C in testo:
        if C>='a' and C<='z':
            prima=prima+C
    return prima

def intermedio1(testo):
    chars=[]
    for C in testo:
        chars.append(C)
    return chars

def intermedio2(lista):
    lista.reverse()
    lista2=[]
    for i in lista:
        if not(i in lista2):
            lista2.insert(0,i)
    return lista2

def poi(lista):
    word= ''.join([str(i) for i in lista])
    return word

def trovaChiave(testo):
    inizio=prima(testo)
    int1=intermedio1(inizio)
    int2=intermedio2(int1)
    fine=poi(int2)
    return fine

def ordine(testo):
    list=intermedio1(testo)
    list.sort()
    ordinata=poi(list)
    return ordinata

def traduttore(testo):
    dict={}
    chiave1=trovaChiave(testo)
    chiave2=ordine(chiave1)
    l=len(chiave1)
    for i in range(0,l):
        d= {chiave2[i] : chiave1[i]}
        dict.update(d)
    return dict
    
        

def codifica(chiave, testo):
    dict=traduttore(chiave)
    word=''
    lista=dict.keys()
    for C in testo:
        if(C in lista) == False :
            word=word+C
        else:
            word= word + dict.get(C)
    return word        

def traduttoreDec(testo):
    dict={}
    chiave1=trovaChiave(testo)
    chiave2=ordine(chiave1)
    l= len(chiave1)
    for i in range(0,l):
        d={chiave1[i]:chiave2[i]}
        dict.update(d)
    return dict

def decodifica(chiave,testo):    
    dict=traduttoreDec(chiave)
    word=''
    lista=dict.keys()
    for C in testo:
        if(C in lista) == False :
            word=word+C
        else:
            word=word + dict.get(C)
    return word        
