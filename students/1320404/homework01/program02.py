# MODULI #
unita={1:'uno',2:'due',3:'tre',4:'quattro',5:'cinque',6:'sei',7:'sette',8:'otto',9:'nove',\
	   10:'dieci',11:'undici',12:'dodici',13:'tredici',14:'quattordici',15:'quindici',16:'sedici',\
       17:'diciassette',18:'diciotto',19:'diciannove'}
	   
decine=['venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']	   
	      
		   
# FUNZIONE DECINE #
def dec(n):
		ris=''
		risp=''
		div=divmod(n,10)
		if n < 20:
			ris=unita[n]
			return ris
		elif div[1] == 1 or div[1] == 8:
			ris=(decine[div[0]-2])
			for i in range(0,len(ris)-1):
				risp=risp+ris[i]
			ris=risp+(unita[div[1]])
			return ris
		elif div[1] == 0:
			ris=decine[div[0]-2]
			return ris
		else:
			ris=(decine[div[0]-2])+(unita[div[1]])
			return ris
			
			
# FUNZIONE CENTINATIA #
def cent(n):
		div=0
		for i in range(1,10):
			if str(n)[0] == str(i):
				if i == 1:
					ris='cento'
					div=divmod(n,100)
					if div[0] == 0 and div[1] < 20:
						ris=unita[div[1]]
					elif div[0] == 1 and div[1] == 0:
						ris=ris
					elif div[1] < 10:
						ris=ris+unita[div[1]]
						return ris
					elif div[1] > 9 and 79<div[1]<90:
						ris='cent'+dec(div[1])
					elif div[1]>9:
						ris=ris+dec(div[1])
						return ris
				else:
					ris=unita[i]+'cento'
					div=divmod(n,100)
					if 79<div[1]<90:
						ris=unita[i]+'cent'+dec(div[1])
					elif div[0] == 0 and 19<div[1]<100:
						ris=dec(div[1])
					elif div[1] == 0 :
						ris=ris
					else:
						ris=ris+dec(div[1])
				return ris
				
# FUNZIONE MIGLIAIA #
def mil(n):
	div=divmod(n,1000)
	if n == 100 or n == 1000 or n == 1100:
		if n == 100:
			ris='cento'
		elif n == 1000:
			ris='mille'
		elif n == 1100:
			ris='millecento'
	else:
		if div[0] == 0:
			n=div[1]
			ris=cent(n)
		elif div[0] < 10 and n < 1100:
			div=divmod(n,100)
			n=div[1]
			ris='mille'+dec(n)
		elif div[0] < 10 and div[1] == 0:
				ris=dec(div[0])+'mila'
		elif div[0] < 10 and div[1] < 100:
				ris=dec(div[0])+'mila'+dec(div[1])
		elif div[0] == 1:
			ris='mille'+cent(div[1])
		elif div[0] < 10 and div[1] >99:
				if div[1] == 100:
					ris=dec(div[0])+'milacento'
				else:
					ris=dec(div[0])+'mila'+cent(div[1])
		elif div[0] > 9 and div[1] == 0 and div[0] < 20:
				ris=unita[div[0]]+'mila'
		elif div[0] > 9 and div[1] == 100 and div[0] < 20:
				ris=unita[div[0]]+'milacento'
		elif div[0] > 9 and div[1] < 20 and div[0] < 20:
				ris=unita[div[0]]+'mila'+unita[div[1]]
		elif div[0] > 9 and div[1] < 100 and div[0] < 20:
				ris=unita[div[0]]+'mila'+dec(div[1])
		elif div[0] > 9 and div[1] > 99 and div[0] < 20:
				ris=unita[div[0]]+'mila'+cent(div[1])
		elif div[0] > 19 and div[1] == 0 and div[0] < 100:
				ris=dec(div[0])+'mila'
		elif div[0] > 19 and div[1] == 100 and div[0] < 100:
				ris=dec(div[0])+'milacento'
		elif div[0] > 19 and div[1] < 20 and div[0] < 100:
				ris=dec(div[0])+'mila'+unita[div[1]]
		elif div[0] > 19 and div[1] < 100 and div[0] < 100:
				ris=dec(div[0])+'mila'+dec(div[1])
		elif div[0] > 19 and div[1] > 99 and div[0] < 100:
				ris=dec(div[0])+'mila'+cent(div[1])
		elif div[0] > 99 and div[1] == 0:
				ris=cent(div[0])+'mila'
		elif div[0] > 99 and div[1] == 100:
				ris=cent(div[0])+'milacento'
		elif div[0] > 99 and div[1] < 20:
				ris=cent(div[0])+'mila'+unita[div[1]]
		elif div[0] > 99 and div[1] < 100:
				ris=cent(div[0])+'mila'+dec(div[1])
		elif div[0] > 99 and div[1] > 99:
				ris=cent(div[0])+'mila'+cent(div[1])
		else:
			ris='mille'+cent(div[1])
	return ris

# FUNZIONE MILIONI #
def mig(n):
	div=divmod(n,1000000)
	if n == 1000000:
		ris='unmilione'
	elif 1000000<n<2000000:
		ris='unmilione'+mil(div[1])
	elif 1999999<n<20000000:
		if div[1] == 0:
			ris=unita[div[0]]+'milioni'
		else:
			ris=unita[div[0]]+'milioni'+mil(div[1])
	elif 19999999<n<100000000:
		if div[1] == 0:
			ris=dec(div[0])+'milioni'
		else:
			ris=dec(div[0])+'milioni'+mil(div[1])
	elif 99999999<n<1000000000:
		if div[1] == 0:
			ris=cent(div[0])+'milioni'
		else:
			ris=cent(div[0])+'milioni'+mil(div[1])
	return ris
	
# FUNZIONE MILIARDI #
def mili(n):
	ris=''
	div=divmod(n,1000000000)
	if n == 1000000000:
		ris='unmiliardo'
	elif 1000000000<n<1001000000:
		ris='unmiliardo'+mil(div[1])
	elif 1000999999<n<2000000000:
		ris='unmiliardo'+mig(div[1])
	elif 1999999999<n<20000000000:
		if div[1] == 0:
			ris=unita[div[0]]+'miliardi'
		else:
			ris=unita[div[0]]+'miliardi'+mig(div[1])
	elif 19999999999<n<100000000000:
		if div[1] == 0:
			ris=dec(div[0])+'miliardi'
		else:
			ris=dec(div[0])+'miliardi'+mig(div[1])
	elif 99999999999<n<1000000000000:
		if div[1] == 0:
			ris=cent(div[0])+'miliardi'
		else:
			ris=cent(div[0])+'miliardi'+mig(div[1])
	return ris
	
	
# MAIN #
def conv(n):
		ris=''
		if n<20:
			ris=unita[n]
		elif 19<n<100:
			ris=dec(n)
		elif 99<n<1000000:
			ris=mil(n)
		elif 999999<n<1000000000:
			ris=mig(n)
		elif 999999999<n<1000000000000:
			ris=mili(n)
		return ris
				
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		