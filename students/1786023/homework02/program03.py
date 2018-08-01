def decod(file,structure):
#open file
    #set of words
    newSet=[]
    with open(file, encoding='utf-8',) as objectPost:
    #start loop
        for newLine in objectPost:
            #trim white spaces .strip()
            newLine = newLine.strip()
            #check if structure lenght == word lenght
            if len(structure)==len(newLine):
                #if stucture == word structure?
                if recogniseStruct(structure,newLine):
                    #print(structure,'  ',newLine)
                    newSet.append(newLine)
    return set(newSet)
                   
#return set

#recognise structure
def recogniseStruct(structure,word):
    lok = dict()
    index=0
    #loop trough structure
    for i in structure:
        #get next key from structure
            #check if key is in list
        if i in lok.keys():
            #if yes -> check if value == to character in this place in word
            if lok[i] == word[index]:
                    #continue true
                index +=1
            else:
                return False
        else:
            #check if value in dictionary
            if word[index] in lok.values():
                return False
            else:
            #else ->not in list ->create new key:value pair in list
                lok[i]=word[index]
                index+=1
    return True

 
