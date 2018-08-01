import json

class Node:
	
	# name = str
	# parent = Node
	# children = []
	
	def __init__(self, name, parent = None, depth = 0):
		self.name = name
		self.parent = parent
		self.depth = depth
		self.children = set()
		
	def __str__(self):
		if self.parent is None:
			return "\"{}\", root node. {} children".format(self.name, len(self.children))
		else:
			return "\"{}\", child of \"{}\". {} children".format(self.name, self.parent.name, len(self.children))
		
	def getAncestors(self):
		ancestors = []
		if self.parent != None:
			ancestors = [self.parent]
			ancestors += self.parent.getAncestors()
		return ancestors
		
	def getDescendants(self):
		descendants = []
		if self.children != []:
			descendants += self.children
			for child in self.children:
				descendants += child.getDescendants()
		return [desc for desc in descendants if desc != []]
	
class Tree:
	# __origin__ = {}
	# __nodes__ = []
	# __root__ = Node
	# levels = {}
	# maxdepth = 0
	
	def __init__(self, dict = {}, path = None):
		if path is None:
			# generate node list from dictionary
			self.__origin__ = dict
			self.__generateNodes__()
		else:
			# load dictionary from path, then generate node list
			with open(path) as f: self.__origin__ = json.load(f)
			self.__generateNodes__()
	
	def __updateMaxDepth__(self, d):
		self.maxdepth = max(self.maxdepth, d)
		if str(self.maxdepth) not in self.levels:
			self.levels[str(self.maxdepth)] = []
		
	def __listdiff__(self, iterable1, iterable2):
		return [element for element in iterable1 if element not in iterable2]
		
	def __findroot__(self):
		self.__nodes__ = []
		self.levels = {}
		children = set()
		for node in self.__origin__.keys():
			children |= set(self.__origin__[node])
		
		root = self.__listdiff__(self.__origin__, children)
		if root:
			self.__root__ = Node(root[0], None, 0)
			self.__root__.children = [Node(name, self.__root__, 1) for name in self.__origin__[root[0]]]
			self.__nodes__ += [self.__root__]
			self.__nodes__ += self.__root__.children
			self.levels["0"] = [root[0]]
			self.levels["1"] = [node.name for node in self.__root__.children]
			self.maxdepth = 1
		else:
			print("WARNING: NO ROOT FOUND.")
			
	def __getdescent__(self, node):
		descent = []
		if self.__origin__.get(node.name):
			node.children = [Node(name, node, node.depth + 1) for name in self.__origin__[node.name]]
			descent += node.children
			for child in node.children:
				self.__updateMaxDepth__(child.depth)
				self.levels[str(child.depth)] += [child.name]
				descent += self.__getdescent__(child)
		return descent
		
	def __generateNodes__(self):
		self.maxdepth = 0
		self.__findroot__()
		
		for child in self.__root__.children:
			self.__nodes__ += self.__getdescent__(child)
		
	def __getchildren__(self, node):
		pairs = [(node.name, [child.name for child in node.children])]
		for child in node.children:
		  	pairs += self.__getchildren__(child)
		return pairs
	
	def subtree(self, rootName):
		root = self.getNodeByName(rootName)
		tree = {}
		if root:
			for pair in self.__getchildren__(root):
				tree[pair[0]] = pair[1]
			return tree
	
	def delete_node(self, nodeName):
		root = self.getNodeByName(nodeName)
		if root:
			root.children = []
			if root.parent:
				del root.parent.children[root.parent.children.index(root)]
				
	def getNodeByName(self, name):
		for node in self.__nodes__:
			if node.name == name:
				return node
				
	def dict(self):
		return self.subtree(self.__root__.name)
		
def parseJson(file):
	with open(file) as f: return json.load(f)
	
def dump(obj, out):
	with open(out, 'w', encoding = 'utf-8') as f:
		json.dump(obj, f)
	
def genera_sottoalbero(fnome,x,fout):
	dump(Tree(path = fnome).subtree(x), fout)
	
def cancella_sottoalbero(fnome,x,fout):
	t = Tree(path = fnome)
	t.delete_node(x)
	dump(t.dict(), fout)
	
def getLevelDictionary(tree, levels = {}, level=0):
	items = tree.levels.get(str(level))
	if items:
		levels[str(level)] = sorted(items)
		return getLevelDictionary(tree, levels, level + 1)
	else:
		return levels
	
def dizionario_livelli(fnome,fout):
	t = Tree(path = fnome)
	d =	getLevelDictionary(t)
			
	dump(d, fout)

def dizionario_gradi_antenati(fnome,y,fout):
	t = Tree(path = fnome)
	d = {}
	
	for node in t.__nodes__:
		d[node.name] = len([ancestor for ancestor in node.getAncestors() if len(ancestor.children) == y])
	
	dump(d, fout)