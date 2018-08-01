import string
import re

def codifica(chiave, testo):
    lista = []
    result = re.sub(r'[^a-z0-9]', '', chiave)
    for i in result:
        result = result.replace(i, "", (result.count(i)-1))
    result2 = ''.join(sorted(result))
    for i in result2:
        lista.append(ord(i))
    output_dict = dict(zip(lista, result))
    return testo.translate(output_dict)

def decodifica(chiave, testo):
    lista = []
    result = re.sub(r'[^a-z0-9]', '', chiave)
    for i in result:
        result = result.replace(i, "", (result.count(i)-1))
    result2 = ''.join(sorted(result))
    for i in result:
        lista.append(ord(i))
    output_dict = dict(zip(lista, result2))
    return testo.translate(output_dict)
