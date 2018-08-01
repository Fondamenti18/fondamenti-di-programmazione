#filtra le lettere dalla chiave
def filtra_lettere_chiave (chiave):
    chiave_temp=''
    for car in chiave:
        if car>='a' and car<='z':
            chiave_temp+=car
    return chiave_temp

#toglie i doppioni dalla chiave
def filtra_doppioni_chiave(chiave_temp):
    chiave_temp=chiave_temp[::-1]
    chiave=''
    for car in chiave_temp:
        if car not in chiave:
            chiave+=car
            if len(chiave)==26:
                return chiave[::-1]
    return chiave[::-1]

#si occupa di preparare la chiave facendo uso di altre funzioni scritte
def elabora_chiave(chiave):
    chiave_temp=filtra_lettere_chiave(chiave)
    chiave=filtra_doppioni_chiave(chiave_temp)
    return chiave

#si occupa di cifrare il testo facendo uso di altre funzione scritte
def elabora_testo(chiave_1,chiave_2,testo):
    chiave_1_lst=list(chiave_1)
    chiave_2_lst=list(chiave_2)
    testo_elaborato_lst=[]
    for lettera in testo:
        testo_elaborato_lst=concatena_testo(lettera,chiave_2_lst,chiave_1_lst,testo_elaborato_lst)
    return "".join(str(x) for x in testo_elaborato_lst)

#concatena il nuovo testo cifrato
def concatena_testo(lettera,chiave_2_lst,chiave_1_lst,testo_elaborato_lst):
    if lettera in chiave_2_lst:
        testo_elaborato_lst+=[chiave_1_lst[chiave_2_lst.index(lettera)]]
    else:
        testo_elaborato_lst+=lettera
    return testo_elaborato_lst

#funzione principale decodifica
def codifica(chiave, testo):
    chiave_disordinata=elabora_chiave(chiave)
    chiave_ordinata=sorted(chiave_disordinata)
    return elabora_testo(chiave_disordinata,chiave_ordinata,testo)
    
# funzione principale codifica
def decodifica(chiave, testo):
    chiave_disordinata=elabora_chiave(chiave)
    chiave_ordinata=sorted(chiave_disordinata)
    return elabora_testo(chiave_ordinata,chiave_disordinata,testo)

