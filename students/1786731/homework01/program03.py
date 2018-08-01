validinput = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def revkey(nuovachiave):
    nuovachiavesingle = []
    for char in nuovachiave:
        if char not in nuovachiavesingle:
            nuovachiavesingle.append(char)
    
    return nuovachiavesingle

def chiavi(chiave):
    revnuovachiave = [ char for char in reversed(chiave) if char in validinput] # check per l'input reversato
    nuovachiavesingle = ''.join(revkey(revnuovachiave)[::-1]) # chiave disordinata
    return nuovachiavesingle, ''.join(sorted(nuovachiavesingle)) # chiave ordinata

def cript(ls1, ls2, testo):
    return ''.join([ char if ls1.find(char) == -1 else ls2[ls1.find(char)] for char in testo ])

def codifica(chiave, testo):
    nuovachiavesingle, nuovachiavesingleord = chiavi(chiave)
    return cript(nuovachiavesingleord, nuovachiavesingle, testo)

def decodifica(chiave, testo):
    nuovachiavesingle, nuovachiavesingleord = chiavi(chiave)
    return cript(nuovachiavesingle, nuovachiavesingleord, testo)