
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
#input: chiave
#elminare lettere maiuscole
#eliminare doppioni tranne l'ultimo
#caratteri ottenuti saranno codificati nel testo(seguenza disordinata)   
#seguenza ordinata messa in corrispondenza con la seguenza disordinata
def codifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    
  
    seg1=minuscole(chiave)
    
    seg1=eliminadoppioni(seg1)
   
    seg2=ordina(seg1)
 
    diz=creadizionario(seg2,seg1)  #associa ogni valore di seg2(seguenza ordinata) al valore corrispondente della seguenza disordinata

    testo_crittografato=codifica_testo(testo,diz)
    return testo_crittografato


    
def decodifica(chiave, testo):
    '''inserire qui la vostra implementazione''' 
    seg1=minuscole(chiave)
    seg1=eliminadoppioni(seg1)
    seg2=ordina(seg1)
    diz=creadizionario(seg1,seg2)
    testo_decodificato=decodifica_testo(testo,diz)
    return testo_decodificato



def minuscole(stringa): #rimuove le maiuscole
    segmento=''
    for carattere in stringa: 
       if 'a'<=carattere<='z':
            segmento=segmento+str(carattere)
       else:continue
    return segmento   
            
def eliminadoppioni(stringa): #elimina i doppioni
    seg1=''
    i=0
    for carattere in stringa:
        if stringa.count(carattere,i)==1:
            seg1=seg1+str(carattere)
           
        i+=1    
    return seg1
            
            
def ordina(stringa):  #ordina la stringa disordinata
    seg=''
    segmento=sorted(stringa)
    seg2=seg.join(segmento)
 
    return seg2 #seguenza ordinata

def codifica_testo(testo,diz): # codifica il testo utilizzando il dizionario creato  
    stringa=''
    lista1=diz.keys()
    lista=testo.split("\n")
    for linea in lista:
        parole=linea.split(" ")
        for parola in parole:
            
            for lettera in parola:

                if lettera in lista1:
                   stringa=stringa+diz[lettera]
              
                else:
                    stringa=stringa+lettera
            if parole[-1]!=parola:
                stringa=stringa+' '
            
    return stringa



def creadizionario(stringa1,stringa2):  #crea dizionario a partire da due stringhe
    diz={}
    for x,y in zip(stringa1,stringa2):
        diz[x]=y  
    return diz    
        
def decodifica_testo(testo,diz): #decodifica il testo utilizzando il dizionario creato
    stringa=''
    lista1=diz.keys()
    lista=testo.split("\n")
    for linea in lista:
        parole=linea.split(" ")
        for parola in parole:
 
            for lettera in parola:

                if lettera in lista1:
                   stringa=stringa+diz[lettera]
              
                else:
                    stringa=stringa+lettera
            if parole[-1]!=parola:
               stringa=stringa+' '             
                   
 
    return stringa






