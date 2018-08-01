'''

Definiamo adiacenti di un pixel p di un immagine i pixel adiacenti a p in  orizzontale o in  verticale.
Se un pixel e' sul bordo dell'immagine il suo vicinato non comprende i pixel non contenuti nell'immagine.
Il pixel dell'immagine con coordinate(x,y) ha dunque come adiacenti i pixel
con coordinate (x-1,y),(x+1,y),(x,y-1),(x,y+1) appartenenti all'immagine.

Definiamo connessi due pixel se e' possibile dall'uno raggiungere l'altro spostandosi solo su
pixel adiacenti e dello stesso colore (ovviamente perche' cio' sia possobile e' necessario
che i due pixel abbiano lo stesso colore).

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una funzione ricolora(fname, lista,  fnameout) che presi:
- il percorso di un file che contiene un'immagine in formato PNG
- una lista di quadruple del tipo (x,y,c1,c2) dove  x e y sono coordinate di un pixel dell'immagine e c1 e c2 due triple colore RGB
- il percorso di un file (fnameout) da creare
legge l'immagine in fname, esegue un'operazione di ricolorazione di alcuni pixel dell'immagine e
registra l'immagine ricolorata nel file fnameout.

L'operazione di ricolorazione e' la seguente. Per ciascuna delle quadruple (x,y,c1,c2) della lista (nell'ordine),
- tutti i pixel connessi al pixel  di coordinate (x,y) nell'immagine vanno ricolorati col colore c1,
- tutti i pixel del perimetro (che si trovano sul 'bordo') della zona che si e' appena colorata devono essere ricolorati col colore c2.
Il perimetro della zona colorata è l'insieme dei pixel che non hanno tutti e 4 i vicini che fanno parte della zona ricolorata
(ovvero almeno uno è di un colore diverso da quello che si sta ricolorando oppure almeno uno non esiste perchè sarebbe fuori dall'immagine)

Si consideri ad esempio l'immagine 'I1.png', l'invocazione di ricolora('I1.png',[(10,10,(255,0,0), (0,0,255))],’OUT1.png')
produrra' l'immagine 'OUT1.png' identica all'immagine di partenza se non per il fatto che,
 tutti i pixel adiacenti al pixel di coordinate (10,10) (e di colore verde), verranno ricolorati
 di rosso ((255,0,0)), mentre i pixel sul bordo della zona inizialmente verde vengono ricolorati di blu.

Per ciascuna area ricolorata bisogna inoltre calcolare area interna e perimetro, che sono definite come segue:
- l'area interna e' il numero di pixel ricolorati con il colore c1
- il perimetro è il numero di pixel ricolorati con il colore c2

La funzone deve tornare la lista di coppie (area interna, perimetro) nello stesso ordine in cui sono state colorate le aree.

Per altri  esempi vedere il file grade03.txt
'''

from immagini import *

def ricolora(fname, lista, fnameout):

    '''
        algoritmo abbastanza sporco; vanno fatti dei miglioramenti dell'algoritmo, rendere più efficienti i tempi,
        stabilire il when del ciclo while all'interno della classe Pixel. Rendere più leggibile il codice e correggere
        le varie ripetizioni. Bisogna calcolare la differenza tra i set delle ._connections, e ._border
        Effettuare all'interno della classe un unione più efficiente dei punti connessi.
        cercare di cambiare il colore dell'immagine ogni volta che si trova un pixel al suo interno
        capire se può essere un problema l'iterazione degli elementi della lista in input sull'oggetto creato in precedenza

        '''

    fname_list = load(fname)
    r_list = []

    for _ in lista:
        immag_ = Pixel(_[0],_[1],fname_list)
        immag_.pointconnection()

        for i in immag_._connections:
            fname_list[i[0]][i[1]] = _[2]
        for j in immag_._border:
            fname_list[j[0]][j[1]] = _[3]

        save(fname_list,fnameout)
        save(fname_list,'mierda.png')

        r_list.append((len(immag_._connections) - len(immag_._border),len(immag_._border)))
    return r_list

class Pixel:
    def __init__(self,x,y,image):
        self._x = x
        self._y = y
        self._image = image
        self._ccolor = self._image[self._y][self._x] #colore del pixel
        self._connections = set() #set delle coordinate di tutte le connessioni
        self._border = set()    #set che contiene il perimetro dell'immagine
        self._seen = []


    def pointconnection(self):
        '''l'errore che si commetteva: quando andavo ad aggiungere le coordinate nel set, non le
           inserivo unendo i due insiemi, ma facendo un'assegnazione ad f_set perdendo tutti gli
           elementi precedentemente calcolati. Bisogna aggiungere la condizione per cui si esce dal
           ciclo while.'''
        pp1 = (self._y,self._x)     #punto di partenza su cui trovare i pixel connessi
        f_set = set()
        s_set = self.neighbors(pp1) # neighbors restituisce il vicinato di un singolo pixel
        when = True                 # fa finire il while dopo n volte
        counter = 0
        while when:
            counter = counter + 1
            for _ in s_set:
                if _ not in self._seen:
                    self._seen.append(_)
                    union = self.neighbors(_) # punto da rendere più efficiente
                    for u in union:
                        f_set.add(u)
                        self._connections.add(u)
                else:
                    continue


            s_set = f_set
            f_set = set()
            if counter == 1000:
                when = False
        return

    def neighbors(self, pp): # con formato coordinate(y,x)
        '''restituisce il vicinato connesso al pixel con colori uguali, e il le coordinate del bordo'''
        neighbors = set()
        for _ in [(pp[0],pp[1]+1),(pp[0],pp[1]-1),(pp[0]+1,pp[1]),(pp[0]-1,pp[1])]:
            if self.inside((_[0],_[1])):
                if self._image[_[0]][_[1]] == self._ccolor:
                    if self.border(_):
                        self._border.add(_)
                    neighbors.add(_)
                else:
                    self._border.add(pp)

                    #self._connections.add(_)
        return neighbors

    def inside(self,coord):
        '''indica se le coordinate si trovano all'interno dell'immagine'''
        iw , ih = len(self._image[0]), len(self._image)
        return 0 <= coord[0] < ih and 0 <= coord[1] < iw

    def border(self, ppb):
        '''controllo che il pixel non faccia parte del bordo'''
        lb , ub = 0, 0
        rb , db = len(self._image)-1 , len(self._image[0])-1
        isborder = False
        if ppb[0] == lb or ppb[1] == ub:
            isborder = True
        if ppb[0] == rb or ppb[1] == db:
            isborder = True

        return isborder



if __name__ == '__main__':
    rosso = (255,   0,   0)
    blu   = (  0,   0, 255)
    verde = (  0, 255,   0)
    nero  = (  0,   0,   0)
    bianco= (255, 255, 255)
    giallo= (255, 255,   0)
    cyan  = (  0, 255, 255)
    magenta= (255,  0, 255)
