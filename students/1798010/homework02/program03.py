def decod(pfile, codice):
    
	result = set()

	with open(pfile,"r") as f:

		for line in f:

			line = line.rstrip("\n")

			if ParseWord(line,codice):
				result.add(line)

	return result

def ParseWord(string,code):

	dic = {}
	lenght = len(code)

	if len(string) != lenght:
		return False

	for num in code:
		dic[num] = set()

	for i in range(lenght):
		dic[code[i]].add(string[i])

	testSet = set()

	for i in dic:
		for j in dic[i]:
			if j not in testSet:
				testSet.add(j)
			else:
				return False

	if len(dic) != len(testSet):
		return False

	return True


#print(decod('file03.txt','121'))