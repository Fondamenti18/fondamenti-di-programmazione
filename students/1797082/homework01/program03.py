
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
    
    ch1=[]
    for i in chiave:
        if 'a'<=i<='z':
            ch1.append(i)
    #print(ch1)
    ch2 = ch1[:]
    ch2 = ch2[::-1]
    ch3=[]
    for carattere in ch2:
        if (carattere in ch3) == False:
            ch3.append(carattere)
    ch3 = ch3[::-1]
    disordinata = ch3
    ordinata = sorted(disordinata)
    #e fino a qui la lista è giusta

    #creazione dizionario elementi accoppiati
    #valore_limite = len(ordinata)+1
    coppie = {}
    for indice in range(0,len(ordinata)):
        coppie[ordinata[indice]]=disordinata[indice]
    # e anche fino a qui funziona
    

    #INIZIO FUNZIONE DI SOSTITUZIONE

    stringa = ""
    for car in testo:
        carattere = car
        s = coppie.get(carattere, carattere) 
        stringa += s
            #sostituire all'elemento i il valoredella chiave del dizionario
            
            
    
    
    print(disordinata)
    print(ordinata)
    return(stringa)

def decodifica(chiave, testo):

    ch1=[]
    for i in chiave:
        if 'a'<=i<='z':
            ch1.append(i)
    #print(ch1)
    ch2 = ch1[:]
    ch2 = ch2[::-1]
    ch3=[]
    for carattere in ch2:
        if (carattere in ch3) == False:
            ch3.append(carattere)
    ch3 = ch3[::-1]
    disordinata = ch3
    ordinata = sorted(disordinata)
    #e fino a qui la lista è giusta

    #creazione dizionario elementi accoppiati
    #valore_limite = len(ordinata)+1
    coppie = {}
    for indice in range(0,len(ordinata)):
        coppie[disordinata[indice]]=ordinata[indice]
    # e anche fino a qui funziona
    

    #INIZIO FUNZIONE DI SOSTITUZIONE

    stringa = ""
    for car in testo:
        carattere = car
        s = coppie.get(carattere, carattere) 
        stringa += s
            #sostituire all'elemento i il valoredella chiave del dizionario
            
            
    
    
    print(disordinata)
    print(ordinata)
    return(stringa)

