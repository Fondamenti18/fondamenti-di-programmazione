'''
import re

from collections import Counter
def post(fposts,insieme):
    f=open(fposts,encoding='UTF-8')
    dati=f.read()
    f.close() 
    
    print(re.match(r'<POST>',dati))
    
def post(fposts,insieme):
    try:
        file=open(fposts,"r",encoding='UTF-8')
        leggi=file.readlines()   
        file.close()
        for parola in insieme:
            lower= parola.lower()
            conta=0
            for frasi in leggi:
                linea = frasi.split()
                for ciascuna in linea:
                    linea2= ciascuna.lower()
                    linea2=linea2.strip("!@.?#_")
                    if lower==linea2:
                        conta +=1
                        print (linea)                    
                    for linea2 in reversed(list(linea)):                      
                        if(linea2==int):
                            print (ciascuna)
            print(lower,":",conta)
        return (lower)
    except FileExistsError:
        print("File non presente") 
        '''
def post(fposts,insieme):
        post_num=[]
        apertura=open(fposts, encoding = 'utf-8')
        lista=[]
        try:
            with apertura as f:          
                    for a_pulita in f.readlines():            
                        a_pulita=a_pulita.lower().replace('>'," ").split()
                        pul=range(len(a_pulita))
                        for parola in pul:          
                            a_pulita[parola] = (a_pulita[parola]).strip("'!@.;^?!,:")            
                            if (a_pulita[parola]=='<post'): 
                                lista += [a_pulita[parola+1]]               
                            for e in insieme:                                                               
                                if e.lower() == a_pulita[parola]:
                                    (post_num) += [lista[-1]]
        except FileExistsError:
            print("Errore")
        return set(post_num)		 