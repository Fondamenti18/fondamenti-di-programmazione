
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
    chiave2 = list(chiave[:])
    lunghezza = len(testo) 
    contatore = 0
    alfabeto= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    chiave1 = []
    while True:
        try:
            lettera = chiave2[contatore]
            contaL = 0
            if lettera in alfabeto:
                contaL = chiave2.count(lettera)
                if contaL > 1:
                    del chiave2[contatore]
                else:
                    chiave1 = chiave1 + [lettera]
                    contatore = contatore +1
                
            else:
                contatore = contatore +1
        except:
            break
    
    chiave2 = [] + chiave1
    chiave2.sort()
    contatore = 0
    testo1 = testo
    lunghezza = len(testo1)
    while contatore < lunghezza:
            testo1 = list(testo1)
            lettera = testo1[contatore]
            if lettera in chiave2:
                chiave2 = "".join(chiave2)
                posizioneL = chiave2.find(lettera)
                cripL = chiave1[posizioneL]
                testo1[contatore] = cripL
                chiave2 = list(chiave2)
                contatore = contatore +1
            else:
                contatore = contatore +1
     
    testo1 = "".join(testo1)
    return(testo1)


def decodifica(chiave, testo):
    chiave2 = list(chiave[:])
    lunghezza = len(testo) 
    contatore = 0
    alfabeto= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    chiave1 = []
    while True:
        try:
            lettera = chiave2[contatore]
            contaL = 0
            if lettera in alfabeto:
                contaL = chiave2.count(lettera)
                if contaL > 1:
                    del chiave2[contatore]
                else:
                    chiave1 = chiave1 + [lettera]
                    contatore = contatore +1
                
            else:
                contatore = contatore +1
        except:
            break
    
    chiave2 = [] + chiave1
    chiave2.sort()
    contatore = 0
    testo1 = testo
    lunghezza = len(testo1)
    while contatore < lunghezza:
            testo1 = list(testo1)
            lettera = testo1[contatore]
            if lettera in chiave1:
                chiave1 = "".join(chiave1)
                posizioneL = chiave1.find(lettera)
                cripL = chiave2[posizioneL]
                testo1[contatore] = cripL
                chiave1 = list(chiave1)
                contatore = contatore +1
            else:
                contatore = contatore +1
     
    testo1 = "".join(testo1)
    return(testo1)
    
