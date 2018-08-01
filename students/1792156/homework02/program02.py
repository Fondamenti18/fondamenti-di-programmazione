
import json


def estrai_dizionario_esami(fcompiti):
    dizionario_esami = dict()
    with open(fcompiti, 'r') as file_compiti:
        # Creo una lista con le righe del file
        righe_file = file_compiti.readlines()
        ultimo_esame_comp = None

        for riga in righe_file:
            # Elimino gli spazi dalla riga
            cleaned = riga.replace(" ", "")
            if "comp" in cleaned:
                # Estraggo il numero dell'esame
                # Lo faccio rimuovendo la parola 'comp' in questo modo resta solo il numero
                id_esame = cleaned.replace("comp", "").replace("\n", "")
                dizionario_esami[id_esame] = None
                ultimo_esame_comp = id_esame
            elif "sub" in cleaned:
                # Estraggo il numero dell'esame
                # Lo faccio rimuovendo la parola 'sub' in questo modo resta solo il numero
                id_esame = cleaned.replace("sub", "").replace("\n", "")
                dizionario_esami[ultimo_esame_comp] = id_esame

        return dizionario_esami


def estrai_dizionario_dipendenze(dizionario_esami, insi):
    # Partendo dal dizionario completo degli esami
    # costruiamo un nuovo dizionario. Questo sarà il dizionario che tiene conto delle dipendenze tra esami
    dizionario_dipendenze = dict()
    for id_esame in insi:
        # Se è stata richiesta una chiave che non c'è nel file degli esami
        # salta al prossimo step del ciclo
        if not id_esame in dizionario_esami:
            continue

        dizionario_dipendenze[id_esame] = []
        # Se ho degli esami precedenti li accedo navigando le opportune chiavi del dizionario
        last_esame = id_esame
        while True:
            esame_precedente = dizionario_esami[last_esame]
            
            if esame_precedente is None:
                break
            else:
                dizionario_dipendenze[id_esame].insert(0,esame_precedente)
                last_esame = esame_precedente
    return dizionario_dipendenze
        
        
def scrivi_su_file(dizionario_dipendenze, fout):
    with open(fout, 'w') as file_out:
        file_out.write(json.dumps(dizionario_dipendenze))


def pianifica(fcompiti, insi, fout):
    dizionario_esami = estrai_dizionario_esami(fcompiti)
    dizionario_dipendenze = estrai_dizionario_dipendenze(dizionario_esami, insi)
    scrivi_su_file(dizionario_dipendenze, fout)
