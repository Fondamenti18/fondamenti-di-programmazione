
from my_html import HTMLNode, fparse
import re

def Spacchetta_R1(selettore):
    #SPacchetta il selettore in elementi solo isaplha()
    
    lista = []
    stringa = ''
    for x in selettore:
        m = re.search('[\w]*', x)
        if m:
            if m.group(0) != '':
                stringa += m.group(0)
            else:
                lista.append(stringa) if not stringa == '' else None
                stringa = ''
    return lista

def Find_by_TAG(node, tag):
    #Ritorna una lista dei nodi che hanno il tag
    
    risultato = []
    if node.tag == tag: risultato += [node]
    if not node.istext():
        for figlio in node.content:
            risultato += Find_by_TAG(figlio, tag)
    return risultato

#Ricorsiva per CN di soli elementi con strutture str(x)+'stringa' for x in ['#', '@', '.']
def CN_Ricorsiva1(doc, selettore, lista):
    
    for figlio in doc.content:
        if not type(figlio) == str:
            dizionario = figlio.attr
            if not len(dizionario) == 0:
                if selettore.startswith('#'):
                    if 'id' in dizionario:
                        if dizionario['id']==selettore[1:]:
                            lista.append(1)
                elif selettore.startswith('.'):
                    if 'class' in dizionario:
                        if selettore[1:] in dizionario['class']:
                            lista.append(1)
                elif selettore.startswith('@'):
                    lista_spacchettata = Spacchetta_R1(selettore)
                    key, value = lista_spacchettata[:]
                    if key in dizionario:
                        if value in dizionario[key]:
                            lista.append(1)
            CN_Ricorsiva1(figlio, selettore, lista)
    return lista

#Funzione per CN Padre Figlio struttura x > y for x, y in [a-zA-Z]
def CN_PadreFiglio(doc, selettore, lista):
    
    lista_selettori = [x.strip() for x in selettore.split('>')]
    selettore1, selettore2 = lista_selettori[:]
    for node in Find_by_TAG(doc, selettore1):
        for figlio in node.content:
            if selettore2 in figlio.tag:
                lista.append(1)
    return lista

#Funzione per CN AvoDiscendente struttura 'x y' for x,y in [a-zA-Z]
def CN_AvoDiscendente(doc, selettore, lista):
    
    lista_selettori = [x.strip() for x in selettore.split()]
    selettore1, selettore2 = lista_selettori[:]
    risultato = []
    for node in Find_by_TAG(doc, selettore1):
        risultato += Ricorsiva_AD(node, selettore2, lista)
    return risultato

#Ricorsiva per CN AvoDiscendente
def Ricorsiva_AD(nodo, selettore2, lista):
    
    for figlio in nodo.content:
        if not type(figlio) == str:
            if selettore2 in figlio.tag:
                lista.append(1)
            Ricorsiva_AD(figlio, selettore2, lista)
    return lista

#Funzione per strutture complesse
#str(x)+'stringa' (for x in ['#', '.', '@']) > y > z for y, z in [a-zA-Z]
def CN_Strutture_Complesse_PF(doc, selettore, lista):
    
    lista_selettori = [x.strip() for x in selettore.split('>')]
    selettore1 = ''
    for x in lista_selettori:
        if not x[0].isalpha():
            selettore1 += x
    lista_selettore1 = CN_Ricorsiva1(doc, selettore1, [])
    if len(lista_selettore1) > 0:
        lista_tag = RicercaTag_Attributo(doc, selettore1, [])
        indice = 1
        for tag in lista_tag:
            lista += (RCS_PF_SelettoreAD(doc, tag, lista_selettori, indice, []))
        return lista
        

#Ricorsiva per CN Strutture Complesse Padre-Figlio
#RCS = Ricorsiva_Strutture_Complesse, PF = Padre-Figlio, AD = Avo-Discendente
def RCS_PF_SelettoreAD(doc, tag, lista_selettori, indice, lista):
    
    if indice == len(lista_selettori):
        return lista
    else:
        for node in Find_by_TAG(doc, tag):
            for figlio in node.content:
                if not figlio.istext():
                    if ' ' in lista_selettori[indice]:
                        lista_selettori2 = [x.strip() for x in lista_selettori[indice].split(' ')]
                        if lista_selettori2[0] in figlio.tag:
                            selettore3 = lista_selettori[indice]
                            lista_AD = Ricorsiva_AD(figlio, selettore3, [])
                            if not len(lista_AD) == 0:
                                indice += 1
                                lista_PF = CN_PadreFiglio(figlio, lista_selettori2[1] + lista_selettori[indice], [])
                                if not len(lista_PF) == 0:
                                    lista.append(1)
                    RCS_PF_SelettoreAD(figlio, figlio.tag, lista_selettori, indice, lista)
        return lista
                
