
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
    '''inserire qui la vostra implementazione'''
    s=''.join(reversed(chiave))                     #giro la chiave al contrario
    
    stringa_pulita=[]                               #inizializzo una lista vuota
    for x in s:
        if(x in"qwertyuiopasdfghjklzxcvbnm" and x not in stringa_pulita):
            stringa_pulita.append(x)                #alla quale ci aggiungo il carattere se è compreso tra 'a' e 'z'
                                                    #in questo modo riesco a elimirare le occorrenze tranne l'ultima         
    stringa_Disordinata=list(reversed(''.join(stringa_pulita)))    #stringa_pulita la inverto e la metto in una lista
    stringa_Ordinata=sorted(stringa_Disordinata)                   #poi rimetto in ordine alfabetico
    stringa_finale=''
    for x in testo:                                                # controllo se il carattere è nella stringa ("qwert..."), se 
        if x not in "qwertyuiopasdfghjklzxcvbnm":                   # non fosse cosi si aggiungono gli spazi nella stringa finale
            stringa_finale+= x
        else:                                                       # se il carattere è presente nella stringa ("qwert..."), inizia 
            for y in range(len(stringa_Disordinata)):               # un secondo for, copia il carattere della stringa disordinta 
                if(x == stringa_Ordinata[y]):                       # nella stringa finale, nella  funzione decodifica accade 
                    stringa_finale+=stringa_Disordinata[y]          # esattamente il contrario.
                
    
    return stringa_finale
    


def decodifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    s=''.join(reversed(chiave))                                   
    
    stringa_pulita=[]
    for x in s:
        if(x in"qwertyuiopasdfghjklzxcvbnm" and x not in stringa_pulita):
            stringa_pulita.append(x)
    
    stringa_Disordinata=list(reversed(''.join(stringa_pulita)))
    stringa_Ordinata=sorted(stringa_Disordinata)
    stringa_finale=''
    for x in testo:
        if x not in "qwertyuiopasdfghjklzxcvbnm":
            stringa_finale+=x
        else:
            for y in range(len(stringa_Disordinata)):
                if(x == stringa_Disordinata[y]):
                    stringa_finale+=stringa_Ordinata[y]
                
    
    return stringa_finale
