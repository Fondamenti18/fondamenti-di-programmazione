def post(fposts,insieme):
	id = ''
	risultato = set()
	file = open(fposts,"r")
	for line in file:
		if '<POST>' in line:
			prova = line.split('<POST>',1)[1]
		for x in insieme:
			if x.lower() in line.lower():
				risultato.add(prova.strip())
	file.close()
	return risultato



# import re
#
# def post(fposts,insieme):
# 	id = ''
# 	risultato = set()
# 	file = open(fposts,"r")
# 	for line in file:
# 		if '<POST>' in line:
# 			prova = line.split('<POST>',1)[1]
# 		prova2 = set(line.split())
# 		if insieme & set(line.lower()):
# 			risultato.add(prova.strip())
# 	file.close()
# 	return risultato
#
# print(post('file01.txt', {'return'}));
