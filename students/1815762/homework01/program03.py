
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
    '''inserire qui la vostra implementazione'''
    chiave_nuova=''
    lista=[]
    lista_ordinata=[]
    x=0
    for x in range(len(chiave)):
            if chiave[x]>='a'and chiave[x]<='z':
                chiave_nuova=chiave_nuova+chiave[x]
    n=len(chiave_nuova)-1
    listasenza=' '
    
    
    while n>=0:
        
        y=0
        while y<len(listasenza):
              
              if chiave_nuova[n]!= listasenza[y]:
                  trovato=False
              else:
                  trovato=True
                  break
              y+=1
        if trovato== False:
            listasenza+=chiave_nuova[n]
            
        n-=1
    
    for x in range(len(listasenza)):
        lista.append(listasenza[x])
    
    lista.reverse()
    b=len(lista)-1
    lista.pop(b)
    lista_ordinata=sorted(lista)
    x=0
    testo_cod=list(testo)
    while x<len(testo):
        z=0
        while z<len(lista_ordinata):
            if testo[x]==lista_ordinata[z]:
                testo_cod[x]=lista[z]
            z+=1
        x+=1
    cod=''.join(testo_cod)
    return(cod)
    


def decodifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    chiave_nuova=''
    lista=[]
    lista_ordinata=[]
    x=0
    for x in range(len(chiave)):
            if chiave[x]>='a'and chiave[x]<='z':
                chiave_nuova=chiave_nuova+chiave[x]
    n=len(chiave_nuova)-1
    listasenza=' '
    
    
    while n>=0:
        
        y=0
        while y<len(listasenza):
              
              if chiave_nuova[n]!= listasenza[y]:
                  trovato=False
              else:
                  trovato=True
                  break
              y+=1
        if trovato== False:
            listasenza+=chiave_nuova[n]
            
        n-=1
    
    for x in range(len(listasenza)):
        lista.append(listasenza[x])
    
    lista.reverse()
    b=len(lista)-1
    lista.pop(b)
    lista_ordinata=sorted(lista)
    x=0
    testo_cod=list(testo)
    while x<len(testo):
        z=0
        while z<len(lista_ordinata):
            if testo[x]==lista[z]:
                testo_cod[x]=lista_ordinata[z]
            z+=1
        x+=1
    cod=''.join(testo_cod)
    return(cod)
