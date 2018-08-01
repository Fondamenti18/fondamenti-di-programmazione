from immagini import *

def check1(col, h):
	if h == col:
		return h

def quadrato(filename,c):
	x = y = z = x3 = y3 = 0
	img = load(filename)
	col1 = 0
	while col1 < len(img):
		riga = 0
		while riga < len(img[0]):
			if img[col1][riga] == c:
				x3 = riga
				y3 = col1
				x2 = 0
				n = x3
				while n < len(img[0]):
					if img[col1][n] != c:
						break
					else:
						x2 += 1
					n += 1
				if z <= x2:
					y2 = 0
					n = y3
					while n < len(img):
						if img[n][x3] == c:
							y2 += 1
						else:
							break
						n += 1
					min1 = min(x2, y2)
					if z <= min1:
						h = min1
						col = y3
						conx3 = min1 + x3
						valida = '1'
						cony3 = min1 + y3
						while col < cony3:
							ri = x3
							while ri < conx3:
								if img[col][ri] != c:
									b = conx3 - ri
									t = b - h
									if h > t:
										h = t
								if h < z:
									valida = '0'
									break
								c1 = check1(col, h)
								if c1 != None:
									min1 = c1
									break
								ri += 1
							col += 1
						if valida == '1':
							if z == min1:
								if x3 == x and y > y3:
									y = y3
								elif x2 > x3:
									y = y3
									x = x3
							elif z < min1:
								z = min1
								x = x3
								y = y3
			riga += 1
		col1 += 1		 
	return tuple([z,(x,y)])