
'''Dato un testo da codificare ed una chiave si propone il seguente schema
crittografico:

- dalla chiave vengono eliminati  tutti i caratteri C per cui C<'a' o C>'z'. 
- di ciascuno dei caratteri restanti vengono cancellate dalla chiave tutte le
  occorrenze tranne l'ultima, ottenendo una sequenza DISORDINATA. 
- i caratteri presenti nella stringa cosi' ripulita saranno i soli caratteri
  del testo ad essere codificati ovvero sostituiti nel testo crittografato (gli
  altri resteranno invariati). 
- la sequenza ORDINATA dei caratteri rimasti nella chiave viene messa in
  corrispondenza con la sequenza DISORDINATA dei caratteri ottenuti al passo precedente.

Come esempio di applicazione  consideriamo la chiave
 "sim sala Bim!"
a seguito delle eliminazioni la chiave produce la sequenza DISORDINATA
 "slaim"
 
I soli caratteri del testo  a subire una codifica sarano 's','l', 'a' 'i' ed 'm'. 
Per sapere con cosa verranno codificati questi caratteri si considera la seguente
corrispondenza tra sequenze:
    "ailms" (sequenza ordinata degli stessi caratteri)
    "slaim" (sequenza disordinata ottenuta dalla chiave)
questo determina gli accoppiamenti (a,s), (i,l) (l,a), (m,i) ed (s,m)
la 'a' dunque sara' codificata con 's', la 'i' con 'l' e cosi' via.

Utilizzando la chiave "sim sala Bim!" per codificare il testo  "il mare sa di
sale" si otterra' il seguente testo crittografato:
    "il mare sa di sale"   (testo in chiaro)
    "la isre ms dl msae"   (testo crittografato)

La decodifica del testo crittografato opera sulla stessa chive ma sostituisce
le lettere presenti nella sequenza disordinata con quelle della sequenza ordinata.
Quindi nell'esempio precedente le sostituzioni sono invertite:
 (s, a), (l, i) (a, l), (i, m) ed (m, s)

Per altri esempi vedere il file grade03.txt

Implementate le due funzioni
    codifica(chiave, testo_in_chiaro) -> testo_crittografato
    decodifica(chiave, testo_crittografato) -> testo_in_chiaro

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'
esercizio e' zero.
'''

def codifica(chiave, testo):
    chv=''
    c=''
    stringa_disordinata=''
    stringa_disordinata+=key(chiave)
    chiave_ordinata=ordine(stringa_disordinata)
    c+=crittografia(chiave_ordinata,testo)
    return c

def ordine(stringa_disordinata):
    lista_ordinata=sorted(stringa_disordinata)
    '''creatore coppie'''
    lista_coppie=[]
    if len(lista_ordinata)==len(stringa_disordinata):
        for x in range(0,len(lista_ordinata)):
            lista_coppie+=[[stringa_disordinata[x],lista_ordinata[x]]]
    return lista_coppie
    

def crittografia(chiave_ordinata,testo):
    testo_crittografato=''
    for x in range(0,len(testo)):
        carattere=testo[x]
        for y in range(0,len(chiave_ordinata)):
            if carattere==chiave_ordinata[y][1]:
                carattere=chiave_ordinata[y][0]
                break
        testo_crittografato+=carattere
    return testo_crittografato

def key(chiave):
    c=''
    s=''
    chiave=chiave.replace(' ','')
    chiave_corretta=''
    chiave_disordinata=''
    chiave1=''
    for x in range(0,len(chiave)):
        if ord('a')<=ord(chiave[x])<=ord('z'):
           chiave_corretta+=chiave[x]
    l=len(chiave_corretta)
    for x in range(0,l):
        carattere=chiave_corretta[x]
        trovato='F'
        for y in range(x+1,l):
           if carattere==chiave_corretta[y]:
               trovato ='T'
               break
        if trovato == 'F':
            chiave_disordinata+=str(chiave_corretta[x])
    return chiave_disordinata

                     



def decodifica(chiave, testo):
    chv=''
    c=''
    stringa_disordinata=''
    stringa_disordinata+=key(chiave)
    chiave_ordinata=ordine(stringa_disordinata)
    c+=decrittografia(chiave_ordinata,testo)
    return c


    

def decrittografia(chiave_ordinata,testo):
    testo_crittografato=''
    for x in range(0,len(testo)):
        carattere=testo[x]
        for y in range(0,len(chiave_ordinata)):
            if carattere==chiave_ordinata[y][0]:
                carattere=chiave_ordinata[y][1]
                break
        testo_crittografato+=carattere
    return testo_crittografato

