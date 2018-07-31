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

   


def contrighe(name): #contrighe file.txt
    f=open(name,'U')
    linee=f.readlines()
    #lung=len(linee)
    f.close()
    return linee





def trPOST(name,s):     #trova numero riga del <POST>
    f=open(name, 'U')
    lineP=[]
    i=1
    for linea in f:
        if linea.find(s)!=(-1):
            lineP.append(i)     
        i+=1
    f.close()
    #print(lineP)
    return lineP




def trID(lineP,linee):
    alf='0123456789'
    #f=open(name,'U')
    i=0
    listID=[]
    while i!=len(lineP):
        strP=linee[lineP[i]-1]
        #print(strP)
        app=''
        for c in strP:
            if c in alf:
               app+= c
        #print('ID->',app)
        listID.append(app)
        #app=''
        i+=1
    return listID




def alf(s): #4             #elimina noalpha caratteri
    eli='abcdefghijklmnopqrstuvwxyz'
    s=s.lower()
    for c in s:
        #if('c:',c,'not in eli)
        if c not in eli:
            #print('TRUE')
            s=s.replace(c,' ')
    #print(s1)
    return s       




def contr(lsp,ic,passpo,ec):  #3   #splitting x spazio 
    #passpo=False
    #lsp=mascontr(lsp)
    #print(lsp)
    x=len(lsp)
    #eli='abcdefghijklmnopqrstuvwxyz'
    
    for i1 in range(0,x): 
        
        #s1=lsp[i1]
        #s1=alf(s1)        #chiamata alf
        #print('s1:',s1)####################debb
        #print(ec)
        if lsp[i1]==ec:
            #----print('trovato nel post ',ic+1,' ID:',)    
            passpo=True 
            #lsp=0
                 
            break       
    return passpo



def fs(ic,linee,lineP,f,i,listID,ec,insout): #2
    s=''
    #i=1

    passpo=False
    #----print('post',ic+1,':')   
    for l in f:
        if i!=lineP[ic]:
            s=l      
        i+=1  
        
        s=alf(s)#chiamare funzione leva non alpha
        lsp=s.split()
        if passpo==False:
            passpo=contr(lsp,ic,passpo,ec)      #chiamat contr
            if passpo==True:
                insout.add(listID[ic])
                #print('ID:',listID[ic])
        #if passpo==True:
         #   break
         #   print('trovato ciao in linea',i) 
        if not i>lineP[len(lineP)-1]:        
            if i==lineP[ic+1]:
                break
        
    
    #if ic==0: 
    #print(s)
    return i, insout
    





def trPar(name,lineP,listID,lf,linee,ec,insout):  #inizio 1
    
    f=open(name,'U')
    i=1
    for ic in range(0,len(lineP)):
        #print('NEW')
        i, insout=fs(ic,linee,lineP,f,i,listID,ec,insout)
        #print(ic)
    f.close()

    return insout



def post(name,ins):
    s='<POST>'
    linee=contrighe(name)
    lf=len(linee)
    lineP=trPOST(name,s)
    listID=trID(lineP,linee)
    insout=set()
    for ec in ins:
        ec=ec.lower()
        insout=trPar(name,lineP,listID,lf,linee,ec,insout)
        #print(x)
    #print(lineP)
    #print(listID)
    #print(linee[0])
    print(insout)
    return insout

    

#ins={'non','Si'}


#post('file01.txt',ins)





