import json
def pianifica(fcompiti,insi,fout):
    diz={}
    with open (fcompiti, encoding='utf-8') as f:
        testo= f.read()
        for elemento in insi:
            lista_valori=ciclo(elemento,testo)
            if lista_valori== False:
                continue
            else:
                diz[elemento]=lista_valori
        file=open(fout, mode='w')
        json.dump(diz,file)
        file.close

                            
def ciclo(valore, testo):
    lista=[]
    while valore != 0:  
        valore=trova(valore, testo)
        if valore==0:
            break
        elif valore == 'Esci':
            return 0
        else:
            lista.append(valore)
    lista1=lista[::-1]
    return lista1

def trova(elemento, testo):
    c=0
    file=testo.split("\n")
    for riga in file:
        c=c+1
        if 'comp' in riga:
            if elemento in riga:
                numero_comp=semplifica('comp', riga)
                if elemento == numero_comp:
                    riga2=file[c]
                    riga2=riga2.strip()
                    if 'sub' in riga2:
                        numero_testo_sub=semplifica('sub', riga2)
                        return numero_testo_sub
                    else:
                        return 0
        elif riga=='':
            return 'Esci'
        else:
            continue       

def semplifica(stringa, riga):
      riga=riga.replace(stringa, ' ')
      riga=riga.replace('\n', ' ')
      risultato=riga.replace(' ', '')   
      return risultato            
                                  
                            