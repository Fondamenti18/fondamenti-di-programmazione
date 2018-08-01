def lastoccurence(test):
    alf = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    final = []
    for i in range(0, len(alf)):
        final.append(test.rfind(alf[i]))
    final[:] = [test for test in final if test != -1]
    final.sort()
    for j in range(0, len(final)):
        result = result + test[final[j]]
    return result

def codifica(chiave, testo):
    key = lastoccurence(chiave)
    keyordered = ''.join(sorted(key))
    key = [ord(test) for test in key]
    keyordered = [ord(test) for test in keyordered]
    diz = dict(zip(keyordered, key))
    return testo.translate(diz)

def decodifica(chiave, testo):
    key = lastoccurence(chiave)
    keyordered = ''.join(sorted(key))
    key = [ord(test) for test in key]
    keyordered = [ord(test) for test in keyordered]
    diz = dict(zip(key, keyordered))
    return testo.translate(diz)