#Funzione di ricerca del tag dato un determinato attributo dalla struttura
#str(x)+'stringa' for x in ['#', '@', '.']
def RicercaTag_Attributo(doc, attributo, lista):
    
    for figlio in doc.content:
        if not figlio.istext():
            dizionario = figlio.attr
            if not len(dizionario) == 0:
                if attributo.startswith('#'):
                    if 'id' in dizionario:
                        if dizionario['id']==attributo[1:]:
                            lista.append(figlio.tag)
                elif attributo.startswith('.'):
                    if 'class' in dizionario:
                        if attributo[1:] in dizionario['class']:
                            lista.append(figlio.tag)
                elif attributo.startswith('@'):
                    lista_spacchettata = Spacchetta_R1(attributo)
                    key, value = lista_spacchettata[:]
                    if key in dizionario:
                        if value in dizionario[key]:
                            lista.append(figlio.tag)
            RicercaTag_Attributo(figlio, attributo, lista)
    return lista

def Remove_by_TAG(node, tag):
    
    #Rimuove dall'albero tutti i nodi con il tag, esclusa la radice
    if node.istext(): return
    for figlio in node.content:
        Remove_by_TAG(figlio, tag)
    risultato = []
    for figlio in node.content:
        if figlio.tag == tag:
            if not figlio.istext():
                risultato += figlio.content
        else:
            risultato += [figlio]
    node.content = risultato

#Funzione di eliminazione dei nodi nel caso di un selettore semplice
#di struttura x > y for x, y in [a-zA-Z]
def EN_PadreFiglio(doc, selettore):
    
    lista_selettori = [x.strip() for x in selettore.split('>')]
    selettore1, selettore2 = lista_selettori[:]
    lista_PF = CN_PadreFiglio(doc, selettore, [])
    if not len(lista_PF) == 0:
        REN_SS_PFAD(doc, selettore2)
        Remove_by_TAG(doc, selettore2)

#Funzione di eliminazione dei nodi nel caso di un selettore semplice
#di struttura x y for x, y in [a-zA-Z]
def EN_AvoDiscendente(doc, selettore):

    lista_selettori = [x.strip() for x in selettore.split(' ')]
    selettore1, selettore2 = lista_selettori[:]
    lista_AD = CN_AvoDiscendente(doc, selettore, [])
    if not len(lista_AD) == 0:
        REN_SS_PFAD(doc, selettore2)
        Remove_by_TAG(doc, selettore2)


#Ricorsiva per EN = elimina nodi Strutture Semplici Padre-Figlio
#REN = Ricorsiva Elimina Nodi, PFAD = PadreFiglioAvoDiscendente
def REN_SS_PFAD(doc, tag):

    for node in Find_by_TAG(doc, tag):
        if not len(Find_by_TAG(doc, tag)) == 0:
            for figlio in node.content:
                   Remove_by_TAG(node, figlio.tag)
                   REN_SS_PFAD(node, figlio.tag)

#Funzione Cambia Attributi Per Strutture semplici solo tag
def CA_StruttureSemplici_TAG(doc, selettore, chiave, valore):
    
    for figlio in doc.content:
        if not figlio.istext():
            if chiave in figlio.attr:
                figlio.attr[chiave] = valore
            CA_StruttureSemplici_TAG(figlio, selettore, chiave, valore)

#Funzione Cambia Attributi per Strutture semplici attributi generali
def CA_StruttureSemplici(doc, selettore, chiave, valore):

    for figlio in doc.content:
        if not figlio.istext():
            if not len(figlio.attr) == 0:
                if selettore.startswith('#'):
                    if 'id' in figlio.attr:
                        if figlio.attr['id']==selettore[1:]:
                            figlio.attr[chiave] = valore
                elif selettore.startswith('.'):
                    if 'class' in figlio.attr:
                        if selettore[1:] in figlio.attr['class']:
                            figlio.attr[chiave] = valore
                else:
                    lista_spacchettata = Spacchetta_R1(selettore)
                    key, value = lista_spacchettata[:]
                    if key in figlio.attr:
                        if figlio.attr[key] == value:
                            figlio[chiave] = valore
            CA_StruttureSemplici(figlio, selettore, chiave, valore)

