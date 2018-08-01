'''
Diciamo che un dizionario d rappresenta un albero (e lo indichiamo come dizionario-albero)
se ciascuna chiave di d e' un identificativo di un nodo dell'albero  e l'attributo della chiave e' la lista 
(eventualmente vuota) degli identificativi dei  figli del nodo. Gli identificativi dei nodi 
all'interno delle liste sono in ordine lessicografico crescente.



Ecco un esempio di dizionario d che rappresenta un dizionario-albero

d={
'a':['b'],
'b':['c','d'],
'c':['i'],
'd':['e','l'],
'e':['f','g','h'],
'f':[],
'g':[],
'h':[],
'i':[],
'l':[]
}

L'albero rappresentato da d e'

                             'a'
                              |
                _____________'b'____________             
               |                            |            
              'c'                  ________'d'_______   
               |                  |                  |  
              'i'         _______'e'_______         'l'
                         |        |        |               
                        'f'      'g'      'h'


Implementare le seguenti funzioni:

1) 
la funzione genera_sottoalbero(fnome,x,fout) che, presi:

- il nome di un file json contenente un dizionario-albero  d (fonome)
- un identificativo x
- il nome di un file json (fout)

produce   il  dizionario-albero che rappresenta   il sottoalbero  radicato 
nell'identificativo x che si ottiene dal dizionario-albero d. 
Il dizionario-albero ottenuto va registrato nel file fout.
Se l'identificativo x non e' tra i nodi di d allora  il dizionario-albero prodotto 
deve essere vuoto.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di 
genera_sottoalbero(fname,'d',fout)
il file fout conterra' il dizionario
{'f': [], 'g': [], 'h': [], 'e': ['f', 'g', 'h'], 'l': [], 'd': ['e', 'l']}



2)
la funzione cancella_sottoalbero(fnome,x,fout) che, presi:

- il nome di un file json contenente un dizionario-albero  d (fonome)
- un identificativo x
- il nome di un file json (fout)

ricava  da d il sottoalbero radicato in x e lo salva nel file fout.
Se x non e' presente tra le chiavi di  d allora  il dizionario-albero d non viene modificato.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di 
cancella_sottoalbero(fname,'d',fout)
il file fout conterra' il dizionario
{'a': ['b'], 'b': ['c'], 'c': ['i'], 'i':[]}


3)
la funzione dizionario_livelli(fnome, fout) che, presi:
- il nome di un file json contenente un dizionario-albero  d (fonome)
- il nome di un file json (fout)

costruisce il  dizionario che ha come  chiavi i livelli del dizionario-albero d. L'attributo di una 
chiave di valore x e' la lista degli identificativi  dei nodi che si trovano a livello x  nell'albero rappresentato da d. 
La lista e' ordinata lessicograficamente ed in modo crescente. 
Il dizionario cosi' costruito va registrato nel file fout.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di  
dizionario_livelli(fname,fout)
il file fout conterra' il dizionario
{0: ['a'], 1: ['b'], 2: ['c', 'd'], 3: ['e','i','l'], 4: ['f', 'g', 'h']}

4)
la funzione dizionario_gradi_antenati(fnome,y,fout) che, presi:
- il nome di un file json contenente un dizionario-albero  d (fonome)
- un intero y
- il nome di un file json (fout)

costuisce  il dizionario che ha come chiavi gli identificativi dei nodi dell'albero 
rappresentato dal dizionario-albero d, Attributo di una chiave di valore x e' il numero 
di antenati di grado y che ha il nodo con identificativo x nell'albero.
Registra il dizionario costruito nel file fout.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di  
dizionario_gradi_antenati(fnome,2,fout)
il file fout conterra' il dizionario 
{'a': 0, 'b': 0, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 1, 'l': 2}

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non
importare moduli che non sono nella libreria standard.
'''

import json

def op(nome): 
  with open(nome) as f: s = json.loads(f.read())
  return s

def sv(nome, content): 
  with open(nome, 'w') as file: file.write(json.dumps(content))

def genera_sottoalbero(fnome,x,fout):
    s = op(fnome)
    content = get_el(s, x, {})
    sv(fout, content)

def get_el(s, x, content):
  el = s.get(x, [])
  content.update({x: el})
  for e in el:
    get_el(s, e, content)
  return content

def cancella_sottoalbero(fnome,x,fout):
    s = op(fnome)
    content = del_el(s, x)
    for a in content:
      if x in content[a]:
        content[a].remove(x)
    sv(fout, content)

def del_el(s, x):
  el = s.get(x, [])
  s.pop(x)
  for e in el:
    del_el(s, e)
  return s
    
def dizionario_livelli(fnome,fout):
  s = op(fnome)
  content = {}
  x = x1(s)
  lvl = lvl1(s, x)
  l = []
  get_lvl(l, lvl, s)
  n = 0
  for a in l:
      content.update({n: sorted(a)})
      n += 1
  sv(fout, content)
 
def x1(s): return {a for b in s.values() for a in b}

def lvl1(s, x): return [a for a in s if a not in x]

def lvl2(lvl, s): return [a for b in lvl for a in s.get(b,())]

def get_lvl(l, lvl, s):
    if lvl:
      l.append(lvl)
      lvl = lvl2(lvl, s)
      get_lvl(l, lvl, s)

def find(b, a, c):
  if a not in b:
    return c
  else:
    c += [b[a]]
    find(b, b[a], c)

def add_root(s):
  d = {}
  for a, b in s.items(): 
    for c in b: d.update({c: a})
  return d

def fix_el(s, x):
  d = {}
  for a in s: 
    if a in x:
      pass 
    else:
      el = a
  d.update({el: 0})
  return d

def end_el(s, l, x, d, y, a):
  n = 0
  for x in l:
    if y == len(s[x]):
      n += 1
    d.update({a: n})

def dizionario_gradi_antenati(fnome, y, fout):
  s = op(fnome)
  d1 = add_root(s)
  x = x1(s)
  d2 = fix_el(s, x)

  for a in d1:
    l1 = list()
    find(d1, a, l1)
    end_el(s, l1, x, d2, y, a)
  sv(fout, d2)