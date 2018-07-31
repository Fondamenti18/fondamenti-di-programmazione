#
# program03 - pattern parole
#

def clamp(n, smallest, largest): 
	return max(smallest, min(n, largest))

def sameLengthAsStructure(structure, dictionary):
	return [word.rstrip() for word in dictionary if len(word.rstrip()) == len(structure)]

def countUnique(string):
	return set(string.count(c) for c in set(string))
	
def getRepeatingCharacters(string):
	return [(i, c) for i, c in enumerate(string) if string.count(c) > 1]
	
def getPatternNumberIndices(pattern, patternNumber):
	return [pn_i for pn_i, pn in enumerate(pattern) if pn == patternNumber]
	
def getCharactersAtIndices(string, indices):
	return [wd_c for wd_i, wd_c in enumerate(string) if wd_i in indices]
	
def wordPassesTestA(word, pattern):
	wSet = set(word)
	pSet = set(pattern)
	
	if len(pSet) != len(wSet):
		return False
	
	patternCount = countUnique(pattern)
	charCount = countUnique(word)
	
	if not patternCount == charCount:
		return False
		
	return True

def wordPassesTestB(word, pattern, c, i):
	index = clamp(pattern.find(c, i + 1), -1, len(word) - 1)
	
	if index == -1:
		pn_positions = getPatternNumberIndices(pattern, c)
		wd_chars = set(getCharactersAtIndices(word, pn_positions))
		
		if len(wd_chars) == 1:
			return 2 
		else:
			return 0
			
		return 1
	
	if not word[i] == word[index]:
		return 0
	
def wordMatchesPattern(word, pattern):
	if not wordPassesTestA(word, pattern):
		return False
	
	for i, c in getRepeatingCharacters(pattern):
		testResult = wordPassesTestB(word, pattern, c, i)
		if testResult == 0:
			return False
		elif testResult == 2:
			continue
	return True
	
def decod(pfile, codice):
	words = set()
	with open(pfile, encoding = "utf-8") as dictionary:
		for word in sameLengthAsStructure(codice, dictionary):
			if wordMatchesPattern(word, codice):
				words.add(word)
	return words