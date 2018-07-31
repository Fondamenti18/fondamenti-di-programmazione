import re         
def post(fposts,insieme):
    lista_insieme=list(insieme)
    lista=[]
    momentaneo= -1
    with open(fposts, encoding='utf-8')as f:
        for riga in f:
            if riga.find('<POST>')!=-1:
                pid=sempl_post(riga)
            else:
                if pid!=momentaneo:
                    riga=semplifica(riga)
                    for h in lista_insieme:
                        elem=semplifica(h)
                        if riga.find(elem)!=-1:
                            lista.append(pid)
                            momentaneo=pid
        risultato=set(lista)
        return risultato
    

def semplifica(elemento):
    elemento1=re.sub('[^a-zA-Z 0-9]', ' ', elemento)
    elemento2=elemento1.lower()
    risultato=' '+elemento2+' '
    return risultato
    
def sempl_post(post):
      post1=post.replace('<POST>', ' ')
      post2=post1.replace('\n', ' ')
      risultato=post2.replace(' ', '')   
      return risultato
  
    
    
    
    
    
    
    
    