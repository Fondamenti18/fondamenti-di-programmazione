
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
 while i!= len(new)//2:          
        print("cdd")
        n=n + [new[i]]
        i=i+1
    j=0
    while j!= len(new)%2+len(new)//2:
        n1=n1+[new[i]]
        i=i+1
        j=j+1
    print(n,n1)

Implementate le due funzioni
    codifica(chiave, testo_in_chiaro) -> testo_crittografato
    decodifica(chiave, testo_crittografato) -> testo_in_chiaro

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''
assegnazione = {}
def codifica(chiave, testo):
    #pulizia chiave
    #new = []
    n= []
    n1= []
    indice = 0
    info=0
    chiave1=[]
    new=pulizia(chiave)
    #newtesto
    #print(new)
    #eliminazione caratteri uguali chiave
    i=0
   #idea: dividere la chiave in due liste
    assegnazione = {}   #sono coerente che questa assegnazione è una diversa assegnazione da quella globale :^
    ne=new
                         #idnice più piccolo
   
    i=0
    ne,altra=crea(new)
    #print(ne,altra)
    assegnazione = creatingd(ne,altra)
    #print(assegnazione)
    while i!=len(testo):
        if (testo[i] in assegnazione.keys()):
            chiave1 = chiave1 + [assegnazione[testo[i]]]
        else:
            chiave1= chiave1 + [testo[i]]
        i=i+1
    #print(chiave1)
    chiave1= ''.join(chiave1)
    return(chiave1)
def pulizia(chiave):                 #funzione che elimina tutto ciò che non è alfabeto minuscolo
    new = []
    for carac in chiave:        #eliminaziuone caratteri strani
        if 'a'<= carac and   carac <= 'z':
            new=new + [carac]
    return(new)
def crea(pulita):
    new=pulita
    ne=new
                         #idnice più piccolo
    i=0
    k=len(ne)-1     #così indica l'ultimo elemento (3 se la lunghezza è 4
    #print(k)
    #print(ne[k],new[i])
    
    #print(len(new))
    while k>=0:
        #print(k,i)
        i=0
        while i!=len(new):          #it works!
            #print(i)
            if (ne[k]==new[i]and i!=k):
                #print("hU",i)
                ne[i]=''
                i=i+1
                #print(ne,i)
            else:
                i=i+1
        k=k-1
    ne=pulizia(ne)
    altra=sorted(ne)
    #print(ne,altra)
    
    
        
    #print(ne)     #ne è la chiave nuova senza ripetizioni ecc

    return(ne,altra)








def creatingd(ne,altra):
    assegnazione = {}
    i=0
    while i!=len(ne):               #creazione di un dizionario con: lettera da sostituire: lettera cifrata 
        assegnazione[altra[i]]=ne[i]
        i=i+1   #richiamo la funzione che crea il dizionari o
    #print(assegnazione.keys())
    return(assegnazione)
    
def creadr(ne,altra):                   #crea un dizionario invertito
    assegnazione = {}
    i=0
    while i!=len(ne):               
        assegnazione[ne[i]]=altra[i]
        i=i+1   
    #print(assegnazione)
    return(assegnazione)
def decodifica(chiave, testo):   #farò in modo che decodifichi anche senza chiamare codifica
    chiave=pulizia(chiave)
    assegnazione={}
    chiave1=[]
    #print(chiave)
    #return(type(crea(chiave)))
    ne,altra=crea(chiave)
    i=0
    #print(ne,altra)
    assegnazione = creadr(ne,altra)
    #return(type(crea(chiave)))
    temp=0
    while i!=len(testo):            
        if (testo[i] in assegnazione.values()):
            chiave1 = chiave1 + [assegnazione[testo[i]]]
        else:
            chiave1= chiave1 + [testo[i]]
        i=i+1
    #print(chiave1)
    chiave1= ''.join(chiave1)
    return(chiave1)
    
    
    
    
    

