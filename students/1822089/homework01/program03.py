
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
    
    #chiave disordinata
    keyCode=key(chiave)
    
    lst=list(keyCode)
    lst.sort()
    #chiave ordinata
    keyCodeSort="".join(lst)
    
    #print(keyCode)
    #print(keyCodeSort)
    
    testoCod=encodingText(keyCode, keyCodeSort, testo)
    
    #print(testoCod)
    
    return testoCod


def decodifica(chiave, testo):
    #chiave disordinata
    keyCode=key(chiave)
    
    lst=list(keyCode)
    lst.sort()
    #chiave ordinata
    keyCodeSort="".join(lst)
    
    #print(keyCode)
    #print(keyCodeSort)
    
    testoDecod=decodingText(keyCode, keyCodeSort, testo)
    print(testoDecod)
    
    return testoDecod

#Elabora la chiave
def key(chiave):
    keychanged=chiave
    
    #Controlla caratteri
    for i in range(0,len(chiave),1):
        if chiave[i]<"a" or chiave[i]>"z":
            #remove char
            keychanged=keychanged.replace(chiave[i], "")
    
    return removeDuplicates(keychanged)

#Elimina le occorrenze
def removeDuplicates(key):
    finalKeys=key
    listKeyChars=list(finalKeys)
    
    for i in range(0,len(key),1):#scorre la lista
        char=key[i]
        #Conta occorrenze
        dupl=finalKeys.count(char)
        if(dupl>1):
            for j in range(0, dupl-1):
                indexToRemove=finalKeys.find(char)
                listKeyChars.pop(indexToRemove)
                finalKeys="".join(listKeyChars)
                
    return finalKeys

#Codifica
def encodingText(keyCode, keyCodeSort, testo):
    notChange=[]#conterrà gli indice dei valori già cambiati
    
    for o in range(0,len(keyCodeSort),1):#caratteri ordinati
        sort=keyCodeSort[o]
        for d in range(0,len(keyCode),1):#caratteri diordinati
            disord=keyCode[d]
            #Indici uguali
            if o==d:
                #scorre il testo per trovare tutte le posizioni i cui valori saranno codificati
                for t in range(0,len(testo),1):
                    charTesto=testo[t]
                    #Cerca il carattere da modifica (sort) e
                    #controlla la posizione del carattere corrente è già stata modificata
                    if(sort==charTesto and t not in notChange):
                        notChange.append(t)
                        lstTesto=list(testo)
                        lstTesto[t]=disord
                        testo="".join(lstTesto)
                #Passa al carattere successivo se trova la corrispondenza delle chiavi
                break
    return testo

#Decodifica
def decodingText(keyCode, keyCodeSort, testo):
    notChange=[]#conterrà gli indice dei valori già cambiati
    
    for d in range(0,len(keyCode),1):#caratteri disordinati
        disord=keyCode[d]
        for o in range(0,len(keyCodeSort),1):#caratteri ordinati
            sort=keyCodeSort[o]
            #Indici uguali
            if o==d:
                for t in range(0,len(testo),1):
                    charTesto=testo[t]
                    if(disord==charTesto and t not in notChange):
                        notChange.append(t)
                        lstTesto=list(testo)
                        lstTesto[t]=sort #change value
                        testo="".join(lstTesto)
                break
    return testo
























