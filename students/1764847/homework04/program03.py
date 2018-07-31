'''
Un documento HTML puo' essere rappresentato sotto forma di albero, come visto a lezione, che si chiama DOM (Document Object Model).

Un qualsiasi nodo di questo albero puo' essere individuato sulla base delle proprie caratteristiche:
    - tag                       un tag del tipo indicato
    - .classe                   una delle parole presenti nel valore dell'attributo "class"
    - #id                       il valore dell'attributo "id"
    - @[attributo="valore"]     valore di un attributo generico
ed in base alla sua relazione con i tag che lo contengono:
    - avo discendente           il tag 'avo' contiene un tag 'discendente' a qualsiasi profondita'
    - padre > figlio            il tag 'padre' contiene il tag 'figlio' nel livello immediatamente sotto

Un selettore CSS e' una successione di selettori di tag separati da spazio che serve ad individuare uno o piu' nodi all'interno del DOM.
Esempio:
    div .class1 > #main_window
        seleziona un qualsiasi tag che ha                                       id="main_window"
        e' il figlio di un tag che ha                                            class="... class1 ..."
        e si trova all'interno (a qualsiasi livello di distanza) di un tag      div
Esempio2:
    p  table > tr > td > a
	seleziona un link (<a ...> </a>)
	figlio di una casella (<td> ... </td>)
	figlia di una riga (<tr> ... </tr>)
	figlia di una tabella (<table> ... </table>)
	contenuta a qualsiasi livello in un paragrafo (<p> .... </p>)

NOTA: questa definizione del CSS e' una versione ridottissima che non segue lo standard completo. 
In particolare, non e' possibile usare piu' relazioni '>' consecutive o costruire selettori alternativi (in OR) e selettori in AND.

Le modifiche da attuare su un DOM possono essere di 3 tipi:
    - conteggio dei nodi che soddisfano il selettore CSS
    - eliminazione di tutti i tag individuati da un selettore CSS
    - modifica degli attributi di tutti i tag individuati da un selettore CSS

Realizzate le funzioni che esplorano e modificano l'albero:
    conta_nodi(       fileIn, selettore)				
    elimina_nodi(       fileIn, selettore, fileOut)				
    cambia_attributo(	fileIn, selettore, chiave, valore, fileOut)

ATTENZIONE: nei test verra' utilizzato un timout globale di 1*N secondi (se il grader fa N test)
'''

import my_html
    

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    #Inserite qui il vostro codice
    pHtml = my_html.fparse(fileIn)
    #print(lstTag)
    # Lista del testo per riga
    lstRighe = pHtml.to_string().split('\n')
    # Lista del testo per spazi
    lstText = pHtml.to_string().split()
    # Lista dei selettori (ricerca padre figlio)
    lstSel = selettore.split('>')
    for i in range(len(lstSel)):
        lstSel[i] = lstSel[i].strip()
    # Se il selettore e' un tag
    if selettore.isalpha():
        #return cntTag(lstTree(pHtml, []), selettore, 0, 0)
        return cntTag1(pHtml, selettore, [])
    # Se il selettore e' un id
    elif selettore[0] == '#':
        return cntId(lstText,selettore, 0, 0)
    # Se il selettore e' una classe
    elif selettore[0] == '.':
        return cntClassi(lstRighe, selettore, 0, 0)
    # Se il selettore e' un attributo generico
    elif selettore[0] == '@':
        return cntAttributo(lstText, selettore, 0, 0)
    # Se il selettore e' un selettore padre figlio
    elif '>' in selettore:
        sel = selettore.split('>')
        sP = sel[0].strip()
        sF = sel[1].strip()
        return cntPadreFiglio(pHtml,sP,sF,[])
    # Se non e' nessuno dei precedenti casi allora si cerca un discendente
    else:
        sel = selettore.split()
        sP = sel[0].strip()
        sD = sel[1].strip()
        return cntDiscendenti(pHtml, sP, sD, [], False)

def cntId(lstText, selettore, i, cnt):
    '''restituisce il numero di selettori (id) presenti
    nel file HTML'''
    if i >= len(lstText):
        return cnt
    if 'id=' + '"'+selettore[1:]+'"' in lstText[i]:
        cnt += 1
    return cntId(lstText, selettore, i +1, cnt)



def cntClassi(lstRighe, selettore, i, cnt):
    '''Restituisce il numero di selettori (classi) presenti
    nel file HTML'''
    if i >= len(lstRighe):
        return cnt
    if selettore[1 :] + '=' in lstRighe[i]:
        cnt += 1
    return cntClassi(lstRighe, selettore, i + 1, cnt)

def cntAttributo(lstText, selettore, i, cnt):
    '''REstituisce il numero di attributi (generici) presenti
    nel file HTML'''
    if i >= len(lstText):
        return cnt
    if selettore[2 : -1] in lstText[i]:
        cnt += 1
    return cntAttributo(lstText, selettore, i +1, cnt)


def cntTag1(radice, selettore, lst):
    '''Restituisce il numero di selettori (tag) presenti 
    nel file HTML'''
    if not radice.istext():
        if radice.tag == selettore:
            lst.append(1)
    for figlio in radice.content:
        if not figlio.istext():
           cntTag1(figlio, selettore, lst)
    return len(lst)



def cntPadreFiglio(radice, sP, sF, lst):
    '''Restituisce il numero di selettori (padre > figlio)
    presenti nel file html'''
    if not radice.istext():
        if radice.tag == sP  and '<'+sF+'>' in lstFigli(radice):
            lst.append(1)
    for figlio in radice.content:
        if not figlio.istext():
            cntPadreFiglio(figlio, sP, sF, lst)
    return len(lst)


            
    
