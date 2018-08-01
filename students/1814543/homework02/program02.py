import json
def risultato_dizionario(lista_compiti):
    current_compito = "" 
    risultato = {}
    i = 0
    l = len(lista_compiti)
    while i < l:
        linea_compito = lista_compiti[i]
        current_compito =linea_compito.replace("comp", "")
        current_compito = current_compito.strip()
        if i < (l-1):
            linea_compito_successiva = lista_compiti[i+1]
            if "sub" in linea_compito_successiva:                
                compito_sub = linea_compito_successiva.replace("sub", "")
                compito_sub = compito_sub.strip()
                risultato[current_compito] = compito_sub
                i = i + 1
            else:
                risultato[current_compito] = ""
        else:
            risultato[current_compito] = ""
        i = i + 1

    return risultato


def pianifica(fcompiti,insi,fout):
    
    risultato_finale={}
    my_input_file = open (fcompiti,'r',encoding = 'utf-8')
    lista_compiti = my_input_file.readlines()
    dizionario = risultato_dizionario(lista_compiti)
    lista_chiavi = list(dizionario.keys())

    for compito_da_cercare in insi:
        i = 0
        compito_target = compito_da_cercare
        ldiz = len(dizionario)
        lista_dipendenze = []
        compito_trovato = False
        while i < ldiz:
            chiave_corrente = lista_chiavi[i]
            if compito_target == chiave_corrente:
                compito_trovato = True
                my_dipendenza = dizionario[chiave_corrente]
                if my_dipendenza != "":
                    lista_dipendenze = [my_dipendenza] + lista_dipendenze
                    compito_target = my_dipendenza
                    i = 0
                else:
                    break
            else:
                i = i +1
        if compito_trovato:
            risultato_finale[compito_da_cercare] = lista_dipendenze
    my_input_file.close()
    my_output_file = open (fout,'w')
    json.dump(risultato_finale, my_output_file)  
    my_output_file.close()