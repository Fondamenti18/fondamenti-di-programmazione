'''
Obiettivo dell'esercizio e' sviluppare la strategia di gioco per il gioco del Mastermind. 

Nel gioco del Mastermind un  giocatore (il "decodificatore"), deve indovinare un  codice segreto.
Il codice segreto e' di N cifre decimali distinte (NO RIPETIZIONI, solo 10 possibili simboli per 
ciascuna posizione).
Il decodificatore cerca di indovinare il codice per tentativi. Strategicamente  nel tentativo 
possono essere presenti anche cifre ripetute pur  sapendo che nel codice non sono presenti 
ripetizioni. 
In risposta ad  ogni tentativo viene fornito un aiuto producendo una coppia di interi (a,b) dove:

- a e' il numero di cifre giuste al posto giusto,
cioe' le cifre del codice da indovinare che sono effettivamente presenti nel tentativo al posto 
giusto.
- b e' il numero di cifre  giuste ma al posto sbagliato,
cioe' le cifre del codice da indovinare che sono effettivamente presenti nel tentativo solo al 
posto sbagliato.

Ad esempio per il codice
    34670915 e il tentativo
    93375948
la risposta deve essere la coppia (2,3).
Il 2 viene fuori dal contributo delle cifre 7 e 9 del codice da indovinare in quarta e sesta 
posizione,
il numero 2 e' dovuto alle cifre 3,4,5 che compaiono tra le cifre del tentativo ma mai al 
posto giusto.

Nella nostra versione di Mastermind il valore di N (lunghezza del codice) puo' essere 6, 
7 o 8 e nella coppia data
in  risposta ai tentativi non si vuole rivelare quale delle due due cifre rappresenta il 
numero di  cifre giuste al posto giusto 
di conseguenza nella coppia di risposta  i valori di a e b possono risultare invertiti.
Ad esempio per il codice 34670915 e il tentativo 93375948 le risposte (2,3) e (3,2) sono 
entrambe possibili.


Una configurazione del  gioco viene rappresentata come lista di liste (L). 
Il primo elemento di L e' un intero N rappresentante la lunghezza del codice.
Ciascuno degli eventuali altri elementi di L rappresenta un tentativo fin qui
effettuato dal decodificatore e la relativa risposta.
Piu' precisamente  L[i] con i>0, se presente, conterra' una tupla composta da due elementi:
- la lista di N cifre  con il tentativo effettuato dal decodificatore in un qualche passo 
precedente
- la tupla di interi (a,b) ricevuta in risposta.


Il programma che dovete realizzare contiene la seguente funzione:
 
    decodificatore(configurazione)

che e' l'AI che guida il gioco. La funzione  riceve come input la configurazione attuale 
del gioco e produce un tentativo (lista di caratteri in '0-9').

Per questo esercizio la valutazione avverra' nel seguente modo: 
avete 150 tentativi e 30 secondi di tempo per indovinare quanti piu' codici possibile.
Il punteggio ottenuto e' dato dal numero di codici che riuscite ad indovinare.

Tutti i vostri elaborati al termine verranno valutati su di uno stesso set di codici,
questa operazione  determinera' una classifica dei vostri elaborati.
Per entrare in classifica bisogna indovinare almeno cinque codici.
La classifica viene suddivisa in 14 fasce che corrispondono ai voti da 18 a 31 ed a 
ciascun programma viene assegnato il voto corrispondente.
Se il numero di valori diversi e' minore di 14 il voto sara' proporzionale alla posizione
nella graduatoria (con il primo che prende 31 e l'ultimo 18)

In allegato vi viene fornito un  simulatore di gioco (simulatore1.py) che vi permettera' di 
autovalutare la vostra strategia. Il simulatore genera  codici casuali e invoca il vostro 
programma per ottenere i vari tentativi. Appena un codice  viene indovinato ne viene 
proposto uno nuovo. Il processo termina quando avete esaurito i vostri 150 tentativi
o sono passati  i 30 secondi.

ATTENZIONE: NON usate lettere accentate ne' nel codice ne' nei commenti
'''



# ESEMPIO di strategia che tira a caso una combinazione di N valori anche ripetuti
ban=[]
pino=0
ris=[]
gino=0
ite=0
gite=0
trovato=False
l=[]
ita=0
indice=0
giga=False
ito=0


def sceglipino():
    global l
    global pino
    
    trova=False
    i=pino 
    while i<=9 and trova==0:
        if i in l:
            trova=True
        else:
            i=i+1
    pino=i
    return pino
    

def ottogino1(gino,n):
           
            global l
            global trovato
            

            l.append(gino)
            l.append(gino+1)
           
            trovato=True

def ottogino2(gino,n,k):
            
            global ris
            

            for x in range (len(ris)):
                k.append(ris[x])
            for x in range(len(ris),n):
                k.append(8)
            return k
 
