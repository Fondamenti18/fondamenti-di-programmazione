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


def post(fposts,insieme):
       ''' implementare qui la funzione'''
       IDFINALE2=[]
       IDFINALE=[]
       insieme2=insieme
       
       insieme=low(insieme)
       f=open(fposts,'r') #apre il file
       testo=f.read()           #pone il testo in modalita lettura
       testo=testo.lower()      #trasforama il testo in MAIUSCOLO
       ID=prendiID(testo)      #crea una lista con tutti gli ID

       #devo dividere il testo in stringhe
       TESTO=testo.split('<post>')
       #Elimino il primo spazio
       TESTO=TESTO[1:]
       #visualizzo le stringhe della lista testo
       for elemento in TESTO:
              #•visualizzo ogni singola riga del Testo
              stringa=elemento.split()
              #divido ogni elemento della stringa
              #i e una lista
              el=trovaParola(stringa,insieme2)
              for elmento in el:
                     IDFINALE.append(TESTO.index(elemento))
       for i in IDFINALE:
              IDFINALE2.append(ID[i])
       return set(IDFINALE2)
                  
       
     
def trovaParola(stringa,insieme):
       indiceParola=[]
       for elemento1 in stringa:
                     elemento1=elemento1.lower()
                     for elemento2 in insieme:
                            elemento2=elemento2.lower()
                            if elemento1==elemento2 and len(elemento1)==len(elemento2) and (elemento2 in stringa):
                                 indiceParola.append(stringa.index(elemento1))
                            else:
                                   if len(elemento1)!= len(elemento2) and elemento1[-1]=='?' or elemento1[-1]=='!' or elemento1[-1]=='.': 
                                          elemento=elemento1[:-1]
                                          if elemento==elemento2:
                                                 indiceParola.append(stringa.index(elemento1))
                                   else:
                                          indiceParola+=[]
                            
       return indiceParola
 
       
def Elimina_spazi(testo):
       testo1=''
       for elemento in testo:
              if elemento!=' ':
                     testo1+=elemento       
       return testo1


def prendiID(testo1):
       testo1=Elimina_spazi(testo1)
       testo1=testo1.split('>')
       ID=[]
       for i in testo1:
                     Napp='' 
                     indice=0      
                     while i[indice].isdigit():
                            Napp+=str(i[indice])
                            indice+=1
                            
                     ID.append(str(Napp))
       ID.remove('')
       return ID

def low(insieme):
    l=[]
    for i in insieme:
        l+=[i.lower()]
    return set(l)

