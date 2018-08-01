# Un documento HTML può essere rappresentato sotto forma di albero, come visto a
# lezione, che si chiama DOM (Document Object Model).
#
# Un qualsiasi nodo di questo albero può essere individuato sulla base delle
# proprie caratteristiche:
#     - tag                       un tag del tipo indicato;
#     - .classe                   una delle parole presenti nel valore
#                                 dell'attributo "class";
#     - #id                       il valore dell'attributo "id";
#     - @[attributo="valore"]     valore di un attributo generico;
# ed in base alla sua relazione con i tag che lo contengono:
#     - avo discendente           il tag 'avo' contiene un tag 'discendente' a
#                                 qualsiasi profondità;
#     - padre > figlio            il tag 'padre' contiene il tag 'figlio' nel
#                                 livello immediatamente sotto.
#
# Un selettore CSS è una successione di selettori di tag separati da spazio che
# serve ad individuare uno o più nodi all'interno del DOM.
# Esempio:
#
#     div .class1 > #main_window
#
#  seleziona un qualsiasi tag che ha id="main_window", è il figlio di un tag che
#  ha class="... class1 ..." e si trova all'interno (a qualsiasi livello di
#  distanza) di un tag div.
#
# Esempio2:
#
#     p table > tr > td > a
#
#  seleziona un link (<a ...> </a>)
#  figlio di una casella (<td> ... </td>)
#  figlia di una riga (<tr> ... </tr>)
#  figlia di una tabella (<table> ... </table>)
#  contenuta a qualsiasi livello in un paragrafo (<p> .... </p>)
#
# NOTA: questa definizione del CSS è una versione ridottissima che non segue lo
# standard completo. In particolare, non è possibile usare più relazioni '>'
# consecutive o costruire selettori alternativi (in OR) e selettori in AND.
#
# Le modifiche da attuare su un DOM possono essere di 3 tipi:
#     - conteggio dei nodi che soddisfano il selettore CSS;
#     - eliminazione di tutti i tag individuati da un selettore CSS;
#     - modifica degli attributi di tutti i tag individuati da un selettore CSS.
#
# Realizzate le funzioni che esplorano e modificano l'albero:
#     - conta_nodi(fileIn, selettore);
#     - elimina_nodi(fileIn, selettore, fileOut);
#     - cambia_attributo(fileIn, selettore, chiave, valore, fileOut).
#
# ATTENZIONE: nei test verrà utilizzato un timout globale di 1*N secondi se il
# grader fa N test).
#
# Esercizio svolto da Emanuele Petriglia.

import my_html

class Token:
    '''Identifica un token CSS.'''

    def __init__(self):
        '''Inizializza gli attributi del token.'''
        self.tag = '' # Il tag da selezionare.
        self.attribute = '' # La chiave dell'attributo (es. 'id' o 'class').
        self.value = '' # Il valore dell'attributo.

        self.direct_child = False # È necessario controllare il padre? ('>').
        self.check_father = False # Il padre soddisfa il selettore?

        self.next_token = '' # Token successivo.

    def copy(self):
        '''Ritorna una nuova copia del token.'''
        new_token = Token()

        new_token.tag = self.tag
        new_token.attribute = self.attribute
        new_token.value = self.value
        new_token.direct_child = self.direct_child
        new_token.check_father = self.check_father

        if self.next_token:
            new_token.next_token = self.next_token.copy()

        return new_token

def parse_special_prefixes(token, raw_token):
    '''Effettua il parsing dei prefissi speciali (' ' e '>'), ritornado
    'raw_token' aggiornato.
    '''
    if raw_token.startswith(' '):
        raw_token = raw_token[1:]
    elif raw_token.startswith('>'):
        token.direct_child = True
        raw_token = raw_token[1:]

    return raw_token

def parse_normal_prefixes(token, raw_token):
    '''Effettua il parsing dei prefissi normali ('@', '.' e '#' o un tag).'''
    special_attributes = {'#' : 'id', '.' : 'class'}

    if raw_token.startswith(('#', '.')):
        token.attribute = special_attributes[raw_token[0]]
        token.value = raw_token[1:]
    elif raw_token.startswith('@'):
        token.attribute = raw_token[raw_token.find('[') + 1 : \
                                    raw_token.find('=')]

        start_value_tmp = raw_token.find('"') + 1
        token.value = raw_token[start_value_tmp : \
                                raw_token.find('"', start_value_tmp)]
    else:
        token.tag = raw_token

def parse_token(raw_token):
    '''Restituisce il token corrispondende a 'raw_token'.'''
    token = Token()

    raw_token = parse_special_prefixes(token, raw_token)

    parse_normal_prefixes(token, raw_token)

    return token

