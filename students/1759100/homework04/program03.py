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


from  my_html import HTMLNode, fparse

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    #Inserite qui il vostro codice
    with open(fileIn,) as f:
        f=f.read()
        l=f.split('\n')
        conto=0
        paragrafo=[]
        if len(selettore.split())==1:
            conto,paragrafo=selezione(selettore,l,conto,paragrafo)
        else: 
            conto,paragrafo=cercadoppia(selettore.split(),l,conto,paragrafo)
        return conto
def selezione(selettore,l,conto,paragrafo):
    '''seleziona come ricercare'''
    if selettore[0]=='#' :
        conto,paragrafo=cercasingola(selettore[1:],l,conto,paragrafo)
    elif selettore[0]=='.':
        conto,paragrafo=cercasingola(selettore[1:]+'=',l,conto,paragrafo)
    elif selettore[0]== '@':
        conto,paragrafo=cercasingola(selettore[2:len(selettore)-1],l,conto,paragrafo)
    else:
        conto,paragrafo=cercasingola('<'+selettore,l,conto,paragrafo)
    return conto,paragrafo
def cercadoppia(sel,lista,conto,par):
    ''' ricerca se abbiamo più condizioni'''
    try:
        if len(lista)==0:
            return conto,par
        else:
            h=spec(lista[0],sel[0])
            i=0
            if '<'+sel[0] in h:
                if sel[i+1][0]=='#' or sel[i+1][0]=='.' or sel[i+1][0]=='@':
                    conto,par=selezione(sel[i+1],h,conto,par)
                elif sel[i+1]=='>':
                    if '<' in h[1:]:
                        if(((h[(h[1:].index('<')+2):]).split())[0])==sel[i+2]:
                            conto+=1
                else:
                    if '<'+sel[i+1] in h:
                        par.append(h[(h[1:].index('<')+3):])
                        conto+=1
            conto,par=cercadoppia(sel,lista[1:],conto,par)
    except IndexError:
        return conto,par
    return conto,par
def cercasingola(sel,lista,conto,par):
    '''' ricerca se abbiamo un'unica condizione ossia classe, attributo oun paragrafo'''
    try:
        if len(lista)==0:
            return conto,par
        else:
            h=spec(lista[0],sel)
            if sel in lista[0]:
                par.append(h)
              #  print(h)
                conto+=1
            conto,par=cercasingola(sel,lista[1:],conto,par)
    except IndexError:
        return conto,par
    return conto,par

def spec(st,sel):
    '''elimina caratteri speciali'''
    special='=>,.-;:_?^!""ç°[]'
    for s in special:
        if s in st and s not in sel:
            st=st.replace(s,' ')
            
    return st
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    with open(fileIn) as f:
        f=f.read()
        l=f.split('\n')
        copy=l[:]
        conto=0
        paragrafo=[]
        if len(selettore.split())==1:
            conto,paragrafo=selezione(selettore,l,conto,paragrafo)
        else: 
            selettore=selettore
            conto,paragrafo=cercadoppia(selettore.split(),l,conto,paragrafo)
        i=0
        paragrafo=''.join(paragrafo)
        paragrafo=paragrafo.split()
        paragrafo=''.join(paragrafo)
        while i<len(list(l)):
            l[i]=spec(l[i],selettore[0])
            l[i]=''.join(l[i].split())
            if len(l[i])<len(paragrafo):
                i+=1
            else:
                h=0
                j=0
                c=0
                while h<len(l[i]) and j<len(paragrafo):
                    if l[i][h]==paragrafo[j]:
                        c+=1
                        j+=1
                        h+=1
                        if c==len(paragrafo):
                            s=i
                    elif c==0:
                        h+=1
                    else:
                        c=0
                        h+=1
                        j=0

                i+=1
        mod=copy[s]
        for x in range(len(mod)):
            if mod[x]=='<' and mod[x+1]==selettore[-1]:
                h=x
        for x in range(len(mod)):
            if mod[x]=='/' and mod[x+1]==selettore[-1]:
                g=mod[h:x+3]
        copy[s]=mod.replace(g,'')
        #print('\n'.join(copy))
        l=[]
        try:
            for x in copy:
                if len(x.split())==1:
                    l.append(x)
                else:
                    s=modifica(x)
                    l.append(s)
        except IndexError:
            pass
    l='\n'.join(l)
   # print(l)
    with open(fileOut,'w') as f:
        f.write(l)
               
