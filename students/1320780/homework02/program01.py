import string

def removePunctuation(parags):
    
    for i in range(len(parags)):
        for ch in string.punctuation:
            parags[i] = parags[i].replace(ch, ' ')
    
    return parags
    
def getLowerWorldsSet(words):
    lwrSet = set()
    for word in words:
        lwrSet.add(word.lower())
    return lwrSet

def post(fposts,insieme):
    with open(fposts, encoding="utf-8") as f:
        
        lowerWords = getLowerWorldsSet(insieme)
        fileText = f.read().lower()
        postsLs = removePunctuation(fileText.split('<post>'))
        
        postIdSet = set()
        
        for post in postsLs:
            postSplit = post.split()
            for word in lowerWords:
                if word in postSplit:
                    postIdSet.add(postSplit[0])
                    
        return postIdSet
                


