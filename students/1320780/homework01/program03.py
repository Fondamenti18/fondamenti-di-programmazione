def initChiaviAndTesto(chiave, testo):
    tmpChiave = list(chiave)
    tmpTesto = list(testo)
    
    for ch in chiave:
        if ch not in 'abcdefghijklmnopqrstuvwxyz' or tmpChiave.count(ch) > 1:
            tmpChiave.remove(ch)
    
    tmpChiaveSorted = sorted(tmpChiave)
    
    return tmpChiave, tmpChiaveSorted, tmpTesto

def encodeFromXToY(keyX, keyY, lsTesto):
    for i in range(len(lsTesto)):
        if lsTesto[i] in keyX:
            lsTesto[i] = keyX[keyY.index(lsTesto[i])]
    return ''.join(lsTesto)


def codifica(chiave, testo):
    
    chiaviETesto = initChiaviAndTesto(chiave, testo)
            
    return encodeFromXToY(chiaviETesto[0],chiaviETesto[1],chiaviETesto[2])


def decodifica(chiave, testo):

    chiaviETesto = initChiaviAndTesto(chiave, testo)
            
    return encodeFromXToY(chiaviETesto[1],chiaviETesto[0],chiaviETesto[2])