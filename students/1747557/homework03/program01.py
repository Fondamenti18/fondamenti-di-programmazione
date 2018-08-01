import png
from immagini import *






def isThisColor(c1, c2):
	return c1[0] == c2[0]and  c1[1] == c2[1] and c1[2] == c2[2]


def converti(img, c):

	n = len(img) #altezza
	m = len(img[0])#larghezza

	Matrix = [[0 for g in range(m)] for r in range(n)]
	#print(Matrix)
	for i in range(n):
		for j in range(m):
			if isThisColor(img[i][j], c):
				Matrix[i][j] = 1
	return Matrix
    
    


	
	
	
	
	
	
def generateRowMatrix(matrix):
    n = len(matrix) #altezza
    m = len(matrix[0])#larghezza
    rowMatrix = [[0 for g in range(m)] for r in range(n)]

    pivot = -1;
    k = 0;
    for i in range(0, n):
        for j in range(0, m):
            if (matrix[i][j] == 1):
                if (pivot == -1):
                    pivot = j
                k += 1;
            elif pivot != -1:
                #scarica
                for q in range(0, k):
                    rowMatrix[i][pivot + q] = k - q;

                k = 0
                pivot = -1
        if pivot != -1:
            #scarica
            for q in range(0, k):
                rowMatrix[i][pivot + q] = k - q;
            k = 0
            pivot = -1
            
        
    return rowMatrix;




def quadrato(filename, c):
	img = load(filename)

	matrix = converti(img, c)
	
	
	

	n = len(matrix) #altezza
	m = len(matrix[0])#larghezza


	rowMatrix = generateRowMatrix(matrix);


	lato = 0
	x = -1
	y = -1
		
	for i in range(0, n):
		if i > n - lato -1:
			#da qui in poi non posso piu trovare quadrati 
			break;
        
		for j in range(0, m):
			q = rowMatrix[i][j]
			lato2 = 0
			x2 = i
			y2 = j

			if j > m - lato -1:
			#da qui in poi non posso piu trovare quadrati 
				break;
			if q != 0:
				if q > min(n,m):
					q = min(n,m)
				if q > n-i or q > m-j:
					q = min(n-i,m-j)
				if q < lato:
					#caso ho gia trovato un quadrato piu grosso
					continue
				if q == 1:
					#caso pixel
					x2 = i
					y2 = j
					lato2 = 1
                    
					if lato2 > lato:
						lato = lato2
						x = x2
						y = y2
						continue
				else:
					#caso piu grande
					
					quadratoQ = True                    
					limit = i+q
					count = 0
					for k in range(i, limit):
						if rowMatrix[k][j] < q:
							if rowMatrix[k][j] < lato:
								quadratoQ = False
								break
							else:
								limit = i+rowMatrix[k][j]
								q = rowMatrix[k][j]
						count+=1
						if count > limit-i-1:
							break;
						
					if quadratoQ:
						x2 = i
						y2 = j
						lato2 = count
			if lato2 > lato:
				lato = lato2
				x = x2
				y = y2
	
	return (lato, (y, x))
	
	
def min(a,b):
	if a<b:
		return a
	else:
		return b
		

