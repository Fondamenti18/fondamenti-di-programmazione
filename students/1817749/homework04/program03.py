from my_html import fparse


#       AVES
#       AVES
#       AVES

def get_valid_aves_from_tag(root, tag, new):
    if root.tag == tag:
        new.append(root)
    for node in root.content:
        if not node.istext():
            get_valid_aves_from_tag(node, tag, new)
    return new


def get_valid_aves_from_class(root, dot, new):
    if "class" in root.attr and dot in root.attr["class"]:
        new.append(root)
    for node in root.content:
        if not node.istext():
            get_valid_aves_from_class(node, dot, new)
    return new


def get_valid_aves_from_id(root, ash, new):
    if "id" in root.attr and ash == root.attr["id"]:
        new.append(root)
    for node in root.content:
        if not node.istext():
            get_valid_aves_from_id(node, ash, new)
    return new


def get_valid_aves_from_attribute_value(root, infos, new):
    if infos[0] in root.attr and infos[1] == root.attr[infos[0]]:
        new.append(root)
    for node in root.content:
        if not node.istext():
            get_valid_aves_from_attribute_value(node, infos, new)
    return new


# SONS
# SONS
# SONS


def get_valid_sons_from_tag(root, tag, new):
    for node in root.content:
        if node.tag == tag:
            new.append(node)
    return new


def get_valid_sons_from_class(root, dot, new):
    for node in root.content:
        if "class" in node.attr and dot in node.attr["class"]:
            new.append(node)
    return new


def get_valid_sons_from_id(root, ash, new):
    for node in root.content:
        if "id" in node.attr and ash == node.attr["id"]:
            new.append(node)
    return new


def get_valid_sons_from_attribute_value(root, infos, new):
    for node in root.content:
        if infos[0] in node.attr and infos[1] == node.attr[infos[0]]:
            new.append(node)
    return new


# END
# END
# END


def get_attribute_and_value(selector):
    split = selector.split("=")
    return split[0][2:], split[1][1:-2]


def get_perfect_selector(selettore):
    return ["-"] + selettore.replace(" ", " - ").replace(" - > - ", " > ").split(" ")


def perform_id_filter(tip, nodes, sieve):
    final = []
    if tip == '-':
        for node in nodes:
            get_valid_aves_from_id(node, sieve, final)
    else:
        for node in nodes:
            get_valid_sons_from_id(node, sieve, final)
    return final


def perform_class_filter(tip, nodes, sieve):
    final = []
    if tip == '-':
        for node in nodes:
            get_valid_aves_from_class(node, sieve, final)
    else:
        for node in nodes:
            get_valid_sons_from_class(node, sieve, final)
    return final


def perform_attribute_filter(tip, nodes, sieve):
    final = []
    if tip == '-':
        for node in nodes:
            get_valid_aves_from_attribute_value(node, get_attribute_and_value(sieve), final)
    else:
        for node in nodes:
            get_valid_sons_from_attribute_value(node, get_attribute_and_value(sieve), final)
    return final


def perform_tag_filter(tip, nodes, sieve):
    final = []
    if tip == '-':
        for node in nodes:
            get_valid_aves_from_tag(node, sieve, final)
    else:
        for node in nodes:
            get_valid_sons_from_tag(node, sieve, final)
    return final


def perform_filter(tip, sieve, nodes):
    if sieve[0] == "#":
        return perform_id_filter(tip, nodes, sieve[1:])
    if sieve[0] == ".":
        return perform_class_filter(tip, nodes, sieve[1:])
    if sieve[0] == "@":
        return perform_attribute_filter(tip, nodes, sieve)
    return perform_tag_filter(tip, nodes, sieve)


def get_perfect_slaves(fin, selettore):
    splitted = get_perfect_selector(selettore)
    fin = [fin]
    for index in range(0, len(splitted), 2):
        fin = perform_filter(splitted[index], splitted[index + 1], fin)
    return fin


def conta_nodi(fileIn, selettore):
    return len(get_perfect_slaves(fparse(fileIn), selettore))


def remove_single_node(doc, node):
    if node in doc.content:
        doc.content.remove(node)
        return True
    else:
        for con in doc.content:
            if not con.istext() and remove_single_node(con, node):
                return True


def elimina_nodi(fileIn, selettore, fileOut):
    doc = fparse(fileIn)
    for node in get_perfect_slaves(doc, selettore):
        remove_single_node(doc, node)
    open(fileOut, 'w', encoding='utf-8').write(doc.to_string())


def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    doc = fparse(fileIn)
    for node in get_perfect_slaves(doc, selettore):
        node.attr[chiave] = valore
    open(fileOut, 'w', encoding='utf-8').write(doc.to_string())
