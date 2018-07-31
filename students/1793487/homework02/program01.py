def post(fposts, insieme):
        set_ID = set()
        low_insieme = set()
        with open(fposts,'r', encoding='utf-8') as testo:
                t=testo.read()
        caratteri=set(t)
        for c in caratteri:
                if not c.isalnum():
                        t= t.replace(c, ' ')
        lista_parole = t.strip().split()
        for parola in insieme:
            low_insieme.add(parola.lower())
        for indice,parola in enumerate(lista_parole):
            parola=parola.lower()
            if parola == 'post':
                ID = lista_parole[indice+1]
            if parola in low_insieme:
                set_ID.add(ID)
        return set_ID
