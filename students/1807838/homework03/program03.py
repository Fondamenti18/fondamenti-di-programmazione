from immagini import *
def ricolora(fname, lista, fnameout):
	global w,h,img
	img=load(fname)
	w=len(img[0])-1
	h=len(img)-1
	ret=[]
	for el in lista:
		area,bordo=adiacenti(el[1],el[0],el[2],el[3])
		ret.append((area,bordo))
	save(img,fnameout)
	return ret

def adiacenti(row,col,ca,cb):
	li=[(row,col)]
	c=img[row][col]
	bordo=set()
	area=0
	per=0
	insi={(row,col)}
	for x in li:
		row=x[0]
		col=x[1]
		if (row+1,col) not in insi:
			if row<h:
				if img[row+1][col]==c:
					li.append((row+1,col))
					insi.add((row+1,col))
				else:
					bordo.add((row,col))
			else:
				bordo.add((row,col))
		if (row-1,col) not in insi:
			if row>0:
				if img[row-1][col]==c:
					li.append((row-1,col))
					insi.add((row-1,col))
				else:
					bordo.add((row,col))
			else:
				bordo.add((row,col))
		if (row,col+1) not in insi:
			if col<w:
				if img[row][col+1]==c:
					li.append((row,col+1))
					insi.add((row,col+1))
				else:
					bordo.add((row,col))
			else:
				bordo.add((row,col))
		if (row,col-1) not in insi:
			if col>0:
				if img[row][col-1]==c:
					li.append((row,col-1))
					insi.add((row,col-1))
				else:
					bordo.add((row,col))
			else:
				bordo.add((row,col))
	for x in insi:
		img[x[0]][x[1]]=ca
		area+=1
	for x in bordo:
		img[x[0]][x[1]]=cb
		per+=1
	return area-per,per
