#
# program01 - ricerca post 
# da ottimizzare
#

import re

def caseInsens(coll):
	return [string.lower() for string in coll]
	
def addIfRequested(word, requested, postIDs, lastId):
	if word.lower() in requested:
		postIDs.add(lastId)

def post(fposts,insieme):
	postIDs = set()
	insieme = caseInsens(insieme)
	numPattern = re.compile(r'\d+')
	wrdPattern = re.compile(r'\w+')
	lastId = None
	with open(fposts, encoding = "utf-8") as postsFile:
		for line in postsFile:
			if "<POST>" in line:
				lastId = re.findall(numPattern, line)[0]
			
			for word in re.findall(wrdPattern, line):
				addIfRequested(word, insieme, postIDs, lastId)
			
	return postIDs