#Funzione Per Cambia attributi Selettore Semplice per Avo Discendente
def CA_StruttureSemplici_AvoDiscendente(doc, selettore, chiave, valore, fileOut):

    lista_selettori = [x.strip() for x in selettore.split(' ')]
    selettore1, selettore2 = lista_selettori[:]
    for node in Find_by_TAG(doc, selettore1):
        Ricorsiva_FunzioneCA(node, selettore2, chiave, valore)
    with open(fileOut, 'w') as file:
        file.write(doc.to_string())

#Ricorsione per CA_StruttureSemplici_AvoDiscendente
def Ricorsiva_FunzioneCA(doc, selettore, chiave, valore):

    for figlio in doc.content:
        if not figlio.istext():
            if selettore in figlio.tag:
                figlio.attr[chiave] = valore
            Ricorsiva_FunzioneCA(figlio, selettore, chiave, valore)

        
        
            
def conta_nodi(fileIn, selettore):
                                                          
    '''Torna il numero dei nodi dell'albero che soddisfano il selettore'''
    doc = fparse(fileIn)
    lista = []
    caratteri_sp = ['>', ' ']
    for x in caratteri_sp: lista.append(1) if not x in selettore else False
    if len(lista) == 2:
        if selettore[0].isalpha():
            lista_NCS = Find_by_TAG(doc, selettore)
            return len(lista_NCS)
        else:
            lista_NCS = CN_Ricorsiva1(doc, selettore, [])
            return len(lista_NCS)
    else:
        if '>' in selettore:
            lista_selettori = [x.strip() for x in selettore.split('>')]
            if len(lista_selettori) == 2:
                lista_CS = CN_PadreFiglio(doc, selettore, [])
                return len(lista_CS)
            elif len(lista_selettori) > 2:
                lista_SC = CN_Strutture_Complesse_PF(doc, selettore, [])
                return len(lista_SC)
        else:
            lista_selettori = [x.strip() for x in selettore.split()]
            if len(lista_selettori) == 2:
                lista_CS = CN_AvoDiscendente(doc, selettore, [])
                return len(lista_CS)

def elimina_nodi(fileIn, selettore, fileOut):

    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS'''
    doc = fparse(fileIn)
    if '>' in selettore:
        lista = [x.stirp() for x in selettore.split('>')]
        lista_controllo = []
        if len(lista) == 2:
            for x in lista: lista_controllo.append(True) if x[0].isalpha else False
            if all(lista_controllo):
                EN_PadreFiglio(doc, selettore)
                with open(fileOut, 'w') as file:
                    file.write(doc.to_string())
    elif ' ' in selettore:
        lista = [x.strip() for x in selettore.split(' ')]
        lista_controllo = []
        if len(lista) == 2:
            for x in lista: lista_controllo.append(True) if x[0].isalpha else False
            if all(lista_controllo):
                EN_AvoDiscendente(doc, selettore)
                with open(fileOut, 'w') as file:
                    file.write(doc.to_string())
    else:
        'ciao'

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):

    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    doc = fparse(fileIn)
    caratteri_sp = ['>', ' ']
    lista = []
    for x in caratteri_sp: lista.append(True) if not x in selettore else False
    print(lista)
    if len(lista) == 2:
        if selettore[0].isalpha():
            CA_StruttureSemplici_TAG(doc, selettore, chiave, valore)
            with open(fileOut, 'w') as file:
                file.write(doc.to_string())
        else:
            CA_StruttureSemplici(doc, selettore, chiave, valore)
            with open(fileOut, 'w') as file:
                file.write(doc.to_string())
    else:
        if '>' in selettore and ' ' in selettore:
            return
        if not '>' in selettore and ' ' in selettore:
            CA_StruttureSemplici_AvoDiscendente(doc, selettore, chiave, valore, fileOut)
    
            
    
if __name__ == '__main__':
    
    #selettori_conta_nodi = ['#id1', '#intestazione', '.title',
                            #'@[width="300"]', 'p', 'p > a', 'p > em',
                            #'p a']

    #selettori_cambia_attributi = ['p a', '#slashdot_deals-title']
    
    #listaCN = [conta_nodi('page1-3.html', x) for x in selettori_conta_nodi]
    
    #doc = fparse('page1-3.html')
    #for node in Find_by_TAG(doc, 'h1'):
        #print(node.to_string())
    #print(doc.to_string())
    
    #print(listaCN)

    #doc = fparse('slashdot.html')
    
    #print(CN_Strutture_Complesse_PF(doc, '@[id="slashboxes"] > article h1 > a',[]))

    #selettori_elimina_nodi = ['p a']

    #listaEN = [elimina_nodi('page1-3.html', x, 'risEN1.html') for x in selettori_elimina_nodi]

    print(cambia_attributo('page1-3.html', 'p a', 'style', 'background-color:red', 'risCA.html'))
    

    
