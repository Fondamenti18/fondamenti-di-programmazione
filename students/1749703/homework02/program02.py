#
# program02 - compiti
#

import re, json

def getRequestedKeys(_set, index):
	return [id for id in _set if id in index.keys()]

def ensureList(index, key):
	if type(index[key]) is not list:
		index[key] = [index[key]]

def generateIndex(content, req):
	index = {}
	parent_task_id = None
	
	for line in content:
		item_id = re.findall(r"\d+", line)[0]
		
		if "comp" in line:
			index[item_id] = []
			parent_task_id = item_id
		else:
			index[parent_task_id] = item_id
		
	return index

def compileSubs(key, index):
	target = key
	subs = []
	while index[target] != []:
		subs.insert(0, index[target])
		target = index[target]
		
	return subs

def pianifica(fcompiti,insi,fout):
	with open(fcompiti, 'r', encoding = "utf-8") as input:
		index = generateIndex(input, insi)
	
	with open(fout, 'w', encoding = "utf-8") as output:
		json.dump({key: compileSubs(key, index) for key in getRequestedKeys(insi, index)}, output)