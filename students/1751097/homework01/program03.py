
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
    # Qui eseguo la funziona per generare la chiave.
    dizionario_chiave = genera_chiave(chiave, "CRIPT")
    # Mi genero il testo crittografato applicando la chiave ordinata.    
    testo_crittografato = sostituzione_testo(testo, dizionario_chiave)
    return testo_crittografato


def decodifica(chiave, testo_crittografato):
    dizionario_chiave = genera_chiave(chiave, "DECRIPT")
    # Mi genero il testo originale applicando la chiave invertita.
    testo = sostituzione_testo(testo_crittografato, dizionario_chiave)
    return testo
    
    

 # Funzione per generare la chiave.
def genera_chiave(chiave, tipo_chiave):     
    chiave_new = ""
    for i in chiave:
        if i <= "z" and i >= "a":
            chiave_new += i
                
    #print(chiave_new) 
    chiave_new = list(chiave_new) # adesso trasformo in lista.
    #print(chiave_new)
    chiave_disordinata = elimina_duplicati(chiave_new)
    #print(chiave_disordinata)
    chiave_ordinata = chiave_disordinata.copy()  # Copiamo elementi dalla lista disordinata.
    chiave_ordinata.sort()                       # E utilizzare cosi la '.sort' sulla stessa lista.
   # print(chiave_ordinata)                       # Per non riordinare cosi la nostra lista iniziale.
    dizionario_chiave = dict([(x, n) for x, n in zip(chiave_ordinata, chiave_disordinata)])
    
    # Verifico se devo invertire o meno il mio dizionario
    if tipo_chiave == "DECRIPT":
        # Inverto il dizionario
        dizionario_chiave = dict( dict([(valore, chiave) for chiave, valore in dizionario_chiave.items()]))
    return dizionario_chiave



 # Funzione che applica la chiave finita al mio testo
def sostituzione_testo(testo, dizionario_chiave):
    testo_crittografato = ""
    for lettera in testo:
        sostituzione = dizionario_chiave.get(lettera, lettera) # Estraggo il valore dal dizionario.
                                                               # Restituisce se stesso in caso non trovi la chiave.
        testo_crittografato += sostituzione
    return testo_crittografato
    

 # Funzione per eliminare caratteri mulitpli tranne l' ultimo.
def elimina_duplicati(chiave_new):
    lista=[]
    for x in reversed(chiave_new):
        if x in lista: # Contiamo quante volte il carattere si ripete.
                chiave_new.remove(x)    # Rimuovo quel carattere x.
        else:
            lista.append(x)
    return chiave_new


if __name__ == '__main__': # eseguo il test solo se lancio lo script direttamente
    key  = 'the quick brown fox jumps over the lazy dog'*100
    text = 'rqrqzbhx b rqrbhb'*100
    res  = 'papaveri e papere'*100
    args = (key, text)
    ret  = decodifica(*args)
    print(ret)
    print("")
    print(res)
    
