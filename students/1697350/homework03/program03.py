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
from collections import defaultdict

from immagini import *

rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)

def colorCell(image, position, color):
    i = position[0]
    j = position[1]
    image[i][j] = color

def connected_components(graph):
    seen = set()
    def dfs(v):
        vs = set([v])
        component=[]
        while vs:
            v = vs.pop()
            seen.add(v)
            vs |= set(graph[v]) - seen
            component.append(v)
        return component
    ans=[]
    for v in graph:
        if v not in seen:
            d=dfs(v)
            ans.append(d)
    return ans

def returnBorderPixels(component):
    newSet = set()
    min_i = min(i for (i,j) in component)
    min_j = min(j for (i, j) in component)
    max_i = max(i for (i,j) in component)
    max_j = max(j for (i, j) in component)
    for (i,j) in component:
        if i == min_i or i == max_i or j == min_j or j == max_j:
            newSet.add((i,j))
    return newSet

def getAdjList(matrix):
    adj_list = defaultdict(set)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            try:
                if matrix[i - 1][j] == matrix[i][j]:
                    adj_list[(i, j)].add((i - 1, j))
            except:
                continue
            try:
                if matrix[i + 1][j] == matrix[i][j]:
                    adj_list[(i, j)].add((i + 1, j))
            except:
                continue
            try:
                if matrix[i][j - 1] == matrix[i][j]:
                    adj_list[(i, j)].add((i, j - 1))
            except:
                continue
            try:
                if matrix[i][j + 1] == matrix[i][j]:
                    adj_list[(i, j)].add((i, j + 1))
            except:
                continue
    return adj_list


def ricolora(fname, lista, fnameout):
    matrix = load(fname)

    result = list()
    for tupla in lista:
        adj_list = getAdjList(matrix)
        connected = connected_components(adj_list)
        t = (tupla[1], tupla[0])
        c1 = tupla[2]
        c2 = tupla[3]
        for component in connected:
            if t in component:
                border = returnBorderPixels(component)
                area = 0
                for point in component:
                    area += 1
                    colorCell(matrix, point, c1)
                perimetro = 0
                for point in border:
                    perimetro += 1
                    colorCell(matrix, point, c2)
                area -= perimetro
                result.append((area,perimetro))

    save(matrix, fnameout)
    return result

#if __name__ == "__main__":
    #lista = [(25, 25, (0, 0, 0), (0, 5 * i, 5 * i)) for i in range(1, 25)]

    #(ricolora('I1.png',lista,'test6.png'))




