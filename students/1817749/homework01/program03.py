def get_nk(chiave):
    nk = ""
    for el in reversed(chiave):
        if 'a' <= el <= 'z':
            if el not in nk:
                nk = el + nk
                if len(nk) == 26:
                    break
    return nk

def clean_key_cod(chiave):
    nk = get_nk(chiave)
    ret = dict(zip(sorted(nk), nk))
    return ret

def clean_key_dec(chiave):
    nk = get_nk(chiave)
    ret = dict(zip(nk, sorted(nk)))
    return ret


def codifica(chiave, testo):
    chiave = clean_key_cod(chiave)
    new_text = ""
    for c in testo:
        if c in chiave:
            new_text += chiave[c]
        else:
            new_text += c
    return new_text


def decodifica(chiave, testo):
    chiave = clean_key_dec(chiave)
    new_text = ""
    for c in testo:
        if c in chiave:
            new_text += chiave[c]
        else:
            new_text += c
    return new_text