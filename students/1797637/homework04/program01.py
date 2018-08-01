import json

class Tree():
    subtree = {}
    diff_subtree={}
    levels={}
    i=0
    
    def __init__(self, dict_tree):
        self.dict_tree = dict_tree
        self.keys = list(dict_tree.keys())
        self.values = list(dict_tree.values())

    def get_children(self, node):
        return self.dict_tree[node]

    def get_subtree(self, node): 
        Tree.subtree[node] = self.get_children(node)
        for subnode in self.get_children(node):
            self.get_subtree(subnode)      
        return Tree.subtree

    def del_subtree(self, node):
        Tree.subtree = self.get_subtree(node)
        for key in self.dict_tree:
            if key not in Tree.subtree:
                Tree.diff_subtree[key] = self.dict_tree[key]
                self.del_subtree2(node, key)
        return Tree.diff_subtree

    def del_subtree2(self, node, key):
        if node in Tree.diff_subtree[key]:
            Tree.diff_subtree[key].remove(node)
    
    def get_levels(self):
        Tree.levels[Tree.i]=[]
        self.manage_levels()
        if Tree.levels[Tree.i]==[]:
            del Tree.levels[Tree.i]
            for level in Tree.levels:
                Tree.levels[level].sort()
            return Tree.levels
        Tree.i += 1
        self.get_levels()

    def manage_levels(self):
        if Tree.i == 0:
            first_level = self.find_first_lev()
            Tree.levels[Tree.i].append(first_level)
        else:
            for node in Tree.levels[Tree.i-1]:
                Tree.levels[Tree.i].extend(self.dict_tree[node])

    def find_first_lev(self):
        nodes = set(self.keys)
        subnodes = set()
        for items in self.values:
            for subnode in items:
                subnodes.add(subnode)
        return list(set.difference(nodes,subnodes))[0]

    def num_children(self, number):
        n_children = {}
        n_children = self.num_children2(n_children)
        ancestors_tree = self.empty_dict()    
        for node in n_children:
            if n_children[node] == number:
                ancestors_tree = self.ancestors(ancestors_tree, node)
        return ancestors_tree

    def num_children2(self, n_children):
        for node in self.dict_tree:
            n_children[node] = len(self.dict_tree[node]) 
        return n_children
    
    def ancestors(self, ancestors_tree, node):
        for subnode in self.dict_tree[node]:
            ancestors_tree[subnode]+=1
            node = subnode
            self.ancestors(ancestors_tree, node)   
        return ancestors_tree

    def empty_dict(self):
        empty_tree = {}
        for node in self.dict_tree:
            empty_tree[node]=0
        return empty_tree

    @classmethod
    def reset(cls):
        cls.subtree = {}
        cls.diff_subtree={}
        cls.levels = {}
        cls.i = 0

def genera_sottoalbero(fnome,x,fout):
    dict_tree = read_json(fnome) 
    tree = Tree(dict_tree)
    try:
        subtree = tree.get_subtree(x)
    except KeyError:
        subtree = {}
    write_json(fout, subtree)
    tree.reset()
    
def cancella_sottoalbero(fnome,x,fout):
    dict_tree = read_json(fnome) 
    tree = Tree(dict_tree) 
    try:
        subtree = tree.del_subtree(x)
    except KeyError:
        subtree = dict_tree 
    write_json(fout, subtree)
    tree.reset()

def dizionario_livelli(fnome,fout):
    dict_tree = read_json(fnome) 
    tree = Tree(dict_tree)
    tree.get_levels()                            #   <---  Why? --
    write_json(fout, tree.get_levels())          #        <------|
    tree.reset()

def dizionario_gradi_antenati(fnome,y,fout):
    dict_tree = read_json(fnome) 
    tree = Tree(dict_tree) 
    write_json(fout, tree.num_children(y)) 
    tree.reset()

def read_json(fnome):
    f = open(fnome, mode='r', encoding='utf-8')
    json_object = json.loads(f.read())
    f.close()
    return json_object

def write_json(fout, json_object):
    f = open(fout, mode='w', encoding='utf-8')
    f.write(json.dumps(json_object))
    f.close()