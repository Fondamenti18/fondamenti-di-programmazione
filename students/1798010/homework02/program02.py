import json
       
def LoadElements(path):
   
    elementDic = {}

    previousElement = None

    with open(path, mode='r') as f:
        for line in f:            
           
            tempId = FindId(line)

            if line.find("c") != -1:

                elementDic[tempId] = ""
                previousElement = tempId;

            elif line.find("s") != -1:    

                elementDic[previousElement] = tempId                
                   
    return elementDic
       
   
def FindId(string):
   
    numString = ""
   
    for c in string:
        if c.isnumeric():
            numString += c
   
    return numString
            

 
def pianifica(fcompiti,insi,fout):
   
    elementDic = LoadElements(fcompiti)
    outputDic = {}

    currentElement,key = 0,0

    newInsi = set()

    for toCheck in insi:        
        if toCheck in elementDic:

            newInsi.add(toCheck)
            key = elementDic[toCheck]
            outputDic[toCheck] = [key]


            while key != "":

                if elementDic[key] != "":
                    outputDic[toCheck] += [elementDic[key]]

                key = elementDic[key]

    for key in newInsi:

        outputDic[key].reverse()

        if "" in outputDic[key]:
            outputDic[key].remove("")    

    with open(fout, mode='w') as f:
        json.dump(outputDic, f)
                