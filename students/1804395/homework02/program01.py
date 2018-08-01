def compassMaker(file): #restituisce una lista di liste che associa ad ogni N post l'insieme delle parole associate
    compass=[]
    fileLenght=len(file)
    translationTable= str.maketrans('''.,;:-_#°§*+^'?=)(/&%$£"!\[]|<>''','''                              ''')
    for lineIndex in range(fileLenght):
        if '<POST>' in file[lineIndex]:
            postNumber= file[lineIndex].strip(' <POST>');
            #postNumber=((((file[lineIndex].translate(translationTable)).split())[0])) #funzione che individuata la linea che identifica il post ne ricava l'ID ##'''alternativa valida (da valutare la piu economica)'''
            #postNumber=(((file[lineIndex].split())[1]) if len((file[lineIndex].split()))==2 else ((file[lineIndex].split())[0][6:]))    #'''alternativa valida (da valutare la piu economica)'''
            compass.append([postNumber,lineIndex]) #funzione che associa ad ogni post ID la linea identificativa del post 
    compass.append(['',fileLenght])    #funzione che appende alla lista un ulteriore elemento di coda
    for i in range((len(compass)-1)):        
        compass[i][1]=set((((' '.join(file[(compass[i][1]+1):(compass[i+1][1])])).lower()).translate(translationTable)).split()) #funzione che associa ad ogni post ID l'insieme delle parole associate       
    return(compass)            
    
def post(fposts,insieme):
    with open(fposts, encoding='utf-8') as f:
        file=(f.read()).splitlines() #funzione che restituisce una lista di stringhe ripulite che corrispondono alle linee di testo
    compass= compassMaker(file) 
    result =set()
    insieme=set(i.lower() for i in insieme)
    for index in range(len(compass)-1):
        commonElements= insieme.intersection(compass[index][1]) #funzine che interseca l'insieme ripulito e l'insieme di parole associato ad ogni post
        if len(commonElements)!= 0:
            result.add(compass[index][0]) #funzione che appende all'insieme risultato gli ID relativi ai post validi
    return (result)
