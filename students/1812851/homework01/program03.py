
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
 
I soli caratteri del testo  a subire una codifica sarano  's','l', 'a' 'i' ed 'm'. 
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
def codifica(chiave, testo):
'''
import sys
sys.setrecursionlimit(10000)

def codifica(chiave,testo):
    #l=len(chiave)
    #print(l)
    global chiavedis
    global chiaveord
    chiavedis=pulisci_chiave(chiave) #chiave pulita 
    #print(chiavedis)
    chiavedis=pulisci_occorrenze()
    chiaveord=sorted(chiavedis)         #ordina chiave
    #print("chiave ord",chiaveord)
    #print("chiave dis",chiavedis)
    return sostituisci(0,testo)



def decodifica(chiave, testo):
    global chiavedis
    global chiaveord
    chiavedis=pulisci_chiave(chiave)
    chiavedis=pulisci_occorrenze()
    chiaveord=sorted(chiavedis)
    return sostituisci(1,testo)
    


def pulisci_chiave(chiave):
    l=len(chiave)
    c=range(0,l)
    lista_dis=[]
    for contatore in c:
        #print(chiave[contatore])
        if chiave[contatore] >='a' and chiave[contatore]<='z':
            lista_dis+=chiave[contatore]
    return lista_dis



def pulisci_occorrenze():
    for c in chiavedis:
        #print(c)
        if chiavedis.count(c)>1:
            chiavedis.remove(c)
            pulisci_occorrenze()
    return chiavedis



def sostituisci(x,testo):   #0 codifica   1 decodifica
    ris=''
    if(x==0):
        print("Codifica")   #da ordinato a disordinato
        prec=chiaveord
        succ=chiavedis
    else:
        print("Decodifica") #da disordinato a ordinato
        prec=chiavedis
        succ=chiaveord
    
    for c in range(0,len(testo)):
        if testo[c] in prec:
            posiz=prec.index(testo[c])
            ris+=(succ[posiz])    
        else:
            ris+=(testo[c])
    return ris


    
    
    
