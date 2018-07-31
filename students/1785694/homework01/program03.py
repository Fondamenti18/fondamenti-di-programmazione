
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

def codifica(chiave,testo):
    
    text = []
    caratteri = set(chiave)
    for c in caratteri:
        if not c.isalpha() or c.isupper():
             chiave = chiave.replace(c, '')
    for x in list(chiave[::-1]):
          if x not in text:
                text.append(x)
    testo1 = ''.join(text)[::-1] 
    testo2 = sorted(testo1)            
    testo3 = {}
    lista = ""
    for x,v in zip(testo1,testo2):
        testo3[v] = x
    for lettera in testo:
        if lettera in testo3:
            lista += testo3[lettera]
        else:
            lista += lettera
    return lista 

def decodifica(chiave,testo):            
     text = []
     caratteri = set(chiave)
     for c in caratteri:
        if not c.isalpha() or c.isupper():
             chiave = chiave.replace(c, '')
     for x in list(chiave[::-1]):
          if x not in text:
                text.append(x)
     testo1 = ''.join(text)[::-1] 
     testo2 = sorted(testo1)            
     testo3 = {}
     lista = ""
     for x,v in zip(testo1,testo2):
        testo3[x] = v
     for lettera in testo:
        if lettera in testo3:
            lista += testo3[lettera]
        else:
            lista += lettera
     return lista