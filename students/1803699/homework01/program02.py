unita = {1:"uno", 2:"due", 3:"tre", 4:"quattro", 5:"cinque", 6:"sei", 7:"sette", 8:"otto", 9:"nove", 0:""}
decine = {1:"dieci", 2:"venti", 3:"trenta", 4:"quaranta", 5:"cinquanta", 6:"sessanta", 7:"settanta", 8:"ottanta", 9:"novanta", 0:""}
teens = {"uno":"undici", "due":"dodici", "tre":"tredici", "quattro":"quattordici", "cinque":"quindici", "sei":"sedici", "sette":"diciassette", "otto":"diciotto", "nove":"diciannove", "":"dieci"}

def aggiusta(z,y,x):
        if x=='uno':
                x='cento'
        elif x=='':
                x=''
        else:
                x=x+'cento'
        if y=='ottanta':
                x=x[:-1]
        if y=='dieci':
                z=teens[z]
                y=''
        elif z=='uno' or z=='otto':
                y=y[:-1]
        aggiustata=x+y+z
        return aggiustata

def conv(n):
	s = str(n)
	q = len(s)
	lista=[]
	for i in range(1, q+1):
		value=s[q-i]
		if i==2 or i==5 or i==8 or i==11:
			lettere=decine[int(value)]
		else:
			lettere=unita[int(value)]
		lista.append(lettere)
	p=len(lista)
	finale=''
	a=''
	b=''
	c=''
	for i in range(0, p):
		if i==0 or i==3 or i==6 or i==9:
			a=lista[i]
		elif i==1 or i==4 or i==7 or i==10:
			b=lista[i]
		elif i==2 or i==5 or i==8 or i==11:
			c=lista[i]
			finale=aggiusta(a,b,c)+finale
			a=''
			b=''
			c=''
		if p>3 and i==2:
			if lista[3]=='uno' and p==4:
				lista[3]=''
				finale='mille'+finale
			elif p>6 and lista[3]==1 and lista[4]=='' and lista[5]=='':
				finale='mille'+finale
			else:
				finale='mila'+finale
		if p>6 and i==5:
			if lista[6]=='uno' and p==7:
				lista[6]=''
				finale='unmilione'+finale
			elif p>9 and lista[6]==1 and lista[7]=='' and lista[8]=='':
				finale='unmilione'+finale
			else:
				finale='milioni'+finale
		if p>9 and i==8:
			if lista[9]=='uno' and p==10:
				lista[9]=''
				finale='unmiliardo'+finale
			else:
				finale='miliardi'+finale
		if i==p-1:
			finale=aggiusta(a,b,c)+finale
	return finale
