
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
    '''inserire qui la vostra implementazione'''
    parolaCrittografata=''
    diz=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    CHIAVE_DISORDINATA= modifica_chiave(diz,chiave)
    CHIAVE_ORDINATA= ordina_chiave(CHIAVE_DISORDINATA)
    #print(CHIAVE_DISORDINATA)
    #print(CHIAVE_ORDINATA)
    DICTT=corr(CHIAVE_DISORDINATA,CHIAVE_ORDINATA)
    for elemento in testo:
           if elemento==' ':
                  parolaCrittografata+=' '
           elif elemento not in DICTT:
                  parolaCrittografata+=elemento
           else:
                  parolaCrittografata+=DICTT[elemento]
    return parolaCrittografata

#========================================================================================================   
    
def decodifica(chiave,testo):
    '''inserire qui la vostra implementazione'''
    parolaDecodificata=''
    diz=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    CHIAVE_DISORDINATA= modifica_chiave(diz,chiave)
    CHIAVE_ORDINATA= ordina_chiave(CHIAVE_DISORDINATA)
    #print(CHIAVE_DISORDINATA)
    #print(CHIAVE_ORDINATA)
    DICTT=corr(CHIAVE_ORDINATA,CHIAVE_DISORDINATA)
    for elemento in testo:
           if elemento==' ':
                  parolaDecodificata+=' '
           elif elemento not in DICTT:
                  parolaDecodificata+=elemento
           else:
                  parolaDecodificata+=DICTT[elemento]
    return parolaDecodificata

#====================================================================================================
def corr(CHIAVE_DISORDINATA,CHIAVE_ORDINATA):
       dictt={}
       for i in CHIAVE_ORDINATA:
              count=0
              while count!=1:
                     dictt[i]=CHIAVE_DISORDINATA[count]
                     CHIAVE_DISORDINATA=CHIAVE_DISORDINATA.replace(CHIAVE_DISORDINATA[0],'')
                     count+=1
       return dictt
              
       
                     

#=================================================================================================================
def ordina_chiave(nuovaChiave):
       '''prende la chiave e la rende ordinata (in base all alfabeto)'''
       nuovaStringa='' #nuova stringa che conterra i caratteri in modo ordinato
       lista_chiave=[] #lista che utilizzo per mettere dentro gli elementi della stringa
       for elemento in nuovaChiave:
              lista_chiave+=elemento #prendo ogni elemento della chiave e lo metto dentro alla lista
       lista_chiave.sort() #ordino la lista
       for elemento in lista_chiave:
              nuovaStringa+=elemento #metto gli elementi nella stringaa(in modo ordinato)
       return nuovaStringa


#=================================================================================================================    
def modifica_chiave(diz,chiave):
       '''prende la chiave e la trasforma nella nuova chiave senza ricorrenze e composta solo dai caratteri che 
       vanno da A a Z'''
       nuovaChiave=''
       chiaveFin=''
       
       for lettera in chiave:
           if lettera in diz:
                  nuovaChiave+=lettera
       
                
       countLettere=0
       while countLettere<len(nuovaChiave):
              countRicorrenza=nuovaChiave.count(nuovaChiave[countLettere])
              if countRicorrenza>1:
                     chiaveFin= nuovaChiave.replace(nuovaChiave[countLettere],'',(countRicorrenza-(countRicorrenza-1)))
                     nuovaChiave=chiaveFin
                     countLettere=countLettere
              else:
                     countLettere+=1
              
       return nuovaChiave
