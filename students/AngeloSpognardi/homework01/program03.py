import logging

ch = logging.StreamHandler()
formatter = logging.Formatter('%(name)s | %(message)s')
ch.setFormatter(formatter)
log = logging.getLogger(__name__)
log.addHandler(ch)
log.propagate = False
log.setLevel(logging.WARNING)

def getkey(chiave):
    chiave=[c for c in chiave if 'a'<=c<='z']
    k=[]
    for i in range(len(chiave)-1,-1,-1):
        if chiave[i] not in k:
            k+=[chiave[i]]
    k.reverse()
    key=k.copy()
    k.sort()
    log.info('k:{0} key:{1}'.format(k, key))
    enc=[chr(i) for i in range(ord('a'),ord('z')+1)]
    dec=enc[:]
    for c, encc in zip(k, key):
        enc[ord(c)-ord('a')]=encc
        dec[ord(encc)-ord('a')]=c
    log.info('enc:{0}'.format(enc))
    log.info('dec:{0}'.format(dec))
    return enc,dec

def codifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    enc, dec  = getkey(chiave)
    s=''
    for c in testo:
        if 'a'<=c<='z': 
            s+=enc[ord(c)-ord('a')]
        else:
            s+=c
    return s
            
def decodifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    enc, dec  = getkey(chiave)
    s=''
    for c in testo:
        if 'a'<=c<='z':
            s+=dec[ord(c)-ord('a')]
        else:
            s+=c
    return s

if __name__=='__main__':
    cod= codifica('sim sala Bim!','il mare sa di sale')
    decod=decodifica('sim sala Bim!', cod)
    print(cod)
    print(decod)
