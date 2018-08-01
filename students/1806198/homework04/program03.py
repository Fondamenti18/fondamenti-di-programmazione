from  my_html import HTMLNode, fparse

#-----Funzione globale----#

#dato l input, ritorna un indice di riconoscimento e 2 parametri per la ricerca ricorsiva
def elabora_selettore(selettore):
    if selettore[0]=='.':
        return 1,selettore[1:],''
    
    elif selettore[0]=='#': 
        return 2,selettore[1:],''
    
    elif selettore[0]=='@': 
        pos=selettore.index('"');
        s1=selettore[2:selettore.index('=')]
        s2=selettore[pos:selettore.index('"',pos)] 
        return 3,s1,s2
    
    elif selettore.find('>')>0: 
        pos=selettore.index('>')
        s1=selettore[0:pos]
        s2=selettore[pos+1:]
        return 5,s1.strip(),s2.strip()
    
    elif selettore.find(' ')>0: 
        selettore=selettore.lstrip()
        pos=selettore.index(' ')
        s1=selettore[0:pos]
        s2=selettore[pos+1:]
        return 4,s1.strip(),s2.strip()
    
    return 0,selettore,'' 



#-----Blocco numero 1----#

def conta0(albero,selettore,att,flag=False):
    cnt=0
    for child in albero.content:
        if child.istext()==False:
            if child.tag==selettore: cnt+=1
            cnt+=conta0(child,selettore,att)
    return cnt

def conta1(albero,selettore,att,flag=False):
    cnt=0
    for child in albero.content:
        if child.istext()==False:
            if 'class' in child.attr.keys():
                if child.attr.get('class').find(selettore)>=0:cnt+=1
            cnt+=conta1(child,selettore,att)
    return cnt

def conta2(albero,selettore,att,flag=False):
    cnt=0
    for child in albero.content:
        if child.istext()==False:
            if child.attr.get('id')==selettore:cnt+=1
            cnt+=conta2(child,selettore,att)
    return cnt

def conta3(albero,selettore,att,flag=False):
    cnt=0
    for child in albero.content:
        if child.istext()==False:
            if selettore in child.attr.keys():
                if child.attr.get(selettore).find(att)>=0:cnt+=1
            cnt+=conta3(child,selettore,att)
    return cnt

def conta4(albero,selettore,att,flag=False):
    cnt=0
    for child in albero.content:
        if child.istext()==False:
            if flag==True and att==child.tag:
                cnt+=1+conta4(child,selettore,att,True)
            if flag==False and selettore==child.tag:
                cnt+=conta4(child,selettore,att,True)
            if flag==False: cnt+=conta4(child,selettore,att,False)
            else: cnt+=conta4(child,selettore,att,True)        
    return cnt

def conta5(albero,selettore,att,flag=False):
    cnt=0
    for child in albero.content:
        if child.istext()==False:
            if flag==True and att==child.tag:
                cnt+=1+conta5(child,selettore,att,True)
            if flag==False and selettore==child.tag:
                cnt+=conta5(child,selettore,att,True)
            cnt+=conta5(child,selettore,att,False)
    return cnt

#funzione numero 1
def conta_nodi(fileIn, selettore):
    albero=fparse(fileIn)
    indice,selettore,att=elabora_selettore(selettore)
    
    if indice==0: return conta0(albero,selettore,att)
    elif indice==1:return conta1(albero,selettore,att)
    elif indice==2:return conta2(albero,selettore,att)
    elif indice==3:return conta3(albero,selettore,att)
    elif indice==4:return conta4(albero,selettore,att)
    else :return conta5(albero,selettore,att)




#-----Blocco numero 2----#


def elimina0(albero,selettore,att,flag=False):
    for child in albero.content:
        if child.istext()==False:
            for figlio in child.content:
                if figlio.tag==selettore:
                    child.content.remove(figlio)
                    elimina0(figlio,selettore,att,False)
            elimina0(child,selettore,att,False)
    return albero

def elimina1(albero,selettore,att,flag=False):
    for child in albero.content:
        if child.istext()==False:
            for figlio in child.content:
                if 'class' in figlio.attr.keys():
                    if figlio.attr.get('class').find(selettore)>=0:
                        child.content.remove(figlio)
                        elimina1(figlio,selettore,att,False)
                elimina1(child,selettore,att,False)    
    return albero

def elimina2(albero,selettore,att,flag=False):
    for child in albero.content:
        if child.istext()==False:
            for figlio in child.content:
                if figlio.attr.get('id')==selettore:
                    child.content.remove(figlio)
                    elimina2(figlio,selettore,att,False)
            elimina2(child,selettore,att,False)
    return albero

