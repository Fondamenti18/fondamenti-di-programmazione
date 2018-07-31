from immagini import *

def quadrato(filename,c):
	lato = [-1]
	vertice = [0, 0]
	img = load(filename)
	for row in range(len(img)):
		for col in range(len(img[0])):
			if img[row][col] == c:
				v = [row, col]
				cerca_quadrati(img, lato, vertice, v, c)
	return (lato[0], (vertice[1], vertice[0]))
				
def cerca_quadrati(image, lato, vertice, v, c):
	value = True
	l = lato[0] + 1
	while v[0] + l < len(image) and v[1] + l < len(image[0]) and value:
		value, l = controlli(image, l, v, c, value)
	if not value and lato[0] < l - 1:
		lato[0] = l
		vertice[:] = v[:]
		
def controlli(image, l, v, c, value):
	if primari(image, l, v, c):
		value = False
	elif secondari(image, l, v, c):
		value = False
	else:
		l += 1
	return value, l
	
def primari(image, l, v, c):
	value = False
	if not vertici(image, l, v, c):
		value = True
	elif not diagonale1(image, l, v, c):
		value = True
	elif not diagonale2(image, l, v, c):
		value = True
	return value
	
def secondari(image, l, v, c):
	value = False
	if l != 0 and not frame(image, l, v, c):
		value = True
	elif l != 0 and not full(image, l, v, c):
		value = True
	return value

def vertici(image, l, v, c):
	return image[v[0]][v[1] + l] == c and image[v[0] + l][v[1]] == c and image[v[0] + l][v[1] + l] == c
	
def diagonale1(image, l, v, c):
	d = 0
	while d < l and image[v[0] + d][v[1] + d] == c:
		d += 1
	return image[v[0] + d][v[1] + d] == c
	
def diagonale2(image, l, v, c):
	d = 0
	while d < l and image[v[0] + d][v[1] + l - d] == c:
		d += 1
	return image[v[0] + d][v[1] + l - d] == c
	
def full(image, l, v, color):
	r = v[0] + 1
	c = v[1] + 1
	l = l - 1
	while r < v[0] + l and image[r][c] == color:
		while c < v[1] + l and image[r][c] == color:
			c += 1
		if image[r][c] == color:
			r += 1
			c = v[1]
	return image[r][c] == color

def frame(image, l, v, color):
	r = v[0]
	c = v[1]
	value1 = altezze(image, r, c, l, color)
	if value1:
		i = 0
		value2 = paralleli(image, r, c, l, color)
	return value1 and value2
	
def altezze(image, r, c, l, color):
	i = 0
	while i < l and image[r + i][c + l] == color and image[r + i][c] == color:
		i += 1
	return image[r + i][c + l] == color and image[r + i][c] == color

def paralleli(image, r, c, l, color):
	i = 0
	while i < l and image[r + l][c + i] == color and image[r][c + i] == color:
			i += 1
	return image[r + l][c + i] == color and image[r][c + i] == color