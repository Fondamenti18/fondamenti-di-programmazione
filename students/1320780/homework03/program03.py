from immagini import *
   
def ricolora(fname, lista, fnameout):
    img = load(fname)
    
    hMax = len(img)
    wMax = len(img[0])
    
    areePerim = []
    
    for posAndClrs in lista:
        x = posAndClrs[0]
        y = posAndClrs[1]
        colif = posAndClrs[2]
        colfr = posAndClrs[3]
        coli0 = img[y][x]
        
        pixStack = [(y,x)]
        checkedPix = set()
        
        frPoints = []
        intPoints = []
        
        while len(pixStack) > 0:
            lastPix = pixStack.pop()
            if lastPix not in checkedPix:
                Yi = lastPix[0]
                Xi = lastPix[1]
                
                sameCNum = 0
                
                if Xi - 1 >= 0 and img[Yi][Xi-1] == coli0:
                    pixStack.append((Yi,Xi-1))
                    sameCNum += 1
                    
                if Yi - 1 >= 0 and img[Yi-1][Xi] == coli0:
                    pixStack.append((Yi-1,Xi))
                    sameCNum += 1
                    
                if Xi + 1 < wMax and img[Yi][Xi+1] == coli0:
                    pixStack.append((Yi,Xi+1))
                    sameCNum += 1
                    
                if Yi + 1 < hMax and img[Yi+1][Xi] == coli0:
                    pixStack.append((Yi+1,Xi))
                    sameCNum += 1
                
                if sameCNum == 4:
                    intPoints.append((Yi,Xi))
                else:
                    frPoints.append((Yi,Xi))
                    
                checkedPix.add((Yi, Xi))
            
        for inp in intPoints:
            img[inp[0]][inp[1]] = colif
            
        for inp in frPoints:
            img[inp[0]][inp[1]] = colfr
        
        areePerim.append((len(intPoints), len(frPoints)))
    
    save(img, fnameout)
    
    return areePerim