def elimina3(albero,selettore,att,flag=False):
    for child in albero.content:
        if child.istext()==False:
            if selettore in figlio.attr.keys():
                if figlio.attr.get(selettore).find(att)>=0:
                    child.content.remove(figlio)
                    elimina3(figlio,selettore,att,False)
            elimina3(child,selettore,att,False)
    return albero

def elimina4(albero,selettore,att,flag=False):
    for child in albero.content:
        if child.istext()==False:
            for figlio in child.content:
                if flag==True and att==figlio.tag:
                    child.content.remove(figlio)
                    elimina4(figlio,selettore,att,True)
                if flag==False and selettore==figlio.tag:
                    elimina4(figlio,selettore,att,True)
                if flag==False: elimina4(child,selettore,att,False)
                else: elimina4(child,selettore,att,True)
    return albero

def elimina5(albero,selettore,att,flag=False):
    for child in albero.content:
        if child.istext()==False:
            for figlio in child.content:
                if flag==True and att==figlio.tag:
                    child.content.remove(figlio)
                    elimina5(figlio,selettore,att,True)
                if flag==False and selettore==figlio.tag:
                    elimina5(figlio,selettore,att,True)
                elimina5(child,selettore,att,False)
    return albero


#funzione numero 2
def elimina_nodi(fileIn, selettore, fileOut):
    albero=fparse(fileIn)
    indice,selettore,att=elabora_selettore(selettore)
    
    if indice==0: albero=elimina0(albero,selettore,att)
    elif indice==1: albero=elimina1(albero,selettore,att)
    elif indice==2: albero=elimina2(albero,selettore,att)
    elif indice==3: albero=elimina3(albero,selettore,att)
    elif indice==4: albero=elimina4(albero,selettore,att)
    else : albero=elimina5(albero,selettore,att)
    
    with open(fileOut,'w') as file:file.write(albero.to_string())




#-----Funzione numero 3----#
        
def modifica0(albero,selettore,att,chiave,valore,flag=False):
    for child in albero.content:
        if child.istext()==False:
            if child.tag==selettore:
                child.attr[chiave]=valore
            modifica0(child,selettore,att,chiave,valore)
    return albero

def modifica1(albero,selettore,att,chiave,valore,flag=False):
    for child in albero.content:
        if child.istext()==False:
            if 'class' in child.attr.keys():
                if child.attr.get('class').find(selettore)>=0:
                    child.attr[chiave]=valore
            modifica1(child,selettore,att,chiave,valore)
    return albero

def modifica2(albero,selettore,att,chiave,valore,flag=False):
    for child in albero.content:
        if child.istext()==False:
            if child.attr.get('id')==selettore:
                child.attr[chiave]=valore
            modifica2(child,selettore,att,chiave,valore)
    return albero

def modifica3(albero,selettore,att,chiave,valore,flag=False):
    for child in albero.content:
        if child.istext()==False:
            if selettore in child.attr.keys():
                if child.attr.get(selettore).find(att)>=0:
                    child.attr[chiave]=valore
            modifica3(child,selettore,att,chiave,valore)
    return albero

def modifica4(albero,selettore,att,chiave,valore,flag=False):
    for child in albero.content:
        if child.istext()==False:
            if flag==True and att==child.tag:
                child.attr[chiave]=valore
                modifica4(child,selettore,att,chiave,valore,True)
            if flag==False and selettore==child.tag:
                modifica4(child,selettore,att,chiave,valore,True)
            if flag==False: modifica4(child,selettore,att,chiave,valore,False)
            else: modifica4(child,selettore,att,chiave,valore,True)
    return albero

def modifica5(albero,selettore,att,chiave,valore,flag=False):
    for child in albero.content:
        if child.istext()==False:
            if flag==True and att==child.tag:
                child.attr[chiave]=valore
                modifica5(child,selettore,att,chiave,valore,True)
            if flag==False and selettore==child.tag:
                modifica5(child,selettore,att,chiave,valore,True)
            modifica5(child,selettore,att,chiave,valore,False)
    return albero


#funzione numero 3
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    albero=fparse(fileIn)
    indice,selettore,att=elabora_selettore(selettore)

    if indice==0: albero=modifica0(albero,selettore,att,chiave,valore)
    elif indice==1: albero=modifica1(albero,selettore,att,chiave,valore)
    elif indice==2: albero=modifica2(albero,selettore,att,chiave,valore)
    elif indice==3: albero=modifica3(albero,selettore,att,chiave,valore)
    elif indice==4: albero=modifica4(albero,selettore,att,chiave,valore)
    else : albero=modifica5(albero,selettore,att,chiave,valore)
    
    with open(fileOut,'w') as file: file.write(albero.to_string())
