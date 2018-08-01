

from  my_html import HTMLNode, fparse

def cercaid(nodo, valore,conta):
     if not nodo.istext():
         for figlio in nodo.content:
             if(valore in figlio.attr.values()):
                 conta+=1
             conta=cercaid(figlio,valore,conta)
     return conta
'''def cercac(nodo,valore):
     nodi=[]
     print(valore)
     if valore in nodo.attr['class']:
         nodi+=[nodo]
     if not nodo.istext():
         for figlio in nodo.content:
             nodi+=cercaa(figlio,valore)
     return nodi'''
  
                      
'''def cercac(nodo,valore,conta):
     if not nodo.istext():
         for figlio in nodo.content:
             if(valore in figlio.attr['class'].values()):
                 conta+=1
             conta+=cercaid(figlio,valore,conta)
     return conta  '''
'''def cercaa(nodo, valore,conta):
     if not nodo.istext():
         for figlio in nodo.content:
             print(figlio.attr.values())
             if(valore in figlio.attr.values()):
                 conta+=1
                 conta+=cercaid(figlio,valore,conta)
     return conta    '''     
def cercat(nodo,s,conta):
     if not nodo.istext():
         for figlio in nodo.content:
             if(figlio.tag==s):
                 conta+=1
                 conta+=cercat(figlio,s,conta)
     return conta                        

def cercac(nodo,valore):
     nodi=[]
     if valore in nodo.attr.values():
         nodi+=[nodo]
     if not nodo.istext():
         for figlio in nodo.content:
             nodi+=cercaa(figlio,valore)
     return nodi
def cercaTag(nodo,t):
     nodi=[]
     if nodo.tag==t:
         nodi+=[nodo]
     if not nodo.istext():
         for figlio in nodo.content:
             nodi+=cercaTag(figlio,t)
     return nodi
    
def cercaa(nodo,valore):
     nodi=[]
     if valore  in nodo.attr:
         nodi+=[nodo]
     if not nodo.istext():
         for figlio in nodo.content:
             nodi+=cercaa(figlio,valore)
     return nodi

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    contaid=0
    contat=0
    contac=0
    contaa=0
    sel=selettore.split()
    radice=fparse(fileIn)
    print(radice)
    conta=0
    for s in sel:
        if radice.tag==s:
            conta=1
        else:
            conta=0
        contat=len(cercaTag(radice,s))
        if s.startswith('#'):
            valore=s[1:]
            print(valore)
            print(radice.attr)
            if valore in radice.attr.keys():
                conta=1
            else:
              conta=0
            contaid=cercaid(radice,valore,conta)
        if s.startswith('.'):
            valore=s[1:]
            print(valore)
            print(radice.attr)
            if valore in radice.attr.keys():
                conta=1
            else:
              conta=0
            contac=len(cercac(radice,valore)) +conta 
        if s.startswith('@'):
            valore1=s[2:-1]
            valore=valore1.split('=')
            
            if valore[0] in radice.attr.keys():
                conta=1
            else:
              conta=0
              contaa=len(cercaa(radice,valore[0])) 
        
    print(contaid+contac+contaa)
    return contaid+contac+contaa+contat
        
def elimina(nodo,s):
    if nodo.istext():
        return
    for figlio in nodo.content:
        elimina(figlio,s)
    nuovo=[]
    for figlio in nodo.content:
        if s in figlio.attr.values():
            nuovo+=figlio.content
        else:
            nuovo+=[figlio]
    nodo.content=nuovo

def trovaTag(nodo,t):
     if nodo.tag==t:
         return True
     return False       

def trovaTag1(nodo,sel):
    nodi=[]
    if(trovaTag(nodo,sel[0])==0):
        return nodi
    else:
        del(sel[0])
        if not nodo.istext():
            for figlio in nodo.content:
                if trovaTag(figlio,sel[0]):
                    nodi+=[figlio]
        return nodi
             
def cercanodi(nodo,s):    
    nodi=[]
    if nodo.istext():
        return
    for figlio in nodo.content:
        if trovaTag(figlio,s):
            nodi+=[figlio]
    return nodi

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    '''sel=selettore.split()'''
    radice=fparse(fileIn)
    elimina(radice,selettore)
    with open (fileOut,'w') as f:
        f.write(radice)
     
    
    

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    radice=fparse(fileIn)
    sel=selettore.split()
    
    nodi=trovaTag1(radice,sel)
    print(nodi.tag)
    for n in nodi:
        n.attr[chiave]=valore
        
    with open (fileOut,'w') as f:
        f.write(radice)
        
