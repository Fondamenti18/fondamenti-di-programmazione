import re

def apri(inp):
    id = ''
    for lett in inp.lstrip():
        if not lett.isdigit():
            break
        id += lett
    return [id, inp.lower()[len(id):]]

def post(fposts, insieme):
    fine = set()
    with open(fposts, 'r') as pagina:
        split = pagina.read().split("<POST>")
        del split[0]
        for blocco in split:
            post = apri(blocco)
            for parola in insieme:
                if re.search(r'\b' + parola.lower() + r'\b', post[1]):
                    fine.add(post[0])
                    break
    return fine