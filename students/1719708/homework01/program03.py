def codifica(chiave, testo):
	return txt_replace(gen_key_c(chiave), testo)

def decodifica(chiave, testo):
	return txt_replace(gen_key_d(chiave), testo)
	
def gen_key_c(chiave):
	key, key_ord = del_repetition(chiave)
	return key_ord, key

def gen_key_d(chiave):
	key, key_ord = del_repetition(chiave)
	return key, key_ord
	
def txt_replace(key_code, testo):
	testo_codificato = ''
	for i in testo:
		if i in key_code[0]:
			testo_codificato += key_code[1][key_code[0].find(i)]
		else:
			testo_codificato += i
	return testo_codificato

def del_repetition(key):
	s = ''
	for i in range(len(key)-1, -1, -1):
		if key[i] not in s and 97 <= ord(key[i]) <= 122:
			s = key[i] + s
	return s, ''.join(sorted(s))