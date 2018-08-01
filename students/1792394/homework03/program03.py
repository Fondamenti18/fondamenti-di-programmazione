from immagini import *

def controllaAdiacenti(file,x,y,listaAdiacenti,insiemeBordo,coloreBack,ColoreBord,xmax,ymax,insiemeBack):
    var=x+1
    if (var,y) not in insiemeBack:
        try:
            if file[y][var] == file[y][x]:
                insiemeBack.add((var,y))
                listaAdiacenti.append((var,y))
            else:
                insiemeBordo.add((x,y))
        except:
                insiemeBordo.add((x,y))

    var = y+1
    if (x,var) not in insiemeBack:   
        try: 
            if file[var][x] == file[y][x]:
                insiemeBack.add((x,var)) 
                listaAdiacenti.append((x,var))
            else:
                insiemeBordo.add((x,y))  
        except:
            insiemeBordo.add((x,y))  
    var = x-1
    if var >= 0:
        if (var,y) not in insiemeBack:
            if file[y][var] == file[y][x]:
                insiemeBack.add((var,y))
                listaAdiacenti.append((var,y))
            else:
                insiemeBordo.add((x,y))
    else:
        insiemeBordo.add((x,y))
    var = y-1
    if var >= 0:
        if (x,var) not in insiemeBack:    
            if file[var][x] == file[y][x] :
                insiemeBack.add((x,var))
                listaAdiacenti.append((x,var))
            else:
                insiemeBordo.add((x,y))
    else:
        insiemeBordo.add((x,y))
    return listaAdiacenti,insiemeBordo


def ricolora(fname, lista, fnameout):
    file = load(fname)
    xmax,ymax=len(file[0]),len(file)
    ris=[]
    for k in range(len(lista)):
        x,y,coloreBordo,coloreBack = lista[k][0],lista[k][1],lista[k][3],lista[k][2]
        listaAdiacenti=[(x,y)]
        insiemeBordo,insiemeBack = set(),{(x,y)}
        for x in listaAdiacenti:
            listaAdiacenti,insiemeBordo = controllaAdiacenti(file,x[0],x[1],listaAdiacenti,insiemeBordo,coloreBack,coloreBordo,xmax,ymax,insiemeBack)
        for c in insiemeBack-insiemeBordo:
            file[c[1]][c[0]] = coloreBack
        for bord in insiemeBordo:
            file[bord[1]][bord[0]] = coloreBordo
        contaBordo = len(insiemeBordo)
        ris.append((len(insiemeBack)-contaBordo,contaBordo))
    save(file,fnameout)
    return ris
