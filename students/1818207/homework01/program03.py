
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
       (testo in chiaro)
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

def codifica(b, a): #creo liste per entrambi i testi
    chiave = list(b)
    codifica = []
    testo = list(a)
    count = 0
    for i in chiave : #mi appoggio a python che conosce gia' il valore corrispondente a una lettera
                      #e scarto i valori non compresi fra l'alfabeto per liberarmi di caratteri e maiuscole
        if i<'a' or i>'z' :
            chiave[chiave.index(i)] = ''
        if chiave.count(i) > 1:
            chiave[chiave.index(i)] = ''
    chiave =''.join(list(chiave))#per non sbalzare indice ho inserito spazi dei quali mi libero adesso
    codifica = sorted(chiave)#mi trovo la lista ordinata di chiave
    codifica =''.join(list(codifica))
    codifica = list(codifica)
    chiave = list(chiave)
    
    unione = [codifica,chiave]#creo una lista contenente sia chiave che codifica che sono composte dallo stesso num 
    for j in testo : #di elementi
        
        for z in unione[0] :  #itero fra di loro per ottenere le corrispondenze da sostituire grazie agli indici
            if j == z :
                testo[count] = unione[1][unione[0].index(z)]
                break
        count += 1
    
    return "".join(testo)#riporto alla forma corretta il testo

def decodifica(b, a): #sostanzialmente una ripetizione del codice precedente invertita nel risultato
    chiave = list(b)
    codifica = []
    testo = list(a)
    count = 0
    for i in chiave :
        
        if i<'a' or i>'z' :
            chiave[chiave.index(i)] = ''
        if chiave.count(i) > 1:
            chiave[chiave.index(i)] = ''
    chiave =''.join(list(chiave))
    codifica = sorted(chiave)
    codifica =''.join(list(codifica))
    codifica = list(codifica)
    chiave = list(chiave)
    
    unione = [chiave,codifica]
    for j in testo :
        
        for z in unione[0] :  
            if j == z :
                testo[count] = unione[1][unione[0].index(z)]
                break
        count += 1
    
    return "".join(testo)