def contacifre(ris,n):
    cifre=n-ris.count("a")
    p_cifre=[]
    p=0
    d=0
    while d<cifre:
        gu=0
        while p<n and gu==0:
            if str(ris[p]).isdigit():
                gu=1
            p=p+1
        p_cifre.append(p-1)
        d=d+1
    return p_cifre
            

def ottogino(gino,n,v,i):


    global trovato
    global l
    
    
    
    
    if v[i-2]==(0, 1) or v[i-2]==(1, 0):
        l.append(8)
        
    else:
        l.append(9)
        
        trovato=True

def novegino(gino,n,k):
    global l
    global ris
    global trovato
    global gite

    if len(l)>=n:
        trovato=True
    elif gino ==9 and  len(l)==n-1:
            l.append(gino)
            trovato=True
    else:
        k=[]
        for x in range (len(ris)):
            k.append(ris[x])
        for x in range(len(ris),n):
            k.append(9)
        gite=True 
        
    return k

def settegino3(gino,n):

    global ris
    global trovato
    global gite

    l.append(gino)
   
    l.append(gino+1)
    
    l.append(gino+2)
 
    trovato=True

def settegino2(gino,n,k):
  
    global ris
    
    global gite
                    
    for x in range (len(ris)):
        k.append(ris[x])
    for x in range(len(ris),n):
        k.append(7)
    gite=True  
    return k

