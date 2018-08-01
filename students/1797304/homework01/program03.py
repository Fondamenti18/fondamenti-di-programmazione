def crea_lista(chiave):
    lista=[]
    for c in chiave:
        if 'a'<= c <='z':
            lista.append(c)
            if lista.count(c)>1:
                lista.remove(c)
    return lista
   



def codifica(chiave, testo):
    lista=crea_lista(chiave)
    ordinata=sorted(lista)
    coppie=dict(zip(ordinata,lista))
    finale=[coppie[c]if c in coppie else c for c in testo]
    return ''.join(finale)
    
    
    
    
    
def decodifica(chiave, testo):
   lista=crea_lista(chiave)
   ordinata=sorted(lista)
   coppie=dict(zip(lista,ordinata))
   finale=[coppie[c]if c in coppie else c for c in testo]
   return ''.join(finale)