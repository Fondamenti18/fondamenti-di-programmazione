
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

def produzionelistachiave(chiave): #funziona
    i=0
    code=[]
    for x in range(len(chiave)):
        if ord(chiave[x])<ord('a') or ord(chiave[x])>ord('z'):
            pass
        else:
            code.append(chiave[x])
        i+=1
    seq=[]
    for c in code:
         if c in seq:
             indice=seq.index(c)
             seq.pop(indice)
             seq.append(c)
         else:
            seq.append(c)
    seqord=[]
    seqord=sorted(seq, key=str.lower) #produzione stringa slaim e ailms
    return seq,seqord

def listadecodifica(seq,seqord): #funziona
    d={}
    i=0
    for x in seqord:
        k=seq[i]#prima seq ordinata e poi la seq
        d[k]=x
        i+=1
        print(d)
    print ('decodifica')
    return d

def listacodifica(seq,seqord): #funziona
    d={}
    i=0
    for x in seq:
        k=seqord[i]#prima seq ordinata e poi la seq
        d[k]=x
        print (d)
        i+=1
    print ('codifica')
    return d


def codifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    seq,seqord=produzionelistachiave(chiave)
    diz=listacodifica(seq,seqord)
    ltesto=[]
    for b in testo:
        if b in diz:
            variabile=b
            variabile=diz[variabile]
            b=variabile
            ltesto.append(b)
            print(ltesto)
        else:
            ltesto.append(b)
    ltesto="".join(ltesto)  
    return ltesto  
    
def decodifica(chiave, testo):
    seq,seqord=produzionelistachiave(chiave)
    diz=listadecodifica(seq,seqord)
    ltesto=[]
    for b in testo:
        if b in diz:
            variabile=b
            variabile=diz[variabile]
            b=variabile
            ltesto.append(b)
        else:
            ltesto.append(b)
    ltesto="".join(ltesto)
    return ltesto
