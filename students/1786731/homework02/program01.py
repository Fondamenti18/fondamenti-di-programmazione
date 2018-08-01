def leftBoundReject(index, text):
	return index != 0 and text[index-1].isalpha()

def rightBoundReject(index, parolalen, text):
	return (index + parolalen) != parolalen and text[index+parolalen].isalpha()

def appendRisultato(index, text, parolalen, risultato):
	# boundary conditions
	if leftBoundReject(index, text):
		return 

	if rightBoundReject(index, parolalen, text):
		return 

	# has to exist
	postlineindexstart = text.rfind("<post>", 0, index)
	postlineindexend   = text.find("\n", postlineindexstart)

	boundedline = text[postlineindexstart:postlineindexend]
	postnum = boundedline[boundedline.find(">")+1:].strip()

	risultato.add(postnum)


def iterParola(parola, text, risultato):
	parola = parola.lower()
	index = text.find(parola)
	parolalen = len(parola)

	while index != -1:
		appendRisultato(index, text, parolalen, risultato)
		index = text.find(parola, index + 1)


def post(fposts,insieme):
	insieme = [ stringa.lower() for stringa in insieme ]
	risultato = set()

	# contiene la linea che specifica post e id, e un concatenamento di linee appartenenti al post
	text = ""

	f = open(fposts)
	text = f.read().lower()

	for parola in insieme:
		iterParola(parola, text, risultato)

	f.close()
	return risultato
