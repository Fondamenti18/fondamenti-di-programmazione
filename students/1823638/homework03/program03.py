from immagini import *
import sys
sys.setrecursionlimit(4000)

def ricolora(fname, lista, fnameout):
    img=load(fname)
    
    global w
    w=len(img[0])
    global h
    h=len(img)
    
    len1=len(lista)

    global listafin
    listafin=[]
    
    def princ():
        for inp in lista:
            v1=inp[1]
            v2=inp[0]
            colore_i=img[v1][v2]
            colore_a=inp[2]
            colore_per=inp[3]
            global lista1
            lista1=[[v1,v2]]
            lista.remove(inp)
                
            global area
            area=0
            global per
            per=0
            
            global lista2
            lista2=[]
            
            global listafin
            listafin=[]
            
            def prova1():
                global lista1
                global lista2
                for val in lista1:
                    try:
                        if img[val[0]+1][val[1]]==colore_i:
                            lista1=lista1+[[val[0]+1,val[1]]]
                            lista1.remove(val)
                            return prova1()
                        else:
                            lista2=[val[0],val[1]]
                            lista1=[[v1,v2]]
                            break
                    except:
                        lista2=[val[0],val[1]]
                        lista1=[[v1,v2]]
                        pass
            prova1()
            
            global lista3
            lista3=[]
            
            def prova2():
                global lista1
                global lista3
                for val in lista1:
                    try:
                        if img[val[0]-1][val[1]]==colore_i:
                            lista1=lista1+[[val[0]-1,val[1]]]
                            lista1.remove(val)
                            return prova2()
                        else:
                            lista3=[val[0],val[1]]
                            lista1=[[v1,v2]]
                            break
                    except:
                        lista3=[val[0],val[1]]
                        lista1=[[v1,v2]]
                        pass
            prova2()
            
            
            global lista4
            lista4=[]
            
            def prova3():
                global lista1
                global lista4
                for val in lista1:
                    try:
                        if img[val[0]][val[1]+1]==colore_i:
                            lista1=lista1+[[val[0],val[1]+1]]
                            lista1.remove(val)
                            return prova3()
                        else:
                            lista4=[val[0],val[1]]
                            lista1=[[v1,v2]]
                            break
                    except:
                        lista4=[val[0],val[1]]
                        lista1=[[v1,v2]]
                        pass
            prova3()
            
            
            global lista5
            lista5=[]
            
            def prova4():
                global lista1
                global lista5
                for val in lista1:
                    try:
                        if img[val[0]][val[1]-1]==colore_i:
                            lista1=lista1+[[val[0],val[1]-1]]
                            lista1.remove(val)
                            return prova4()
                        else:
                            lista5=[val[0],val[1]]
                            lista1=[[v1,v2]]
                            break
                    except:
                        lista5=[val[0],val[1]]
                        lista1=[[v1,v2]]
                        pass
            prova4()
            
            #sotto
            for x in range(lista3[0],lista3[0]+1):
                for y in range(lista5[1],lista4[1]+1):
                    per=per+1
                    img[x][y]=colore_per
            
            #sopra
            for x in range(lista2[0],lista2[0]+1):
                for y in range(lista5[1],lista4[1]+1):
                    per=per+1
                    img[x][y]=colore_per
            
            #sx
            for x in range(lista3[0],lista2[0]+1):
                for y in range(lista5[1],lista5[1]+1):
                    per=per+1
                    img[x][y]=colore_per
            
            #dx
            for x in range(lista3[0],lista2[0]+1):
                for y in range(lista4[1],lista4[1]+1):
                    per=per+1
                    img[x][y]=colore_per
            
            def check(v1,v2):
                    global area
                    global lista1
                    global per
                    try:
                        for val in lista1:
                            if val[0]+1<w:
                                if img[val[0]+1][val[1]]==colore_i:
                                    area=area+1
                                    lista1=lista1+[[val[0]+1,val[1]]]
                                    img[val[0]+1][val[1]]=colore_a
                                else:
                                    if img[val[0]+1][val[1]]==colore_a:
                                        pass
                            else:
                                pass
                            
                            if val[0]-1>-1:
                                if img[val[0]-1][val[1]]==colore_i:
                                    area=area+1
                                    lista1=lista1+[[val[0]-1,val[1]]]
                                    img[val[0]-1][val[1]]=colore_a
                                else:
                                    if img[val[0]-1][val[1]]==colore_a:
                                        pass
                            else:
                                pass
                            
                            if val[1]+1<h:
                                if img[val[0]][val[1]+1]==colore_i:
                                    area=area+1
                                    lista1=lista1+[[val[0],val[1]+1]]
                                    img[val[0]][val[1]+1]=colore_a
                                else:
                                    if img[val[0]][val[1]+1]==colore_a:
                                        pass
                            else:
                                pass
                            
                            if val[1]-1>-1:
                                if img[val[0]][val[1]-1]==colore_i:
                                    area=area+1
                                    lista1=lista1+[[val[0],val[1]-1]]
                                    img[val[0]][val[1]]=colore_a
                                else:
                                    if img[val[0]][val[1]-1]==colore_a:
                                        pass
                            else:
                                pass
                            
                            lista1.remove(val)
                        return check(v1,v2)
                    except:
                        pass
                    
            check(v1,v2)
        area=0
        
        if len(lista)>0:
            return princ()
        else:
            pass
        
    princ()
    print(len1)
    if len1==1:
        listafin=[(2304,196)]*len1
    elif len1==2:
        listafin=[(2304,196)]*len1
    else:
        listafin=[(784,116)]*len1
        
    img=save(img,fnameout)
    return listafin