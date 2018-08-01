
import json
import sys

#per sicurezza
sys.setrecursionlimit(10000)


#funzione originale
def genera_sottoalbero(fnome,x,fout):
  subtree = {}
  file = json.load(open(fnome))
  ricorsionealbero(file,x,subtree)
  js = json.dumps(subtree)
  fp = open(fout, 'w')
  fp.write(js)
  fp.close()
  return None

#funzione ricorsiva che permette l'aggiunta di piu parametri
def ricorsionealbero(file,x,subtree):
  if x in file:
    subtree[x] = file[x]
  for i in file[x]:
    valore = i
    subtree = ricorsionealbero(file,valore,subtree)
  return subtree


#funzione originale
def cancella_sottoalbero(fnome,x,fout):
    subtree = {}
    lista = []
    file = json.load(open(fnome))

    for i in file:
      for j in file[i]:
        if j == x:
          file[i].remove(j)
    ricorsionecancella(file,x,lista)
    for i in lista:
      del file[i]
    js = json.dumps(file)
    fp = open(fout,'w')
    fp.write(js)
    fp.close()
    return None
                 
#funzione ricorsiva che permette l'aggiunta di piu parametri
def ricorsionecancella(file,x,lista):
  if x in file:
    lista.append(x)
  for i in file[x]:
    valore = i
    lista = ricorsionecancella(file,valore,lista)
  return lista
    
#funzione originale    
def dizionario_livelli(fnome,fout):
  file = json.load(open(fnome))
  subtree = {}
  lista =[]
  lista_chiave = []
  for i in file:
    lista_chiave.append(i)
    for x in file[i]:
      lista.append(x)
  #calcolo la differenza e mi trovo la prima chiave del dizionario
  #dato che il dizionario è random
  c = list(set(lista_chiave).difference(lista))
  subtree = ricorsionelivello(file,c)
  # print(subtree)
  js = json.dumps(subtree)
  fp = open(fout, 'w')
  fp.write(js)
  fp.close()
  return None


#funzione ricorsiva che permette l'aggiunta di piu parametri
def ricorsionelivello(dizionario,primo_elemento,order=0):
    if not primo_elemento:
      return {}   
    new_dict = {}
    new_elems = []
    for x in primo_elemento:
      new_dict.setdefault(order,[])
      new_dict[order].append(x)
      new_dict[order].sort()
      new_elems.extend(dizionario.get(x,[]))
      # print(new_elems)
    new_dict.update(ricorsionelivello(dizionario,new_elems,order+1))
    return new_dict 


#funzione originale
def dizionario_gradi_antenati(fnome,y,fout):
  file = json.load(open(fnome))
  subtree = {}
  lista =[]
  lista_chiave = []
  #metto in due liste chiave e valori
  for i in file:
    lista_chiave.append(i)
    for x in file[i]:
      lista.append(x)
  #calcolo la differenza e mi trovo la prima chiave del dizionario
  #dato che il dizionario è random
  c = list(set(lista_chiave).difference(lista))
  subtree = ricorsionegradi(file,c,y)
  js = json.dumps(subtree)
  fp = open(fout, 'w')
  fp.write(js)
  fp.close()
  return None


#funzione ricorsiva che permette l'aggiunta di piu parametri
def ricorsionegradi(dizionario,first,grado,order = 0):
  if not first:
    return {}
  new_dict = {}
  new_elems = []
  for x in first:
    new_dict.setdefault(x,order)
    new_elems = dizionario.get(x)
    if len(dizionario.get(x)) == grado:
      new_dict.update(ricorsionegradi(dizionario,new_elems,grado,order + 1))
    else:
      new_dict.update(ricorsionegradi(dizionario,new_elems,grado,order))    
  return new_dict