def settegino(gino,n,k):
   
    global ris
   
   
    for x in range (len(ris)):
        k.append(ris[x])
    for x in range(len(ris),(n-len(ris))//2):
        k.append(gino)
    for x in range((((n-len(ris))//2)),n):
        k.append(gino+1)
    return k           

def decodificatore(configurazione):
    global ban
    global gino
    global ite
    global ris
    global trovato
    global gite
    global pino
    global l
    global ita
    global indice
    global giga
    global ito

        
    n=configurazione[0]

    i=len(configurazione)
    v=[]
 
    k=[]
    risposta=[] 
    
    if len(configurazione)==1:
        ban=[]
        pino=0
        ris=[]
        gino=0
        ite=0
        gite=0
        trovato=False
        l=[]
        ita=0
        indice=0
        giga=False
        ito=0
  
    for x in range(1,len(configurazione)):
        v.append(configurazione[x][1])

    if gite ==0:
        for t in range(n):
            k.append(gite)
       
    if 0 < gite and gite < 10:
        
        for t in range(n):
            k.append(gite)
        if v[i-2]==(1,0) or v[i-2]==(0,1):
            l.append(gite-1)
        
    if gite==10:
        if v[i-2]==(1,0) or v[i-2]==(0,1):
            l.append(gite-1)
        
        trovato=True
    gite+=1    

      
      
    if trovato ==True:
     gino=0
     
     if ris==[]:
      for x in range(n):
          ris.append("a")
      giga=False   
      
      
     if giga==False:
      #print("ita",ita)
        
      if ita==0:
        k=[]        
        
        
        pino=l[0]
        k.append(l[0])        
        for x in range(len(k),(n-1)):
            k.append(10)
        k.append(l[-1]) 
        
      elif ita==1:
          k=[]
          k.append(10)
          k.append(l[0])
          for x in range(len(k),(n-1)):
              k.append(10)
          k.append(l[-1]) 
          ita=1
      
      elif ita==2:
          k=[]
          if v[i-3]==(1,1):
              if v[i-2]==(1,1):
                  for x in configurazione[-1][0]:
                     k.append(x)
                  indice =2
                  ris[n-1]=k[n-1]
                  
                  l.remove(k[n-1])
                  
                  k=[]
                  for x in range(len(ris)):
                      if ris[x]=="a":
                          k.append(10) 
                      else:
                          k.append(ris[x])
                  k[indice]=l[0]
                

                  ita=3
              else:
                  indice=2
                  k=[]
                  for x in range(0,indice):
                      k.append(10)                 
                  k.append(l[0])
                  for x in range(indice+1,(n-1)):
                      k.append(10)
                  k.append(l[-1]) 
                  ita=2
          elif v[i-3]==(2,0) or v[i-3]==(0,2):
              if v[i-2]==(1,1):
                  indice =2
                  k=[]
                  for x in range(0,indice):
                      k.append(10)                 
                  k.append(l[0])
                  for x in range(indice+1,(n-1)):
                      k.append(10)
                  k.append(l[-1])
                  ita=4
              elif v[i-2]==(2,0) or v[i-2]==(0,2):
                  indice =2
                  k=[]
                  for x in range(0,indice):
                      k.append(10)                 
                  k.append(l[0])
                  for x in range(indice+1,(n-1)):
                      k.append(10)
                  k.append(l[-1])  
                  ita=5
                 
      elif ita==6:
           k=[]
           for x in configurazione[-1][0]:
               k.append(x)
           if v[i-2]==(1,1):
             ris[indice]=k[indice]
             
             l.remove(k[indice])
     
             ito=0
             giga=True
           else:
             k=[]
             indice+=1
             for x in range(0,indice):
                  k.append(10)                 
             k.append(l[0])
             for x in range(indice+1,(n-1)):
                  k.append(10)
             k.append(l[-1])            
             ita=5

      elif ita==5:
          k=[]
          for x in configurazione[-1][0]:
               k.append(x)          
          if v[i-2]==(1,1):
             ris[n-1]=k[n-1]
            
             l.remove(k[n-1])
             ris[0]=k[indice]
             
             l.remove(k[indice])
      
             ito=0
             giga=True
          else:
             ris[1]=k[indice]
            
             l.remove(k[indice]) 
             
             ito=0
             giga=True
      elif ita==3:
          
          k=[]
          for x in configurazione[-1][0]:
             k.append(x)         
          if v[i-2]==(1,1):
             ris[n-1]=k[n-1]
             
             l.remove(k[n-1])
             ris[1]=k[indice]
             
             l.remove(k[indice])
      
             ito=0
             giga=True
          else:
            ris[0]=k[indice]
            
            l.remove(k[indice])
       
            ito=0            
            giga=True
      elif ita==4:
         k=[]
         for x in configurazione[-1][0]:
             k.append(x)
         if v[i-2]==(len(ris)-len(l),1) or v[i-2]==(1,len(ris)-len(l)):
             indice+=1
             k=[]
             for x in range(0,indice):
                 k.append(10)                 
             k.append(l[0])
             for x in range(indice+1,(n-1)):
                 k.append(10)
             k.append(ris[-1]) 
             ita=3
         else:
             ris[indice]=k[indice]
          
             l.remove(k[indice])
       
       
             ito=0
             giga=True
      ita=ita+1
     
     if giga==True:
       #print("ito",ito)
       
       if ((len(ris)-ris.count("a"))>=1 and ris.count("a")>2):
         if ito==0:
             #print("sono ito", ito)
             indice=0
            
             k=[]
             for x in range(len(ris)):
                  if ris[x]=="a": 
                      k.append(10)
                  else:
                      k.append(ris[x])
             ind=0
             for z in range(len(k)):
                 if k[z]==10:
                     ind=z
        
             k[ind]=l[0]
             ito=0 
         elif ito==1:  
             p_cifre=contacifre(ris,n)
             k=[]
             for x in range(n):
                 k.append(10)                 
             for r in p_cifre:
                 k[r]=ris[r]
             ind=0
             for z in range(len(k)):
                 if k[z]==10:
                     ind=z                 
             if v[i-2]==(len(ris)-len(l),1) or v[i-2]==(1,len(ris)-len(l)):
       
                 indice=indice+1
                 #print("k",k)
                 #print("l",l)
                 #print("ind",ind)
                 #print("indice",indice)
                 k[ind]=l[indice]
                 
                 ito=0 
             elif v[i-2]==(len(ris)-len(l)+1,0) or v[i-2]==(0,len(ris)-len(l)+1):
                ris[ind]=configurazione[-1][0][ind]
           
                l.remove(ris[ind])
          
                indice=0
                k=[]
                for x in range(n):
                    k.append(10)  
                p_cifre=contacifre(ris,n)
                for r in p_cifre:
                    k[r]=ris[r]
                ind=0
                for z in range(len(k)):
                  if k[z]==10:
                     ind=z                 
     
                k[ind]=l[0]
                ito=0
             else:
                  #print("non lo deve fare")
                  ito=0
                 
       elif ris.count("a")==2:
           
               
           for r in ris:
               k.append(r)
           
           
           if v[i-2]==(len(k)-2,2) or v[i-2]==(2,len(k)-2):
               if len(l)==1:
                   k.insert(k.index("a"),l[0])
                   k.remove("a")
               else:
                   k.insert(k.index("a"),l[1])
                   k.remove("a")
                   k.insert(k.index("a"),l[0])
                   k.remove("a")
           else:
              if len(l)==1:
                  k.insert(k.index("a"),l[0])
                  k.remove("a")
              else:
                  k.insert(k.index("a"),l[0])
                  k.remove("a")
                  k.insert(k.index("a"),l[1])
                  k.remove("a")
               
           
           
            
                  
       ito=ito+1            

                         
                 
                 
         
         

            
    

    
    
    risposta=[]
    for x in range(len(k)):
        risposta.append(k[x])
            
    #print("cifre definitive", globalvar.keys())
    #print("cifre definitive", l)
    #print("the huge complete ris", ris)
    #print("the true answer", risposta)
    #print("risp pls", globalvar)
    return risposta
