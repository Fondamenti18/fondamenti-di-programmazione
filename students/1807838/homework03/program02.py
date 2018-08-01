from immagini import *
def cammino(fname,  fname1):
	img=load(fname)
	ret=''
	direzione=0
	row=0
	col=0
	stop=0
	quad(img,row,col,40,40,(0,255,0))
	while stop<2:
		if direzione==0:
			if col+40<=len(img[0])-1 and img[row][col+40]!=(255,0,0) and img[row][col+40]!=(0,255,0):
				col+=40
				quad(img,row,col,40,40,(0,255,0))
				ret+=str(direzione)
				if stop==1:stop=0
			else: direzione=1
		if direzione==1:
			if row+40<=len(img)-1 and img[row+40][col]!=(255,0,0) and img[row+40][col]!=(0,255,0):
				row+=40
				quad(img,row,col,40,40,(0,255,0))
				ret+=str(direzione)
				if stop==1:stop=0
			else:direzione=2
		if direzione==2 :
			if col>=40 and img[row][col-40]!=(255,0,0) and img[row][col-40]!=(0,255,0):
				col-=40
				quad(img,row,col,40,40,(0,255,0))
				ret+=str(direzione)
				if stop==1:stop=0
			else:direzione=3
		if direzione==3 :
			if row>=40 and img[row-40][col]!=(255,0,0) and img[row-40][col]!=(0,255,0):
				row-=40
				quad(img,row,col,40,40,(0,255,0))
				ret+=str(direzione)
				if stop==1:stop=0
			else:direzione=4
		if direzione==4:
			direzione=0
			stop+=1
	quad(img,row,col,40,40,(0,0,255))
	save(img,fname1)
	return ret

def quad(img,x,y,w,h,c):
	#disegna sull'immagine img un rettangolo di colore c , ampiezza w e altezza h a partire da x,y
	for row in range (x,x+w):
		for col in range (y,y+h):
			img[row][col]=c
