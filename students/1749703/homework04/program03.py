from my_html import HTMLNode, fparse

def parseCSSQuery(query):
	keys = []
	if query.startswith('.'):
		keys += ['class']
		query = query[1:]
	if query.startswith('#'):
		keys += ['id']
		query = query[1:]
	if query.startswith('@'):
		parts = query.split('=')
		keys += [parts[0][2:]]
		query = parts[1][1:-2]
	return query, keys
			
def count_tags(DOM, selettore, keys):
	count = 0
	
	if DOM.istext():
		return 0
		
	elif keys != []:
		if(DOM.attr.get(keys[0])):
			count += int(selettore in DOM.attr[keys[0]])
		count += sum([count_tags(t, selettore, keys) for t in DOM.content])
		return count
		
	elif ' ' in selettore:
		if '>' in selettore:
			if not DOM.closed:
				return 0
			else:
				tag = selettore.split('>')[0][:-1]
				child = selettore.split('>')[1][1:]
				if(tag in DOM.tag):
					for t in DOM.content:
						count += int(child in t.tag)
						if not t.istext():
							break
							
				count += sum([count_tags(t, selettore, keys) for t in DOM.content])
				return count
		else:
			if not DOM.closed:
				return 0
			else:
				tag = selettore.split(' ')[0]
				child = selettore.split(' ')[1]
				count += count_children(DOM, selettore, tag, child)
				return count
	else:
		count += int(DOM.tag == selettore)
		count += sum([count_tags(t, selettore, keys) for t in DOM.content])
		return count
	
def count_children(DOM, tag, child, newTag = False):
	count = 0
	newTag = DOM.tag == tag
	count += sum([int(not element.istext() and (newTag and child in element.tag)) for element in DOM.content])
	newTag = not DOM.close_tag() == '</'+ tag + '>'
	count += sum([count_children(element, tag, child, newTag) for element in DOM.content if not element.istext()])		
	return count		
	
def conta_nodi(fileIn, selettore):
	documento = fparse(fileIn)
	selettore, keys = parseCSSQuery(selettore)
	return count_tags(documento, selettore, keys)
	
	
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice

