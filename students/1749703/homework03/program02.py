from math import sin, cos, radians
from immagini import * 
import png, time

def clamp(n, smallest, largest): 
	return max(smallest, min(n, largest))
  
def sum_tuple(a, b):
	return (a[0] + b[0], a[1] + b[1])

def multiply_tuple(a, n):
	return (a[0] * n, a[1] * n)

def dirVector(degree):
	return (int(cos(radians(degree))), int(sin(radians(degree))))
	
def dvToCode(dir):
	return \
		'0' * (dir == (1, 0) ) + \
		'1' * (dir == (0, 1) ) + \
		'2' * (dir == (-1, 0)) + \
		'3' * (dir == (0, -1))		

  
def drawRect(img, pos, color):
	for y in range(pos[0], clamp(pos[0] + 40, 0, len(img))):
		for x in range(pos[1], clamp(pos[1] + 40, 0, len(img[0]))):
			img[x][y] = color

def cammino(fname, fname1):
	image = load(fname)
	pos, rot = (0, 0), 0
	allowedColors = [(255, 255, 255), (0, 0, 0)]
	redirects = 0
	result = ""
	
	drawRect(image, pos, (0, 255, 0))
	#print('  POS \t\t DIR \t\t PROJ \t\t COLOR \t\t\t ROT \t RES')
	#print('-------------------------------------------------------------------------------')
	while redirects < 4:
		direction = dirVector(rot)
		proj_pos = (clamp(pos[0] + direction[0] * 40, 0, 599), clamp(pos[1] + direction[1] * 40, 0, 599))
		projection = image[proj_pos[1]][proj_pos[0]]
		#print(' ', pos, '\t', direction, '\t', proj_pos, '\t', projection, '      \t', rot, '\t', result)
		if projection in allowedColors:
			pos = proj_pos
			result += dvToCode(direction)
			drawRect(image, pos, (0, 255, 0))
			redirects = 0
		else:
			#print("  rotating")
			rot += 90
			redirects += 1
			
	drawRect(image, pos, (0, 0, 255))
	save(image, fname1)
	# print(result)
	return result 
	
#cammino('I1.png','t1.png')