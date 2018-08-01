
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

def funzione1(chiave):
    
                ########                                   ########
    
    ls_1=[]
                   
                ########                                   ########
    for n in chiave:
        if True==n.isalpha() and n>= 'a' and n<= 'z' :
            ls_1+=n
                  
                ########                                   ########
    
    c=len(ls_1)
    
                ########                                   ########
    
    while c!=0:
        c=c-1
        if ls_1.count(ls_1[c])>1:
            ls_1.remove(ls_1[c])
    
                ########                                   ########
    
    return ls_1
                ########                                   ########
def funzione2(chiave):
    
                ########                                   ########
    
    ls_1=funzione1(chiave)
    ls_2=sorted(ls_1)
    cont=0
    v=[]
               ########                                   ########
    for z in ls_1:
        v+=[ls_2[cont]+ls_1[cont]]
        cont+=1
               ########                                   ########
    return v

               ########                                   ########

def codifica(chiave,testo):
               ########                                   ########
    v=funzione2(chiave)
    Q1=''
    
               ########                                   ########
    
    for el in testo :
        d=1
        for i in v :
            d+=1
            if i[0]==el:
                Q1+=i[1]
                break
            
               ########                                   ########
            
            if d>len(v):
                Q1+=el
                break
    
               ########                                   ########
    
    testo=''
    testo+=Q1
    del Q1
    
               ########                                   ########
    
    return testo

               ########                                   ########

def decodifica (chiave, testo):
   
               ########                                   ########
    
    v=funzione2(chiave)
    Q2=''
    
               ########                                   ########
    
    for il in testo:
        d=1
        for i in v:
           d+=1
            
               ########                                   ########
           
           if i[1]==il:
                Q2+=i[0]
                break
           
               ########                                   ########
            
           if d>len(v):
                Q2+=il
                break
            
               ########                                   ########
    
    testo=''
    testo+=Q2
    del Q2
    
               ########                                   ########
    
    return testo
