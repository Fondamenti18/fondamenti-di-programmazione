def codifica(chiave, testo):
    testo = esegui_cd_dcd(chiave, testo, True);
    return testo

def decodifica(chiave, testo):
    testo = esegui_cd_dcd(chiave, testo, False);
    return testo


def esegui_cd_dcd(chv,tst,codifica):
    lc_dis = crea_lista_disordinata(chv)
    lc_ord = sorted(lc_dis)
    ltst = [ord(car) for car in (tst)]

    if (codifica):
        for i in range(len(ltst)):
            val_da_cod = ltst[i]
            for j in range(len(lc_ord)):
                if (lc_ord[j] == val_da_cod):
                    ltst[i] = lc_dis[j]
    else:
        for i in range(len(ltst)):
            val_cod = ltst[i]
            for j in range(len(lc_dis)):
                if (lc_dis[j] == val_cod):
                    ltst[i] = lc_ord[j]

    tst = "".join(chr(val) for val in ltst)

    return tst

def crea_lista_disordinata (st):
   lnum = []
   lbool =  []
   lbool += [False]*97
   lbool += [True]*26

   for i in range(len(st)-1,-1,-1):
       cod = ord(st[i])
       if (cod<123):
           if (lbool[cod]):
               lnum += [cod]
               lbool[cod]=False

   lnum.reverse()
   return lnum
