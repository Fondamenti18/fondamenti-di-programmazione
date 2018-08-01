def pulisci_chiave(chiave):
    chiave = [el for el in chiave if 'a'<=el<='z']
    return chiave

def crea_diz_cod(chiave):
    diz={}
    chiave2 = chiave.copy()
    chiave2.sort()
    for el in range(0, len(chiave)):
        diz[chiave2[el]] = chiave[el]
    return (diz)

def crea_diz_decod(chiave):
    diz={}
    chiave2 = chiave.copy()
    chiave2.sort()
    for el in range(0, len(chiave)):
        diz[chiave[el]] = chiave2[el]
    return (diz)

def crea_chiave(chiave):
    chiave = pulisci_chiave(chiave)
    chiave_n = []
    chiave.reverse()
    for car in chiave:
        if car not in chiave_n:
            chiave_n += [car]
    chiave_n.reverse()
    return (chiave_n)

def codifica(chiave, testo):
    diz = crea_diz_cod(crea_chiave(chiave))
    txt_cod=''

    for car in testo:
        if car in diz: txt_cod = txt_cod + diz[car]
        else: txt_cod = txt_cod + car
    return (txt_cod)

def decodifica(chiave, testo):
    diz = crea_diz_decod(crea_chiave(chiave))
    txt_dec=''
    
    for car in testo:
        if car in diz: txt_dec = txt_dec + diz[car]
        else: txt_dec = txt_dec + car
    return (txt_dec)
