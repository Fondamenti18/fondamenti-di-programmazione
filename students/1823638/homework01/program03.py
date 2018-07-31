def codifica(chiave, testo):
    chiavefin=''
    for car in ' ABCDEFGHIJKLMNOPQRSTWXYZ1234567890':
        chiave=chiave.replace(car,'')
        ricercalet=chiave[::-1]
    for car in ricercalet:
        if car not in chiavefin:
            chiavefin=chiavefin+car
    chiavefin=chiavefin[::-1]
    ordin=sorted(chiavefin)
    diz1={}
    count=0
    for i in chiavefin:
        diz1[ordin[count]]=i
        count+=1
    testofin=''
    for lettere in testo:
        if lettere in diz1:
            lettere=lettere.replace(lettere,diz1[lettere])
            testofin=testofin+lettere
        elif lettere not in diz1:
            testofin=testofin+lettere
    return testofin

def decodifica(chiave, testo):
    chiavefin=''
    for car in ' ABCDEFGHIJKLMNOPQRSTWXYZ1234567890':
        chiave=chiave.replace(car,'')
        ricercalet=chiave[::-1]
    for car in ricercalet:
        if car not in chiavefin:
            chiavefin=chiavefin+car
    chiavefin=chiavefin[::-1]
    ordin=sorted(chiavefin)
    diz1={}
    count=0
    for i in ordin:
        diz1[chiavefin[count]]=i
        count+=1
    testofin=''
    for lettere in testo:
        if lettere in diz1:
            lettere=lettere.replace(lettere,diz1[lettere])
            testofin=testofin+lettere
        elif lettere not in diz1:
            testofin=testofin+lettere
    return testofin
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

