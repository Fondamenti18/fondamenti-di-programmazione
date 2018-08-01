


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
    num='0123456789'
    fileT=open(fposts, 'r')
    punt=['.',',',':','!','-','_','+','=','?']
    b=list(insieme)
    testo=str(fileT.read())
    fileT.close()
    for item in punt:
            testo=testo.replace(item,' ')

    testo=testo.split('<POST>')
#    print(testo)
 #   app=''
  #  for i,v in enumerate(testo):
   #     for c in v:
    #        if c.isalpha() or c in num:
     #         app+=c
      #      else:
       #         app+=' '
       # testo[i]=app
        #app=''
    
   # print(testo)
    #for i in testo:
    #    print('********',i)
    #controllo='<POST>'
   
    #alf='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    
    insiemePid=set([])    
    for ogg in b:
        
        pid=''
        for i in testo:
            
            appOgg=ogg.lower()
            appI=i.lower()
            succ=appI[appI.find(appOgg)+len(appOgg)]
            prec=appI[appI.find(appOgg)-1]
            #if appI.find(appOgg)!=-1:
             #   print(appI.find(appOgg)+len(appOgg),appOgg,prec,succ)
           # if appI.find(' '+appOgg+' ')!=-1  or (appI.find(' '+appOgg)!=-1 and appI[appI.find(' '+appOgg)+len(appOgg)].isalpha()==False)  :
            if (appI.find(appOgg)!=-1 and succ.isalpha()==False and prec.isalpha()==False) or appI.find(' '+appOgg+' ')!=-1  :
                pid=''
                c=0
                
                while i[c]==' ':
                #    print(i[c],c,i,len(i))
                    c+=1
                app=c
                for c in range(app,app+5):
                    
                    if i[c] in num:
                        pid+=i[c]
                insiemePid.add(pid)
                
    #print(insiemePid)
    return insiemePid
                
#print(post('file01.txt',{'return'}))
        


