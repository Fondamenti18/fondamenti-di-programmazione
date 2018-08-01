
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

def elspec(chiave):
    chiave=chiave.replace("!","")
    chiave=chiave.replace("?","")
    chiave=chiave.replace(".","")
    chiave=chiave.replace(";","")
    chiave=chiave.replace("@","")
    chiave=chiave.replace("&","")
    chiave=chiave.replace("$","")
    chiave=chiave.replace("#","")
    chiave=chiave.replace(",","")
    chiave=chiave.replace(" ","")
    chiave=chiave.replace("A","")
    chiave=chiave.replace("B","")
    chiave=chiave.replace("C","")
    chiave=chiave.replace("D","")
    chiave=chiave.replace("E","")
    chiave=chiave.replace("F","")
    chiave=chiave.replace("G","")
    chiave=chiave.replace("H","")
    chiave=chiave.replace("I","")
    chiave=chiave.replace("L","")
    chiave=chiave.replace("M","")
    chiave=chiave.replace("N","")
    chiave=chiave.replace("O","")
    chiave=chiave.replace("P","")
    chiave=chiave.replace("Q","")
    chiave=chiave.replace("R","")
    chiave=chiave.replace("S","")
    chiave=chiave.replace("T","")
    chiave=chiave.replace("U","")
    chiave=chiave.replace("V","")
    chiave=chiave.replace("X","")
    chiave=chiave.replace("W","")
    chiave=chiave.replace("Y","")
    chiave=chiave.replace("Z","")
    chiave=chiave.replace("J","")
    chiave=chiave.replace("K","")
    return chiave




def conv(chiave):
    chiave=elspec(chiave)
    lista=list(chiave)
    for x in lista:
        while lista.count(x)>1:
            lista.remove(x)
    for x in lista:
        while lista.count(x)>1:
            lista.remove(x)
    return lista
    
        

        

def codifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    lista=conv(chiave)
    lista1=sorted(lista)
    lista1=list(lista1)
    testoinlista=list(testo)
    u=0
    while (u<len(testoinlista)):
        c=0
        i=0
        while(i<len(lista) and c==0):
            membro1=lista[i]
            membro2=lista1[i]
            membro3=testoinlista[u]
            if(membro3==membro2):
                testoinlista[u]=membro1
                c=1
            else:
                i=i+1 
        u=u+1
    i=0
    testocod=''
    while(i<len(testoinlista)):
        testocod=testocod+testoinlista[i]
        i=i+1
    return(testocod)
              
            
        


def decodifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    lista=conv(chiave)
    lista1=sorted(lista)
    lista1=list(lista1)
    testoinlista=list(testo)
    u=0
    while (u<len(testoinlista)):
        c=0
        i=0
        while(i<len(lista) and c==0):
            membro1=lista[i]
            membro2=lista1[i]
            membro3=testoinlista[u]
            if(membro3==membro1):
                testoinlista[u]=membro2
                c=1
            else:
                i=i+1 
        u=u+1
    i=0
    testocod=''
    while(i<len(testoinlista)):
        testocod=testocod+testoinlista[i]
        i=i+1
    return(testocod)
