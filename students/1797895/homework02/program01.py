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

'''cerca("file01_40.txt",{"si"})'''

def elspec(chiave):
    chiave=chiave.replace("!","")
    chiave=chiave.replace("?","")
    chiave=chiave.replace(".","")
    chiave=chiave.replace(";","")
    chiave=chiave.replace("@","")
    chiave=chiave.replace("&","")
    chiave=chiave.replace("$","")
    chiave=chiave.replace("#","")
    chiave=chiave.replace(",","")
    chiave=chiave.replace(" ","")
    chiave=chiave.replace("a","")
    chiave=chiave.replace("b","")
    chiave=chiave.replace("c","")
    chiave=chiave.replace("d","")
    chiave=chiave.replace("e","")
    chiave=chiave.replace("f","")
    chiave=chiave.replace("g","")
    chiave=chiave.replace("h","")
    chiave=chiave.replace("i","")
    chiave=chiave.replace("l","")
    chiave=chiave.replace("m","")
    chiave=chiave.replace("n","")
    chiave=chiave.replace("o","")
    chiave=chiave.replace("p","")
    chiave=chiave.replace("q","")
    chiave=chiave.replace("r","")
    chiave=chiave.replace("s","")
    chiave=chiave.replace("t","")
    chiave=chiave.replace("u","")
    chiave=chiave.replace("v","")
    chiave=chiave.replace("x","")
    chiave=chiave.replace("w","")
    chiave=chiave.replace("y","")
    chiave=chiave.replace("z","")
    chiave=chiave.replace("j","")
    chiave=chiave.replace("k","")
    chiave=chiave.replace("è","")
    chiave=chiave.replace("é","")
    chiave=chiave.replace("\"","")
    chiave=chiave.replace("+","")
    chiave=chiave.replace("'","")
    chiave=chiave.replace("à","")
    chiave=chiave.replace("ò","")
    chiave=chiave.replace("ù","")
    chiave=chiave.replace(":","")
    chiave=chiave.replace("_","")
    chiave=chiave.replace("=","")
    chiave=chiave.replace("_","")
    chiave=chiave.replace("*","")
    chiave=chiave.replace("(","")
    chiave=chiave.replace(")","")
    chiave=chiave.replace("{","")
    chiave=chiave.replace("}","")
    chiave=chiave.replace("]","")
    chiave=chiave.replace("[","")
    chiave=chiave.replace("-","")
    chiave=chiave.replace("°","")
    chiave=chiave.replace("#","")
    chiave=chiave.replace("ã","")
    chiave=chiave.replace("¬","")    
    chiave=chiave.replace("²","")    
    chiave=chiave.replace("¨","")    
    chiave=chiave.replace("ˆ","")    

    return chiave

def cerca(nome_file,ricerca):
    import re
    ls=[]
    f=open(nome_file, "r", encoding="UTF-8")
    stringa=f.read()
    stringa=stringa.split("<POST>")
    for x in ricerca:
        for a in stringa:
            ciao=''
            aiuto=''
            ciao=a
            ciao=ciao.lower()
            if re.search(r'\b' + x.lower() + r'\b' ,ciao) != None:
                '''ciao=elspec(ciao)'''
                ciao=ciao.replace("\n","")
                ciao=ciao.replace(" ","")
                m=list(ciao)
                i=0
                c=0
                st=''
                while(c==0):
                    if(m[i]=="0" or
                       m[i]=="1" or
                       m[i]=="2" or
                       m[i]=="3" or
                       m[i]=="4" or
                       m[i]=="5" or
                       m[i]=="6" or
                       m[i]=="7" or
                       m[i]=="8" or
                       m[i]=="9"):
                        st=st+m[i]
                        i=i+1
                    else:
                        c=c+1
                ls.append(st)
    return set(ls)
       
        
    

def post(nome_file,ricerca):
    """scrivere qui il programma"""
    insieme=cerca(nome_file,ricerca)
    return(insieme)
