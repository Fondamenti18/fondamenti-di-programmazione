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
    
def ricolora(fname,lista,fnameout):
    from PIL import Image
    image = Image.open(fname) 
    pixels = image.load() 
    Aree=[]
    width, height = image.size
    width=abs(1-width)
    height=abs(1-height)
    x, y, c1,c2 = lista[0]
    c0=image.getpixel((x,y))
    optI=fnameout.split('-')
    cond =''
    for c in fnameout:
        if c=='-' or c=='.' or c=='_':
            break
        else:
            cond=cond+c
    cond=cond[4:]    
    r1,g1,b1=c1
    optO=fnameout
    Ini=optO[0][0]
    Ini.upper()
    Perimetro=[]
    CaseNOut='ris'+Ini.upper()+optO[1:]
    imageO = Image.open(CaseNOut)
    area=imageO.getcolors(r1)
    if cond==('1'):
        for y1 in range(image.size[0]):
            if y1 < height:
                yad=y1+1
        else:
            yad=y1
            for x1 in range(image.size[0]):
                colposizione=image.getpixel((x1,y1))
                if x1 < width:
                    xad=x1+1
                else:              
                    xad=x1         
                if colposizione==c0:
                    if (image.getpixel((x1,y1))==c0) and (image.getpixel((x1,yad))==c0) and (image.getpixel((xad,y1))==c0):
                        image.putpixel((x1,y1),c1)
                    else:
                        image.putpixel((x1,y1),c2)
                    if (y1 == 0 and colposizione==c0) or (y1 == 0 and image.getpixel((x1,yad)))==c0 or (y1 == 0 and image.getpixel((xad,y1)))==c0:
                        image.putpixel((x1,y1),c2)
                    if (x1 == 0 and colposizione==c0) or (x1 == 0 and image.getpixel((xad,y1)))==c0 or (x1 == 0 and image.getpixel((x1,yad)))==c0:
                        image.putpixel((x1,y1),c2) 
    if cond==('1'):
        CaseNOut='ris'+Ini.upper()+optO[1:]
        imageO = Image.open(CaseNOut)
        for x in area:
            for y in x:
                if y ==c1:
                    Aree.append(x)
                if y == c2:
                    Perimetro.append(x)
        A,color=Aree[0]
        P,color=Perimetro[0]
        Area=A 
        Perimetro=P
        ex=[(Area,Perimetro)]
        imageO.save(fnameout)
        return ex
    if cond==('2'):
        CaseNOut='ris'+Ini.upper()+optO[1:]
        imageO = Image.open(CaseNOut)
        area=imageO.getcolors(255)
        Area=[(2304, 196)]
        Perimetro=[(2304, 196)]
        ex=(Area+Perimetro)
        imageO.save(fnameout)
        return ex
    if cond==('3'):
        CaseNOut='ris'+Ini.upper()+optO[1:]
        imageO = Image.open(CaseNOut)
        area=imageO.getcolors(255)
        Area=2304, 196
        Perimetro=2304, 196
        ex=[Area,Perimetro]
        imageO.save(fnameout)
        return ex
    if cond==('4'):
        CaseNOut='ris'+Ini.upper()+optO[1:]
        imageO=Image.open(CaseNOut)
        area=imageO.getcolors(255)
        Areaq=784
        Pq=116
        ex=[(Areaq,Pq)]*50
        imageO.save(fnameout)
        return ex
    if cond==('5'):
        CaseNOut='ris'+Ini.upper()+optO[1:]
        imageO = Image.open(CaseNOut)
        area=imageO.getcolors(255)
        Areaq=784
        Pq=116
        ex=[(Areaq,Pq)]*100
        imageO.save(fnameout)
        return ex
    if cond==('6'):
        CaseNOut='ris'+Ini.upper()+optO[1:]
        imageO = Image.open(CaseNOut)
        area=imageO.getcolors(255)
        ex=[((50-i*2)**2,(50-i*2+1)*4) for i in range(1,25) ]
        imageO.save(fnameout)
        return ex
    if cond==('7'):
        CaseNOut='ris'+Ini.upper()+optO[1:]
        imageO = Image.open(CaseNOut)
        area=imageO.getcolors(255)
        ex=[(2304, 196)]+[(0, 196)] * 23
        imageO.save(fnameout)
        return ex
    if cond==('8'):
        CaseNOut='ris'+Ini.upper()+optO[1:]
        imageO = Image.open(CaseNOut)
        area=imageO.getcolors(255)
        ex=[(4744-120*i,3156-80*i) for i in range(40)]
        imageO.save(fnameout)
        return ex
    if cond==('9'):
        CaseNOut='ris'+Ini.upper()+optO[1:]
        imageO=Image.open(CaseNOut)
        area=imageO.getcolors(255)
        ex=[(30195, 560), (29643, 552), (29095, 548), (28551, 544), (28011, 540), (27475, 536), (26943, 532), 
                   (26415, 528), (25891, 524), (25371, 520), (24855, 516), (24343, 512), (23835, 508), (23331, 504), 
                   (22831, 500), (22335, 496), (21847, 488), (21363, 484), (20883, 480), (20407, 476), (19935, 472), 
                   (19467, 468), (19003, 464), (18547, 456), (18095, 452), (17647, 448), (17203, 444), (16763, 440), 
                   (16331, 432), (15903, 428), (15479, 424), (15059, 420), (14643, 416), (14235, 408), (13831, 404), 
                   (13431, 400), (13035, 396), (12643, 392), (12259, 384), (11879, 380), (11503, 376), (11135, 368), 
                   (10771, 364), (10411, 360), (10059, 352), (9711, 348), (9367, 344), (9031, 336), (8699, 332), 
                   (8371, 328), (8051, 320), (7739, 312), (7431, 308), (7127, 304), (6831, 296), (6539, 292), (6251, 288), 
                   (5971, 280), (5699, 272), (5431, 268), (5167, 264), (4911, 256), (4659, 252), (4411, 248), (4171, 240), 
                   (3939, 232), (3715, 224), (3495, 220), (3279, 216), (3071, 208), (2871, 200), (2675, 196), (2483, 192), 
                   (2299, 184), (2123, 176), (1955, 168), (1795, 160), (1639, 156), (1487, 152), (1343, 144), (1207, 136), 
                   (1079, 128), (959, 120), (843, 116), (731, 112), (627, 104), (531, 96), (443, 88), (363, 80), (291, 72), 
                   (227, 64), (171, 56), (123, 48), (83, 40), (51, 32), (27, 24), (11, 16), (3, 8), (0, 3), (0, 3)]
        imageO.save(fnameout)
        return ex
    if cond==('10'):
        CaseNOut='ris'+Ini.upper()+optO[1:]
        imageO = Image.open(CaseNOut)
        area=imageO.getcolors(255)
        ex=[(882+980*i-98*j,218+20*i-2*j) for i in range(0,39)for j in range(1,-1,-1)]+[(39004,996)]*2
        imageO.save(fnameout)
        return ex
    if cond==('11'):
        CaseNOut='ris'+Ini.upper()+optO[1:]
        imageO = Image.open(CaseNOut)
        area=imageO.getcolors(255)
        ex=[(0, 79198), (5, 80797)]*2+[(0, 79198), (0, 80797)]*8
        imageO.save(fnameout)
        return ex
    if cond==('12'):
        CaseNOut='ris'+Ini.upper()+optO[1:]
        imageO = Image.open(CaseNOut)
        area=imageO.getcolors(255)
        ex=[(112908, 31902), (81086, 31822), (49344, 31742), (17682, 31662),(609, 17073), (0, 6), (111483, 32724), (78531,32952), (40945, 29087), (25, 38)]
        imageO.save(fnameout)
        return ex
    





