def getKeys(chiave):
	# rimuovi tutte i char < 'a' o char > 'z' ).
	key = ''.join([c for c in chiave if not (c < 'a' or c > 'z')])
	
	# cancella i caratteri doppi e ottieni una sequenza disordinata
	# 
	# key_unsorted = set()
	# key_unsorted = ''.join([c for c in key[::-1] if not (c in key_unsorted or key_unsorted.add(c))][::-1])
	key_unsorted = []
	for c in key[::-1]:
		if c not in key_unsorted:
			key_unsorted += [c]
	key_unsorted = ''.join(list(key_unsorted[::-1]))
	
	# calcola la sequenza ordinata su quella disordinata
	key_sorted   = ''.join(sorted(key_unsorted))
	
	return key_unsorted, key_sorted

def replaceCharacters(text, key1, key2):
	r = ''
	for c in text:
		if c in key1:
			r += key2[key1.find(c)]
		else:
			r += c
	return r
	
def codifica(chiave, testo):
	# genero le chiavi
	key_sorted, key_unsorted = getKeys(chiave)
	
	# codifico
	return replaceCharacters(testo, key_unsorted, key_sorted)
	
def decodifica(chiave, testo):
	# genero le chiavi
	key_unsorted, key_sorted = getKeys(chiave)
	
	# decodifico
	return replaceCharacters(testo, key_unsorted, key_sorted)