def modifica(x):
    j=0
    s=''
    while x[j]!='>':
        j+=1
    b=x[:]
    h=x[:j]
    h=h.split()
    h=h[1:]
    j=h[:]
   # print(j)
    diz=[]
    s=''
    for x in range(len(j)):
        if '=' in j[x]:
          #  print(j[x])
            s+=j[x]
            if s.count('"')!=2:
                f=j[x]
            else: 
                diz.append(s)
                s=''
        else:
          #  print(j[x])
            s+=' '+j[x]
         #   print(s)
            if s.count('"')==2:
                diz.append(s)
                s=''



    #print(diz)
    h=sorted(diz)
   # print(b)
    b=b.split()
    s+=b[0]
 #   print(b[0])
    x=' '.join(b)
    for el in range(len(h)):
        s+=' '
        s+=h[el]
        if h[el].count('"')==1:
           # print(h[el])
            d=j.index(h[el])
          #  print(j[d+1])
            s+=j[d]
   # print(x[x.index('>'):])
    s+=x[x.index('>'):]
    #print(s)
    return s


def repeat(x,f):
    el=0
    while x[el]!=' ':
        f+=x[el]
        el+=1
    return f
if __name__ == '__main__':
    with open('risTest9-3.html') as f:
        f=f.read()
        print (f)

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    with open(fileIn) as f:
        f=f.read()
        l=f.split('\n')
        copy=l[:]
        conto=0
        paragrafo=[]
        if len(selettore.split())==1:
            conto,paragrafo=selezione(selettore,l,conto,paragrafo)
        else: 
            conto,paragrafo=cercadoppia(selettore.split(),l,conto,paragrafo)
        i=0
        paragrafo=''.join(paragrafo)
        paragrafo=paragrafo.split()
        paragrafo=''.join(paragrafo)
        while i<len(list(l)):
            l[i]=spec(l[i],selettore[0])
            l[i]=''.join(l[i].split())
            if len(l[i])<len(paragrafo):
                i+=1
            else:
                h=0
                j=0
                c=0
                while h<len(l[i]) and j<len(paragrafo):
                    if l[i][h]==paragrafo[j]:
                        c+=1
                        j+=1
                        h+=1
                        if c==len(paragrafo):
                            s=i
                    elif c==0:
                        h+=1
                    else:
                        c=0
                        h+=1
                        j=0
                i+=1
        mod=copy[s]
        for x in range(len(mod)):
            if mod[x]=='<' and mod[x+1]==selettore[-1]:
                h=x+2
        for x in range(len(mod)):
            if mod[x]=='/' and mod[x+1]==selettore[-1]:
                g=mod[h:x-1]
                j=x-1
        g=g.split()
        for x in range(len(g)):
            if '=' in g[x]:
                if g[x][:g[x].index('=')]>chiave:
                   g[x:x]=[chiave+'='+'"'+valore+'" ']
        a=copy[s][:h+1]
        for x in g:
            a+=str(x)
        a+=mod[j:]
        copy[s]=a
        copy=('\n'.join(copy))
        print(copy)
        l=[]
        try:
            for x in copy:
                if len(x.split())==1:
                    l.append(x)
                else:
                    s=modifica(x)
                    l.append(s)
        except IndexError:
            pass
    l='\n'.join(l)
    print(l)
    
    with open(fileOut,'w') as f:
        f=f.write(copy)

if __name__=='__main__':
    with open('risTest9-3.html') as f:
        f.read()