def prepare_and_parse_token(tokens, position, last_token):
    '''Prepara il token in posizione 'position' nella lista 'tokens' e una volta
    parsato ritorna il token, aggiornando anche 'last_token'.
    '''
    token = tokens[position]

    if token == '>': # Si salta il parsing al token successivo
        tokens[position + 1] = '>' + tokens[position + 1]
        return last_token
    elif token.startswith(' '):
        tokens[position] = ' ' + tokens[position]

    last_token.next_token = parse_token(tokens[position])
    return last_token.next_token

def get_css_selector_from(raw_selector):
    '''Restituisce il primo token di 'raw_selector'.'''
    tokens = raw_selector.split()

    first_token = parse_token(tokens[0])

    last_token = first_token

    for position in range(1, len(tokens)):
        last_token = prepare_and_parse_token(tokens, position, last_token)

    return first_token

# ------------------------------------------------------------------------------

def check_father(node, selector, needed):
    '''Controlla se il padre del nodo 'node' con il selettore 'selector', se
    necessario (indicato dal valore booleano 'needed').
    Ritorna True o False in base al risultato del controllo.
    '''
    if needed: # È necessario controllare il padre?
        if selector.direct_child:
            return selector.check_father # True -> c'è, False -> non c'è.
    else: # Bisogna ricordare agli altri token che non combacia questo.
        selector.check_father = needed

    return needed

def check_node(node, selector):
    '''Controlla se il nodo 'node' soddisfa il selettore 'selector', tornando
    True o False di conseguenza.
    '''
    check = False

    # Si controlla il tag o un attributo.
    if selector.tag:
        check = node.tag == selector.tag
    else:
        check = selector.value in node.attr.get(selector.attribute, "")

    check = check_father(node, selector, check)

    if selector.next_token: # C'è un altro token
        selector.next_token.check_father = check

    return check

def check_actual_node(document, selector):
    '''Controlla il nodo 'document' con il selettore 'selector'.'''
    if check_node(document, selector):
        if selector.next_token: # Anche se combacia c'è altro da controllare.
            return selector.next_token, 0
        else:
            return selector, 1 # Nodo trovato.

    return selector, 0

def count_nodes(document, selector):
    '''Ritorna il numero di nodi in 'document' che soddisfano il selettore
    'selector'.
    '''
    if document.tag == '_text_':
        return 0

    selector, count = check_actual_node(document, selector)

    for sub_node in document.content:
        count += count_nodes(sub_node, selector.copy())

    return count

def conta_nodi(filename, raw_selector):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    document = my_html.fparse(filename)

    selector = get_css_selector_from(raw_selector)

    return count_nodes(document, selector)

# ------------------------------------------------------------------------------

def check_actual_node_remove(document, selector):
    '''Segnala la rimozione del nodo 'document' se soddisfa il selettore
    'selector'.
    '''
    if check_node(document, selector):
        if selector.next_token: # Anche se combacia c'è altro da controllare.
            return selector.next_token
        else:
            return False

    return selector

def remove_nodes(document, selector):
    '''Rimuove i nodi in 'document' che soddisfano il selettore 'selector'.'''
    if document.tag == '_text_':
        return True

    selector = check_actual_node_remove(document, selector)
    if not selector:
        return False

    # Filtra i vari nodi, salvando solo quelli che non si devono eliminare.
    document.content = list(filter(
                               lambda node: remove_nodes(node, selector.copy()),
                               document.content))

    return True

def elimina_nodi(input_file, raw_selector, output_file):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS,
    compreso il loro contenuto.
    '''
    document = my_html.fparse(input_file)

    selector = get_css_selector_from(raw_selector)

    remove_nodes(document, selector)

    open(output_file, "w").write(document.to_string())

# ------------------------------------------------------------------------------

def check_actual_node_change(document, selector, key, new_value):
    '''Controlla il nodo 'document' con il selettore 'selector' ed in caso
    positivo cambia l'attributo 'key' con il valore 'new_value'.
    '''
    if check_node(document, selector):
        if selector.next_token: # Anche se combacia c'è altro da controllare.
            return selector.next_token
        else: # Nodo trovato.
            document.attr[key] = new_value

    return selector

def change_nodes(document, selector, key, new_value):
    '''Modifica i nodi in 'document' che soddisfano il selettore 'selector',
    cambiando l'attributo 'key' con il valore 'new_value'.
    '''
    if document.tag == '_text_':
        return

    selector = check_actual_node_change(document, selector, key, new_value)

    set(map(lambda node: change_nodes(node, selector.copy(), key, new_value),
            document.content))

def cambia_attributo(input_file, selector, chiave, valore, output_file):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS.'''
    document = my_html.fparse(input_file)

    selector = get_css_selector_from(selector)

    change_nodes(document, selector, chiave, valore)

    open(output_file, "w").write(document.to_string())
