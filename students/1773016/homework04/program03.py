import my_html 
#--------------------------------------------------------------------------------------------------------------------------
#Classe modificata
class modMy_html(my_html.HTMLNode):
    def __init__(self,tag,attr,content,closed=True):
        self.precedenti = []
        self.nodiAntenati = []
        super().__init__(tag,attr,content,closed=True) 
class _modMyHTMLParser(my_html._MyHTMLParser):
    def _init_(self):
        super().__init__()
    def handle_starttag(self, tag, attrs):
        '''Metodo invocato per tag aperti'''
        closed = tag not in ['img','br','meta','link', 'input', 'wbr', 'hr']
        node = modMy_html(tag,dict(attrs),[],closed)
        if not self.root:
            self.root = node
        if self.stack: 
            self.stack[-1].content.append(node)
        if closed:
            self.stack.append(node)
    def handle_data(self, data):
        '''Metodo invocato per il testo'''
        if not self.stack: return
        self.stack[-1].content.append(
            modMy_html('_text_',{},data))
    def handle_entityref(self, name):
        '''Metodo invocato per caratteri speciali'''
        if name in name2codepoint:
            c = unichr(name2codepoint[name])
        else:
            c = '&'+name
        if not self.stack: return
        self.stack[-1].content.append(
            modMy_html('_text_',{},c))
    def handle_charref(self, name):
        '''Metodo invocato per caratteri speciali'''
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        if not self.stack: return
        self.stack[-1].content.append(
            modMy_html('_text_',{},c))
def parse(html):
    '''Esegue il parsing HTML del testo html e
    ritorna la radice dell'albero.'''
    parser = _modMyHTMLParser()
    parser.feed(html)
    return parser.root

def fparse(fhtml):
    '''Esegue il parsing HTML del file fhtml e
    ritorna la radice dell'albero .'''
    with open(fhtml, encoding='utf8') as f:
        root = parse(f.read())
        return root
#--------------------------------------------------------------------------------------------------------------------------
def formatSelettore(selettore):
    out = None
    if '.' in selettore:
        return 1,selettore[1:]
    elif '#' in selettore:
        return 2,['id','=',selettore[1:]]
    elif '@' in selettore:
        out = [selettore[2:selettore.find('=')],'=',
               selettore[selettore.find('=')+2:selettore.rfind('"')]]
        return 3,out
    elif '>' in selettore:
        out = []
        char = 0
        while char<len(selettore):   
            if selettore[char] != ' ': 
                i = char
                s = selettore[i]
                while i+1 < len(selettore) and selettore[i+1] != ' ':
                    s+=selettore[i+1]
                    i+=1
                out.append(s)
                char = i
            char+=1
        return 4,out
    elif ' ' in selettore:
        out = []
        for char in selettore:   
            if char != ' ': 
                out.append(char)
                out.append('')
        return 5,out
    else:
        return 6,selettore
 
#<p class="par1" id="paragrafo1">Un paragrafo con testo <em>enfatizzato</em> e <strong>molto enfatizzato</strong>.</p>
def funContaNodi(alb,tipo,sel,n):   
    if type(sel) == list:
        if ('=' in sel and sel[0] in alb.attr.keys()
           and alb.attr[sel[0]] == sel[2]):
            n[0]+=1
        elif tipo==4 and alb.tag == sel[2]:    
            index = len(alb.precedenti)
            if alb.precedenti[index-1] == sel[0]:
                n[0]+=1
        elif tipo == 5 and alb.tag == sel[2]:
            print(alb.precedenti)
            index = len(alb.precedenti)-1
            while index >= 0:   
                if alb.precedenti[index] == sel[0]:
                    n[0]+=1
                    break
                index -= 1  
    elif tipo == 6 and alb.tag == sel:
        n[0]+=1
    elif tipo == 1 and sel in alb.attr.keys():
        n[0]+=1
    if  type(alb.content) is not str: 
        prima = alb.precedenti
        prima.append(alb.tag)   
        for elem in alb.content:
            elem.precedenti = prima 
            funContaNodi(elem,tipo,sel,n)
def scorriAlb(alb):
    if  type(alb.content) is not str: 
        for elem in alb.content:
            scorriAlb(elem)
def funEliminaNodo(alb,tipo,sel):  
    if type(sel) == list: 
        if ('=' in sel and sel[0] in alb.attr.keys()
           and alb.attr[sel[0]] == sel[2]):
            n[0]+=1
        elif tipo==4 and alb.tag == sel[2]:    
            index = len(alb.precedenti)
            match = False
            if alb.precedenti[index-1] == sel[0]:
                match = True
            if match: 
                alb.nodiAntenati[len(alb.precedenti)-1].content.remove(alb)
        elif tipo == 5 and alb.tag == sel[2]: 
            index = len(alb.precedenti)-1
            match = False
            while index >= 0:   
                if alb.precedenti[index] == sel[0]:
                    match = True
                    break
                index -= 1
            if match: 
                alb.nodiAntenati[len(alb.precedenti)-1].content.remove(alb)
    elif tipo == 6 and alb.tag == sel:
        n[0]+=1
    elif tipo == 1 and sel in alb.attr.keys():
        n[0]+=1
    if  type(alb.content) is not str: 
        prima = alb.precedenti
        prima.append(alb.tag)
        antenati = alb.nodiAntenati
        antenati.append(alb) 
        for elem in alb.content:
            elem.precedenti = prima
            elem.nodiAntenati = antenati
            funEliminaNodo(elem,tipo,sel)
#-----------------------------------------------------------------------------
def conta_nodi(fileIn, selettore):
    file = fparse(fileIn)
    t,fSelettore = formatSelettore(selettore)
    num = [0]
    funContaNodi(file,t,fSelettore,num) 
    return num[0]

def elimina_nodi(fileIn, selettore, fileOut):
    file = fparse(fileIn)
    out = open(fileOut,'w',encoding = 'UTF-8')
    t,fSelettore = formatSelettore(selettore) 
    funEliminaNodo(file,t,fSelettore)
    s = file.to_string()
    print(s,file=out)
    out.close()
    return 0

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    file = fparse(fileIn)
    out = open(fileOut,'w',encoding = 'UTF-8')
    t,fSelettore = formatSelettore(selettore) 
    s = file.to_string()
    print(s,file=out)
    out.close()
    return 0
