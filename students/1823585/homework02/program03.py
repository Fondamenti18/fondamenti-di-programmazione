def decod(pfile, codice):
    contenuto=set()
    voc={}
    lettura=open(pfile,'r')
    lun_cod=len(codice)
    lung_set_cod=len(set(codice))
    try:
        with lettura as f:
                rr=f.readlines()
                for p in rr:  
                    lemma=""
                    p=p[:-1]
                    lungset_p=len(set(p))
                    #variabili di assegnamento Booleane così velocizzo il codice
                    if (len(p)==lun_cod)==True:
                        if(lungset_p is lung_set_cod)==True:
                            voc={el_1:el_2 for el_1,el_2 in zip(codice,p)}
                            for e in codice:
                                lemma+=voc[e]
                                if (lemma==p)==True:
                                    contenuto.add(lemma)
    except FileExistsError:
        print("File non presente")
    return contenuto