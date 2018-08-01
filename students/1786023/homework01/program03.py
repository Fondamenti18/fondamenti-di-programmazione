def codifica(chiave,testo):
    #get unsorted key
    unsortedKey = getEncodingKey(chiave)
    sortedKey = sorted(unsortedKey)

    #save after sorting abc
     
    #print("unsorted list ",unsortedKey)
    #print("sorted list ",sortedKey)
    #start encoding
    encoded=[]
    for i in range(len(testo)):
        if sortedKey.count(testo[i]):
            #check the index in new list
            #get the letter from old list in index
            #append new letter to new testo
            encoded.append(unsortedKey[sortedKey.index(testo[i])])
        #else append testo[i] to newTesto
        else:
            encoded.append(testo[i])
    #print original string
    #print("Original word: ",testo)
    #print encoded string
    #print ("Encoded word: ",''.join(encoded))
    #return encoded word for future usage
    return ''.join(encoded)

def decodifica(chiave,testo):
    unsortedKey = getEncodingKey(chiave)
    sortedKey = sorted(unsortedKey)
    #decoded testo
    decoded = []
    #loop though the testo
    for i in range(len(testo)):
        #if testo[i] exist in unsorted cheave key
        if unsortedKey.count(testo[i]):
            #get index of key inside unsorted cheave
            #get char in sorted cheave and append to DECODED list
            decoded.append(sortedKey[unsortedKey.index(testo[i])])
        else:
            #else append the char to DECODED LIST
            decoded.append(testo[i])
    #print decoded and return
    #print ("decoded word: ",''.join(decoded))
    return ''.join(decoded)


def getEncodingKey(chiave):  
    unsortedKey = []
    for i in range(len(chiave)):
        if(ord(chiave[i])>96 and ord(chiave[i])<123):
            #print keys and integer codes
            #print(chaeve[i]," ",ord(chaeve[i]))
            unsortedKey.append(chiave[i])
    #print(unsortedKey)
    #new list of duplicated chars
    dublicatet = []
    for k in range(len(unsortedKey)):
        #check if letter is duplicated
        if unsortedKey.count(unsortedKey[k])>1:
            #append unique duplicate char
            if dublicatet.count(unsortedKey[k])==0:
                dublicatet.append(unsortedKey[k])
    # remove first accureance of letter
    for i in range(len(dublicatet)):
        while unsortedKey.count(dublicatet[i])>1:
            unsortedKey.remove(dublicatet[i])         
    #print("duplicatet chars: ",dublicatet)       
    #save UNsorted  
    
    sortedKey = sorted(unsortedKey)

    #save after sorting abc
     
    #print("unsorted list ",unsortedKey)
    return unsortedKey

# =============================================================================
# #encode the word
# codifica = encoding(chiave,testo)
# #decode the encoded word
# decodifica(chiave,encoded)
# =============================================================================
