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
    chiave_codifica=genera_chiave(chiave, "cod")
    return cod(chiave_codifica, testo)


def decodifica(chiave, testo):
    chiave_codifica=genera_chiave(chiave, "decod")
    return cod(chiave_codifica, testo)

def cod (chiave, testo):
    testo_cod=testo
    j=0
    temp=["!A1A!","!B1B!","!C3C!","!D4D!","!E5E!","!F6F","!G7G!","!H8H!","!I9I!","!J1J!","!K2K!","!L3L!","!M4M!","!N5N!","!O6O!","!P7P!","!Q8Q!","!R9R!","!S1S!","!T2T!","!U3U!","!V4V!","!W5W!","!X6X!","!Y7Y!","!Z8Z!"]
    while j<len(chiave):
        testo_cod=testo_cod.replace(chiave[j][0], temp[j])
        j+=1
    j=0
    while j<len(chiave):
        testo_cod=testo_cod.replace(temp[j], chiave[j][1])
        j+=1
    return testo_cod
    
def elimina_caratteri_chiave(chiave):
    i=0
    while i < len(chiave):
        if chiave[i]<'a' or chiave[i]>'z':
            chiave=chiave[:i]+chiave[i+1:]
        else:
            i+=1
    return chiave
            
def elimina_occorrenze_chiave(chiave):
    i=0
    while (i < len(chiave)):
        car=chiave[i]
        if chiave.count(car)>1:
            pos=chiave.find(car)
            chiave=chiave[:pos]+chiave[pos+1:]
        else:
            i+=1
    return chiave
def genera_chiave(ch, ope):
    c=elimina_caratteri_chiave(ch)
    chiave=elimina_occorrenze_chiave(c)
    i=0
    lista=[]
    chiave_decodifica=[]
    while i<len(chiave):
        lista.append(chiave[i])
        i+=1
    lista.sort()
    i=0
    while i<len(chiave):
        if (lista[i]!=chiave[i]):
            if(ope=="cod"):
                chiave_decodifica.append( (lista[i] , chiave[i]))
            else:
                chiave_decodifica.append( (chiave[i], lista[i]))
        i+=1
    return chiave_decodifica