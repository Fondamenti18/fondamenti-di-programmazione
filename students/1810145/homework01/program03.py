def pulisci(chiave):
    app=[]
    for i in chiave:
        if True==i.isalpha() and 'a'<= i <= 'z':
            app+=i
    l=len(app)
    while l!=0:
        l-=1
        if app.count(app[l])>1:
            app.remove(app[l])
    return app


def ordina(chiave):
    app=pulisci(chiave)
    sorapp=sorted(app)
    cont=0
    coppie=[]
    for i in app:
        coppie+=[sorapp[cont]+app[cont]]
        cont+=1
    return coppie


def codifica(chiave, testo):
    coppie=ordina(chiave)
    str=''
    for i in testo:
        cont=1
        for j in coppie:
            cont+=1
            if j[0]==i:
                str+=j[1]
                break
            if cont > len(coppie):
                str+=i
                break
    testo=''
    testo+=str
    return testo


def decodifica(chiave, testo):
    coppie=ordina(chiave)
    str=''
    for i in testo:
        cont=1
        for j in coppie:
            cont+=1
            if j[1]==i:
                str+=j[0]
                break
            if cont > len(coppie):
                str+=i
                break
    testo=''
    testo+=str
    return testo



