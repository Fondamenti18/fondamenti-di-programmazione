def decod(pfile, codice):
    '''inserire qui il codice'''
    words=dict()
    risposta=set()
    f=open(pfile,'r')
    linee=f.readlines()
    for linea in linee:
        linea=linea.strip()
        words=dict()
        lista=crea_lista(linea,codice)
        if lista[2]==lista[3]:
            if lista[0]==lista[1]:
                conta=0
                for n in codice:
                    words[n]=linea[conta]
                    conta=conta+1
                wordsok=''
                for n in codice:
                    wordsok+=words.get(n)
                if linea==wordsok:
                    risposta.add(linea)
    return risposta

def crea_lista(linea,codice):
    lista=[]
    lista+=[len(linea)]
    lista+=[len(codice)]
    lista+=[len(set(linea))]
    lista+=[len(set(codice))]
    return lista
    
                
            
        
            
            
        
    
        
        
        
    





