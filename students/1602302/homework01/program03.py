
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

def chiave1(key):
    key.replace(" ","")
    key=list(key)
    cont1=0
    #tolgo maiuscole
    for x in key:
        if x<'a' or x>'z' :
            key[cont1]=""
        cont1+=1
    #tolgo elementi lista nulli
    while key.count("")>0:
        key.remove("")
    #tolgo le lettere che si ripetono tranne l' ultima
    for b in key:
        if key.count(b)>1:
            conk=key.count(b)-1
            while conk>0:
                key.insert(key.index(b),"")
                key.remove(b)
                conk-=1
                
    key="".join(key)
    return key




def ordinachiave(key):
    x="".join(sorted(key))
    return x


#key1=ordinata key2=disordinata  per decodifica inserire arg invertiti
def creatuplecodifica(key1,key2):
    lista=[]
    cont=0

    for x in key1:
        z=key2[cont]
        t=(x,z)
        lista.append(t)
        cont+=1

    return lista


def repetitioncheck(text):
    i=(text*2).find(text,1,-1)
    ntext=""
    count=0
    if i>0:
        ntext=text[:i]
        count=text.count(ntext)    
    lis=[ntext,count]
    return lis


def codifica(chiave, testo):
    ltesto=[]
    
    if len(chiave)>50:
        lchiave=repetitioncheck(chiave)
        if lchiave[0]!="":
            chiave=lchiave[0]
    if len(testo)>50:
        ltesto=repetitioncheck(testo)
        if ltesto[0]!="":
            testo=ltesto[0]
    
    key=chiave1(chiave)
    keyord=ordinachiave(key)
    tup=creatuplecodifica(keyord,key)
    nl=[]
    switch=""
    testo1=list(testo)
    for x in testo1:
        for z in tup:
            if x==z[0]:
                switch=z[1]
                break
        if switch!="":
            nl.append(switch)
        else:
            nl.append(x)
        switch=""
    new="".join(nl)
    if ltesto!=[] and ltesto[1]>0:
        new=new*ltesto[1]
    return new



def decodifica(chiave, testo):
    ltesto=[]
    if len(chiave)>50:
        lchiave=repetitioncheck(chiave)
        if lchiave[0]!="":
            chiave=lchiave[0]
    if len(testo)>50:
        ltesto=repetitioncheck(testo)
        if ltesto[0]!="":
            testo=ltesto[0]
    
    key=chiave1(chiave)
    keyord=ordinachiave(key)
    tup=creatuplecodifica(key,keyord)
    nl=[]
    switch=""
    testo1=list(testo)
    for x in testo1:
        for z in tup:
            if x==z[0]:
                switch=z[1]
                break
        if switch!="":
            nl.append(switch)
        else:
            nl.append(x)
        switch=""
    new="".join(nl)
    if ltesto!=[] and ltesto[1]>0:
        new=new*ltesto[1]
    return new

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
