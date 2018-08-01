
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
    
    l=""
    if len(chiave)>1:   #se la chiave è fatta da due stringhe
        for x in chiave:
            l+=x.replace(' ', '')
    else:
        l=chiave.replace(' ', '') #elimino gli spazi nella chiave
    chiave=l[:]

    l=list(chiave) #trasformo la chiave in una lista

    appoggio=l[:]
    for c in appoggio:
        if c < "a" or c > "z":
                l.remove(c)    #rimuovo i caratteri minori di a e maggiori di z
    appoggio=l[:]


    for i in appoggio:
        if l.count(i)>1:
            l.remove(i)   #elimino le occorrenze
    ordine=l[:]
    ordine.sort()

        

    accoppiamenti = {}
    for x in l:
        i=l.index(x)
        for y in ordine:
            ii=ordine.index(y)   
            if ii==i:
                accoppiamenti[y]= x #creo dizionario con la chiave fatta da le
                                #lettere di l accoppiate con le lettere di ordine

    testo1=list(testo)
    testo2=testo1[:]
    indici=[]
    for chiave, valore in accoppiamenti.items():
    
        for x in testo2:        
            if x == chiave:
                i=[i for i,y in enumerate(testo2) if y==x]
 
                
                for y in i:
                    if y not in indici:
                        del testo2[y]
                        testo2.insert(y,valore) #codifico il testo
                indici+=i
                 
    chiave = ''.join(l) #trasformo la chiave da lista a stringa
    ordine = ''.join(ordine) #trasformo ordine da lista a stringa 
    stringa= ''.join(testo2)
    return stringa


def decodifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    l=""
    if len(chiave)>1:   #se la chiave è fatta da due stringhe
        for x in chiave:
            l+=x.replace(' ', '')
    else:
        l=chiave.replace(' ', '') #elimino gli spazi nella chiave
    chiave=l[:]

    l=list(chiave) #trasformo la chiave in una lista

    appoggio=l[:]
    for c in appoggio:
        if c < "a" or c > "z":
                l.remove(c)    #rimuovo i caratteri minori di a e maggiori di z
    appoggio=l[:]


    for i in appoggio:
        if l.count(i)>1:
            l.remove(i)   #elimino le occorrenze
    ordine=l[:]
    ordine.sort()

        

    accoppiamenti = {}
    for x in l:
        i=l.index(x)
        for y in ordine:
            ii=ordine.index(y)   
            if ii==i:
                accoppiamenti[x]= y #creo dizionario con la chiave fatta da le
                                #lettere di l accoppiate con le lettere di ordine

    testo1=list(testo)
    testo2=testo1[:]
    indici=[]
    for chiave, valore in accoppiamenti.items():
    
        for x in testo2:        
            if x == chiave:
                i=[i for i,y in enumerate(testo2) if y==x]
 
                
                for y in i:
                    if y not in indici:
                        del testo2[y]
                        testo2.insert(y,valore) #codifico il testo
                indici+=i
                 
    chiave = ''.join(l) #trasformo la chiave da lista a stringa
    ordine = ''.join(ordine) #trasformo ordine da lista a stringa 
    stringa= ''.join(testo2)
    return stringa

