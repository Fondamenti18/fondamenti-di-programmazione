def codifica(chiave, testo):
    
    chiave_processata = Elimina_caratteri(chiave, testo)
    Testo_criptato = Criptamento_chiave(chiave, testo)
    
    return Testo_criptato
    

def decodifica(chiave, testo):
    
    chiave_processata = Elimina_caratteri(chiave, testo)
    Testo_decriptato = Decriptamento_testo(chiave, testo)
    
    return Testo_decriptato
    
    
def Elimina_caratteri(chiave, testo):
    
    Lettere_minuscole = {0 : 'a', 1 : 'b', 2 : 'c', 3 : 'd', 4 : 'e', 5 : 'f', 6 : 'g', 7 : 'h', 8 : 'i', 9 : 'j', 10 : 'k', 11 : 'l', 12 : 'm', 13 : 'n', 14 : 'o', 15 : 'p', 16 : 'q', 17 : 'r', 18 : 's', 19 : 't', 20 : 'u', 21 : 'v', 22 : 'w', 23 : 'x', 24 : 'y', 25 : 'z'}
    Lista_caratteri_chiave = list(chiave)
    Lista_caratteri_chiave_minuscoli = []
    
    for a in range(len(Lista_caratteri_chiave)):
        
        for b in range(len(Lettere_minuscole)):
            
            if Lista_caratteri_chiave[a] == Lettere_minuscole[b]: Lista_caratteri_chiave_minuscoli += Lista_caratteri_chiave[a]
    
    return Lista_caratteri_chiave_minuscoli

def Elimina_doppie(chiave, testo):
    
    Caratteri_chiave_minuscoli = Elimina_caratteri(chiave, testo)
    
    for b in Caratteri_chiave_minuscoli[:]:
      
        Appoggio = Caratteri_chiave_minuscoli.count(b)
          
        if Appoggio > 1: 
          
            Posizione_inizio = Caratteri_chiave_minuscoli.index(b)
            del Caratteri_chiave_minuscoli[Posizione_inizio]
    
    return Caratteri_chiave_minuscoli

def Criptamento_chiave(chiave, testo):
    
    chiave_disordinata = Elimina_doppie(chiave, testo)
    chiave_ordinata = sorted(Elimina_doppie(chiave, testo))
    testo_criptato = ""
    
    Dizionario = dict(zip(chiave_ordinata, chiave_disordinata))
    
    for c in testo: 
        
        if c in Dizionario: testo_criptato += Dizionario[c]
        else: testo_criptato += c
    
    return testo_criptato



def Decriptamento_testo(chiave, testo):
    
    chiave_disordinata = Elimina_doppie(chiave, testo)
    chiave_ordinata = sorted(Elimina_doppie(chiave, testo))
    testo_decriptato = ""
    
    Dizionario = dict(zip(chiave_disordinata, chiave_ordinata))
    
    for c in testo: 
        
        if c in Dizionario: testo_decriptato += Dizionario[c]
        else: testo_decriptato += c
        
    return testo_decriptato