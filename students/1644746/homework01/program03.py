
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
    lChiave=[]
    lChiaveOrd=[]
    lTesto=[]
    i=0
    # Copiare i caratteri nelle liste
    while(i<len(chiave)):
        #Verifico tutti i caratteri idonei
        if(chiave[i:i+1]>='a' and chiave[i:i+1]<='z'):
                lChiave.insert(i,chiave[i:i+1])
                lChiaveOrd.append(chiave[i:i+1])
        i+=1
    
    
    i=0
    
    #Rimuovo tutte le occorrenze
    while(i<len(lChiave)):
        if(lChiave.count(lChiave[i]) >1):
            lChiave.remove(lChiave[i])
        i+=1
    
    i=0
    while(i<len(testo)):
        lTesto.append(testo[i:i+1])
        i+=1
    
    lChiaveOrd=lChiave[:]
    lChiaveOrd.sort()
    
    i=0
    lTestoCodificato=[]
    #Sostituisco i caratteri nel testo - codifica
    while(i<len(lTesto)):
        #Contatore chiave
        f=0
        sostituito=False
        while(f<len(lChiave)):
            if(lTesto[i]==lChiaveOrd[f]):
                lTestoCodificato.insert(i,lChiave[f])
                sostituito=True
            f+=1
        if(sostituito==False):
            lTestoCodificato.insert(i,lTesto[i])
        i+=1
    
    i=0
    testo_crittografato=''
    while(i<len(lTestoCodificato)):
        testo_crittografato+=str(lTestoCodificato[i])
        i+=1
    
    return testo_crittografato


def decodifica(chiave, testo):
    lChiave=[]
    lChiaveOrd=[]
    lTesto=[]
    i=0
    
    # Copiare i caratteri nelle liste
    while(i<len(chiave)):
        #Verifico che i caratteri siano idonei
        if(chiave[i:i+1]>='a' and chiave[i:i+1]<='z'):
                lChiave.insert(i,chiave[i:i+1])
                lChiaveOrd.append(chiave[i:i+1])
        i+=1
    
    
    i=0
    #Rimuovo tutte le occorrenze
    while(i<len(lChiave)):
        if(lChiave.count(lChiave[i]) >1):
            lChiave.remove(lChiave[i])
        i+=1
    
    i=0
    while(i<len(testo)):
        lTesto.append(testo[i:i+1])
        i+=1
    
    lChiaveOrd=lChiave[:]
    lChiaveOrd.sort()
    
    i=0
    lTestoD=[]
    #Sostituisco i caratteri nel testo - decodifica
    while(i<len(lTesto)):
        #Contatore chiave
        f=0
        sostituito=False
        while(f<len(lChiave)):
            if(lTesto[i]==lChiave[f]):
                lTestoD.insert(i,lChiaveOrd[f])
                sostituito=True
            f+=1
        if(sostituito==False):
            lTestoD.insert(i,lTesto[i])
        i+=1
    
    i=0
    testo_in_chiaro=''
    while(i<len(lTestoD)):
        testo_in_chiaro+=str(lTestoD[i])
        i+=1
    
    return testo_in_chiaro