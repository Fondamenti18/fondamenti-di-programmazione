
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

La decodifica del testo crittografato opera sulla stessa chiave ma sostituisce le lettere
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
    '''inserire qui la vostra implementazione'''
    testo1 = []
    codifica = {}
    codifica = eliminaChiave(chiave)
    for carattere in testo:
        if carattere not in codifica:
            testo1.append(carattere)
        for k, v in codifica.items():
            if carattere == k:
                testo1.append(v)
           
    testo1 = ''.join(testo1)

    return testo1

def decodifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    testo2 = []
    codifica = {}
    codifica = eliminaChiave(chiave)
    for carattere in testo:
        if carattere not in codifica:
            testo2.append(carattere)
        for k, v in codifica.items():
            if carattere == v:
                testo2.append(k)
       
    testo2 = ''.join(testo2)

    return testo2  




def eliminaChiave(stringa):
    '''restituisce slaim  e ailms e il dizionario che scambia le parole'''
    

    indici = []
    stringa1 = ''
    stringa2 = []
    stringa3 = []
    
    
    for c in stringa:
        if 'a' <= c <= 'z':
            
            stringa1 = stringa1 + c
   
       
    indici += [stringa1.rfind(c) for c in stringa1]
    indici = set(indici)   #trasformo la lista in un set(insieme) che non ammette duplicati!!! e lo ritrasforma in una lista
    for i in indici:
        for lettera in stringa1:
            if lettera not in stringa2:
                if i == stringa1.rfind(lettera): stringa2 += lettera

    stringa3[:] = stringa2
    stringa3.sort()
    stringa2 = ''.join(stringa2)
    stringa3 = ''.join(stringa3)
    
    
    
    
    return dict(zip(stringa3, stringa2))


if __name__ == '__main__':
    decodifica('the quick brown fox jumps over the lazy dog', 'rqrqzbhx b rqrbhb')

  


