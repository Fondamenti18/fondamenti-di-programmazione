'''
Obiettivo dell'esercizio e' sviluppare la strategia di gioco per il gioco del Mastermind. 

Nel gioco del Mastermind un  giocatore (il "decodificatore"), deve indovinare un  codice segreto.
Il codice segreto e' di N cifre decimali distinte (NO RIPETIZIONI, solo 10 possibili simboli per ciascuna posizione).
Il decodificatore cerca di indovinare il codice per tentativi. Strategicamente  nel tentativo 
possono essere presenti anche cifre ripetute pur  sapendo che nel codice non sono presenti ripetizioni. 
In risposta ad  ogni tentativo viene fornito un aiuto producendo una coppia di interi (a,b) dove:

- a e' il numero di cifre giuste al posto giusto,
cioe' le cifre del codice da indovinare che sono effettivamente presenti nel tentativo al posto giusto.
- b e' il numero di cifre  giuste ma al posto sbagliato,
cioe' le cifre del codice da indovinare che sono effettivamente presenti nel tentativo solo al posto sbagliato.

Ad esempio per il codice
    34670915 e il tentativo
    93375948
la risposta deve essere la coppia (2,3).
Il 2 viene fuori dal contributo delle cifre 7 e 9 del codice da indovinare in quarta e sesta posizione,
il numero 2 e' dovuto alle cifre 3,4,5 che compaiono tra le cifre del tentativo ma mai al posto giusto.

Nella nostra versione di Mastermind il valore di N (lunghezza del codice) puo' essere 6, 7 o 8 e nella coppia data
in  risposta ai tentativi non si vuole rivelare quale delle due due cifre rappresenta il numero di  cifre giuste al posto giusto 
di conseguenza nella coppia di risposta  i valori di a e b possono risultare invertiti.
Ad esempio per il codice 34670915 e il tentativo 93375948 le risposte (2,3) e (3,2) sono entrambe possibili.


Una configurazione del  gioco viene rappresentata come lista di liste (L). 
Il primo elemento di L e' un intero N rappresentante la lunghezza del codice.
Ciascuno degli eventuali altri elementi di L rappresenta un tentativo fin qui
effettuato dal decodificatore e la relativa risposta.
Piu' precisamente  L[i] con i>0, se presente, conterra' una tupla composta da due elementi:
- la lista di N cifre  con il tentativo effettuato dal decodificatore in un qualche passo precedente
- la tupla di interi (a,b) ricevuta in risposta.


Il programma che dovete realizzare contiene la seguente funzione:
 
    decodificatore(configurazione)

che e' l'AI che guida il gioco. La funzione  riceve come input la configurazione attuale del gioco e produce un tentativo (lista di caratteri in '0-9').

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

import random 

# ESEMPIO di strategia che tira a caso una combinazione di N valori anche ripetuti

def decodificatore(configurazione):
    ''' inserire qui la vostra soluzione'''
    #print(configurazione)
    Mastermind=tentativo(configurazione)
    risposta=Mastermind.crea_lista_tentativi(configurazione)
    #print(Mastermind.lstentativi_casuali)
    #print(Mastermind.lsnumeri_si , Mastermind.lsnumeri_no , Mastermind.lsdubbi)
    #print(Mastermind.ls2_0 , Mastermind.ls1_1 , Mastermind.lscombinazione)
    #print(Mastermind.lscombinazione)
    return risposta

class tentativo:
    def __init__(self, configurazione):
        self.lunghezza=configurazione[0]
        self.lstentativi=[]
        self.Ntentativi=0
        self.lsnumeri_si=[]
        self.lsnumeri_no=[]
        self.lsnumeri=[0,1,2,3,4,5,6,7,8,9]
        self.lsdubbi=[] #lista di tuple
        self.lscronologia=[]
        self.lscronologia1=[]
        self.ls2_0=[]
        self.ls1_1=[]
        self.lscombinazione=[]
        #self.lstentativi_casuali=[]
        
    def crea_lista_tentativi(self,configurazione):
        self.lstentativi=[c for c in configurazione]
        self.lstentativi.pop(0)
        self.Ntentativi=len(self.lstentativi)
        return self.analizza_tentativi()
        
        
    def tentativo_Fase0(self):
        if len(self.lsdubbi)>0 and len(self.lsnumeri_si)>0:
            n1=self.lsnumeri_si[0]
            n2=self.lsdubbi[0][0]
            ls=[n1 for i in range(self.lunghezza)]
            ls[0]=n2
            return ls
        if len(self.lsdubbi)>0 and len(self.lsnumeri_no)>0:
            n1=self.lsnumeri_no[0]
            n2=self.lsdubbi[0][0]
            ls=[n1 for i in range(self.lunghezza)]
            ls[0]=n2
            return ls            
        return self.tentativi_iniziali()
    
    def tentativo_Fase1(self):
        if len(self.ls2_0)>0:   #verifica combinazione 2_0
            n0,n1=self.ls2_0[0]
            for n in self.lsnumeri_si:
                if n!=n0 and n!=n1:
                    ls=[n1 for i in range(self.lunghezza)]
                    ls[0]=n
                    return ls
        elif len(self.ls1_1)>0:
            n0,n1=self.ls1_1[0]
            ls=[]
            lsinsi=list(set(self.lsnumeri_si)-set([n0,n1]))
            for n in lsinsi:
                if not (n,n1) in self.ls1_1:
                    ls=[n1 for i in range(self.lunghezza)]
                    ls[0]=n
                    return ls
        elif len(self.ls2_0)==0:
            n0=self.lsnumeri_si[0]
            n1=self.lsnumeri_si[1]
            ls=[n1 for i in range(self.lunghezza)]
            ls[0]=n0
            return ls
    
    def sistema_primoN(self):
        #print('sistema_primoN')
        ok=self.lscombinazione[0]
        lsinsi=list(set(self.lsnumeri_si)-set([ok]))
        lsinsi.sort()
        n=lsinsi[0]
        ls=[self.lscombinazione[i] for i in range(self.lunghezza)]
        ls[1]=n
        return ls        
    
    def tentativo_FaseN(self,t,a,b):
#        elif max(a,b)==(self.lunghezza)-2:
#            return self.tentativo_casuale()
        if max(a,b)<self.lunghezza-2 and min(a,b)==1 and len(set(t) & set(self.lsnumeri_no))==1:
            #print('FaseN min==1')
            ok=[t[i] for i in range(max(a,b))]
            lsinsi=list(set(self.lsnumeri_si)-set(ok))
            lsinsi.sort()            
            #print(self.lsnumeri_si , ok , lsinsi)            
            n=t[len(ok)]
            upgrade=False
            if lsinsi.index(n)==len(lsinsi)-2:
                upgrade=True
            nuovo_n=lsinsi.index(n)+1
            n=lsinsi[nuovo_n]
            ls=[t[i] for i in range(self.lunghezza)]
            ls[max(a,b)]=n
            if upgrade==False:
                return ls
            else:
                a_r=len(set(self.lsnumeri_si) & set(ls))
                config_r=(self.lunghezza,(ls,(a_r,0)))
                Mastermind_ricors=tentativo(config_r)
                Mastermind_ricors.lsnumeri_si=self.lsnumeri_si
                Mastermind_ricors.lsnumeri_no=self.lsnumeri_no
                return Mastermind_ricors.tentativo_FaseN(ls,a_r,0)
        elif max(a,b)==self.lunghezza-2 and min(a,b)==0 and len(set(t) & set(self.lsnumeri_no))==1:
            n0,n1=tuple(set(self.lsnumeri_si)-set(t)-set(self.lsnumeri_no))
            ls=[t[i] for i in range(self.lunghezza)]
            ls[self.lunghezza-2]=n0
            ls[self.lunghezza-1]=n1
            return ls
        elif max(a,b)==self.lunghezza-2 and min(a,b)==2 and len(set(t) & set(self.lsnumeri_no))==0:
            ls=[t[i] for i in range(self.lunghezza)]
            n0=ls[self.lunghezza-2]
            n1=ls[self.lunghezza-1]
            ls[self.lunghezza-2]=n1
            ls[self.lunghezza-1]=n0
            return ls
        elif min(a,b)==0 and len(set(t) & set(self.lsnumeri_no))==1:
            #print('FaseN min==0')
            self.lscombinazione=[t[i] for i in range(self.lunghezza)]
            ok=[self.lscombinazione[i] for i in range(max(a,b))]
            lsinsi=list(set(self.lsnumeri_si)-set(ok))
            lsinsi.sort()
            n=lsinsi[0]
            
            #print(self.lscombinazione , ok , lsinsi)
            
            ls=[self.lscombinazione[i] for i in range(self.lunghezza)]
            ls[self.FaseN()]=n
            return ls            
        
        
        return self.tentativo_casuale()
    
    def Inizio(self):
        return self.Ntentativi==0
    
    def Fase0(self):
        return len(self.lsnumeri_si)==self.lunghezza and len(self.lsnumeri_no)==10-self.lunghezza

    def Fase1(self):
        return len(set(self.lscombinazione) & set(self.lsnumeri_si))==1

    def FaseN(self):
        return len(set(self.lscombinazione) & set(self.lsnumeri_si))
    
    def ultimo_tentativo(self):
        t=len(self.lstentativi)-1
        return self.lstentativi[t]

    def penultimo_tentativo(self):
        t=len(self.lstentativi)-2
        return self.lstentativi[t]

    def trovati_si(self):        
        return len(self.lsnumeri_si)==self.lunghezza
    
    def trovati_no(self):        
        return len(self.lsnumeri_no)==10-self.lunghezza

    def analizza_tentativi(self):
        if self.Inizio():
            return self.tentativi_iniziali()
        
        for i in range(len(self.lstentativi)):        
            t1=self.lstentativi[i]
            n1=t1[0][0]
            n2=t1[0][1]
            a1,b1=t1[1]
            
            if i>0:
                t2=self.lstentativi[i-1]
                n1_2=t2[0][0]
                n2_2=t2[0][1]
                a2,b2=t2[1]
            
            if not self.Fase0(): #self.trovati_si():
                #self.lscronologia.append(False)
                if not n2 in self.lsnumeri_si and not n2 in self.lsnumeri_no:                
                    if a1+b1==2:
                        self.lsnumeri_si.append(n1)
                        self.lsnumeri_si.append(n2)
                    if a1+b1==0:
                        self.lsnumeri_no.append(n1)
                        self.lsnumeri_no.append(n2)
                    if a1+b1==1:
                        self.lsdubbi.append((n1,n2))
                        self.trip_mentale_sui_dubbi()
                else:
                    ris=a1+b1
                    self.gestisci_dubbio(n1,n2,ris)                    
            #else:
                #self.lscronologia.append(True)
            
            self.popola_si_no()
        self.crea_combinazione1()
                
        if not self.Fase0():
            #print('brancolo nel buio')
            return self.tentativo_Fase0()
        
        if not self.Fase1():
            #print('brancolo nel buio')
            return self.tentativo_Fase1()
        
        (j,k)=self.assegna_tentativo(t1[0])
        #print(j,k)
        if j==1 or (j==0 and k==2) or (j==2 and k==0):
            return self.sistema_primoN()                
        return self.tentativo_FaseN(t1[0],a1,b1) #self.tentativo_casuale()
    
    def assegna_tentativo(self,tentativo):
        ls_si=[]
        ls_no=[]
        for t in tentativo:
            if t in self.lsnumeri_si:
                ls_si.append(t)
            else:
                ls_no.append(t)
        return len(set(ls_si)),len(set(ls_no))
    
    def popola_si_no(self):
        if self.trovati_si():
            lsinsi=list(set(self.lsnumeri)-set(self.lsnumeri_si))
            self.lsnumeri_no=[lsinsi[i] for i in range(len(lsinsi))]
            self.lsdubbi=[]
        elif self.trovati_no():
            lsinsi=list(set(self.lsnumeri)-set(self.lsnumeri_no))
            self.lsnumeri_si=[lsinsi[i] for i in range(len(lsinsi))]
            self.lsdubbi=[]
        elif len(self.lsnumeri_si)==self.lunghezza-1 and len(self.lsnumeri_no)==(10-self.lunghezza)-1:
            tpinsi=tuple(set(self.lsnumeri)-(set(self.lsnumeri_si)|set(self.lsnumeri_no)))
            n1,n2=tpinsi
            self.lsdubbi.append((n1,n2))
        return

    def crea_combinazione1(self):
        self.creals_2_0_1_1()
        if len(self.ls2_0)>0:
            self.verificals_2_0()
            if len(self.lscombinazione)==0: self.verificals_1_1()           
        return

    def creals_2_0_1_1(self):
        for tent in range(len(self.lstentativi)):
            t=self.lstentativi[tent]
            t0=t[0]
            t1,t2=t0[0],t0[1]
            at,bt=t[1]
            if max(at,bt)==2 and min(at,bt)==0 and not(t1,t2) in self.ls2_0:
                self.ls2_0.append((t1,t2))
            if max(at,bt)==1 and min(at,bt)==1 and not(t1,t2) in self.ls1_1:
                self.ls1_1.append((t1,t2))
        return
    
    def verificals_2_0(self):
        ls=[0 for i in range(10)]
        for l in self.ls2_0:
            n1,n2=l
            ls[n1]+=1
            ls[n2]+=1
        for l in ls:
            if l>1:
                self.lscombinazione=[self.lsnumeri_no[0] for i in range(self.lunghezza)]
                self.lscombinazione[0]=ls.index(l)
                return
        return
    
    def verificals_1_1(self):
        for l1 in self.ls2_0:                
            n1,n2=l1
            for l2 in self.ls1_1:
                n3,n4=l2
                if n2==n4:
                    self.lscombinazione=[self.lsnumeri_no[0] for i in range(self.lunghezza)]
                    self.lscombinazione[0]=n1                            
                    return
        return

    def gestisci_dubbio(self,n1,n2,ris):
        for i in range(len(self.lsdubbi)):
            if n1 in self.lsdubbi[i]:
                d=self.lsdubbi[i]
                self.lsdubbi.pop(i)
                if n2 in self.lsnumeri_si:
                    if ris==2:
                        self.lsnumeri_si.append(d[0])
                        self.lsnumeri_no.append(d[1])
                    else:
                        self.lsnumeri_no.append(d[0])
                        self.lsnumeri_si.append(d[1])
                else:
                    if ris==1:
                        self.lsnumeri_si.append(d[0])
                        self.lsnumeri_no.append(d[1])
                    else:
                        self.lsnumeri_no.append(d[0])
                        self.lsnumeri_si.append(d[1])
            return
    
    def trip_mentale_sui_dubbi(self):
        if len(self.lsdubbi)==10-self.lunghezza:
            ls=[]
            for j in range(len(self.lsdubbi)):
                for i in range(len(self.lsdubbi[j])):
                    ls.append(self.lsdubbi[j][i])
            lsinsi=list(set(self.lsnumeri)-(set(self.lsnumeri_si)|set(self.lsnumeri_no)|set(ls)))
            for i in range(len(lsinsi)):
                self.lsnumeri_si.append(lsinsi[i])
        return
        
    def sistema_numeri1(self,ls):
        n0,n1=self.numeri_si_first_last()
        if n0 in ls:
            pos_n0=ls.index(n0)
            ls[pos_n0]=n1
            start=pos_n0+1
        else:
            start=0
        for i in range(start,len(ls)):
            if ls[i]==n1:
                ls[i]=n0
                break        
        return ls

    def sistema_numeri2(self,ls,upgrade):
        pos=len(set(ls))-1
        if not upgrade:
            pos-=1
        n0=self.lsnumeri_si[pos]
        n1=self.lsnumeri_no[0]
        if n0 in ls:
            pos_n0=ls.index(n0)
            ls[pos_n0]=n1
            start=pos_n0+1
        else:
            start=0
        for i in range(start,len(ls)):
            if ls[i]==n1:
                ls[i]=n0
                break
        #print (n0 , n1 , self.lsnumeri_si)
        return ls

    def tentativi_iniziali(self):
        ls=[]
        for j in range(len(self.lstentativi)):
            ls+=self.lstentativi[j][0]
        lsinsi=list(set(self.lsnumeri)-set(ls))
        n1=random.choice(lsinsi)
        lsinsi.remove(n1)
        n2=random.choice(lsinsi)
        return self.tentativo_bi_numero(n1,n2)
    
    def tentativo_bi_numero(self,n1,n2):
        lsrisposta=[n2 for i in range(self.lunghezza)]
        lsrisposta[0]=n1
        return lsrisposta

    def tentativo_mono_numero(self,n):
        lsrisposta=[n for i in range(self.lunghezza)]
        return lsrisposta
    
    def tentativo_casuale(self):
        x=''
        for i in range(len(self.lsnumeri_si)):
            x+=str(self.lsnumeri_si[i])
        risposta=[]
        for _ in range(self.lunghezza):
            y=random.choice(x)
            risposta+=[int(y)]
            x=x.replace(y,'')
        return risposta