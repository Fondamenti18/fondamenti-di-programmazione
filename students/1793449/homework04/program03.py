from my_html import HTMLNode, fparse

from html.parser import HTMLParser

def find_by_tag(nodo, tag):
    ret = []
    if nodo.tag == tag: ret += [nodo]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            ret += find_by_tag(figlio,tag)
    return ret

def get_type(selettore):
    if selettore.startswith('#'):
        t = 'id'
    elif selettore.startswith('.'):
        t = 'class'
    elif selettore.startswith('@'):
        t = 'gen'
    else:
        t = 'tag'
    return t

def sv(nome, content): 
  with open(nome, 'w') as file: file.write(content)

def conta_rec(attrs, n, c, selettore, t, d=None):
    if d != None:
        return c
    else:
        if n < len(attrs):
            if attrs[n] in attrs:
                if t != 'gen':
                    if t == attrs[n][0] and selettore[1:] in attrs[n][1]:
                        c += 1
                else:
                    s = selettore.split('[')
                    s1 = s[1].split('=')
                    if s1[0] == attrs[n][0]:
                        c += 1
            n += 1
            return conta_rec(attrs, n, c, selettore, t)
        else:
            return conta_rec(attrs, n, c, selettore, t, True)
            
def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    t = get_type(selettore)

    class MyHTMLParser(HTMLParser):
        c = 0
        def handle_starttag(self, tag, attrs):
            self.c = conta_rec(attrs, 0, self.c, selettore, t)

    parser = MyHTMLParser()
    doc = fparse(fileIn)
    if t != 'tag':
        parser.feed(doc.to_string())
        return parser.c
    else:
        c = 0
        for nodo in find_by_tag(doc,selettore):
            c += 1
        return c

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    t = get_type(selettore)
    class MyHTMLParser(HTMLParser):
        l = []
        def handle_starttag(self, tag, attrs):
            for attr in attrs:
                if t != 'gen':
                    if t == attr[0] and selettore[1:] in attr[1]:
                            l.append(tag)
                    else:
                        print(tag)
                else:
                    s = selettore.split('[')
                    s1 = s[1].split('=')
                    if s1[0] == attr[0]:
                        l.append(tag)

    parser = MyHTMLParser()
    doc = fparse(fileIn)
    if t != 'tag':
        parser.feed(doc.to_string())
        for a in parser.l:
            elimina_ric(a, 0)
    else:
        for nodo in find_by_tag(doc,selettore):
            elimina_ric(nodo, 0)
    sv(fileOut, str(doc))

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    t = get_type(selettore)
    class MyHTMLParser(HTMLParser):
        l = []
        def handle_starttag(self, tag, attrs):
            for attr in attrs:
                if t != 'gen':
                    if t == attr[0] and selettore[1:] in attr[1]:
                            self.l.append(tag)
                else:
                    s = selettore.split('[')
                    s1 = s[1].split('=')
                    if s1[0] == attr[0]:
                        self.l.append(tag)

    parser = MyHTMLParser()
    doc = fparse(fileIn)
    if t != 'tag':
        parser.feed(doc.to_string())
        for a in parser.l:
            cambia_attr_ric(a, 0, chiave, valore)
    else:
        for a in find_by_tag(doc,selettore):
            cambia_attr_ric(a, 0, chiave, valore)
    sv(fileOut, str(doc))