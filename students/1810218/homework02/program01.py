'''
I post di un forum sono raccolti in alcuni file che hanno il seguente formato. 
Un file contiene uno o piu' post, l'inizio di un post e' marcato da una linea che contiene
in sequenza le due sottostringhe "<POST>" ed "N" (senza virgolette) eventualmente 
inframmezzate, precedute e/o seguite da 0,1 o piu' spazi. 
"N" e' l'ID del post (un numero positivo).  
Il contenuto del post e' nelle linee successive fino alla linea che marca il prossimo post 
o la fine del file (si veda ad esempio il file "file01.txt"). 
E' assicurato che la stringa "<POST>" non e' contenuta in nessun post.

Nel seguito per parola intendiamo come al solito una qualsiasi sequenza di caratteri
alfabetici di lunghezza massimale. I caratteri alfabetici sono quelli per cui
ritorna True il metodo isalpha().

Scrivere una funzione post(fposts,insieme) che prende in input:
- il percorso di un file (fposts) 
- ed un insieme  di parole (insieme)
e che restituisce un insieme (risultato).

L'insieme restituito (risultato) dovra' contenere gli identificativi (ID) dei post 
che contengono almeno una parola dell'inseme in input.
Due parole sono considerate uguali anche se  alcuni caratteri alfabetici compaiono in una 
in maiuscolo e nell'altra in minuscolo.

Per gli esempi vedere il file grade.txt

AVVERTENZE:
	non usare caratteri non ASCII, come le lettere accentate;
	non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
'''
        
def uguali(parola1,parola2):
    l=[]
    if len(parola1)!=len(parola2):
        return False
    else:
        pos=0
        while pos<len(parola1):
            if parola1[pos]==parola2[pos] or ord(parola1[pos])==ord(parola2[pos])+32 or ord(parola1[pos])==ord(parola2[pos])-32:
                l.append(1)
            pos+=1
        if len(l)==len(parola1):
            return True
        else:
            return False    
    









def post(fposts,insieme):
    f=open(fposts,'r')
    ris=[]
    
    linee=f.readlines()
   
    for linea in linee:
        
        
        linea=linea.split()
        
        for parola1 in insieme:
            for parola2 in linea:
                
                if parola2[len(parola2)-1]=='.' or parola2[len(parola2)-1]=='?' or parola2[len(parola2)-1]==':' or parola2[len(parola2)-1]=='!' or parola2[len(parola2)-1]==',' or parola2[len(parola2)-1]==';':
                    
                    if uguali(parola1,parola2) or uguali(parola1,parola2[:len(parola2)-1]):
                        linea=' '.join(linea)+'\n'
                        pos=linee.index(linea)
                        linea=linea.split()
                
                        while '<POST>' not in linee[pos]:
                            pos=pos-1
                        ris.append(linee[pos])
                        
                elif parola2[len(parola2)-1].isalpha:
                    if uguali(parola1,parola2):
                        linea=' '.join(linea)+'\n'
                        pos=linee.index(linea)
                        linea=linea.split()
                
                        while '<POST>' not in linee[pos]:
                            pos=pos-1
                        ris.append(linee[pos])
    
                        
            
            
        
        
     
    
    
    
    
    
    
    
    
    
    
    
    
    f.close()
    
    
      
    
    
    
    for pos in range(len(ris)):
        ris[pos]=ris[pos].replace('<','')
        ris[pos]=ris[pos].replace('>','')
        ris[pos]=ris[pos].replace('P','')
        ris[pos]=ris[pos].replace('O','')
        ris[pos]=ris[pos].replace('S','')
        ris[pos]=ris[pos].replace('T','')
        ris[pos]=ris[pos].replace('\n','')
        ris[pos]=ris[pos].replace(' ','')
    

            
    
    
  
                
    risultato=set(ris)    
    return risultato
'''
import os
os.chdir('C:\\Users\\andre\\Desktop\\homework02\\es1')



        
def uguali(parola1,parola2):
    l=[]
    if len(parola1)!=len(parola2):
        return False
    else:
        pos=0
        while pos<len(parola1):
            if parola1[pos]==parola2[pos] or ord(parola1[pos])==ord(parola2[pos])+32 or ord(parola1[pos])==ord(parola2[pos])-32:
                l.append(1)
            pos+=1
        if len(l)==len(parola1):
            return True
        else:
            return False    
    









def post(fposts,insieme):
    f=open(fposts,'r')
    ris=[]
    
    linee=f.readlines()
   
    for linea in linee:
        
        
        linea=linea.split()
        
        for parola1 in insieme:
            for parola2 in linea:
                for x in parola2:
                    if x.isalpha==False:
                        parola2.replace(x,'')
                        
                        
                if uguali(parola1,parola2) or uguali(parola1,parola2[:len(parola2)-1]):
                    linea=' '.join(linea)+'\n'
                    pos=linee.index(linea)
                    linea=linea.split()
                    while '<POST>' not in linee[pos]:
                        pos=pos-1
                    ris.append(linee[pos])
    
                        
            
            
        
        
     
    
    
    
    
    
    
    
    
    
    
    
    
    f.close()
    
    
      
    
    
    
    for pos in range(len(ris)):
        ris[pos]=ris[pos].replace('<','')
        ris[pos]=ris[pos].replace('>','')
        ris[pos]=ris[pos].replace('P','')
        ris[pos]=ris[pos].replace('O','')
        ris[pos]=ris[pos].replace('S','')
        ris[pos]=ris[pos].replace('T','')
        ris[pos]=ris[pos].replace('\n','')
        ris[pos]=ris[pos].replace(' ','')
    

            
    
    
  
                
    risultato=set(ris)    
    return risultato
'''

                
        