def lstFigli(nodo):
    '''Restituisce la lista dei figli del nodo'''
    if not nodo.istext():
        lst = []
        for i in nodo.content:
            if not i.istext():
                lst.append(str(i))
    return lst

def lstTree(radice, lst):
    '''Restituisce la lista di tutti i nodi dell'albero'''
    if not radice.istext():
        lst.append(str(radice))
        for child in radice.content:
            lstTree(child, lst)
    return lst

        

def cntDiscendenti(radice, sP, sD, lst, boole):
    '''Restituisce il numero di selettori (padre discendente)
    presenti nel file html'''
    if not radice.istext():
        if radice.tag == sP:
            boole = True
        if boole == True and radice.tag == sD:
            lst.append(1)
            boole = False
        for figlio in radice.content:
            if not figlio.istext():
                cntDiscendenti(figlio, sP, sD, lst, boole)
    return len(lst)

   
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    pHtml = my_html.fparse(fileIn)
    pHtmlMod = None
    # Se il selettore e' un nodo 
    if selettore.isalpha():
        pHtmlMod = cancellaNodi(pHtml, selettore, selettore, False, pHtml)
    # Se il selettore e' un selettore padre figlio
    elif '>' in selettore:
        liSel = selettore.split('>')
        pHtmlMod = cancellaNodiPF(pHtml, liSel[0].strip(), liSel[1].strip(), pHtml)
    # se si cerca un discendente da eliminare
    else:
        liSel = selettore.split(' ')
        pHtmlMod = cancellaNodi(pHtml,liSel[0], liSel[1],False, pHtml)
    f = open(fileOut, 'w')
    f.write(pHtmlMod)
    f.close()
    
def cancellaNodi(radice, sP, sD, boole, rad):
    ''' Elimina i nodi (avo) and restituisce la radice dell'albero'''
    if radice.tag == sP:
        boole = True
    if boole == True and radice.tag == sD:
        delTag(rad, sD)
        boole = False
    for figlio in radice.content:
        if not figlio.istext():
            cancellaNodi(figlio, sP, sD, boole, rad)
    return radice.to_string()

def cancellaNodiPF(radice, sP, sD, rad):
    ''' Elimina i nodi (padre > figlio) and restituisce la radice dell'albero'''
    lstF = lstFigli(radice)
    if radice.tag == sP and '<'+sD+'>' in lstF: 
        delTag(rad, sD)
    for figlio in radice.content:
        if not figlio.istext():
            cancellaNodiPF(figlio, sP, sD, rad)
    return radice.to_string()


def delTag(nodo, tag):
    '''Elimina il tag'''
    for figlio in nodo.content:
        if not figlio.istext():
            delTag(figlio, tag)
    lstFigli = []
    for figlio in nodo.content:
        if figlio.tag == tag:
            if not figlio.istext():
                for i in figlio.content:
                    if not i.istext():
                        lstFigli.append(i)
        else:
            lstFigli += [figlio]
    nodo.content = lstFigli



def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    pHtml = my_html.fparse(fileIn)
    pHtmlMod = None
    # Modifica i nodi padre figlio
    if '>' in selettore:
        liSel = selettore.split('>')
        pHtmlMod = modificaNodiPF(pHtml, liSel[0].strip(), liSel[1].strip(), chiave, valore)
    # Modifica i nodi evo
    elif ' ' in selettore :
        liSel = selettore.split(' ')
        pHtmlMod = modificaNodiE(pHtml,liSel[0], liSel[1],False, chiave, valore)
    # Modifica gli id or classi or attributi
    else:
        a = None
        if selettore[0] == '@':
            a = selettore.split('=')
            a = a[0][2:]
        dizSel = {'#' : 'id', '.' : 'class', '@' : a}
        idS = selettore[0]
        pHtmlMod =  modificaNodi(pHtml, selettore, chiave, valore, idS, dizSel)
    
    
    f = open(fileOut, 'w')
    f.write(pHtmlMod)
    f.close()
    

def modificaNodiE(radice, sP, sD, boole, chiave, valore):
    '''Modifica i nodi and restituisce la radice dell'albero'''
    if not radice.istext():
        if radice.tag == sP:
            boole = True
        if boole == True and radice.tag == sD:
            radice.attr[chiave] = valore
            boole = False
        for figlio in radice.content:
            if not figlio.istext():
                modificaNodiE(figlio, sP, sD, boole, chiave, valore)
    return radice.to_string()

def modificaNodiPF(radice, sP, sD, chiave, valore):
    ''' Modifica i nodi (padre > figlio) and restituisce la radice dell'albero'''
    lstF = lstFigli(radice)
    if radice.tag == sP and '<'+sD+'>' in lstF: 
        for i in radice.content:
            if i.tag == sD:
                i.attr[chiave] = valore
    for figlio in radice.content:
        if not figlio.istext():
            modificaNodiPF(figlio, sP, sD, chiave, valore)
    return radice.to_string()

def modificaNodi(radice, selettore, chiave, valore, idSel, dizSel):
    '''Modifica i nodi che soddisfano il selettore (.) or (#) or (@)
    e restituisce la radice dell'albero'''
    if not radice.istext():
        d = radice.attr
        a = selettore.split('=')
        if len(a) >= 2:
            a = a[1][1:-2]
        if d.get(dizSel[idSel],-1) != -1 and radice.attr[dizSel[idSel]] == selettore[1:] or d.get(dizSel[idSel],-1) != -1 and radice.attr[dizSel[idSel]] == a:
            radice.attr[chiave] = valore
        for figlio in radice.content:
            if not figlio.istext():
                modificaNodi(figlio, selettore, chiave, valore, idSel, dizSel)
    return radice.to_string()

            

